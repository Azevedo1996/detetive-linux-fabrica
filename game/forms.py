from django import forms
PHASE_CHOICES = (
    (1, 'Fase 1 — Bem-vindo à Fábrica'),
    (2, 'Fase 2 — Gerenciando a Fábrica e Suas Entregas'),
    (3, 'Fase 3 — Operação Nuvem e Resgate'),
    (4, 'Fase 4 — Sala de Crise e Troubleshooting'),
)
class StartGameForm(forms.Form):
    player_name = forms.CharField(label='Nome do detetive', max_length=80, required=False)
    selected_phase = forms.ChoiceField(label='Escolha a fase', choices=PHASE_CHOICES, initial=1)
class AnswerForm(forms.Form):
    answer = forms.CharField(label='Sua resposta', max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite o comando, ferramenta ou conceito...','autocomplete':'off','autofocus':'autofocus'}))
