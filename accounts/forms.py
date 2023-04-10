from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = PasswordInput()

        # You don't want the `remember` field?
        if 'remember' in self.fields.keys():
            del self.fields['remember']

        helper = FormHelper()
        helper.form_show_labels = False
        helper.layout = Layout(
            Field('login', placeholder = 'Email address'),
            Field('password', placeholder = 'Password'),
            FormActions(
                Submit('submit', 'Log me in to Cornell Forum', css_class = 'btn-primary')
            ),
        )
        self.helper = helper
