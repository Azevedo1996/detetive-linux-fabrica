# Detetive Linux: O Mistério da Fábrica

Versão completa com 4 fases.

## Rodar no Windows CMD

```bat
cd c:\Users\leazevedo\Music\jogo_detetive_linux
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_missions
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Fases

- Fase 1: comandos e diretórios básicos.
- Fase 2: usuários, grupos, permissões e pacotes.
- Fase 3: processos, serviços, redes, SSH e SCP.
- Fase 4: monitoramento, logs e troubleshooting.
