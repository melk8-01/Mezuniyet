from flask import Flask, render_template, request
import os
from model import get_class  # model.py'den tahmin fonksiyonunu import ediyoruz

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    resim = None
    tahmin = None
    confidence = None

    if request.method == "POST":
        f = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(filepath)
        resim = filepath  # Yüklenen fotoğrafı göstermek için

        # Artık sadece 1 parametre gönderebilirsin, çünkü model ve class_names default tanımlı
        tahmin, confidence = get_class(filepath)
        confidence = round(confidence * 100, 2)

    return render_template("index.html", resim=resim, tahmin=tahmin, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
