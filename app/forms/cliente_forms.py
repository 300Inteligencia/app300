from django import forms
from django.forms import DateInput

from ..models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email','telefone', 'data_nascimento', 'cpf', 'profissao', 'medico']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': "date"}
            )
        }
        
class FiltroMedicoForm(forms.Form):
    medicos_choices = [(choice[0], choice[1]) for choice in Cliente.medico_choices]
    Médico = forms.ChoiceField(choices=[('', 'Todos')] + medicos_choices, required=False)
    pesquisa = forms.CharField(max_length=100, required=False, label='Paciente')
