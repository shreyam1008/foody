from django.shortcuts import render,redirect
from .models import Chat, User



def index(request):
    username = request.POST.get('UserName', None)
    if username and request.method == 'POST':
        user = User(name=username)
        user.save()
        Chat.objects.all().delete()
        msg = "Hello " + username + ". I am here to serve you. what do you want?"
        c = Chat(username='BHAUJU', message=msg, isuser=False)
        c.save()

        return redirect('chatbot:Chatbot')

    else:
        return render(request, 'chatbot/index.html')
