# from django.shortcuts import render

# Create your views here.

import urllib
from django.shortcuts import render
import numpy as np
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
import matplotlib.pyplot as plt
import cv2

# Create your views here.
class UploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        file = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(file)
        #print(upload_data)
        img = upload_data['url']


        #load models
        keras_model = google_techable_model.model

        # resnet_chest = ResNetModelConfig.model
        # vgg_chest = VGGModelConfig.model
        # inception_chest = InceptionModelConfig.model
        # xception_chest = ExceptionModelConfig.model

        req = urllib.request.urlopen(img)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1) # 'Load it as it is'
        #image = cv2.imread('upload_chest.jpg') # read file 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # arrange format as per keras
        image = cv2.resize(image,(224,224))
        image = np.array(image) / 255
        image = np.expand_dims(image, axis=0)

        googlet_pred = keras_model.predict(image)
        probability = googlet_pred[0]
        #print("Resnet Predictions:")
        if probability[0] > 0.5:
            keras_model_pred = str('%.2f' % (probability[0]*100) + '% Property') 
        else:
            keras_model_pred = str('%.2f' % ((1-probability[0])*100) + '% NonProperty')
        #print(resnet_chest_pred)

        
        # resnet_pred = resnet_chest.predict(image)
        # probability = resnet_pred[0]
        # #print("Resnet Predictions:")
        # if probability[0] > 0.5:
        #     resnet_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
        # else:
        #     resnet_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
        # #print(resnet_chest_pred)

        # vgg_pred = vgg_chest.predict(image)
        # probability = vgg_pred[0]
        # #print("VGG Predictions:")
        # if probability[0] > 0.5:
        #     vgg_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
        # else:
        #     vgg_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
        # #print(vgg_chest_pred)

        # inception_pred = inception_chest.predict(image)
        # probability = inception_pred[0]
        # #print("Inception Predictions:")
        # if probability[0] > 0.5:
        #     inception_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
        # else:
        #     inception_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
        # #print(inception_chest_pred)

        # xception_pred = xception_chest.predict(image)
        # probability = xception_pred[0]
        # #print("Xception Predictions:")
        # if probability[0] > 0.5:
        #     xception_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
        # else:
        #     xception_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
       
             #print(xception_chest_pred)
        return Response({
            'status': 'success',
            'data': upload_data,
            'url':img,
            # 'xception_chest_pred':xception_chest_pred,
            # 'inception_chest_pred':inception_chest_pred,
            # 'vgg_chest_pred':vgg_chest_pred,
            # 'resnet_chest_pred':resnet_chest_pred,
            'keras_model_pred' :keras_model_pred
        }, status=201)


# class CTUploadView(APIView):
#     parser_classes = (
#         MultiPartParser,
#         JSONParser,
#     )

#     @staticmethod
#     def post(request):
#         file = request.data.get('picture')
#         upload_data = cloudinary.uploader.upload(file)
#         #print(upload_data)
#         img = upload_data['url']


#         #load models
#         resnet_chest = ResNetCTModelConfig.model
#         vgg_chest = VGGCTModelConfig.model
#         inception_chest = InceptionCTModelConfig.model
#         xception_chest = ExceptionCTModelConfig.model

#         req = urllib.request.urlopen(img)
#         arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
#         image = cv2.imdecode(arr, -1) # 'Load it as it is'
#         #image = cv2.imread('upload_chest.jpg') # read file 
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # arrange format as per keras
#         image = cv2.resize(image,(224,224))
#         image = np.array(image) / 255
#         image = np.expand_dims(image, axis=0)

#         resnet_pred = resnet_chest.predict(image)
#         probability = resnet_pred[0]
#         #print("Resnet Predictions:")
#         if probability[0] > 0.5:
#             resnet_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
#         else:
#             resnet_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
#         #print(resnet_chest_pred)

#         vgg_pred = vgg_chest.predict(image)
#         probability = vgg_pred[0]
#         #print("VGG Predictions:")
#         if probability[0] > 0.5:
#             vgg_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
#         else:
#             vgg_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
#         #print(vgg_chest_pred)

#         inception_pred = inception_chest.predict(image)
#         probability = inception_pred[0]
#         #print("Inception Predictions:")
#         if probability[0] > 0.5:
#             inception_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
#         else:
#             inception_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
#         #print(inception_chest_pred)

#         xception_pred = xception_chest.predict(image)
#         probability = xception_pred[0]
#         #print("Xception Predictions:")
#         if probability[0] > 0.5:
#             xception_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID') 
#         else:
#             xception_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
#         #print(xception_chest_pred)
#         return Response({
#             'status': 'success',
#             'data': upload_data,
#             'url':img,
#             'xceptionCT_chest_pred':xception_chest_pred,
#             'inceptionCT_chest_pred':inception_chest_pred,
#             'vggCT_chest_pred':vgg_chest_pred,
#             'resnetCT_chest_pred':resnet_chest_pred,
#         }, status=201)
