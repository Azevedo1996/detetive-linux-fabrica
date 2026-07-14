from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import StartGameForm, AnswerForm
from .models import Mission, PlayerSession, AnswerLog

PHASES = {
    1: {'title':'Fase 1 — Bem-vindo à Fábrica Investigativa','description':'Primeiros comandos e localização no Linux.'},
    2: {'title':'Fase 2 — Gerenciando a Fábrica','description':'Usuários, grupos, permissões e pacotes.'},
    3: {'title':'Fase 3 — Operação Nuvem e Resgate','description':'Serviços, processos, rede, SSH e SCP.'},
    4: {'title':'Fase 4 — Sala de Crise e Troubleshooting','description':'Monitoramento, logs e diagnóstico.'},
    5: {'title':'Fase 5 — O Relatório Final do Caso','description':'Revisão, parabéns e convite ao Detetive Linux 2.'},
}

def _get_session(request):
    sid = request.session.get('player_session_id')
    if not sid: return None
    try: return PlayerSession.objects.get(id=sid)
    except PlayerSession.DoesNotExist:
        request.session.pop('player_session_id', None)
        return None

def home(request):
    cards=[{'number':n, **d, 'missions':Mission.objects.filter(phase=n).count()} for n,d in PHASES.items()]
    return render(request,'game/home.html',{'phase_cards':cards,'current_session':_get_session(request)})

@require_http_methods(['GET','POST'])
def start_game(request):
    initial={}
    phase=request.GET.get('phase')
    if phase and phase.isdigit() and int(phase) in PHASES: initial['selected_phase']=int(phase)
    if request.method == 'POST':
        form=StartGameForm(request.POST)
        if form.is_valid():
            selected=int(form.cleaned_data['selected_phase'])
            ps=PlayerSession.objects.create(player_name=form.cleaned_data.get('player_name') or 'Detetive Linux', selected_phase=selected, user=request.user if request.user.is_authenticated else None)
            request.session['player_session_id']=ps.id
            return redirect('game:mission')
    else: form=StartGameForm(initial=initial)
    return render(request,'game/start.html',{'form':form})

@require_http_methods(['GET','POST'])
def mission(request):
    ps=_get_session(request)
    if not ps: return redirect('game:start')
    total=Mission.objects.filter(phase=ps.selected_phase).count()
    if total == 0:
        messages.warning(request,'Nenhuma missão cadastrada. Rode: python manage.py seed_missions')
        return redirect('game:home')
    if ps.finished or ps.current_mission > total:
        ps.finished=True; ps.save(update_fields=['finished'])
        return render(request,'game/finished.html',{'session':ps,'total':total,'phase_title':PHASES[ps.selected_phase]['title'],'rewards':ps.reward_list()})
    current=get_object_or_404(Mission, phase=ps.selected_phase, order=ps.current_mission)
    feedback=None; form=AnswerForm()
    if request.method == 'POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            raw=form.cleaned_data['answer']; answer=raw.strip().lower(); correct=answer in current.accepted_answers()
            AnswerLog.objects.create(session=ps, mission=current, answer=raw, correct=correct)
            if correct:
                ps.score += current.points
                ps.add_reward(current.reward)
                ps.current_mission += 1
                if ps.current_mission > total: ps.finished=True
                ps.save()
                feedback={'correct':True,'title':'[OK] Evidência confirmada','message':current.explanation,'example':current.command_example,'reward':current.reward,'finished':ps.finished}
            else:
                feedback={'correct':False,'title':'[ERRO] Hipótese não confirmada','message':'Revise a missão e tente novamente. Pense no comando que resolve a situação.','hint':'Dica: a resposta pode ser um comando, caminho, opção ou conceito Linux.'}
    progress=int(((ps.current_mission-1)/total)*100)
    return render(request,'game/mission.html',{'session':ps,'mission':current,'form':form,'feedback':feedback,'total':total,'progress':progress,'phase_title':PHASES[ps.selected_phase]['title']})

def restart(request):
    request.session.pop('player_session_id', None)
    return redirect('game:home')
