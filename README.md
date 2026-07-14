# 🕵️ Detetive Linux — O Mistério da Fábrica

Jogo web em **Python + Django** que funciona como sequência da **A Fantástica Fábrica do Linux**.

## Papel na trilha

1. **A Fantástica Fábrica do Linux** - porta de entrada para conceitos e comandos básicos.
2. **Detetive Linux — O Mistério da Fábrica** - aplicação prática dos comandos em missões investigativas.
3. **Detetive Linux 2 — A Fábrica em Produção** - aprofundamento intermediário em operação, troubleshooting e infraestrutura.

## Melhorias desta versão

- Recompensas por missão.
- Sistema de pontuação.
- Fase final de fechamento: **O Relatório Final do Caso**.
- Tela final de parabéns.
- Convite para continuar no **Detetive Linux 2 — A Fábrica em Produção**.
- README, instruções, treinamento e gabarito para apoiar o instrutor.

## Fases

1. Bem-vindo à Fábrica Investigativa
2. Gerenciando a Fábrica
3. Operação Nuvem e Resgate
4. Sala de Crise e Troubleshooting
5. O Relatório Final do Caso

Total: **50 missões**.

## Rodar localmente

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_missions
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

## Admin

```powershell
python manage.py createsuperuser
```

Acesse:

```text
http://127.0.0.1:8000/admin/
```
