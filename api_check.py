import openai

response = openai.chat.completions.create( model="gpt-4", messages=[{"role": "user", "content": "Generate a 3 sentence story about friendship"}] ) 
#print(response)
print(response.choices[0].message.content)
breakpoint()