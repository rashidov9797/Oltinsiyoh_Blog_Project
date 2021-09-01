
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import  User
from django import  forms 
from theblog.models import Profile


class ProfilePageForm(forms.ModelForm):

  class Meta:

    model = Profile
    fields = ('bio','profile_pic')
    widgets = {

      'bio': forms.TextInput(attrs={'class': 'form-control'}),
 
    } 
  
   


class SignUpForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'Email manzilingizni kiriting...'}))
  first_name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ismingiznikiriting...'}),)
  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Familyangizni kiriting...'}),)


  class  Meta:
    model = User
    fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')

  def __init__(self, *args,**kwargs):
    super(SignUpForm, self).__init__(*args,**kwargs)


    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'

 


class EditProfileForm(UserChangeForm):

  email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'Email manzilingizni kiriting...'}))

  first_name = forms.CharField(max_length=100 ,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ismingiznikiriting...'}),)

  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Familyangizni kiriting...'}),)

  
  username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control',}))

  
  last_login = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control',}))


  is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class' : 'form-check',}))

  is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class' : 'form-check',}))  

  is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class' : 'form-check',}))


  date_joined = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control',}))

  class Meta:
    model = User
    fields = ('username','first_name','last_name','email', 'is_superuser','is_staff','is_active','date_joined')




class PasswordChangingForm(PasswordChangeForm):
  old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type': 'password' ,'placeholder': 'Eski pasportingini  kiriting...'}))
  new_password1 = forms.CharField(max_length=100 ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password' ,'placeholder':'Yangisini kiriting...'}),)
  new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password' ,'placeholder':'Yangisini tasdiqlang ...'}),)


  class  Meta:
    model = User
    fields = ('old_password', 'new_password1','new_password2')    