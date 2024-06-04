import numpy as np
from PIL import Image as im 
import serial


image=""
def readimage():
    global iamge
    while s!=True:
        try:
            ser = serial.Serial('/dev/ttyACM0') #znień na swuj port
            s=True
        except:
            s=False
    line = str(ser.readline(), 'UTF-8')
    image=line.split("\n")[0]
    ser.close()

readimage()
image=image.split("[")[1].split("|]")[0]
print(image)
img_tab1=image.split("|")
img_tab2=[]
img_tab2int=[]
img_list=[]
for i in img_tab1:
    img_tab2=i.split(",")
    for j in img_tab2:
        try:
            img_tab2int.append(int(j))
        except:
            pass
    img_list.append(img_tab2int)

print(img_list)
img_array=np.array(img_list)
print(img_array)

# Define the color mode (grayscale for simplicity)
img_mode = "L"

# Create the image from the array
data = im.fromarray(img_array, mode=img_mode)
    
# saving the final output  
# as a PNG file 
data.save('gfg_dummy_pic.png') 



