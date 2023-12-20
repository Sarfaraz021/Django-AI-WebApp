# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()

def make_openai_request(prompt):
    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("OpenAI Request:", response)
    return response


def chat_view(request):
    conversation = request.session.get('conversation', [])

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Define your chatbot's predefined prompts
        prompts = []

        # Append user input to the conversation
        if user_input:
            conversation.append({"role": "user", "content": user_input})

        # Append conversation messages to prompts
        prompts.extend(conversation)
        response = make_openai_request("".join(message["content"] for message in conversation))

        # Extract chatbot replies from the response
        chatbot_replies = [message['choices'][0]['message']['content'] for message in response['choices'] if message['role'] == 'assistant']

        # Append chatbot replies to the conversation
        for reply in chatbot_replies:
            conversation.append({"role": "assistant", "content": reply})

        # Update the conversation in the session
        request.session['conversation'] = conversation

        return render(request, 'myapp/chat.html', {'user_input': user_input, 'chatbot_replies': chatbot_replies, 'conversation': conversation})
    else:
        request.session.clear()
        return render(request, 'myapp/chat.html', {'conversation': conversation})

def chat(request):
    return render(request, "myapp/chat.html")

def chatAPI(request):
    response = make_openai_request("")
    return JsonResponse(response)
