import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 模型定义
def create_model():
    model = Sequential([
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')  # 假设有10种不同的UI元素
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# 训练模型
def train_model():
    model = create_model()
    datagen = ImageDataGenerator(rescale=1./255)
    train_data = datagen.flow_from_directory('data/training_data/', target_size=(64, 64), batch_size=32, class_mode='categorical')
    model.fit(train_data, epochs=10)
    model.save('data/models/ai_model.h5')

if __name__ == "__main__":
    train_model()
