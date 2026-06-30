from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    version = "1.0.4"
    heure = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%d/%m/%Y")

    return f"""<!DOCTYPE html>
<html lang="fr" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps App</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

        :root, [data-theme="light"] {{
            --bg:       #f4f6f8;
            --surface:  #ffffff;
            --surface2: #f0f2f5;
            --border:   #d0d7de;
            --border-s: #b0b8c1;
            --text:     #1c2128;
            --text-2:   #57606a;
            --text-3:   #aab0b7;
            --cyan:     #0969da;
            --cyan-bg:  rgba(9,105,218,.08);
            --cyan-bd:  rgba(9,105,218,.22);
            --green:    #1a7f37;
            --green-bg: rgba(26,127,55,.08);
            --green-bd: rgba(26,127,55,.22);
            --amber:    #9a6700;
            --amber-bg: rgba(154,103,0,.08);
            --mono:     'JetBrains Mono', monospace;
            --sans:     'Inter', sans-serif;
        }}

        [data-theme="dark"] {{
            --bg:       #0d1117;
            --surface:  #161b22;
            --surface2: #1c2333;
            --border:   #30363d;
            --border-s: #444c56;
            --text:     #e6edf3;
            --text-2:   #8b949e;
            --text-3:   #484f58;
            --cyan:     #39d0f0;
            --cyan-bg:  rgba(57,208,240,.10);
            --cyan-bd:  rgba(57,208,240,.25);
            --green:    #3fb950;
            --green-bg: rgba(63,185,80,.10);
            --green-bd: rgba(63,185,80,.25);
            --amber:    #d29922;
            --amber-bg: rgba(210,153,34,.10);
        }}

        html {{ transition: background .25s, color .25s; }}

        body {{
            background: var(--bg);
            color: var(--text);
            font-family: var(--sans);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 1rem;
            transition: background .25s;
        }}

        .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 2rem;
            width: 100%;
            max-width: 620px;
            transition: background .25s, border-color .25s;
        }}

        svg.icon {{
            display: inline-block;
            vertical-align: middle;
            flex-shrink: 0;
            stroke: currentColor;
            fill: none;
            stroke-width: 1.75;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}

        /* ── Topbar ── */
        .topbar {{
            display: flex;
            justify-content: flex-end;
            margin-bottom: 1.25rem;
        }}
        .theme-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--surface2);
            border: 1px solid var(--border);
            color: var(--text-2);
            font-family: var(--sans);
            font-size: 12px;
            font-weight: 500;
            padding: 5px 12px;
            border-radius: 20px;
            cursor: pointer;
            transition: background .2s, border-color .2s;
        }}
        .theme-btn:hover {{ background: var(--border); color: var(--text); }}

        /* ── Terminal ── */
        .terminal {{
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1rem 1.25rem;
            margin-bottom: 1.75rem;
            font-family: var(--mono);
            font-size: 12px;
            min-height: 120px;
            transition: background .25s, border-color .25s;
        }}
        .terminal-bar {{
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 10px;
        }}
        .dot {{ width: 10px; height: 10px; border-radius: 50%; }}
        .log {{ line-height: 1.9; color: var(--text-2); }}
        .log .ok   {{ color: var(--green); }}
        .log .info {{ color: var(--cyan); }}
        .log .dim  {{ color: var(--text-3); }}
        .cursor {{
            display: inline-block;
            width: 8px; height: 13px;
            background: var(--text-2);
            vertical-align: -2px;
            animation: blink 1s step-end infinite;
        }}
        @keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0}} }}

        /* ── Header ── */
        .header {{
            display: flex;
            align-items: flex-start;
            gap: 14px;
            margin-bottom: 1.5rem;
        }}
        .app-icon {{
            width: 46px; height: 46px;
            border-radius: 10px;
            background: var(--cyan-bg);
            border: 1px solid var(--cyan-bd);
            display: flex; align-items: center; justify-content: center;
            color: var(--cyan);
            flex-shrink: 0;
        }}
        .app-title {{
            font-family: var(--mono);
            font-size: 20px;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: var(--text);
        }}
        .app-sub {{ font-size: 13px; color: var(--text-2); margin-top: 2px; }}
        .badge-online {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--green-bg);
            border: 1px solid var(--green-bd);
            color: var(--green);
            font-size: 12px;
            font-weight: 500;
            padding: 3px 10px;
            border-radius: 20px;
            margin-top: 6px;
        }}
        .pulse {{
            width: 7px; height: 7px;
            border-radius: 50%;
            background: var(--green);
            animation: pulse 2s ease-in-out infinite;
        }}
        @keyframes pulse {{ 0%,100%{{opacity:1;transform:scale(1)}} 50%{{opacity:.5;transform:scale(.8)}} }}

        /* ── Metrics ── */
        .metrics {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 1.5rem;
        }}
        .metric {{
            background: var(--surface2);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 14px 16px;
            transition: background .25s, border-color .25s;
        }}
        .metric-label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: .8px;
            color: var(--text-3);
            font-weight: 500;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .metric-value {{
            font-family: var(--mono);
            font-size: 20px;
            font-weight: 700;
            color: var(--text);
        }}
        .metric-value.green {{ color: var(--green); }}
        .metric-value.cyan  {{ color: var(--cyan); }}
        .metric-value.amber {{ color: var(--amber); }}

        /* ── Pipeline ── */
        .pipeline {{ margin-bottom: 1.5rem; }}
        .pipeline-label {{
            font-size: 11px;
            font-weight: 500;
            color: var(--text-3);
            text-transform: uppercase;
            letter-spacing: .8px;
            margin-bottom: 12px;
        }}
        .steps {{ display: flex; align-items: center; }}
        .step {{ display: flex; flex-direction: column; align-items: center; flex: 1; }}
        .step-node {{
            width: 34px; height: 34px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            border: 1px solid var(--border);
            background: var(--surface2);
            color: var(--text-3);
            position: relative;
            z-index: 1;
        }}
        .step-node.done   {{ background: var(--green-bg); border-color: var(--green-bd); color: var(--green); }}
        .step-node.active {{ background: var(--cyan-bg);  border-color: var(--cyan-bd);  color: var(--cyan); }}
        .step-text {{
            font-size: 10px;
            color: var(--text-3);
            margin-top: 6px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: .5px;
        }}
        .connector {{ flex: 1; height: 1px; background: var(--border); margin-top: -17px; }}
        .connector.done {{ background: var(--green-bd); }}

        /* ── Footer ── */
        .footer {{
            border-top: 1px solid var(--border);
            padding-top: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .footer-info {{
            font-size: 12px;
            color: var(--text-3);
            font-family: var(--mono);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .version-tag {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            background: var(--cyan-bg);
            border: 1px solid var(--cyan-bd);
            color: var(--cyan);
            font-family: var(--mono);
            font-size: 12px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 6px;
        }}
    </style>
</head>
<body>
<div class="card">

    <!-- Topbar -->
    <div class="topbar">
        <button class="theme-btn" id="toggle-btn" onclick="toggleTheme()" aria-label="Basculer le thème">
            <!-- icône lune (light) / soleil (dark) -->
            <svg class="icon" id="theme-icon" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
            </svg>
            <span id="theme-label">Mode sombre</span>
        </button>
    </div>

    <!-- Terminal -->
    <div class="terminal">
        <div class="terminal-bar">
            <div class="dot" style="background:#ff5f57"></div>
            <div class="dot" style="background:#febc2e"></div>
            <div class="dot" style="background:#28c840"></div>
            <span style="font-size:11px;color:var(--text-3);margin-left:4px">jenkins@pipeline ~ </span>
        </div>
        <div class="log" id="log-output">
            <div><span class="dim">$</span> <span class="info">docker pull devops-app:{version}</span></div>
        </div>
    </div>

    <!-- Header -->
    <div class="header">
        <div class="app-icon">
            <!-- Rocket / server icon -->
            <svg class="icon" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
                <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
                <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/>
                <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>
            </svg>
        </div>
        <div>
            <div class="app-title">DevOps App</div>
            <div class="app-sub">CI/CD Pipeline Demo</div>
            <div class="badge-online">
                <div class="pulse"></div>
                En ligne
            </div>
        </div>
    </div>

    <!-- Metrics -->
    <div class="metrics">
        <div class="metric">
            <div class="metric-label" style="color:var(--green)">
                <svg class="icon" width="13" height="13" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
                Version
            </div>
            <div class="metric-value green">{version}</div>
        </div>
        <div class="metric">
            <div class="metric-label" style="color:var(--cyan)">
                <svg class="icon" width="13" height="13" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                Heure
            </div>
            <div class="metric-value cyan" id="time">{heure}</div>
        </div>
        <div class="metric">
            <div class="metric-label" style="color:var(--amber)">
                <svg class="icon" width="13" height="13" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                Date
            </div>
            <div class="metric-value amber">{date}</div>
        </div>
    </div>

    <!-- Pipeline -->
    <div class="pipeline">
        <div class="pipeline-label">Pipeline</div>
        <div class="steps">
            <div class="step">
                <div class="step-node done">
                    <svg class="icon" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
                <div class="step-text">Build</div>
            </div>
            <div class="connector done"></div>
            <div class="step">
                <div class="step-node done">
                    <svg class="icon" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
                <div class="step-text">Test</div>
            </div>
            <div class="connector done"></div>
            <div class="step">
                <div class="step-node done">
                    <svg class="icon" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
                <div class="step-text">Image</div>
            </div>
            <div class="connector done"></div>
            <div class="step">
                <div class="step-node active">
                    <svg class="icon" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                </div>
                <div class="step-text">Deploy</div>
            </div>
            <div class="connector"></div>
            <div class="step">
                <div class="step-node">
                    <svg class="icon" width="15" height="15" viewBox="0 0 24 24" aria-hidden="true"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                </div>
                <div class="step-text">Monitor</div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <div class="footer-info">
            <svg class="icon" width="13" height="13" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
            jenkins &amp; docker · auto-deploy
        </div>
        <div class="version-tag">
            <svg class="icon" width="12" height="12" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>
            v{version}
        </div>
    </div>

</div>

<script>
    // ── Icônes SVG pour le toggle ──
    const ICON_MOON = `<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>`;
    const ICON_SUN  = `<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>`;

    function setToggleIcon(isDark) {{
        const svg = document.getElementById('theme-icon');
        svg.innerHTML = isDark ? ICON_SUN : ICON_MOON;
        document.getElementById('theme-label').textContent = isDark ? 'Mode clair' : 'Mode sombre';
    }}

    function toggleTheme() {{
        const html = document.documentElement;
        const isDark = html.getAttribute('data-theme') === 'dark';
        const next = isDark ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        setToggleIcon(!isDark);
    }}

    (function() {{
        const saved = localStorage.getItem('theme');
        if (saved === 'dark') {{
            document.documentElement.setAttribute('data-theme', 'dark');
            setToggleIcon(true);
        }}
    }})();

    // ── Horloge ──
    function pad(n) {{ return String(n).padStart(2, '0'); }}
    function tick() {{
        const now = new Date();
        const el = document.getElementById('time');
        if (el) el.textContent = pad(now.getHours()) + ':' + pad(now.getMinutes()) + ':' + pad(now.getSeconds());
    }}
    setInterval(tick, 1000);

    // ── Terminal animé ──
    const logEl = document.getElementById('log-output');
    const lines = [
        {{ delay: 700,  html: '<div><span class="ok">&#10003;</span> <span class="dim">Image pulled (142 MB)</span></div>' }},
        {{ delay: 1400, html: '<div><span class="dim">$</span> <span class="info">docker run -p 8000:8000 devops-app:{version}</span></div>' }},
        {{ delay: 2300, html: '<div><span class="ok">&#10003;</span> <span class="dim">Container started [id: a3f9c2]</span></div>' }},
        {{ delay: 3000, html: '<div><span class="ok">&#10003;</span> <span class="dim">Health check passed — port 8000 OK</span></div>' }},
        {{ delay: 3700, html: '<div><span class="ok">&#10003;</span> Deployment complete <strong style="color:var(--green)">SUCCESS</strong></div>' }},
        {{ delay: 4300, html: '<div><span class="dim">$</span> <span class="cursor"></span></div>' }},
    ];
    lines.forEach(l => setTimeout(() => {{
        logEl.insertAdjacentHTML('beforeend', l.html);
    }}, l.delay));
</script>
</body>
</html>"""