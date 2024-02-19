import base64
import requests
import os
import re
import json

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_data(api_key, image_path, disease, plant, questions):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": f"The image here is of a {plant} plant infected with a disease called {disease}. Based on this information, write three answers in detail to the following three questions, all in one line : 1 :  {questions[0]} 2 : {questions[1]} 3 : {questions[2]} 4 : {questions[3]} 5 : {questions[4]}" 
            },
            {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
            ]
        }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    breakpoint()
    return (response.json()['choices'][0]['message']['content'])

def split_string(input_string):
    # Use regular expression to split the string based on numbers followed by a dot
    sentences = re.split(r'\d+[\.:]', input_string)

    # Remove empty strings from the list
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return sentences

def create_data_json(root_img_dir, questions, api_key):
    all_plants = {}
    #breakpoint()
    for plant in os.listdir(root_img_dir):
        all_diseases = {}
        for disease in os.listdir(os.path.join(root_img_dir, plant)):
            all_conversations = {}
            for image in os.listdir(os.path.join(root_img_dir, plant, disease))[0:5]:
                conversation = {}
                answers = get_data(image_path= os.path.join(root_img_dir, plant, disease, image), disease= disease, plant= plant, questions=questions, api_key= api_key)
                #breakpoint()
                try:
                    answer1, answer2, answer3, answer4, answer5 = split_string(answers)[0], split_string(answers)[1], split_string(answers)[2], split_string(answers)[3], split_string(answers)[4]
                    question1 = questions[0]
                    question2 = questions[1]
                    question3 = questions[2]
                    question4 = questions[3]
                    question5 = questions[4]
                    
                    conversation[question1] = answer1
                    conversation[question2] = answer2
                    conversation[question3] = answer3
                    conversation[question4] = answer4
                    conversation[question5] = answer5
                    all_conversations[root_img_dir + '/' + plant + '/' +  disease + '/' + image] = conversation
                except:
                    continue   
                all_diseases[disease] = all_conversations 
            all_plants[plant] = all_diseases
    return all_plants

def open_json(file_path):
    # Load the prettified JSON file
    with open(file_path, 'r') as json_file:
        loaded_dict = json.load(json_file)

    # Print the loaded dictionary (now in a prettified format)
    print(json.dumps(loaded_dict, indent=4))

def save_json(file, name):
    with open(f'{name}.json', 'w') as json_file:
        json.dump(file, json_file)