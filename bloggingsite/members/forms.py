from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from mainplatform.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','twitter','facebook','instagram','theards')


        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            # 'profile_pic': forms.TextInput(attrs={'class':'form-control','value':'','id':'authornameid','type':'hidden'}),
            'twitter': forms.TextInput(attrs={'class':'form-control','placeholder':'TWITTER ID'}),
            'facebook': forms.TextInput(attrs={'class':'form-control','placeholder':'FACEBOOK ID'}),
            'instagram': forms.TextInput(attrs={'class':'form-control','placeholder':'INSTAGRAM ID'}),
            'theards': forms.TextInput(attrs={'class':'form-control','placeholder':'THREADS ID'}),

        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = None
    is_superuser = None
    is_staff = None
    is_active = None
    date_joined = None

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(label = "OLD PASSWORD",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}))
    new_password1 = forms.CharField(label = "NEW PASSWORD",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    new_password2 = forms.CharField(label = "CONFORM PASSWORD",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter Password'}))


    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')