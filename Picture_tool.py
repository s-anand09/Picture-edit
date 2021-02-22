# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:24:39 2021

@author: shrey
"""
def layers(background,overlay,bt,x,y):
    import cv2
    if type(background)==str:
        background=cv2.imread(background)
        overlay=cv2.imread(overlay)
    
    final=background

    thick=bt #border thickness

    #Adding borders
    h_o=len(overlay)
    w_o=len(overlay[1])
    for i in range(0,w_o):
        for j in range(0,thick):
            overlay[0+j,i]=[0,0,0]
            overlay[(h_o-1)-j,i]=[0,0,0]
    for j in range(0,h_o):
        for i in range(0,thick):
            overlay[j,0+i]=[0,0,0]
            overlay[j,(w_o-1)-i]=[0,0,0]

    #Adding images and saving
    for i in range(0,len(overlay)):
        for j in range(0,len(overlay[1])):
            final[y-1+i][x-1+j]=overlay[i][j]
            
    return final



def borders(img,bt):
    import cv2
    if type(img)==str:
        img=cv2.imread(img)
    h_o=len(img)
    w_o=len(img[1])
    for i in range(0,w_o):
        for j in range(0,bt):
            img[0+j,i]=[0,0,0]
            img[(h_o-1)-j,i]=[0,0,0]
    for j in range(0,h_o):
        for i in range(0,bt):
            img[j,0+i]=[0,0,0]
            img[j,(w_o-1)-i]=[0,0,0]
    return img



def crop(img,x1,x2,y1,y2):
    import cv2
    import numpy as np
    
    if type(img)==str:
        img=cv2.imread(img)
        
    size1=y2-y1
    size2=x2-x1
    
    nimg=np.zeros(shape=(size1,size2,3))
    nimg=nimg.astype(np.uint8)
    
    for j in range(0,size1):
        for i in range(0,size2):
            nimg[j,i]=img[y1+j-1,x1+i-1]
    return nimg




def resz(img,x,y):
    import cv2
    
    if type(img)==str:
        img=cv2.imread(img)
        
    imr=cv2.resize(img,(x,y))
    
    return imr



def hattach(img_list):
    import cv2
    n=len(img_list)
    for i in range(0,n):
        if type(img_list[i])==str:
            img_list[i]=cv2.imread(img_list[i])
    im_h=img_list[0]
    for i in range(1,n):
        im_h=cv2.hconcat([im_h,img_list[i]])
    
    return im_h



def vattach(img_list):
    import cv2
    n=len(img_list)
    for i in range(0,n):
        if type(img_list[i])==str:
            img_list[i]=cv2.imread(img_list[i])
    im_v=img_list[0]
    for i in range(1,n):
        im_v=cv2.vconcat([im_v,img_list[i]])
    
    return im_v



def extbord(img,x,y,rgb_list):
    import cv2
    import numpy as np
    
    if type(img)==str:
        img=cv2.imread(img)
        
    h=len(img)
    w=len(img[1])
    
    nx=((x-w)/2)-1
    ny=((y-h)/2)-1   
    
    rgb=[rgb_list[2],rgb_list[1],rgb_list[0]]
    
    nimg=np.zeros(shape=(y,x,3))
        
    for j in range(0,y):
        for i in range(0,x):
            nimg[j,i]=rgb
    
    for j in range(0,h):
        for i in range(0,w):
            nimg[int(j+ny),int(i+nx)]=img[j,i]
    
    return nimg
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    