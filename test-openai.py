#%%
from dotenv import load_dotenv
from openai import OpenAI 

#%%
# The load_dotenv() function from the python-dotenv library
# loads environment variables from a .env file into the
# current process's environment variables. This allows us
# to store sensitive information like API keys in a separate
# file that is not committed to version control.
load_dotenv()

#%%
# Create a client object that will be used to interact with the OpenAI API.
client = OpenAI()

#%%
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, 
              {"role": "user", "content": "What is the weather in Bern?"}]
)
#%%
print(response)

#%%
print(response.choices[0].message.content)