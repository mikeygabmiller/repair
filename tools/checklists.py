#!/usr/bin/env python3
"""Build the garage checklists page from the procedure files.

  python3 tools/checklists.py           # write procedures/checklists.html
  python3 tools/checklists.py --check   # exit 1 if checklists.html is out of date

One phone page with every procedure in `procedures/`: pick a job, tick each step as you go
(ticks are saved on that phone only), then fill the log box and copy it into the chat so
Claude adds it to log.md and ledger.csv.

The page is generated, never edited by hand: the .md procedure is the source of record and
its numbers already come from specs.md (tools/check.py enforces that). Run this after any
procedure, schedule.csv or procedures/README.md change. tools/check.py warns when it's stale.
"""
import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "procedures"
OUT = PROC / "checklists.html"
CAR = next(p for p in (ROOT / "vehicles").iterdir() if p.is_dir())

PLAIN_SECTIONS = re.compile(r"couldn.t verify|still needed|not confirmed|gotcha|why it matters|"
                            r"what.s known|specs|targets|intervals|pattern|what diy can", re.I)
TAGS = [("OFFICIAL RECORD", "v"), ("UNVERIFIED", "u"), ("VERIFIED", "v"), ("COMMUNITY", "c"),
        ("TENTATIVE", "u"), ("DRAFT", "u"), ("NOT FOUND", "u")]


def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
               r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r"&lt;(https?://[^&\s]+)&gt;", r'<a href="\1" target="_blank" rel="noopener">\1</a>', t)
    for word, cls in TAGS:
        # don't tag the VERIFIED inside UNVERIFIED
        pat = r"(?<![A-Z])" + re.escape(word) + r"(?![A-Z])"
        t = re.sub(pat, f'<span class="tag {cls}">{word}</span>', t)
    return t


def slug(path):
    return path.stem.replace("accord-2005-", "")


def statuses():
    """Job name and status for each procedure, from the table in procedures/README.md."""
    out = {}
    for line in (PROC / "README.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3:
            m = re.search(r"`([^`]+\.md)`", cells[1])
            if m:
                out[m.group(1)] = (cells[0], cells[2])
    return out


def schedule():
    with open(CAR / "schedule.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    by_proc = {}
    for r in rows:
        by_proc.setdefault(Path(r["procedure"]).name, []).append(r)
    return by_proc


def interval_text(r):
    bits = []
    if r["first_miles"] or r["first_months"]:
        first = []
        if r["first_miles"]:
            first.append(f"{int(r['first_miles']):,} mi")
        if r["first_months"]:
            first.append(f"{int(r['first_months']) // 12} yr")
        bits.append("first at " + " or ".join(first))
    every = []
    if r["every_miles"]:
        every.append(f"{int(r['every_miles']):,} mi")
    if r["every_months"]:
        mo = int(r["every_months"])
        every.append(f"{mo // 12} yr" if mo % 12 == 0 else f"{mo} months")
    if every:
        bits.append(("then every " if bits else "every ") + " or ".join(every))
    return f"{r['item']}: " + ", ".join(bits) + f" ({r['source']})"


class Body:
    """Turns one procedure's markdown into HTML, list items as checkboxes."""

    def __init__(self):
        self.out = []
        self.para = []
        self.items = []      # [text, [subitems]] for the open list
        self.list_kind = None
        self.table = []
        self.code = None
        self.plain = False

    def flush_para(self):
        if self.para:
            self.out.append("<p>" + inline(" ".join(self.para)) + "</p>")
            self.para = []

    def flush_list(self):
        if not self.items:
            return
        if self.plain:
            lis = []
            for text, subs in self.items:
                sub = "".join(f"<li>{inline(s)}</li>" for s in subs)
                lis.append(f"<li>{inline(text)}" + (f"<ul>{sub}</ul>" if sub else "") + "</li>")
            tag = "ol" if self.list_kind == "ol" else "ul"
            self.out.append(f'<{tag} class="plain">' + "".join(lis) + f"</{tag}>")
        else:
            lis = []
            for text, subs in self.items:
                sub = "".join(f"<li>{inline(s)}</li>" for s in subs)
                body = inline(text) + (f"<ul>{sub}</ul>" if sub else "")
                lis.append(f'<li><label><input type="checkbox"><span class="stxt">{body}'
                           "</span></label></li>")
            cls = "steps num" if self.list_kind == "ol" else "steps"
            self.out.append(f'<ol class="{cls}">' + "".join(lis) + "</ol>")
        self.items, self.list_kind = [], None

    def flush_table(self):
        if not self.table:
            return
        rows = [r for r in self.table if not re.fullmatch(r"\|?[\s:|-]+\|?", r.strip())]
        cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
        head = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
        body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                       for r in cells[1:])
        self.out.append(f'<div class="tbl"><table><thead><tr>{head}</tr></thead>'
                        f"<tbody>{body}</tbody></table></div>")
        self.table = []

    def flush(self):
        self.flush_para()
        self.flush_list()
        self.flush_table()

    def feed(self, line):
        if self.code is not None:
            if line.strip().startswith("```"):
                self.out.append("<pre>" + html.escape("\n".join(self.code)) + "</pre>")
                self.code = None
            else:
                self.code.append(line)
            return
        if line.strip().startswith("```"):
            self.flush()
            self.code = []
            return
        m = re.match(r"^(#{2,4})\s+(.*)", line)
        if m:
            self.flush()
            level = len(m.group(1))
            self.plain = bool(PLAIN_SECTIONS.search(m.group(2)))
            self.out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            return
        if line.lstrip().startswith("|"):
            self.flush_para()
            self.flush_list()
            self.table.append(line)
            return
        self.flush_table()
        m = re.match(r"^(\s*)(?:[-*]|\d+\.)\s+(?:\[[ xX]\]\s+)?(.*)", line)
        if m:
            self.flush_para()
            indent, text = len(m.group(1)), m.group(2)
            if indent >= 2 and self.items:
                self.items[-1][1].append(text)
            else:
                kind = "ol" if re.match(r"^\s*\d+\.", line) else "ul"
                if self.items and kind != self.list_kind:
                    self.flush_list()
                self.list_kind = kind
                self.items.append([text, []])
            return
        if not line.strip():
            self.flush_para()
            return
        if self.items and line.startswith((" ", "\t")):
            last = self.items[-1]
            if last[1]:
                last[1][-1] += " " + line.strip()
            else:
                last[0] += " " + line.strip()
            return
        self.flush_list()
        self.para.append(line.strip())


def job_html(path, status, sched_rows):
    lines = path.read_text().splitlines()
    title = re.sub(r"^#\s+", "", lines[0])
    intro, rest = [], lines[1:]
    while rest and not rest[0].startswith("## "):
        intro.append(rest.pop(0))
    b = Body()
    for line in rest:
        b.feed(line)
    b.flush()
    ib = Body()
    ib.plain = True
    for line in intro:
        ib.feed(line)
    ib.flush()
    s = slug(path)
    draft = "DRAFT" in status or "DRAFT" in title
    badge = (f'<span class="pill {"draft" if draft else "ok"}">'
             f'{"Draft: not fully sourced" if draft else "Sourced"}</span>')
    sched = "".join(f"<li>{html.escape(interval_text(r))}</li>" for r in sched_rows)
    keys = ",".join(r["key"] for r in sched_rows)
    return f'''<section class="job" id="{s}" data-job="{s}" data-keys="{keys}" data-title="{html.escape(title)}" hidden>
<p class="back"><a href="#">&larr; All jobs</a></p>
<div class="bar"><div class="prog" aria-hidden="true"><i></i></div><span class="count">0 / 0</span></div>
<h1>{inline(title)}</h1>
<p class="meta">{badge} <span class="status">{inline(status)}</span></p>
{"<div class='card sched'><b>Honda's schedule</b><ul class='plain'>" + sched + "</ul></div>" if sched else ""}
<div class="intro">{"".join(ib.out)}</div>
{"".join(b.out)}
<h2>Log this job</h2>
<div class="card log">
<p class="sub">Fill this in at the car. Then copy it and paste it into the chat: Claude adds it to <code>log.md</code>, <code>ledger.csv</code> and <code>maintenance.md</code>.</p>
<div class="fields">
<label for="{s}-date">Date</label><input type="date" id="{s}-date" data-k="date">
<label for="{s}-odo">Odometer (mi)</label><input type="text" inputmode="numeric" id="{s}-odo" data-k="odo" placeholder="from the dash">
<label for="{s}-cost">Total cost ($)</label><input type="text" inputmode="decimal" id="{s}-cost" data-k="cost" placeholder="parts + fluids">
<label for="{s}-by">Done by</label><input type="text" id="{s}-by" data-k="by" value="owner">
<label for="{s}-parts">Parts and fluids used</label><input type="text" id="{s}-parts" data-k="parts" placeholder="brand and part number">
<label for="{s}-notes">Notes</label><textarea id="{s}-notes" data-k="notes" rows="3" placeholder="what seized, real time it took, anything odd"></textarea>
</div>
<textarea class="out" id="{s}-out" rows="5" readonly></textarea>
<div class="btns"><button type="button" class="copy">Copy for the chat</button><button type="button" class="reset">Clear ticks and log</button></div>
<p class="msg" aria-live="polite"></p>
</div>
</section>'''


CSS = """
:root{
  --bg:#f3f4f2; --card:#ffffff; --ink:#1b1d1c; --muted:#5b605d; --line:#d8dbd7;
  --accent:#b4441b; --accent-soft:#fbe9e1;
  --ok:#1f6f43; --ok-soft:#e3f2e9; --warn:#8a5a00; --warn-soft:#fdf1d8;
  --stop:#a3201c; --stop-soft:#fbe4e2; --tag:#e8ebe7;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#131514; --card:#1d201e; --ink:#e9ebe8; --muted:#a2a8a4; --line:#333834;
    --accent:#f08a5d; --accent-soft:#3a2219;
    --ok:#7fd1a0; --ok-soft:#18301f; --warn:#f2c46b; --warn-soft:#352a12;
    --stop:#ff8a83; --stop-soft:#3a1716; --tag:#2a2e2b; color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#131514; --card:#1d201e; --ink:#e9ebe8; --muted:#a2a8a4; --line:#333834;
  --accent:#f08a5d; --accent-soft:#3a2219;
  --ok:#7fd1a0; --ok-soft:#18301f; --warn:#f2c46b; --warn-soft:#352a12;
  --stop:#ff8a83; --stop-soft:#3a1716; --tag:#2a2e2b; color-scheme:dark;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
  font:17px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding-block:12px 64px;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1{font-size:1.45rem;line-height:1.2;margin:10px 0 6px;text-wrap:balance}
h2{font-size:1.12rem;margin:28px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--accent);text-wrap:balance}
h3,h4{font-size:1rem;margin:20px 0 8px}
p{margin:6px 0}
a{color:var(--accent)}
code{font:.88em ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--tag);padding:0 4px;border-radius:4px;overflow-wrap:anywhere}
pre{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;overflow-x:auto;font-size:.85rem}
.sub,.meta .status,.intro{color:var(--muted);font-size:.93rem}
.intro p{margin:4px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:12px 0}
.tag{display:inline-block;font-size:.7rem;font-weight:650;letter-spacing:.03em;background:var(--tag);
  color:var(--muted);border-radius:6px;padding:0 6px;white-space:nowrap;vertical-align:1px}
.tag.v{color:var(--ok)} .tag.c{color:var(--warn)} .tag.u{color:var(--stop)}
.pill{display:inline-block;font-size:.78rem;font-weight:650;border-radius:999px;padding:2px 10px;margin-right:6px}
.pill.ok{background:var(--ok-soft);color:var(--ok)} .pill.draft{background:var(--warn-soft);color:var(--warn)}
ol.steps{list-style:none;padding:0;margin:0;counter-reset:s}
ol.steps>li{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:8px 0}
ol.steps>li label{display:grid;grid-template-columns:30px minmax(0,1fr);gap:10px;padding:11px 13px;cursor:pointer}
ol.steps input{width:24px;height:24px;margin:2px 0 0;accent-color:var(--accent)}
ol.steps.num>li{counter-increment:s}
ol.steps.num .stxt::before{content:counter(s) ". ";font-weight:700;color:var(--accent)}
ol.steps li.done{opacity:.55}
ol.steps li.done .stxt{text-decoration:line-through;text-decoration-color:var(--muted)}
.stxt ul,ul.plain ul{margin:6px 0 0;padding-left:20px}
ul.plain,ol.plain{padding-left:20px;margin:6px 0}
ul.plain li,ol.plain li{margin:4px 0}
.sched ul{margin:6px 0 0}
.tbl{overflow-x:auto;margin:10px 0;border:1px solid var(--line);border-radius:10px;background:var(--card)}
table{border-collapse:collapse;font-size:.9rem;min-width:100%}
th,td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
th{font-weight:650;background:var(--tag)}
tr:last-child td{border-bottom:0}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:2;background:var(--bg);padding:8px 0;display:flex;gap:10px;align-items:center;border-bottom:1px solid var(--line)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.prog{flex:1;height:10px;background:var(--line);border-radius:6px;overflow:hidden}
.prog i{display:block;height:100%;width:0;background:var(--accent);transition:width .2s}
.count{font-size:.9rem;color:var(--muted);min-width:60px;text-align:right;font-variant-numeric:tabular-nums}
.back{margin:4px 0 0;font-size:.95rem}
.fields{display:grid;grid-template-columns:minmax(0,1fr);gap:4px 0}
.fields label{font-size:.85rem;color:var(--muted);margin-top:6px}
input[type=text],input[type=date],textarea{width:100%;font:inherit;font-size:16px;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink)}
textarea.out{margin-top:12px;font:13px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace}
.btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
button{font:inherit;font-size:.95rem;padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
button.copy{background:var(--accent);border-color:var(--accent);color:var(--bg);font-weight:650}
button.armed{border-color:var(--stop);color:var(--stop)}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.msg{font-size:.9rem;color:var(--ok);min-height:1.4em}
.list h1{font-size:1.6rem}
.jobs{list-style:none;padding:0;margin:8px 0;display:grid;gap:8px}
.jobs a{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 10px;align-items:center;text-decoration:none;color:var(--ink);
  background:var(--card);border:1px solid var(--line);border-radius:12px;padding:11px 13px}
.jobs a:hover{border-color:var(--accent)}
.jobs .n{font-weight:650}
.jobs .d{grid-column:1/-1;font-size:.85rem;color:var(--muted)}
.jobs .p{font-size:.78rem;color:var(--muted);font-variant-numeric:tabular-nums}
@media (prefers-reduced-motion:reduce){.prog i{transition:none}}
"""

JS = r"""
(function(){
  function load(k){ try{ return JSON.parse(localStorage.getItem(k)||'{}')||{}; }catch(e){ return {}; } }
  function store(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
  function csv(s){ s=String(s==null?'':s); return /[",\n]/.test(s)?'"'+s.replace(/"/g,'""')+'"':s; }
  var jobs=[].slice.call(document.querySelectorAll('section.job'));
  var list=document.getElementById('list');
  jobs.forEach(function(sec){
    var key='chk:'+sec.dataset.job, st=load(key);
    var boxes=[].slice.call(sec.querySelectorAll('input[type=checkbox]'));
    var fields=[].slice.call(sec.querySelectorAll('[data-k]'));
    var out=sec.querySelector('textarea.out'), msg=sec.querySelector('.msg');
    function compose(){
      var v={}; fields.forEach(function(f){ v[f.dataset.k]=f.value.trim(); });
      var keys=(sec.dataset.keys||'').split(',').filter(Boolean);
      var kind=keys.length?'maintenance':'repair';
      if(!keys.length) keys=[sec.dataset.job];
      var rows=keys.map(function(k,i){
        return [v.date,v.odo.replace(/[^0-9]/g,''),kind,k,i===0?v.cost.replace(/[$,\s]/g,''):'',v.by||'owner',
          sec.dataset.title,i===0?[v.parts,v.notes].filter(Boolean).join('. '):'cost on the first row'].map(csv).join(',');
      });
      var done=boxes.filter(function(b){return b.checked;}).length;
      out.value='JOB DONE: '+sec.dataset.title+'\nSteps ticked: '+done+' of '+boxes.length+
        '\nParts: '+(v.parts||'(not filled in)')+'\nNotes: '+(v.notes||'(none)')+
        '\nledger.csv rows:\n'+rows.join('\n');
    }
    function refresh(){
      var n=0; boxes.forEach(function(b){ var li=b.closest('li'); if(li) li.classList.toggle('done',b.checked); if(b.checked) n++; });
      sec.querySelector('.count').textContent=n+' / '+boxes.length;
      sec.querySelector('.prog i').style.width=(boxes.length?n/boxes.length*100:0)+'%';
      var p=list.querySelector('[data-p="'+sec.dataset.job+'"]');
      if(p) p.textContent=n?(n+' / '+boxes.length+' ticked'):boxes.length+' steps';
      compose();
    }
    boxes.forEach(function(b,i){ b.checked=!!st['c'+i]; b.addEventListener('change',function(){ st['c'+i]=b.checked; store(key,st); refresh(); }); });
    fields.forEach(function(f){ var k='f-'+f.dataset.k; if(st[k]!=null) f.value=st[k];
      f.addEventListener('input',function(){ st[k]=f.value; store(key,st); compose(); }); });
    var dateF=sec.querySelector('[data-k=date]');
    if(!dateF.value){ var d=new Date(); dateF.value=d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0'); }
    sec.querySelector('.copy').addEventListener('click',function(){
      compose();
      function fallback(){ out.focus(); out.select(); msg.textContent='Selected: copy it with your phone’s Copy.'; }
      try{ navigator.clipboard.writeText(out.value).then(function(){ msg.textContent='Copied. Paste it into the chat.'; },fallback); }
      catch(e){ fallback(); }
    });
    var reset=sec.querySelector('.reset'), armed=null;
    reset.addEventListener('click',function(){
      if(!armed){ reset.classList.add('armed'); reset.textContent='Tap again to clear';
        armed=setTimeout(function(){ armed=null; reset.classList.remove('armed'); reset.textContent='Clear ticks and log'; },4000); return; }
      clearTimeout(armed); armed=null; reset.classList.remove('armed'); reset.textContent='Clear ticks and log';
      st={}; store(key,st); boxes.forEach(function(b){ b.checked=false; });
      fields.forEach(function(f){ f.value=f.dataset.k==='by'?'owner':''; });
      dateF.value=''; msg.textContent='Cleared.'; refresh();
    });
    refresh();
  });
  function route(){
    var id=(location.hash||'').slice(1), hit=null;
    jobs.forEach(function(s){ var on=s.id===id; s.hidden=!on; if(on) hit=s; });
    list.hidden=!!hit; window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',route); route();
})();
"""


def build():
    st = statuses()
    sched = schedule()
    files = [p for p in sorted(PROC.glob("accord-2005-*.md"))]
    order = {name: i for i, name in enumerate(st)}
    files.sort(key=lambda p: order.get(p.name, 999))
    jobs, items = [], []
    for p in files:
        name, status = st.get(p.name, (p.stem, ""))
        rows = sched.get(p.name, [])
        jobs.append(job_html(p, status, rows))
        draft = "DRAFT" in status
        items.append(f'<li><a href="#{slug(p)}"><span class="n">{inline(name)}</span>'
                     f'<span class="p" data-p="{slug(p)}"></span>'
                     f'<span class="d">{"<span class=\'pill draft\'>Draft</span>" if draft else ""}'
                     f'{inline(status)}</span></a></li>')
    return f'''<title>Accord Garage Checklists</title>
<meta name="claude:viewport-fit-sides" content="cover">
<!-- GENERATED by tools/checklists.py from procedures/*.md. Don't edit: change the .md and re-run. -->
<style>{CSS}</style>
<main>
<section class="list" id="list">
<h1>Garage checklists</h1>
<p class="sub">2005 Honda Accord EX-L, 2.4 L, automatic. Pick the job, tick each step as you go, then fill in the log box and paste it into the chat. Ticks save on this phone only.</p>
<p class="sub"><span class="tag v">VERIFIED</span> owner's manual or Chilton · <span class="tag c">COMMUNITY</span> forum or YouTube tip · <span class="tag u">UNVERIFIED</span> not confirmed for this car. A <span class="pill draft">Draft</span> job has steps or numbers that aren't sourced yet.</p>
<ul class="jobs">{"".join(items)}</ul>
<p class="sub">Built from the repair repo's procedure files. If this page and the repo ever disagree, the repo wins.</p>
</section>
{"".join(jobs)}
</main>
<script>{JS}</script>
'''


def main():
    page = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != page:
            print("procedures/checklists.html is out of date. Run: python3 tools/checklists.py")
            sys.exit(1)
        return
    OUT.write_text(page)
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(files_count := page.split('<section class=\"job\"')) - 1} jobs)")


if __name__ == "__main__":
    main()
