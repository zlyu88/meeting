from django import forms


class LogIn(forms.Form):
    name = forms.CharField(label='Your name', max_length=50)
    password = forms.CharField(label='Password', max_length=32)


class SignUp(forms.Form):
    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
    image = forms.ImageField(required=False, label='Select a file')


# class InfoEdit():


# class Reserv(forms.Form):
