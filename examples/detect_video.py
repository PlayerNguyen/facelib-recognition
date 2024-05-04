import time
import tracemalloc

import cv2

from facelib import FaceLib

'''
This example will detect the first face that appear on your camera (if accessible)
and draw a bounding box around it.
'''
def main():
    

  detector = FaceLib("mtcnn", download=True)

  vid = cv2.VideoCapture(0) 
  width  = vid.get(cv2.CAP_PROP_FRAME_WIDTH)   
  height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)  

  fps = vid.get(cv2.CAP_PROP_FPS)
  print("Maximun fps: {}".format(fps))


  prev_frame_time = 0
  new_frame_time = 0

  while(True): 
      ret, frame = vid.read() 
      # Down scale frame
      scaled_down_img = cv2.resize(frame, dsize=(round(width * .1), round(height * .1)))
    
      result = detector.detect(scaled_down_img)
      
      # Draw box for the first face
      if len(result) > 0:
        for box in result:
          x, y, x1, y1 = list(map(lambda v: int(v) * 10, result[0]["box"]))
          print("Confidence: {}".format(result[0]["confidence"]))
          print(x, y, x1, y)
          # Crop and store the capture image
          cropped_img = frame[y:y1, x:x1]
          # cv2.imshow("Face", cropped_img)
          
          cv2.imwrite("./examples/results/{}.png".format(round(time.time_ns() * 10e7)), cropped_img)
          
          # Draw a frame
          frame = cv2.rectangle(frame, color=(255, 0, 0), pt1=(x, y), pt2=(x1, y1), thickness=2)

      # Frame capture
      new_frame_time = time.time()   
      fps = 1/(new_frame_time-prev_frame_time) 
      prev_frame_time = new_frame_time 
      fps = str(int(fps))
      
      cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2, cv2.LINE_AA)
      
      print("Current fps: {}".format(fps))
      current, peak = tracemalloc.get_traced_memory()
      print("Memory [current: {:3f} GBytes, peak: {:3f} GBytes]".format(current*10e-9, peak*10e-9))
      cv2.imshow('frame', frame) 
    
      if cv2.waitKey(1) & 0xFF == ord('q'): 
          break
    
  vid.release() 
  cv2.destroyAllWindows()
  
if __name__ == "__main__":
  tracemalloc.start()
  main()
  tracemalloc.stop()