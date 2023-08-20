import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image #library to help open images

picture = Image.open('./KOA_Nassau_2697x1517.jpg') 

print(type(picture))    
#picture.show()     #to display the image
print(picture.size)

pic_arr = np.asarray(picture)   #converts the image to an array of values
#print(pic_arr.shape)   #guess shape

#plt.imshow(pic_arr)  #shows images when input data is of arrays
#plt.show()


#pic_arr_red = pic_arr[:,:,0]       #give task to capture one particular color channel
#plt.imshow(pic_arr_red)
#plt.show() 

pic_arr_second = Image.open("./ac-color-shuffle-2-bgra-1.jpg")
nparray = np.asarray(pic_arr_second)

plt.imshow(nparray[:,:,0])
plt.show()
#print(nparray[:,:,:])

npcopy = nparray.copy()
npcopy.flags.writeable = True   #if numpy array is not writeable
npcopy[:,:,2] = 0
npcopy[:,:,1] = 0
plt.imshow(npcopy)
plt.show()