from django.db import models
from django.contrib.auth.models import User

class Mission(models.Model):
    phase = models.PositiveIntegerField('Fase', default=1)
    title = models.CharField('Título', max_length=160)
    story = models.TextField('História')
    question = models.TextField('Pergunta')
    expected_answer = models.CharField('Resposta esperada', max_length=160)
    aliases = models.CharField('Respostas aceitas', max_length=350, blank=True, help_text='Separe por vírgula.')
    explanation = models.TextField('Explicação')
    command_example = models.CharField('Exemplo de comando', max_length=220, blank=True)
    order = models.PositiveIntegerField('Ordem', default=1)
    points = models.PositiveIntegerField('Pontos', default=10)
    class Meta:
        ordering = ['phase', 'order']
        unique_together = ('phase', 'order')
        verbose_name = 'Missão'
        verbose_name_plural = 'Missões'
    def __str__(self): return f'Fase {self.phase} - {self.order}. {self.title}'
    def accepted_answers(self):
        values = [self.expected_answer]
        if self.aliases: values += [a.strip() for a in self.aliases.split(',') if a.strip()]
        return [v.lower().strip() for v in values]

class PlayerSession(models.Model):
    player_name = models.CharField('Nome do jogador', max_length=80, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    selected_phase = models.PositiveIntegerField(default=1)
    current_mission = models.PositiveIntegerField(default=1)
    score = models.PositiveIntegerField(default=0)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Sessão do jogador'
        verbose_name_plural = 'Sessões dos jogadores'
    def __str__(self): return f'{self.player_name or "Detetive"} - Fase {self.selected_phase}'

class AnswerLog(models.Model):
    session = models.ForeignKey(PlayerSession, on_delete=models.CASCADE, related_name='answers')
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['created_at']
