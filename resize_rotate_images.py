import os 
import cv2
import numpy as np

src_path = 'my_imgs_hi_res_3'
dest_path = 'my_imgs_rotated_resized_3'
file_names = [file for file in os.listdir(src_path) if file.endswith(('.jpg','.jpeg','.png','.JPG'))]
dim = (800, 480)
for file_name in file_names:
    print(os.path.join(src_path,file_name))
    img = cv2.imread(os.path.join(src_path,file_name))
    if img.shape[0]> img.shape[1]:
        img = np.rot90(img,1)
    img = cv2.resize(img,dim,interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(filename=os.path.join(dest_path,file_name),img=img)
    # cv2.imshow('rotated',img)  
    # cv2.waitKey()
    # cv2.destroyAllWindows() 
