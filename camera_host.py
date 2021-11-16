import numpy as np
import cv2
import os
import glob

from deepface_private import DeepFace

def create_encoded_database_from_jpg(db_path, dir_decoded = "db_decoded", dir_encoded = "db_encode", model_name="Facenet"):
    search_paths = []
    for type_e in ["jpg", "png"]:
        path  = os.path.join(db_path, dir_decoded, "**", "*." + type_e) 
        search_paths.extend(glob.glob(path, recursive=True))

    for path in search_paths:
        path_orig = path
        # path
        path = path.replace(os.sep + dir_decoded + os.sep, os.sep + dir_encoded+"_"+model_name + os.sep)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            continue

        img_representation = DeepFace.represent(path_orig, model_name)
        
        #
        np.save(path, np.asarray(img_representation))

def get_encoding_from_camera(model_name="Facenet") -> np.ndarray:
    camera = cv2.VideoCapture(0, cv2.CAP_V4L)
    if not camera.isOpened():
        print('Unable to load camera.')
    return_value, image = camera.read()
    del(camera)
    return DeepFace.represent(image, model_name)

def get_encoding_from_image(image, model_name="Facenet") -> np.ndarray:
    return np.asarray(DeepFace.represent(image, model_name))
