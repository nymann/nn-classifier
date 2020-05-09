import os

from PIL import ImageFile
from keras_preprocessing.image import ImageDataGenerator
from matplotlib.pyplot import tight_layout, show, subplots
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class TrainingData:
    def __init__(self, training_dir: str, validation_dir: str, img_size: int = 150):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        # The training data will take the form of [[img, label],[img, label]...]
        self.train_weeb_dir = os.path.join(training_dir, "weeb")
        self.train_not_dir = os.path.join(training_dir, "not")

        self.weeb_training_pics = len(os.listdir(self.train_weeb_dir))
        self.not_training_pics = len(os.listdir(self.train_not_dir))
        self.total_training_images = self.weeb_training_pics + self.not_training_pics
        print("Total training weeb pics:", self.weeb_training_pics)
        print("Total training not-weeb pics:", self.not_training_pics)

        self.validation_weeb_dir = os.path.join(validation_dir, "weeb")
        self.validation_not_dir = os.path.join(validation_dir, "not")

        self.weeb_validation_pics = len(os.listdir(self.validation_weeb_dir))
        self.not_validation_pics = len(os.listdir(self.validation_not_dir))
        self.total_validation_images = self.weeb_validation_pics + self.not_validation_pics
        print("Total validation weeb pics:", self.weeb_validation_pics)
        print("Total validation not-weeb pics:", self.not_validation_pics)

        self.batch_size = 256
        self.epochs = 10
        self.img_height = img_size
        self.img_width = img_size

        train_image_generator = ImageDataGenerator(
            rescale=1. / 255)  # Generator for our training data
        validation_image_generator = ImageDataGenerator(
            rescale=1. / 255)  # Generator for our validation data

        self.train_data_gen = train_image_generator.flow_from_directory(
            batch_size=self.batch_size,
            directory=training_dir,
            shuffle=True,
            target_size=(
                self.img_height,
                self.img_width),
            class_mode='binary')

        self.val_data_gen = validation_image_generator.flow_from_directory(
            batch_size=self.batch_size,
            directory=validation_dir,
            target_size=(
                self.img_height,
                self.img_width),
            class_mode='binary')

        sample_training_images, _ = next(self.train_data_gen)

        self.plot_images(sample_training_images[:5])

    def plot_images(self, images_arr):
        fig, axes = subplots(1, 5, figsize=(20, 20))
        axes = axes.flatten()
        for img, ax in zip(images_arr, axes):
            ax.imshow(img)
            ax.axis('off')
        tight_layout()
        show()
