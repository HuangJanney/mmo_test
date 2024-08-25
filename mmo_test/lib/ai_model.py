import tensorflow as tf
from tensorflow.keras.models import load_model

# 加载模型
model = load_model('data/models/ai_model.h5')

# 使用模型进行预测
def predict_ui_action(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(64, 64))
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_array = tf.expand_dims(img_array, 0)  # 增加batch维度

    predictions = model.predict(img_array)
    predicted_class = tf.argmax(predictions[0])
    return predicted_class.numpy()
