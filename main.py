import tensorflow
import cv2
import numpy as np
import pywhatkit 
import time

def main():
    def notification(frame,ind):

        phone_number = "+91**********"
        caption = 'pest detected'
 
        img_path="detected_pest.jpg"

        cv2.imwrite(img_path,frame)
        model=tensorflow.keras.models.load_model("keras_model.h5")

        frame=cv2.imread(img_path)
        if frame is None:
            return 0

        img = cv2.resize(frame, (224,224))
        img=np.expand_dims(img,axis=0)
        img=img.astype('float32')/255.0
            

        prediction=model.predict(img)

            
        index=np.argmax(prediction[0])
        if (index==ind):
        
            pywhatkit.sendwhats_image(phone_number,img_path, caption)
            return 1
        return 0

    model=tensorflow.keras.models.load_model("keras_model.h5")

    label=[]
    with open ("labels.txt","r") as file:
        label=file.read().splitlines()

    cap=cv2.VideoCapture(0)


    while True:
        ret,frame=cap.read()

        if not ret:
            break

        img = cv2.resize(frame, (224,224))
        img=np.expand_dims(img,axis=0)
        img=img.astype('float32')/255.0
        

        prediction=model.predict(img)

        
        index=np.argmax(prediction[0])
        predicted_label=label[index]
        confidence=prediction[0][index]
        
        
        
        if confidence >0.8  and index >0 :
            print(index)
            
            return_val=notification(frame,index)

            if return_val==1:

                time.sleep(10)
                


        cv2.imshow("camera",frame)

        if cv2.waitKey(1) & 0xFF== 27:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()
