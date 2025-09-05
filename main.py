from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    resim = None
    if request.method == "POST":
        f = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(filepath)
        resim = filepath  # Yüklenen fotoğrafı göstermek için
    return render_template("index.html", resim=resim)

if __name__ == "__main__":
    app.run(debug=True) 
