import openai, os
from dotenv import load_dotenv

# Load enviroment variables
load_dotenv()

# Get OpenAI API Token
OPENAI = os.getenv('OPENAI_TOKEN')
# Set API Key to the OpenAI Token
openai.api_key = OPENAI

# Load local files
import Json.json_handling as json

def get_gpt_response(new_entry): 
    # Read the existing GPT chat log from the JSON file
    data = json.Data('./OpenAI/gpt_log.json')

    # Check if the json data is empty
    if data.is_empty():
        # GPT System Setup
        Flag = {
            "role": "system",
            "content": """You are a helpful food manager assistant for the company "Food Manager", if asked you suggests different ingredients in recepies, you will also suggest recepies to makes based on the ingredients the user informs you they have.
            You should keep your answers short and concise, you should not refer to competing websites."""
        }

        messages = data.save_and_retrive(Flag, new_entry)

    else:
        # Save the new entry to the json then retrieve the entire thing
        messages = data.save_and_retrive(new_entry)

    # Create a OpenAI Chat Response using gpt-4 and the message variable
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.1,
    max_tokens=250,
    top_p=0.1,
    frequency_penalty=0,
    presence_penalty=0
    )

    # Store the OpenAI response message
    gpt_message = response["choices"][0]["message"]

    # Save the gpt response to the JSON Data
    data.save(gpt_message)
    
    # Return the GPT response
    return gpt_message["content"]