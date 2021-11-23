# Paper "Enhancing privacy and security in Computer Vision by exposing Deep Learning Embeddings as API"
### Project for Course "Current Topics at System Security Fall 21" at Technical University of Denmark

## 1.1 Installation


clone repository.
```
git clone https://github.com/michaelfeil/DeepEmbeddingAPI.git
```
Have [Anaconda](https://docs.anaconda.com/anaconda/install/linux/) installed.
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

### FAST-API:
start Fast-API app with uvicorn:
```
uvicorn deepcamera_host_fastapi:app --reload
```
The api is now exposed under http://127.0.0.1:8000/ . 
For the API documentation check out http://127.0.0.1:8000/docs


### FAST-API clients applications:
To get embedings go to http://127.0.0.1:8000/camera?modelname=Facenet

sample client application for RE-ID / Reidentification:
```
# In another terminal
conda activate syssec
# place user1 in front of camera for 5 seconds -> register user1
python registeruser_client_fastapi.py --name user1 
# place user2,3,4.. in front of camera for 5 seconds -> register user2
python registeruser_client_fastapi.py --name user2 
# evalute which user is sitting in front of the camera.
python simple_client_fastapi.py
```

## Licence for students outside the Project Group:
Copy or reuse of the parts of code for Submissions at Technical University of Denmark is not allowed.
Paper authors: Michael Feil, Hanna Reß, William Hansen, Kristóf Maár 

## Licence for the deepface_private Fork
See licenceing of deepface in ./deepface_private
