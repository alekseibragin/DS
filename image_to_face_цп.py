# устанавливаем пакеты
#pip3 install opencv-python numpy

# import required module
import os
import cv2
import  numpy as  np
global file_path
# assign directory
directory = './1'
# существенно здесь положение лица на фотографии, чем более фронтально оно расположено тем лучше распознование

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1) #
    return cv_img


def cv_res(file_path):
    # функция imread() загружает изображение из указанного файла  и возвращает N-мерный массив
    image = cv_imread(file_path)

    # Функция детектор ожидает получить черно белое изображение, и поэтому отформатируем image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # следующим этапом необходимо загрузить файл haarcascade_fontalface_default.xml либо если он установлен найти и прописать полный путь к нему или переместить в папку с нашим скриптом.  
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # функция detectMultiScale() принимает изображения, определяет искомые объекты и возвращает список прямоугольных областей  
    faces = face_cascade.detectMultiScale(image_gray)

    print(str(len(faces)) + "  faces detected in the image.")

    # обведем каждое обнаруженное лицо синим прямоугольником
    for x, y, width, height in faces:
        #cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
        roi_color = image_gray[y:y+height, x:x+width]

        # сохраним полученное изображение
        cv2.imwrite(str(file_path)+"_new"+".jpg", roi_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    return


  
# itrate over files in 
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.path)
        cv_res(filename.path)