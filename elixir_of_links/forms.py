from django import forms

class URLForm(forms.Form):
    url = forms.CharField(max_length=200, label="URL")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Enter URL'})
        
    

# class ChangePasswordForm(forms.Form):
#     old_password = forms.CharField(widget=forms.PasswordInput(), max_length=120)
#     password = forms.CharField(widget=forms.PasswordInput(), max_length=120)
#     confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=120)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['old_password'].widget.attrs.update({'class': 'form-control form-control-lg'})
#         self.fields['password'].widget.attrs.update({'class': 'form-control form-control-lg'})
#         self.fields['confirm_password'].widget.attrs.update({'class': 'form-control form-control-lg'})