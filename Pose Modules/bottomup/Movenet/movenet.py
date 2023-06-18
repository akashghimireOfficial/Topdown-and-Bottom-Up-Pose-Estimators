#!/usr/bin/env python
# coding: utf-8

# In[54]:


import tensorflow as tf 
import cv2
import numpy as np
import pandas as pd 




model=tf.saved_model.load('movenet_singlepose_thunder_4')
movenet = model.signatures['serving_default']





def get_keypoints(img):
    input_img=img.copy()
    input_img=cv2.resize(input_img,(256,256))
    input_img=np.array(input_img,dtype='int32')
    input_image = tf.cast(input_img, dtype=tf.int32)
    input_img=tf.convert_to_tensor(input_img)
    input_img=tf.expand_dims(input_img,axis=0)
    outputs=movenet(input_img)
    arr=outputs['output_0'][0][0]
    arr=np.array(arr)
    
    confidence=outputs['output_0'][0][0][:,2]
    features=np.zeros(shape=(17,2),dtype=np.float32)
    for i in range(17):
        conf=confidence[i]
        if conf<=0.12:
            features[i]=np.zeros(shape=(2,),dtype=np.float32)
            df=pd.DataFrame(np.zeros((17,3)),columns=['x','y','confidence'])
        
        else:
            features[i]=arr[i,:2]
            df=pd.DataFrame(arr,columns=['x','y','confidence'])

    features=features.flatten()
    return features,df       



