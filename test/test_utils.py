from facelib.utils.version import extract_major


def test_extract_version():
  assert extract_major("12.2.2") == "12";