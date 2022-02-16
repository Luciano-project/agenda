from django.contrib.auth import authenticate

user = authenticate(username=username, password=password)


from django.contrib.auth import login

login(request, user)


