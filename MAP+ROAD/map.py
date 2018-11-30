import numpy as np
from PIL import ImageGrab
import cv2
import time
from key import PressKey, W, A, S, D,ReleaseKey
m1 = 1.111

def s():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
def r():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)
def l():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def b():
    PressKey(S)
    ReleaseKey(W)
    ReleaseKey(D)
    ReleaseKey(S)
    
    

    
def draw_lines(img, lines):
    m2 = 1.111
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [0,0,255], 5)
            x1 = coords[0]
            y1 = coords[1]
            x2 = coords[2]
            y2 = coords[3]
            if (x1 - x2 ) != 0.0 :
                m1 = (y1 - y2)/(x1 - x2)
            print(" m1 ====",m1," m2 ====",m2)
            if m1 < 0.0 and m2 < 0.0:
                print("left")
                #b()
                s()
                r()
            elif m1 > 0.0 and m2 > 0.0:
                print("right")
                #b()
                s()
                l()
            else:
                print("strait")
                s()
            
            
            m2 = m1
            #print(" x1 ==",x1, " y1 == ",y1," x2 ==",x2," y2== ",y2," and m==== ",m1)
            #i = i + 1
            #print("   i===",i)

    except:
        s()
    #print(lines)
    #if line == None" :
       # print("yes")   
    
    cv2.imshow('windo', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


    

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (3,3), 0 )
    vertices = np.array([[255,250],[425,250], [425,350], [225,350]], np.int32)
    cv2.imshow('windo', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    #cv2.rectangle(original_image, (225,250), (425,350), [255,0,0], 5)
    cv2.line(original_image, (225,250), (425,250), [0,255,0], 2)
    cv2.line(original_image, (425,250), (450,350), [0,255,0], 2)
    cv2.line(original_image, (450,350), (200,350), [0,255,0], 2)
    cv2.line(original_image, (200,350), (225,250), [0,255,0], 2)
    #cv2.imshow('windo', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    processed_img = roi(processed_img, [vertices])
    #cv2.imshow('windo2', processed_img)
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 18, np.array([]), 2, 2)
    draw_lines(original_image,lines)
    return processed_img




while True:
    screen =  np.array(ImageGrab.grab(bbox=(0,40,600,400)))
    new_screen = process_img(screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
















        
