

from facelib.detector import Detector


class MtCnnDetector(Detector):
  def __init__(self, download: bool = False) -> None:
    super().__init__(download)
    
    from facenet_pytorch import MTCNN
    self.model = MTCNN(image_size=480)
    
  def detect(self, image=..., threshold: float = 0.76) -> any:
    faces, probs = self.model.detect(image)
    if faces is None:
      return []
    
    responses = []
    for face, prob in zip(faces, probs):
      print(face, prob)
      response_item = dict()
      
      response_item["box"] = face;
      response_item["confidence"] = probs
      
      responses.append(response_item)
      del response_item
      
    return responses
  