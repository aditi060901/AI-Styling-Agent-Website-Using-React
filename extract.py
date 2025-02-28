from PIL import Image 
import numpy as np
from numpy.linalg import norm 
import tensorflow
import cv2
import os
import glob
import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tqdm import tqdm
#from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import euclidean




path="C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\sample_bot\\*.*"
x=1
for im in glob.glob(path):
    img=cv2.imread(im)
    img=cv2.resize(img,(224,224))
    denoised = cv2.medianBlur(img, 5)
    normalized_image = cv2.normalize(
    denoised, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    cv2.imwrite("C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\processed_bot\\b%d.png" % x,normalized_image)
    x=x+1

path="C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\sample_top\\*.*"
x=1
for im in glob.glob(path):
    img=cv2.imread(im)
    img=cv2.resize(img,(224,224))
    denoised = cv2.medianBlur(img, 5)
    normalized_image = cv2.normalize(
    denoised, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    cv2.imwrite("C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\processed_top\\t%d.png" % x,normalized_image)
    x=x+1


path1="C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\processed_top\\*.*"
path2="C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\processed_bot\\*.*"

k=1
for im in glob.glob(path1):
    img1=cv2.imread(im)
    for im1 in glob.glob(path2):
        img=cv2.imread(im1)
        cv2.imwrite('C:\\Users\\aditi\\OneDrive\\Desktop\\AIStyling Agent\\comb\\bt%d.png' %k, cv2.vconcat([img1, img]))
        k=k+1

feat_list=np.array(pickle.load(open('features.pkl','rb')))
fname=pickle.load(open('filenames.pkl','rb'))

