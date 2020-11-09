from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.


def krypton_login(request):
    if request.method == "POST":
        user_form = AuthenticationForm(request.POST)
        print("\n", user_form.is_valid())
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('pasword')
            user = authenticate(username=username, password=password)
            print(f"username:{username}\n password:{password}\n user:{user}")
            if user:
                login(request, user)
                return redirect('index')

        return redirect('login',context={"form":user_form})

    elif request.method == 'GET':
        context = {"form": AuthenticationForm()}
        return render(request, 'krypton_users/login.html', context)


def krypton_signup(request):

    if request.method == 'POST':
        krypton_signup_form = UserCreationForm(request.POST)
        print(krypton_signup_form)
        print('\nis valid?:', krypton_signup_form.is_valid(), '\n')
        if krypton_signup_form.is_valid():
            krypton_signup_form.save()
            username = krypton_signup_form.cleaned_data.get('username')
            password = krypton_signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user=user)
            print(username,'\n')
            print(password,'\n')
            print(user)
            return redirect('index')
        else:
            print(krypton_signup_form.error_messages)
            return render(request, 'krypton_users/signup.html', {'form': krypton_signup_form})

    elif request.method == 'GET':
        krypton_signup_form = UserCreationForm()
        context = {"form": krypton_signup_form}
        return render(request, 'krypton_users/signup.html', context)
