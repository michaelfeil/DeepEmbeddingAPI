import numpy as np
import os
import glob

from deepface_private import DeepFace


def create_encoded_database_from_jpg(
    db_path, dir_decoded="db_decoded", dir_encoded="db_encode", model_name="Facenet"
):
    search_paths = []
    for type_e in ["jpg", "png"]:
        path = os.path.join(db_path, dir_decoded, "**", "*." + type_e)
        search_paths.extend(glob.glob(path, recursive=True))

    for path in search_paths:
        path_orig = path
        # path
        path = path.replace(
            os.sep + dir_decoded + os.sep,
            os.sep + dir_encoded + "_" + model_name + os.sep,
        )

        if os.path.exists(path):
            continue

        img_representation = DeepFace.represent(path_orig, model_name)

        safe_img_representation(path, img_representation)


def safe_img_representation(path, img_representation):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.save(path, np.asarray(img_representation))


if __name__ == "__main__":
    db_path = os.path.expanduser("~/syssec/syssec/Images")
    create_encoded_database_from_jpg(db_path)
