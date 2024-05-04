import os
import urllib
import urllib.request

from ultralytics import YOLO
from ultralytics import __version__ as YoloVersion

from facelib.detector import Detector
from facelib.utils.version import extract_major


class YoloV8Detector(Detector):
  def __init__(self, download: bool = False, imgsz: int = 192) -> None:
    
    # Check if ultralytics is install with the same version
    major_version = extract_major(YoloVersion)
    if int(major_version) != 8:
      raise "Invalid ultralytics version, please install ultralytics with version 8."
    
    # Load the model
    self.imgsz = imgsz
    self.model = self.__load_model__(download)

  def detect(self, image = any, threshold: float = 0.25):
    faces = []
    
    # We detecting only one image
    # TODO: create an option that allow multiple input
    results = self.model.predict(image, imgsz=self.imgsz, conf=threshold)
    
    if len(results[0].boxes) == 0:
      return faces  

    # Extract boxes
    boxes = map(lambda result: result.boxes, results)
    
    for _, box  in enumerate(boxes): 
      box_dict = dict()
      box_dict["box"] = box.xyxy[0].numpy()
      box_dict["confidence"] = box.conf
      
      faces.append(box_dict)
      del box_dict
    
    return faces
    
  def __load_model__(self, download: bool):
    model_store_directory = os.path.join(os.getcwd(), "models", "yolo")
    model_file_dest = os.path.join(model_store_directory, 'yolov8n-face.pt')
    
    # If the directory model is stored or not.
    if os.path.exists(model_store_directory) is False:
      
      if download == False: 
        raise "Unable to extract model from directory {}. Please use Detector(download=True) to allow download."
      else: 
        # Create a directory
        os.makedirs(model_store_directory, exist_ok=True)
        # Download file
        self.__download_model__(model_file_dest)
    
    # Load model
    print("Loading model from {}".format(model_file_dest))
    return YOLO(model_file_dest)
  
  
  def __download_model__(self, file):
    print("Start downloading yolov8-face models: ")
    
    urllib.request.urlretrieve('https://github.com/akanametov/yolov8-face/releases/download/v0.0.0/yolov8n-face.pt', file)
    