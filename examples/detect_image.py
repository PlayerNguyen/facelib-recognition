from facelib import FaceLib

face_lib = FaceLib(download=True)
detect_result = face_lib.detect('./test/assets/face.png')
  
for index, face in enumerate(detect_result):
  print(index, face)
  
# 0 {'box': tensor([190.4473, 131.4462, 397.8910, 410.0258]), 'confidence': tensor([0.5698])}

