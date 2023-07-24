import pywt
import cv2
import numpy as np
import base64
import json,joblib

__class_name_to_number=None
__class_number_to_name=None
__model=None


def classify_image(image_base64_data=None,file_path=None):
    imgs=get_cropped_img_2_eyes(file_path,image_base64_data)
    result=[]
    for img in imgs:
        scaled_raw_img=cv2.resize(img,(32,32))
        img_har=w2d(img,'db1',5)
        scaled_img_har=cv2.resize(img_har,(32,32))
        combined_img=np.vstack((scaled_raw_img.reshape(32*32*3,1),scaled_img_har.reshape(32*32*1,1)))
        len_image_array=32*32*3+32*32*1
        try:
            final=combined_img.reshape(1,len_image_array).astype(float)
            result.append({
                'class':__model.predict(final)[0],
                'class_probability':np.round(__model.predict_proba(final)*100,2).tolist()[0],
                'class_dictionary':__class_name_to_number
                })
            return result
        except Exception as e:
            print("Face in Image too small..cannot resize image to required size ")
            print(e)

def load_saved_artifacts():
    print("Loading artifacts.....")
    global __class_name_to_number
    global __class_number_to_name

    with open('./server/artifacts/class_dictionary.json','r') as f:
        __class_name_to_number=json.load(f)
        __class_number_to_name={v:k for k,v in __class_name_to_number.items()}
    global __model
    if __model is None:
        with open('./server/artifacts/saved_model.pkl','rb') as f:
            __model=joblib.load(f)
    print("loading artifacts done")

def w2d(img,mode='haar',level=1):

    imArray=img

    imArray=cv2.cvtColor(imArray,cv2.COLOR_BGR2GRAY)
    imArray=np.float32(imArray)
    imArray/=255

    coeff=pywt.wavedec2(imArray,mode,level=level)

    coeff_H=list(coeff)
    coeff_H[0]*=0

    imArray_H= pywt.waverec2(coeff_H,mode)
    imArray_H*=255
    imArray_H=np.uint8(imArray_H)
    
    return imArray_H


def get_cv2_image_from_base64(b64str):
    encoded_data=b64str.split(',')[1]
    nparr=np.frombuffer(base64.b64decode(encoded_data),np.uint8)
    img=cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    return img

def get_cropped_img_2_eyes(image_path=None,image_base64_data=None):
    face_cascade=cv2.CascadeClassifier('./server/opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade=cv2.CascadeClassifier('./server/opencv/haarcascades/haarcascade_eye.xml')
    if image_path:
        img=cv2.imread(image_path)
    else:
        img=get_cv2_image_from_base64(image_base64_data)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    cropped_faces=[]
    for (x,y,w,h) in faces:
        roi_gray= gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes= eye_cascade.detectMultiScale(roi_gray)
        if len(eyes)>=2:
            cropped_faces.append(roi_color)
    return cropped_faces

def get_b64_test_image():
    with open("./server/b64.txt") as f:
       return f.read()


if __name__=="__main__":
    load_saved_artifacts()
    # print(classify_image(get_b64_test_image(),None))
    # print(classify_image(None,'./model/dataset/lionel_messi/messiface.jpg'))
