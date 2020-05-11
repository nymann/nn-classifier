import numpy
from keras_preprocessing import image
from matplotlib import pyplot
from tensorflow import keras
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.losses import BinaryCrossentropy

from weeb_classifier.neural_net.training_data import TrainingData

CLASS_NAMES = ['Not-weeb', 'Weeb']


class NeuralNetwork:
    trained = False

    def __init__(self):
        self.img_size = 150
        self.model = self._get_model()

    def train(self, td: TrainingData = None, epochs=20):
        """
        Args:
            td (TrainingData):
            epochs:
        """
        if td is None:
            td = TrainingData("/home/knj/code/github/weeb-purger/nn-classifier/dataset/training",
                              "/home/knj/code/github/weeb-purger/nn-classifier/dataset/validation")

        history = self.model.fit(
            td.train_data_gen,
            steps_per_epoch=td.total_training_images // td.batch_size,
            epochs=epochs,
            validation_data=td.val_data_gen,
            validation_steps=td.total_validation_images // td.batch_size
        )

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        pyplot.figure(figsize=(8, 8))
        pyplot.subplot(1, 2, 1)
        pyplot.plot(epochs_range, acc, label='Training Accuracy')
        pyplot.plot(epochs_range, val_acc, label='Validation Accuracy')
        pyplot.legend(loc='lower right')
        pyplot.title('Training and Validation Accuracy')

        pyplot.subplot(1, 2, 2)
        pyplot.plot(epochs_range, loss, label='Training Loss')
        pyplot.plot(epochs_range, val_loss, label='Validation Loss')
        pyplot.legend(loc='upper right')
        pyplot.title('Training and Validation Loss')
        pyplot.show()
        self.model.save("/tmp/weeb_model")
        self.trained = True

    def solve(self, image_path: str, confidence_level: int = 500):
        if not self.trained:
            self.train()
        img = image.load_img(image_path, target_size=(self.img_size, self.img_size))
        img = image.img_to_array(img)
        img = numpy.expand_dims(img, axis=0)
        pred = (self.model.predict(img) > confidence_level).astype("int32")[0][0]
        # return CLASS_NAMES[pred]
        return pred

    def _get_model(self):
        try:
            model = keras.models.load_model("/tmp/weeb_model")
            self.trained = True
        except IOError:
            model = Sequential([
                Conv2D(16, 3, padding='same', activation='relu',
                       input_shape=(self.img_size, self.img_size, 3)),
                MaxPooling2D(),
                Conv2D(32, 3, padding='same', activation='relu'),
                MaxPooling2D(),
                Conv2D(64, 3, padding='same', activation='relu'),
                MaxPooling2D(),
                Flatten(),
                Dense(512, activation='relu'),
                Dense(1)
            ])
            model.compile(optimizer='adam',
                          loss=BinaryCrossentropy(from_logits=True),
                          metrics=['accuracy'])
            model.summary()
        return model
