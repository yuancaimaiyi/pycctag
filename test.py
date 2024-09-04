import time
import pycctag
time1 = time.time()
vector = pycctag.detect_from_file('/home/yuancaimaiyi/testcctag/cube_sfm/cube/frame_000029_perspective_00000000.jpg')
for i in range(len(vector)):
    print(vector[i].id ," ",vector[i].x," ",vector[i].y)
time2 = time.time()
print(time2 - time1)
