import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import cv2
st.set_option('deprecation.showfileUploaderEncoding', False)

html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing Lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Collor Palette
         """
         )

img = np.zeros((200,200,3), np.uint8)
G = st.slider('G', min_value=0, max_value=255, step=1)

def import_and_predict(image_data):
  #img = image.load_img(image_data, target_size=(224, 224))
  #image = image.img_to_array(img)
  #img_reshap= np.expand_dims(image, axis=0)
  #img_reshap = preprocess_input(img_reshap)
   
  image_data[:] = [0,G,0]
  st.image(image_data, use_column_width=True)
  return 0


#st.image(img,caption='Black Image.', use_column_width=True)
    
if st.button("Change Color"):
  result=import_and_predict(img)
  
if st.button("About"):
  st.header(" Jatin Tak")
  st.subheader("Student, Department of Computer Engineering")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing Experiment</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
