from django import forms
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.forms import AuthenticationForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=120)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control p_input'})
        self.fields['password'].widget.attrs.update({'class': 'form-control p_input'})
        
    

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), max_length=120)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=120)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=120)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control p_input'})
        self.fields['password'].widget.attrs.update({'class': 'form-control p_input'})
        self.fields['confirm_password'].widget.attrs.update({'class': 'form-control p_input'})



       
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control p_input', 'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control p_input', 'placeholder': 'Enter Email Address'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control p_input', 'placeholder': 'Enter Firstname'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control p_input', 'placeholder': 'Enter Lastname'})
        
# class YouTubeForm(forms.Form):
#     youtube_link = forms.CharField(max_length=200)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['youtube_link'].widget.attrs.update({'class': 'form-control p_input', 'placeholder': 'Enter YouTube link..'})
        