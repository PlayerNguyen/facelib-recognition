from facelib import FaceLib


def test_detection():
  # Yolo
  face_lib = FaceLib(download=True)
  detect_result = face_lib.detect('./test/assets/face.png')
  assert detect_result[0]['box'] is not None
  assert detect_result[0]['confidence'] is not None
  
