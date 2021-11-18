import requests
import json
import os
import time

from deepface_private import DeepFace
from deepface_private.commons.functions import EmbeddingHolder

# Use Facenet from API
MODELNAME = "Facenet"
# Previously requested Embeddings
PATH_ENCODED_DB = os.path.join(
    os.path.expanduser("~/syssec/syssec/Images"), "db_encode_" + MODELNAME
)


def get_embedding_from_camera_api(model_name):
    """request embeddings from API until success"""
    while True:
        print("Request new embedding from api")
        result = requests.get("http://127.0.0.1:8000/camera/" + model_name)
        response = json.loads(result.content)

        if response["success"] == True:
            # got an embedding with a Face
            return EmbeddingHolder(response["embedding"])
        time.sleep(0.1)


if __name__ == "__main__":
    while True:
        # get embedding
        camera_represenation = get_embedding_from_camera_api(MODELNAME)
        print("Got an camera_represenation. Comaring to Database! :)")

        # compare to previous embeddings
        result = DeepFace.find(
            img_path=camera_represenation, db_path=PATH_ENCODED_DB, model_name=MODELNAME
        )

        if result.empty:
            print("No similar emeddings. Face not known! :)")
            continue

        result.identity = result.identity.str.split(
            pat=PATH_ENCODED_DB, n=1, expand=True
        )[1]
        print(result)
