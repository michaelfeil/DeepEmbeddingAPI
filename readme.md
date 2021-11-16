# Project for Course "Current Topics at System Security Fall 21" at Technical University of Denmark

## 1.1 Installation
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
Running the live demo
```
conda activate syssec
python client_cameraless.py
```

## Licence for students outside the Project Group:
Copy or reuse of the parts of code for Submissions at Technical University of Denmark is not allowed.
