from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SingUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')
