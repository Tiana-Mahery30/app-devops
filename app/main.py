from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    version = "v1.0.1"
    heure = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%d/%m/%Y")

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App - Carte</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #f0f2f5;
            padding: 1.5rem;
        }}

        .card {{
            max-width: 440px;
            width: 100%;
            background: #ffffff;
            border-radius: 24px;
            padding: 2.5rem 2rem;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
            border: 1px solid #e8ecf0;
            transition: 0.2s;
        }}

        .card:hover {{
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
        }}

        .badge {{
            display: inline-block;
            font-size: 11px;
            font-weight: 500;
            letter-spacing: 0.5px;
            color: #ffffff;
            background: #2d3748;
            padding: 4px 14px;
            border-radius: 30px;
            margin-bottom: 1.5rem;
        }}

        .title {{
            font-size: 26px;
            font-weight: 600;
            color: #1a202c;
            letter-spacing: -0.3px;
            margin-bottom: 0.25rem;
        }}

        .subtitle {{
            font-size: 15px;
            font-weight: 400;
            color: #718096;
            margin-bottom: 2rem;
        }}

        .divider {{
            height: 1px;
            background: #e2e8f0;
            margin-bottom: 1.5rem;
        }}

        .info-grid {{
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}

        .info-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 15px;
            padding: 0.5rem 0;
            border-bottom: 1px solid #f0f2f5;
        }}

        .info-row:last-child {{
            border-bottom: none;
        }}

        .info-label {{
            color: #718096;
            font-weight: 400;
        }}

        .info-value {{
            color: #1a202c;
            font-weight: 500;
            font-feature-settings: "tnum";
        }}

        .info-value.version {{
            color: #2b6cb0;
            font-weight: 600;
        }}

        .footer-note {{
            margin-top: 2rem;
            text-align: center;
            font-size: 12px;
            color: #a0aec0;
            letter-spacing: 0.3px;
            border-top: 1px solid #e2e8f0;
            padding-top: 1.25rem;
        }}

        .status-dot {{
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #38a169;
            border-radius: 50%;
            margin-right: 6px;
            animation: pulse-dot 2s infinite;
        }}

        @keyframes pulse-dot {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.5; transform: scale(0.85); }}
        }}

        .status-text {{
            display: inline-flex;
            align-items: center;
            font-size: 13px;
            color: #38a169;
            font-weight: 500;
        }}
    </style>
</head>
<body>

<div class="card">
    <div class="badge">CI/CD</div>
    <div class="title">Pipeline Demo</div>
    <div class="subtitle">Application de démonstration</div>

    <div class="divider"></div>

    <div class="info-grid">
        <div class="info-row">
            <span class="info-label">Version</span>
            <span class="info-value version">{version}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Heure</span>
            <span class="info-value">{heure}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Date</span>
            <span class="info-value">{date}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Statut</span>
            <span class="info-value">
                <span class="status-dot"></span>
                <span class="status-text">Opérationnel</span>
            </span>
        </div>
    </div>

    <div class="footer-note">
        Automatisation via Jenkins et Docker
    </div>
</div>

</body>
</html>"""