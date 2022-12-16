from django import forms
from tela.models import banco_de_login

class form_login (forms.ModelForm):
    class Meta:
        model = banco_de_login
        fields = '__all__'


class form_cadastro (forms.ModelForm):
    class Meta:
        model = banco_de_login
        fields = '__all__'