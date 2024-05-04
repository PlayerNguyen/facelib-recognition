from facelib import FaceLib, __version__


def has_version():
  assert __version__ is not None

def test_default_load():
  assert FaceLib is not None
  # Can create a new instance
  faceLib = FaceLib(download=True)
  assert faceLib is not None
 
  
