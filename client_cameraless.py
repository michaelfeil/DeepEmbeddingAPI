import numpy as np
import cv2
import os
import glob

from deepface_private import DeepFace
from camera_host import create_encoded_database_from_jpg, get_encoding_from_image

MODEL_NAME = "Facenet"

# db_path
db_path = os.path.expanduser("~/Desktop/syssec/Images")
create_encoded_database_from_jpg(db_path)

# only have access to db_encode_Facenet, not to the original images
path_encoded_db = os.path.join(db_path, "db_encode_"+MODEL_NAME) 
known_representations = glob.glob(os.path.join(path_encoded_db, "**", "*.npy"), recursive=True)

# ask to get an image representation from a dummy image
camera_represenation = get_encoding_from_image(os.path.join(db_path, "search", "Michael_unknown.jpg"), model_name=MODEL_NAME)

# verification from embedding:
print(f"running camera image agaist {known_representations[3]}")
result = DeepFace.verify(img1_path=known_representations[3], img2_path=camera_represenation, model_name=MODEL_NAME)
print(result)

# Re-Identifification from embedding:
result = DeepFace.find(img_path=camera_represenation, db_path=path_encoded_db, model_name=MODEL_NAME)
result.identity = result.identity.str.split(pat=path_encoded_db, n=1, expand=True)[1]
print(result)
pass
