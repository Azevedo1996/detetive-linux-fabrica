from django import forms
PHASE_CHOICES = tuple((i, f'Fase {i}') for i in range(1, 6))
class StartGameForm(forms.Form):
    player_name = forms.CharField(label='Nome do detetive', max_length=80, required=False)
    selected_phase = forms.ChoiceField(label='Escolha a fase', choices=PHASE_CHOICES, initial=1)
class AnswerForm(forms.Form):
    answer = forms.CharField(label='Resposta', max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite o comando ou conceito...','autocomplete':'off','autofocus':'autofocus','class':'terminal-input'}))
