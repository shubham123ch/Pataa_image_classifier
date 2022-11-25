from django.apps import AppConfig
import os
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2
import numpy as np

class ClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classifier'


# added model 
  
class google_techable_model(AppConfig):
    name = 'kerasAPI'
    # MODEL_FILE = os.path.join(settings.MODELS, "property_image_classification/ml/models/keras_model.h5")
    MODEL_FILE = os.path.join(settings.MODELS,"keras_model.h5")
    model = keras.models.load_model(MODEL_FILE)
     
# class ResNetModelConfig(AppConfig):
#     name = 'resnetAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "resnet_chest.h5")
#     model = keras.models.load_model(MODEL_FILE)

# class ResNetCTModelConfig(AppConfig):
#     name = 'resnetCTAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "resnet_ct.h5")
#     model = keras.models.load_model(MODEL_FILE)

# class VGGModelConfig(AppConfig):
#     name = 'vggAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "vgg_chest.h5")
#     model = keras.models.load_model(MODEL_FILE)

# class VGGCTModelConfig(AppConfig):
#     name = 'vggCTAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "vgg_ct.h5")
#     model = keras.models.load_model(MODEL_FILE)    

# class InceptionModelConfig(AppConfig):
#     name = 'inceptionv3_chestAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "inceptionv3_chest.h5")    
#     model = keras.models.load_model(MODEL_FILE)

# class InceptionCTModelConfig(AppConfig):
#     name = 'inceptionv3_chestCTAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "inception_ct.h5")    
#     model = keras.models.load_model(MODEL_FILE)    

# class ExceptionModelConfig(AppConfig):
#     name = 'xception_chestAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "xception_chest.h5")    
#     model = keras.models.load_model(MODEL_FILE)

# class ExceptionCTModelConfig(AppConfig):
#     name = 'xception_chestCTAPI'
#     MODEL_FILE = os.path.join(settings.MODELS, "xception_ct.h5")    
#     model = keras.models.load_model(MODEL_FILE)    

    
    # end added model 