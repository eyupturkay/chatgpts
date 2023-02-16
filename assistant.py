# pip install openai
import openai   
import os
try:   
    from gtts import gTTS   
except ImportError:   
    os.system("pip3 install gTTS")   
    from gtts import gTTS

# Insert your OpenAI API key here   
openai.api_key = "Your_API_HERE"

def talk_to_GPT3(prompt):   
    response = openai.Completion.create(   
        engine="text-davinci-002",   
        prompt=prompt,   
        max_tokens=2048,   
        n = 1,   
        stop=None,   
        temperature=0.5,   
    )   
    message = response.choices[0].text   
    print("GPT-3: ", message)   
    tts = gTTS(message, lang='en')   
    tts.save("response.mp3")   
    os.system("mpg321 response.mp3")

while True:   
    user_input = input("You: ")   
    print("You: ", user_input)   
    talk_to_GPT3(user_input)
