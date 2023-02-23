import cv2
import os
import time
import uuid
import time

phonemes = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'y', 'z', 'th1', 'th2', 'ng', 'sh', 'ch', 'zh', 'wh', 'a1', 'e1', 'i1', 'o1', 'u1', 'a2', 'e2', 'i2', 'o2', 'u2', 'oo1', 'oo2', 'oy', 'ar1', 'ar2', 'ir', 'or', 'ur']
IMAGES_PATH = "./assets"
number_imgs = 2
label = "b"

args = sys.argv[0]

for phoneme in phonemes[0:1]:
    print(phoneme)
    cap = cv2.VideoCapture(0)
    time.sleep(2)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        file_name = phoneme+"-"+str(uuid.uuid1())+".jpg"
        image_name = os.path.join(IMAGES_PATH, file_name)
        # image_name = os.path.join(IMAGES_PATH,  "asdf.jpg")
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        print(file_name + "created")
    cap.release()
