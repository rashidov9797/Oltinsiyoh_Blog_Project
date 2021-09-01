

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import  reverse_lazy
from django.contrib.auth.views import  PasswordChangeView
from .forms import ProfilePageForm, SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from theblog.models import Profile

# Create your views here.


# CreateProfilePageView
class  CreateProfilePageView(CreateView):
  model = Profile
  form_class = ProfilePageForm
  template_name = 'registration/create_user_profile_page.html'


  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)


# EditProfilePageView

class EditProfilePageView(generic.UpdateView):
  model = Profile
  template_name = 'registration/edit_profile_page.html'
  fields = ['bio','profile_pic']
  success_url = reverse_lazy('home')





# ShowProfilePageView
class ShowProfilePageView(DetailView):
  model = Profile
  template_name = 'registration/user_profile.html'

  def get_context_data(self,*args,**kwargs):
      #users = Profile.objects.all()
      context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
    
      page_user = get_object_or_404(Profile,id=self.kwargs['pk'])

      context["page_user"] = page_user
      return context


class PasswordsChangeView(PasswordChangeView):
  form_class = PasswordChangingForm
  # form_class = PasswordChangeForm
  success_url = reverse_lazy('password_succes')
  # success_url = reverse_lazy('home')

def password_succes(request):
  return render(request, 'registration/password_succes.html',{})  


class UserRegisterView(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/edit_profile.html'
  success_url = reverse_lazy('login') 

  def get_object(self):
    return self.request.user 

  