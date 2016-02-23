from g_utils.utils import GForm
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Field, HTML


class LoginForm(GForm):
    username = CharField(max_length=100, required=True)
    password = CharField(max_length=50, required=True, widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Field('password'),
            FormActions(
                HTML(u'<button class="btn btn-primary" ng-click="doLogin()" />Zaloguj</>')
            )
        )
        super(LoginForm, self).__init__(*args, **kwargs)
