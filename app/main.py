from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    version = "v1.0.0"
    heure = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%d/%m/%Y")

    return f"""<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Pipeline</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --bg: #0f0f1a;
            --surface: #1a1a2e;
            --surface2: #252540;
            --border: #3a3a5c;
            --text: #e8e8f0;
            --text2: #8888aa;
            --text3: #555577;
            --primary: #ff6b6b;
            --primary-glow: rgba(255, 107, 107, 0.15);
            --green: #51cf66;
            --green-glow: rgba(81, 207, 102, 0.15);
            --orange: #ffa94d;
            --radius: 16px;
            --shadow: 0 20px 60px rgba(0,0,0,0.6);
        }}
        
        [data-theme="light"] {{
            --bg: #f5f5fa;
            --surface: #ffffff;
            --surface2: #ececf5;
            --border: #d0d0dd;
            --text: #1a1a2e;
            --text2: #555577;
            --text3: #9999bb;
            --shadow: 0 20px 60px rgba(0,0,0,0.08);
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1.5rem;
            transition: background .3s, color .3s;
        }}
        
        .dashboard {{
            max-width: 640px;
            width: 100%;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 2rem;
            box-shadow: var(--shadow);
            transition: background .3s, border-color .3s;
        }}
        
        /* Header */
        .dash-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }}
        .dash-title {{
            font-size: 18px;
            font-weight: 700;
            letter-spacing: -0.3px;
        }}
        .dash-title span {{ color: var(--primary); }}
        
        .theme-toggle {{
            background: var(--surface2);
            border: 1px solid var(--border);
            color: var(--text2);
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 12px;
            cursor: pointer;
            transition: .2s;
            font-weight: 500;
        }}
        .theme-toggle:hover {{
            background: var(--border);
            color: var(--text);
        }}
        
        /* Status Bar */
        .status-bar {{
            background: var(--surface2);
            border-radius: 10px;
            padding: 10px 16px;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 13px;
            border: 1px solid var(--border);
        }}
        .status-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 12px var(--green-glow);
            animation: pulse-dot 2s infinite;
        }}
        @keyframes pulse-dot {{
            0%,100% {{ opacity:1; transform:scale(1); }}
            50% {{ opacity:.5; transform:scale(.85); }}
        }}
        .status-label {{ color: var(--text2); }}
        .status-value {{ font-weight: 600; color: var(--green); }}
        
        /* Grid Metrics */
        .grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 1.5rem;
        }}
        .grid-item {{
            background: var(--surface2);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 16px;
            text-align: center;
        }}
        .grid-item .label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text3);
            font-weight: 600;
        }}
        .grid-item .value {{
            font-size: 22px;
            font-weight: 700;
            margin-top: 4px;
            font-feature-settings: "tnum";
        }}
        .value.green {{ color: var(--green); }}
        .value.blue {{ color: var(--primary); }}
        .value.orange {{ color: var(--orange); }}
        
        /* Log / Terminal */
        .log-box {{
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1rem 1.25rem;
            margin-bottom: 1.5rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            min-height: 100px;
            line-height: 1.9;
        }}
        .log-box .line {{ color: var(--text2); }}
        .log-box .ok {{ color: var(--green); }}
        .log-box .cmd {{ color: var(--primary); }}
        .log-box .dim {{ color: var(--text3); }}
        .cursor {{
            display: inline-block;
            width: 7px;
            height: 14px;
            background: var(--text2);
            vertical-align: -2px;
            animation: blink 1s step-end infinite;
        }}
        @keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0}} }}
        
        /* Pipeline progress */
        .pipeline {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            gap: 4px;
        }}
        .step {{
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1;
            font-size: 10px;
            color: var(--text3);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .step .icon {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: var(--surface2);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            margin-bottom: 4px;
            transition: .2s;
        }}
        .step.done .icon {{ background: var(--green-glow); border-color: var(--green); color: var(--green); }}
        .step.active .icon {{ background: var(--primary-glow); border-color: var(--primary); color: var(--primary); }}
        .step-line {{
            flex: 1;
            height: 2px;
            background: var(--border);
            margin-bottom: 18px;
        }}
        .step-line.done {{ background: var(--green); }}
        
        /* Footer */
        .footer {{
            border-top: 1px solid var(--border);
            padding-top: 1rem;
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            color: var(--text3);
        }}
        .footer .tag {{
            background: var(--surface2);
            padding: 4px 12px;
            border-radius: 20px;
            border: 1px solid var(--border);
            font-weight: 500;
            color: var(--text2);
        }}
        .footer .tag span {{ color: var(--primary); }}
    </style>
</head>
<body>
<div class="dashboard">

    <!-- Header -->
    <div class="dash-header">
        <div class="dash-title">🔥 <span>CI/CD</span> Pipeline</div>
        <button class="theme-toggle" onclick="toggleTheme()" id="themeBtn">🌙 Sombre</button>
    </div>

    <!-- Status -->
    <div class="status-bar">
        <div class="status-dot"></div>
        <span class="status-label">Statut :</span>
        <span class="status-value">Déployé</span>
        <span style="margin-left:auto; color:var(--text3);">{version}</span>
    </div>

    <!-- Metrics -->
    <div class="grid">
        <div class="grid-item">
            <div class="label">📦 Version</div>
            <div class="value green">{version}</div>
        </div>
        <div class="grid-item">
            <div class="label">🕒 Heure</div>
            <div class="value blue" id="time">{heure}</div>
        </div>
        <div class="grid-item">
            <div class="label">📅 Date</div>
            <div class="value orange">{date}</div>
        </div>
    </div>

    <!-- Log -->
    <div class="log-box" id="log">
        <div class="line"><span class="dim">$</span> <span class="cmd">docker pull pipeline-app:{version}</span></div>
    </div>

    <!-- Pipeline -->
    <div class="pipeline">
        <div class="step done"><div class="icon">✓</div>Build</div>
        <div class="step-line done"></div>
        <div class="step done"><div class="icon">✓</div>Test</div>
        <div class="step-line done"></div>
        <div class="step done"><div class="icon">✓</div>Image</div>
        <div class="step-line done"></div>
        <div class="step active"><div class="icon">▶</div>Deploy</div>
        <div class="step-line"></div>
        <div class="step"><div class="icon">◉</div>Monitor</div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <span>🔄 auto-deploy · Jenkins + Docker</span>
        <span class="tag"><span>{version}</span></span>
    </div>

</div>

<script>
    // Theme
    function toggleTheme() {{
        const html = document.documentElement;
        const isDark = html.getAttribute('data-theme') === 'dark';
        html.setAttribute('data-theme', isDark ? 'light' : 'dark');
        document.getElementById('themeBtn').textContent = isDark ? '🌙 Sombre' : '☀️ Clair';
        localStorage.setItem('theme', isDark ? 'light' : 'dark');
    }}
    if (localStorage.getItem('theme') === 'light') {{
        document.documentElement.setAttribute('data-theme', 'light');
        document.getElementById('themeBtn').textContent = '☀️ Clair';
    }}

    // Clock
    function pad(n) {{ return String(n).padStart(2,'0'); }}
    setInterval(() => {{
        const now = new Date();
        document.getElementById('time').textContent = pad(now.getHours()) + ':' + pad(now.getMinutes()) + ':' + pad(now.getSeconds());
    }}, 1000);

    // Terminal animation
    const log = document.getElementById('log');
    const lines = [
        {{ delay: 800, html: '<div class="line"><span class="ok">✔</span> <span class="dim">Image pulled (145 MB)</span></div>' }},
        {{ delay: 1600, html: '<div class="line"><span class="dim">$</span> <span class="cmd">docker run -p 8000:8000 pipeline-app</span></div>' }},
        {{ delay: 2400, html: '<div class="line"><span class="ok">✔</span> <span class="dim">Container started [id: c8f4b2]</span></div>' }},
        {{ delay: 3200, html: '<div class="line"><span class="ok">✔</span> <span class="dim">Health check passed — port 8000 OK</span></div>' }},
        {{ delay: 4000, html: '<div class="line"><span class="ok">✔</span> Deployment <strong style="color:var(--green)">SUCCESS</strong></div>' }},
        {{ delay: 4600, html: '<div class="line"><span class="dim">$</span> <span class="cursor"></span></div>' }},
    ];
    lines.forEach(l => setTimeout(() => log.insertAdjacentHTML('beforeend', l.html), l.delay));
</script>
</body>
</html>"""