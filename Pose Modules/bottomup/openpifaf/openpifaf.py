#!/usr/bin/env python
# coding: utf-8

# In[60]:


import torch 
import numpy as np 
import openpifpaf
import cv2
from PIL import Image
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler


# In[61]:


predictor = openpifpaf.Predictor(checkpoint='shufflenetv2k30')
scaler=MinMaxScaler()


# In[55]:


def get_features_df(img):
    img_pil = Image.fromarray(img)
    predictions, gt_anns, image_meta = predictor.pil_image(img_pil)
    num_people=len(predictions)
    if num_people == 1:
        features=predictions[0].data
        df=DataFrame(features,columns=['x','y','confidence'])
        features=features[:,:2]
        scaled_features=scaler.fit_transform(features)
        scaled_features=scaled_features.flatten()
        return num_people,scaled_features
    else:
        return num_people,np.zeros(34,dtype=np.float32)
    

