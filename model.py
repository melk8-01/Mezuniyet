from keras.models import load_model

# Modeli yükle
MODEL_PATH = "model/keras_model.h5"
model = load_model(MODEL_PATH, compile=False)

# Label dosyasını oku
class_names = open("model/labels.txt", "r").readlines()

def get_class(image_path, model=model, class_names=class_names):
    from PIL import Image, ImageOps
    import numpy as np

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  # strip() ekledim, gereksiz boşlukları siler
    confidence_score = prediction[0][index]
    return class_name, confidence_score
