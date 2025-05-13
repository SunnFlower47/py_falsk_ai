from groq import Groq

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

AI_KEY = "masukkan_api_key_disini" 

client = Groq(api_key=AI_KEY)

def ai_call(year):
    try:
        cahat_competition = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content":f"berikan saya 1 fakta teknologi menarik di tahun {year}  dan jelaskan dalam bahsa indonesia. "
                }

            ],
            model="masukkan_model_ai_disini",
            stream=False,
        )

        ai_output = cahat_competition.choices[0].message.content
        return ai_output

    except Exception as e:
        print(f"Error during AI call: {e}")
        return "Error: Tidak dapat menghubungi AI. Silakan coba lagi nanti."
    
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/usia', methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        # Ambil data dari form
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir

        # Panggil fungsi AI
        ai_output = ai_call(tahun_lahir)

        print(ai_output)

        return render_template('cek_usia.html', usia=usia, tahun_lahir=tahun_lahir, ai_output=ai_output)
    return render_template('cek_usia.html', usia= None)

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5020)
