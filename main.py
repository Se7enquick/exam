import numpy as np
from scipy import ndimage
from scipy.ndimage import convolve
import cv2
import matplotlib.pyplot as plt


def high_freq_filter(image, degree):
    # створення 3х3 високочастотного фільтру
    filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # застосовування фільтру
    filtered_image = convolve(image, filter)

    # нормалізація фільтрованого зображення
    filtered_image = (filtered_image / np.max(filtered_image)) * degree

    return filtered_image

# функція для відображення зображень у зручному форматі

def plot(data, title):
    plot.i += 1
    plt.subplot(2, 2, plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)


plot.i = 0

# Зчитування картинки
image = cv2.imread('cat.jpg', 0)
plot(image, 'Оригінальне зображення')

# застосування фільтру з 20% різкістю(ступеню гостроти)
filtered_image_20 = high_freq_filter(image, 0.2)

plot(filtered_image_20, 'Зображення з ступенем гостроти 20%')
# застосування фільтру з 30% різкістю(ступеню гостроти)
filtered_image_30 = high_freq_filter(image, 0.3)

plot(filtered_image_30, 'Зображення з ступенем гостроти 30')
lowpass = ndimage.gaussian_filter(image, 3)
gauss_highpass = image - lowpass
plot(gauss_highpass, r'Нормалізація зображення з фільтром по Гаусу, sigma = 3 pixels')
plt.savefig('result.jpg')