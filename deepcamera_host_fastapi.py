"""
Author: michaelfeil.eu

"""

from typing import Optional

from fastapi import FastAPI

from deepface_private import DeepFace
import os
import numpy as np
import cv2

app = FastAPI()

def represent_image(args):
    args.update({"enforce_detection": True})
    try:
        return True, np.asarray(DeepFace.represent(**args), dtype=float)
    except ValueError:
        return False, np.zeros(1, dtype=float)

def take_image():
    camera = cv2.VideoCapture(0, cv2.CAP_V4L)
    if not camera.isOpened():
        print('Unable to load camera.')
        return False
        
    return_value, image = camera.read()
    del(camera)
    return image

# FastAPI app stuff:

@app.get("/")
def read_root():
    return {"DeepFaceAPI": "running"}

@app.get("/camera/{modelname}")
def read_item(modelname: str):
    """request to take image with camera and embed"""
    args = {"model_name": modelname}
    return_dict = {"modelname": modelname, "embedding": [], "success": False, "error": ""}

    camera_image = take_image()
    if not type(camera_image) is np.ndarray:
        return_dict.update({"error": "camera image failed", "success": False})
        return return_dict
    args.update({"img_path": camera_image})

    success, embedding= represent_image(args)
    return_dict.update({"embedding": embedding.tolist(), "success": success})
    return return_dict
    

@app.get("/image/{modelname}")
def read_item(modelname: str, path_load: str):
    """request to take image from storage camera and embed"""
    return_dict = {"modelname": modelname, "embedding": [], "success": False, "error": ""}
    args = {}

    # load from path
    path_load = os.path.expanduser(path_load)
    if os.path.exists(path_load):
        args.update({"img_path": path_load})
    else:
        return_dict.update({"error": f"path {path_load} is not accessible"})
        return return_dict
        
    success, embedding= represent_image(args)
    return_dict.update({"embedding": embedding.tolist(), "success": success})
    return return_dict

