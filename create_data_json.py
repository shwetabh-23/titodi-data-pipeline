from utils import create_data_json, save_json, open_json


root_img_dir = r'images/'
questions = [
    'what do you see in the image?',
    'what is the cure for this diease, give names of medicines?',
    'How to prevent this disease?',
    'Can you describe the symptoms of the disease shown in the image?',
    'How severe is the infection in this particular case?'
]

user = input('option 1 for generating the responses or option 2 for opening the json : ')
if user == '1':
    all_plants = create_data_json(r'data/processed_images/images', questions = questions, api_key= api_key)
    save_json(all_plants)
elif user == '2':
    open_json('final_output.json')
else:
    print('invalid entry')
