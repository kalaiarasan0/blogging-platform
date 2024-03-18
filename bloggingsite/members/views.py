from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from mainplatform.models import Profile


class CreateUserProfileView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/change_password_view.html')
    

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])

        context["page_user"] = page_user
        return  context
    

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_user_profile.html'
    fields =['bio','profile_pic','twitter','facebook','instagram','theards' ]
    success_url = reverse_lazy('Home')