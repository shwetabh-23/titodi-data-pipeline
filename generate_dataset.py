import json
import os
from utils import save_json, open_json

def dataset(json_file, root_dir):
    with open(json_file, 'r') as file:
        data = json.load(file)
    all_conversation = []
    for plant in data.keys():
        conversations = []
        sample = {}
        for disease in data[plant].keys():
            for image in data[plant][disease].keys():
                for key in data[plant][disease][image].keys():
                    for i in range(2):
                        if i % 2 == 0:
                            element = {}
                            element['from'] = 'user'
                            element['value'] =  f"Picture 1: <img>{os.path.join(root_dir, plant, disease, image)}</img>\n{key}"

                            conversations.append(element)
                        else:
                            element = {}
                            element['from'] = 'assistant'
                            element['value'] = data[plant][disease][image][key]
                            conversations.append(element)

        sample['id'] = plant
        sample['conversations'] = conversations
        all_conversation.append(sample)
    output_json = {}
    output_json['list'] = all_conversation
    
    return output_json

if __name__ == '__main__':
    req_json = dataset('output.json', root_dir= r'data\processed_images\images')
    save_json(req_json, 'test')