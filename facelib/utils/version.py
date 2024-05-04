

def extract_major(version:str):
  '''
  Extract the major (the most left) number of version. Note that the 
  version will be returned as a string, not a number.
  
  Examples:
  
  ```python
  >> extract_major("12.4.4") # 12
  >> extract_major("0.120.4049") # 0
  ```
  
  
  Returns the major version (the most left) of semver version type from input version as a string.
  '''
  return version.split('.')[0]