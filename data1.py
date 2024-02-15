import pandas as pd
import numpy as np
import cv2
import os
def display_image(image):
    while True:
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 900, 900)
        cv2.imshow('image', image)
        k = cv2.waitKey(0)
        if k %256 == 32:
            cv2.destroyAllWindows()
            break
root = r'New Plant Diseases Dataset(Augmented)\New Plant Diseases Dataset(Augmented)\train'
all_dir = os.listdir(root)
crops = []
disease = []
number_of_images = []
for dir in all_dir:
    crops.append(dir.split('__')[0])
    disease_name = dir.split('__')
    disease.append(''.join(element[1:] if element.startswith('_') else element for element in disease_name))
    #breakpoint()
    number_of_images.append(len(os.listdir(os.path.join(root, dir))))
crops1= crops
data1 = pd.DataFrame(data = [crops, disease, number_of_images]).T

root = r'CCMT_FInal Dataset/'
all_dir = os.listdir(root)
crops = []
disease = []
number_of_images = []
for dir in all_dir:
    crops.append(dir.split('_')[0])
    disease_name = dir.split('_')
    disease.append(''.join(element[1:] if element.startswith('_') else element for element in disease_name))
    #breakpoint()
    number_of_images.append(len(os.listdir(os.path.join(root, dir))))
crops2 = crops

commoncrops = []
for crop in crops1:
    if crop in crops2:
        commoncrops.append(crop)
data2 = pd.DataFrame(data = [crops, disease, number_of_images]).T

final_df = pd.concat([data1, data2], axis = 0, ignore_index= True, sort= True) 
final_df.columns = ['crops', 'disease', 'number of images']
grouped_df = final_df.groupby('crops').apply(lambda group: group.reset_index(drop=True))
grouped_counts = final_df.groupby('crops')['disease'].nunique().reset_index(name='unique_counts')
final_df_merged = pd.merge(final_df, grouped_counts, on='crops')
grouped_df = final_df_merged.groupby('crops').apply(lambda group: group.reset_index(drop=True))
breakpoint()

if __name__ == '__main__':
    image = cv2.imread('rice+leaf+diseases\Bacterial leaf blight\DSC_0365.JPG')
    display_image(image=image)

