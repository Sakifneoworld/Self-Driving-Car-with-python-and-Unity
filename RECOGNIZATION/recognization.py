import cv2
import numpy as np
from PIL import ImageGrab
from key import PressKey, W, A, S, D,ReleaseKey
import time

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


img = cv2.imread('1.png',0)
#w, h = img.shape[::-1]

font = cv2.FONT_HERSHEY_SIMPLEX






def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked








a = 10

while True:
    game = np.array(ImageGrab.grab(bbox =(0,40,600,400)))
    game = cv2.cvtColor(game, cv2.COLOR_BGR2RGB)
    game_black = cv2.cvtColor(game, cv2.COLOR_BGR2GRAY)
    

    
    res = cv2.matchTemplate(game_black, img, cv2.TM_CCOEFF_NORMED)
    
    s()


    match = 0.85
    loc = np.where(res >= match)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(game, pt, (pt[0]+50, pt[1]+100), (255,0,0), 2)
        #for i in 1...1000:
        b()
        #b()
        #b()
        
        cv2.putText(game,'RED LIGHT',(pt[0],pt[1]), font, 1, (0,0,255), 1, cv2.LINE_AA)
        #time.sleep(.5)


    cv2.imshow('BLACK',game)




    
    cv2.imwrite('red.png',game_black)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break











    
