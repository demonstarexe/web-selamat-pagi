from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    nama = request.args.get("nama", "Kamu")
    jam = datetime.now().hour

    if jam < 11:
        salam = "Selamat Pagi ☀️"
    elif jam < 15:
        salam = "Selamat Siang 🌤️"
    elif jam < 18:
        salam = "Selamat Sore 🌅"
    else:
        salam = "Selamat Malam 🌙"

    return f"""
    <html>
    <head>
        <title>Untuk Kamu ❤️</title>
        <style>
            body {{
                background: linear-gradient(135deg, #ffdde1, #ee9ca7);
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 20px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{salam}, {nama} ❤️</h1>
            <p>Semoga harimu indah dan penuh senyum 😊</p>
            <p><b>— Dari aku</b></p>
        </div>
    </body>
    </html>
    """

app.run()
