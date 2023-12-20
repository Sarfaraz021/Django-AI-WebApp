# myapp/views.py
from django.shortcuts import render
from .forms import Chatform
from openai import OpenAI
import os

from dotenv import load_dotenv
load_dotenv('var.env')


key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=key)
print(f"The response is : {key}\n\n\n")

def make_openai_request(prompt):
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=500
    )
    print("OpenAI Request:", response)
    return response


def chat(request):
    conversation = request.session.get('conversation', [])
    if request.method == 'POST':
        if request.POST.get('query'):
            form =Chatform(request.POST)
            user_input=''
            if form.is_valid():
                user_input=form.cleaned_data['userquery']
            # Define your chatbot's predefined prompts
            # prompts = []

            # Append user input to the conversation
            if user_input:
                conversation.append({"role": "user", "content": user_input})

            # Append conversation messages to prompts
            # prompts.append(conversation)
            queryresponse = make_openai_request(user_input)

            # Extract chatbot replies from the response
            chatbot_replies = queryresponse.choices[0].text

            # Append chatbot replies to the conversation
            conversation.append({"role": "assistant", "content": chatbot_replies})

            # Update the conversation in the session
            request.session['conversation'] = conversation

            return render(request, 'chat.html', {'user_input': user_input, 'chatbot_replies': chatbot_replies, 'conversation': conversation,'form':form})
        else:        
            request.session.clear()
            form =Chatform()
            return render(request, 'chat.html', {'conversation': [],'form':form})
    else:
        request.session.clear()
        form =Chatform()
        return render(request, 'chat.html', {'conversation': conversation,'form':form})

