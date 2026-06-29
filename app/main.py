from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    version = "1.0.0"
    heure = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps App</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}

            .card {{
                background: rgba(255, 255, 255, 0.95);
                border-radius: 30px;
                padding: 60px 80px;
                box-shadow: 0 30px 60px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 600px;
                backdrop-filter: blur(10px);
                transition: transform 0.3s ease;
            }}

            .card:hover {{
                transform: scale(1.02);
            }}

            .logo {{
                font-size: 60px;
                margin-bottom: 10px;
            }}

            h1 {{
                color: #2d3748;
                font-size: 32px;
                font-weight: 700;
                margin-bottom: 10px;
            }}

            .subtitle {{
                color: #718096;
                font-size: 16px;
                margin-bottom: 30px;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 20px;
            }}

            .info {{
                display: flex;
                justify-content: space-around;
                gap: 20px;
                flex-wrap: wrap;
            }}

            .info-item {{
                background: #f7fafc;
                padding: 15px 25px;
                border-radius: 15px;
                flex: 1;
                min-width: 120px;
                border: 1px solid #e2e8f0;
            }}

            .info-item .label {{
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 1px;
                color: #a0aec0;
                font-weight: 600;
            }}

            .info-item .value {{
                font-size: 22px;
                font-weight: 700;
                color: #2d3748;
                margin-top: 5px;
            }}

            .version-badge {{
                display: inline-block;
                background: #48bb78;
                color: white;
                padding: 5px 20px;
                border-radius: 50px;
                font-size: 14px;
                font-weight: 600;
                letter-spacing: 0.5px;
                margin-top: 25px;
            }}

            .footer {{
                margin-top: 25px;
                font-size: 13px;
                color: #a0aec0;
            }}

            .status {{
                display: inline-block;
                width: 12px;
                height: 12px;
                background: #48bb78;
                border-radius: 50%;
                margin-right: 8px;
                animation: pulse 2s infinite;
            }}

            @keyframes pulse {{
                0% {{ opacity: 1; }}
                50% {{ opacity: 0.5; }}
                100% {{ opacity: 1; }}
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="logo">🚀</div>
            <h1>DevOps App</h1>
            <p class="subtitle">CI/CD Pipeline Demo</p>

            <div class="info">
                <div class="info-item">
                    <div class="label">📦 Version</div>
                    <div class="value" style="color: #48bb78;">{version}</div>
                </div>
                <div class="info-item">
                    <div class="label">🕒 Heure</div>
                    <div class="value" style="color: #4299e1;">{heure}</div>
                </div>
                <div class="info-item">
                    <div class="label">📅 Date</div>
                    <div class="value" style="color: #ed8936;">{date}</div>
                </div>
            </div>

            <div class="version-badge">
                <span class="status"></span> En ligne
            </div>

            <div class="footer">
                ✅ Déploiement automatique via Jenkins & Docker
            </div>
        </div>
    </body>
    </html>
    """
