from django.shortcuts import render
import google.generativeai as genai
from .forms import RequestForm
import os

from django.shortcuts import render
import google.generativeai as genai

def chat (request):
    if request.method != "POST":
        form = RequestForm()
        return render(request,"aiapp/chat.html",{"form":form})
    else:
        user_input = request.POST.get('user_input')
        genai.configure(api_key=os.environ["API_KEY"])
        response = genai.GenerativeModel('gemini-1.0-pro-latest').generate_content(user_input)
        return render(request, 'aiapp/chat.html', {'response': response})
    
        