from dotenv import load_dotenv
import os

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_base_url = os.getenv("DEEPSEEK_URL")

from openai import OpenAI

#initialize the client
client = OpenAI(api_key= deepseek_api_key, base_url= deepseek_base_url)

# Define a simple query to test AI's capbilities
prompt = "Who am I speaking with?"

#load system prompt from file
def load_system_prompt(file_path: str):
    try:
        with open(file_path,'r') as f:
            return f.read()
    except Exception as e:
        print(f'Error loading system prompt:{e}')
        return "You are a helpful tutor."

system_prompt= load_system_prompt('data/system_prompt.txt')

#Create send_message function to interact with the model
def send_message(messages):
    response = client.chat.completions.create(
        model = "deepseek-chat",
        max_tokens=150,
        messages = messages,
    )
    return response.choices[0].message.content.strip()
    
conversation = [{"role":"system", "content":system_prompt},
                {"role":"user", "content":prompt}
                ]

# extract the reply
reply =send_message(conversation)

print(f"User:\n{conversation[1]['content']}\n")
print(f"Chatbot:\n{reply}")