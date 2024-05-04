__version__ = "0.0.1-a1"


class FaceLib:
  def __init__(self, detector_backend="yolov8", download: bool = False) -> None:
    self.detector_backend = detector_backend
    self.download = download
    
    self.detector = self.__load_detector__(detector_backend, download)

  def detect(self, image: any, threshold: float = 0.4):
    if self.detector_backend is None:
      raise "detector_backend parameter cannot be none"
    
    return self.detector.detect(image, threshold)
    
    
  def __load_detector__(self, name: str, download: bool):
    print("Load detector {} (download={})".format(name, download))
    if name == 'yolov8':
      from facelib.detector import yolov8
      return yolov8.YoloV8Detector(download=download)
    if name == 'mtcnn':
      from facelib.detector import mtcnn
      return mtcnn.MtCnnDetector(download=download)
    else :
      # Default detector: yolov8
      from facelib.detector import yolov8
      return yolov8.YoloV8Detector(download=download)
