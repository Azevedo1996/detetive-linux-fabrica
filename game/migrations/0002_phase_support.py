from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [('game', '0001_initial')]
    operations = [
        migrations.AddField(model_name='mission', name='phase', field=models.PositiveIntegerField(default=1, verbose_name='Fase')),
        migrations.AddField(model_name='playersession', name='selected_phase', field=models.PositiveIntegerField(default=1)),
        migrations.AlterModelOptions(name='mission', options={'ordering':['phase','order'], 'verbose_name':'Missão', 'verbose_name_plural':'Missões'}),
        migrations.AlterUniqueTogether(name='mission', unique_together={('phase','order')}),]
