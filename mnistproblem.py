import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. Load Data
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# 2. Normalize (0-255 -> 0-1)
train_images, test_images = train_images / 255.0, test_images / 255.0

# 3. Build the Brain
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 4. Compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train
print("Starting Training...")
model.fit(train_images, train_labels, epochs=5)

# 6. Test
print("\nStarting Evaluation...")
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Final Accuracy: {test_acc*100:.2f}%')

# 1. Get ALL the predictions for the test set
all_predictions = model.predict(test_images)

# 2. Find the index where the AI's guess doesn't match the real label
mistakes = []
for i in range(len(test_labels)):
    ai_guess = np.argmax(all_predictions[i])
    if ai_guess != test_labels[i]:
        mistakes.append(i)

# 3. Let's look at the very first mistake
first_mistake_idx = mistakes[0]
plt.imshow(test_images[first_mistake_idx], cmap='gray')
plt.title(f"Real: {test_labels[first_mistake_idx]} | AI thought: {np.argmax(all_predictions[first_mistake_idx])}")
plt.axis('off')
plt.show()

print(f"Total mistakes: {len(mistakes)} out of 10,000")
