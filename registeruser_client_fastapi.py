"""
Author: michaelfeil.eu

"""
from deepface_private import DeepFace
from simple_client_fastapi import get_embedding_from_camera_api, PATH_ENCODED_DB, MODELNAME
from helpers import safe_img_representation
import re
import time
import os
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument("--name", "-n", help="name of user", type=str, default="unknown_registration")
    parser.add_argument("--recordtime", "-r", help="Time to store embeddings as person name from camera", type=int, default=10)
    args = parser.parse_args()

    assert args.name == re.sub(r'[^a-zA-Z0-9_-]', '', args.name), \
        "name can only contain 'a-zA-Z0-9_-' characters"
    start_time = time.time()
    while True:
        camera_represenation = get_embedding_from_camera_api(MODELNAME)
        if (time.time() - start_time) > args.recordtime:
            break
        path = os.path.join(PATH_ENCODED_DB, args.name, f"{args.name}_record_{time.time():.2f}")
        print(f"saving embedding to {path}")
        safe_img_representation(path, camera_represenation)

