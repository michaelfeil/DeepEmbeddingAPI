from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from deepface_private import DeepFace
import os
import numpy as np
import cv2

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

def represent_image(args):
    args.update({"enforce_detection": True})
    try:
        return True, np.asarray(DeepFace.represent(**args), dtype=float)
    except ValueError:
        return False, np.zeros(128, dtype=float)
    return np.asarray(DeepFace.represent(**args))

def take_image():
    camera = cv2.VideoCapture(0, cv2.CAP_V4L)
    if not camera.isOpened():
        print('Unable to load camera.')
    return_value, image = camera.read()
    del(camera)
    return image

# app:

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/camera/{modelname}")
def read_item(modelname: str):
    camera_image = take_image()

    args = {"img_path": camera_image}
    if modelname is not None:
        args.update({"model_name": modelname})
    success, embedding= represent_image(args)
    print(embedding.shape)
    return {"modelname": modelname, "embedding": embedding.tolist(), "success": success}

@app.get("/image/{modelname}")
def read_item(modelname: str):
    args = {"img_path": os.path.expanduser("~/syssec/syssec/Images/search/Michael_unknown.jpg")}
    
    if modelname is not None:
        args.update({"model_name": modelname})
        
    success, embedding= represent_image(args)
    print(embedding.shape)
    return {"modelname": modelname, "embedding": embedding.tolist(), "success": success}

