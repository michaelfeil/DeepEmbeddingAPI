# Project for Course "Current Topics at System Security Fall 21" at Technical University of Denmark

## 1.1 Installation
Have [conda](https://docs.anaconda.com/anaconda/install/linux/) installed.
create new conda enviroment `syssec` using anaconda
```
conda env create --file ./environment.yml
conda activate syssec
pip install -e ./deepface_private
```

## 1.2 keeping up to date
periodically updated the dependencies on changes:
```
conda activate syssec
conda env update --file environment.yml --prune
```

## 2. Usage

## FAST-API:
start Fast-API app with uvicorn:
```uvicorn deepcamera_host_fastapi:app --reload```

run client application
```
conda activate syssec
# place user1 in front of camera for 5 seconds -> register user1
python registeruser_client_fastapi.py --name mister_x 
# place user2 in front of camera for 5 seconds -> register user2
python registeruser_client_fastapi.py --name miss_y 
# evalute which user is sitting in front of the camera.
python simple_client_fastapi.py
```

## Licence for students outside the Project Group:
Copy or reuse of the parts of code for Submissions at Technical University of Denmark is not allowed.

## Licence for the deepface_private Fork
See licenceing of deepface in ./deepface_private