from tensorflow.keras.utils import img_to_array, load_img
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    width_shift_range= 0.2,
    height_shift_range= 0.2,
    horizontal_flip= True,
    vertical_flip= True,
    shear_range= 0.2,
    zoom_range= 0.2,
    fill_mode= 'nearest')

img = load_img('/home/santo/Project/dataset/5.jpg')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)

i = 0
for batch in datagen.flow(x, batch_size=1,
    save_to_dir='preview', save_prefix='cat', save_format='jpeg'):
    i += 1
    if i > 20:
        break


