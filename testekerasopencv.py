# !/usr/bin/python3
#teste de verificação para imagens em formato 3D

# está com erro no keras

import numpy as np
import cv2
#import image_utils
print(1)
#from keras.applications.vgg16 import VGG16 # tem erro aqui
print(1)
#from keras.layers import Input, Activation, Dropout, Flatten, Dense
#from keras.models import Sequential, Model
print(1)
#from keras.preprocessing import image
import json
from keras.utils.data_utils import get_file
from keras import backend as K

CLASS_INDEX = None
CLASS_INDEX_PATH = 'https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json'


def preprocess_input(x, dim_ordering='default'):
    if dim_ordering == 'default':
        dim_ordering = K.image_dim_ordering()
    assert dim_ordering in {'tf', 'th'}

    if dim_ordering == 'th':
        x[:, 0, :, :] -= 103.939
        x[:, 1, :, :] -= 116.779
        x[:, 2, :, :] -= 123.68
        # 'RGB'->'BGR'
        x = x[:, ::-1, :, :]
    else:
        x[:, :, :, 0] -= 103.939
        x[:, :, :, 1] -= 116.779
        x[:, :, :, 2] -= 123.68
        # 'RGB'->'BGR'
        x = x[:, :, :, ::-1]
    return x


def decode_predictions(preds, top=5):
    global CLASS_INDEX
    if len(preds.shape) != 2 or preds.shape[1] != 1000:
        raise ValueError('`decode_predictions` expects '
                         'a batch of predictions '
                         '(i.e. a 2D array of shape (samples, 1000)). '
                         'Found array with shape: ' + str(preds.shape))
    if CLASS_INDEX is None:
        fpath = get_file('imagenet_class_index.json',
                         CLASS_INDEX_PATH,
                         cache_subdir='models')
        CLASS_INDEX = json.load(open(fpath))
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        result = [tuple(CLASS_INDEX[str(i)]) + (pred[i],) for i in top_indices]
        results.append(result)
    return results


cap = cv2.VideoCapture(1)

while 1:
    print(1)
    ret, img = cap.read()
    """
    print(1)
    imgv = image.load_img(img, target_size=(224, 224))
    print(1)
    imgv = image.img_to_array(imgv)

    print(1)
    imgv = np.expand_dims(imgv, axis=0)
    """
    print(1)
    imgv = preprocess_input(img)
    print(1)
    print("[INFO] loading network...")
    model = VGG16(weights="imagenet")

    preds = model.predict(imgv)
    (enID, nome) = decode_predictions(preds)[0]
    print("ID: {0}, Nome: {1}".format(enID, nome))
    cv2.putText(img, "{}".format(nome), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    print(img)
    cv2.imshow("VIDEO", img)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
