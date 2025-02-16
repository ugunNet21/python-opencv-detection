
## Struktur

````
hand-detection/
├── face/
│   ├── caffe.py
│   ├── cascades.py
│   ├── deploy.prototxt
│   └── res10_300x300_ssd_iter_140000.caffemodel
├── hand-detect/
│   └── hand-detection.py
├── yolo/
│   ├── coco.names
│   ├── yolo.py
│   ├── yolov3.cfg
│   └── yolov3.weights
├── .gitignore
├── .gitattributes
└── README.md

````

## run python

- python3 -m venv venv
- source venv/bin/activate
- pip install mediapipe opencv-python
- python hand-detection.py

## yolo dan face

- pip install opencv-python numpy tensorflow
- sudo apt install libqt5gui5

## clear cache
- git rm --cached yolo/yolov3.weights


````
- https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg
- https://github.com/pjreddie/darknet/blob/master/data/coco.names
- https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights

````