import os
import pandas as pd
data_path = r'Rice Leaf Disease Images'
data = {}
for dir in os.listdir(data_path):
    curr_dir = os.path.join(data_path, dir)
    data[curr_dir.split('\\')[1]] = len(os.listdir(curr_dir))

data_path = r'Large Wheat Disease Classification Dataset'
for dir in os.listdir(data_path):
    curr_dir = os.path.join(data_path, dir)
    data[curr_dir.split('\\')[1]] = len(os.listdir(curr_dir))

data_path = r'Cotton plant disease'
for dir in os.listdir(data_path):
    curr_dir = os.path.join(data_path, dir)
    data[curr_dir.split('\\')[1]] = len(os.listdir(curr_dir))

df = pd.DataFrame(data = data.items())
a = ['rice'] * 4
b = ['wheat'] * 4
c = ['cotton'] * 6
a.extend(b)
a.extend(c)
df.insert(0, 'category', a)

df.columns = ['category', 'Name of disease', 'Number of Images']
breakpoint()
