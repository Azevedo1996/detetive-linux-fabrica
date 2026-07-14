# 🕵️ Detetive Linux — O Mistério da Fábrica

![Status](https://img.shields.io/badge/status-atualizado-22c55e?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Treinamento-FCC624?style=for-the-badge&logo=linux&logoColor=black)

> Um jogo web educacional em **Python + Django** para praticar comandos Linux em formato de investigação, funcionando como continuação natural da **A Fantástica Fábrica do Linux**.

---

## 📖 Sobre o projeto

**Detetive Linux — O Mistério da Fábrica** é um jogo educacional criado para ajudar pessoas iniciantes a aplicarem comandos Linux em situações práticas.

Depois de conhecer os conceitos básicos na **A Fantástica Fábrica do Linux**, o participante deixa de ser apenas visitante da fábrica e passa a atuar como **detetive técnico**, investigando problemas, coletando evidências e usando comandos reais para resolver missões.

A proposta é transformar o aprendizado de Linux em uma experiência mais interativa, prática e memorável.

---

## 🧭 Papel na trilha de aprendizado

Este projeto faz parte de uma trilha de aprendizagem em três etapas:

```text
1. A Fantástica Fábrica do Linux
   Porta de entrada para conceitos e comandos básicos.

2. Detetive Linux — O Mistério da Fábrica
   Aplicação prática dos comandos em missões investigativas.

3. Detetive Linux 2 — A Fábrica em Produção
   Linux intermediário, troubleshooting e operação real.
```

A ideia é que a **Fantástica Fábrica do Linux** seja o primeiro contato, o **Detetive Linux** seja a etapa de prática guiada e o **Detetive Linux 2** seja a evolução para profissionais de TI.

---

## 🎯 Objetivo

O objetivo do jogo é fazer o participante entender **quando** e **por que** usar comandos Linux.

Em vez de apenas decorar comandos, o jogador recebe uma situação investigativa e precisa responder qual comando, caminho ou conceito resolve o problema.

Exemplo:

```text
Missão:
A fábrica precisa descobrir em qual sala/diretório está.

Pergunta:
Qual comando mostra o diretório atual?

Resposta:
pwd
```

Após o acerto, o jogo apresenta:

- a explicação técnica;
- um exemplo de comando;
- uma recompensa/evidência;
- pontuação da missão.

---

## ✨ Melhorias desta versão

Esta versão foi atualizada para ficar alinhada ao padrão da **A Fantástica Fábrica do Linux**.

Principais melhorias:

- recompensas por missão;
- sistema de pontuação;
- tela final de parabéns;
- fase final de fechamento;
- convite para o **Detetive Linux 2 — A Fábrica em Produção**;
- documentação mais completa;
- arquivo de instruções;
- gabarito para instrutor;
- material de apoio para treinamento.

---

## 🕹️ Como funciona o jogo

O jogador escolhe uma fase e responde às missões.

Cada missão possui:

- história curta;
- pergunta;
- resposta esperada;
- respostas alternativas aceitas;
- exemplo de comando;
- explicação após o acerto;
- recompensa/evidência;
- pontuação.

Ao acertar, o jogador recebe pontos, coleta uma recompensa/evidência e avança para a próxima missão.

---

## 🏭 Fases disponíveis

O jogo possui **5 fases** e **50 missões**.

---

### ✅ Fase 1 — Bem-vindo à Fábrica Investigativa

Primeiros comandos e localização no Linux.

Conteúdos abordados:

```bash
pwd
cd
/etc
/var/log
tail
touch
root
/tmp
rm
clear
```

Objetivo da fase:

```text
Revisar e aplicar comandos fundamentais aprendidos na Fantástica Fábrica do Linux.
```

---

### ✅ Fase 2 — Gerenciando a Fábrica

Usuários, grupos, permissões e pacotes.

Conteúdos abordados:

```bash
useradd
passwd
groupadd
usermod
id
groups
chown
chmod
apt update
dnf install zabbix
```

Objetivo da fase:

```text
Mostrar como o Linux organiza usuários, departamentos, permissões e instalação de ferramentas.
```

---

### ✅ Fase 3 — Operação Nuvem e Resgate

Serviços, processos, rede, SSH e SCP.

Conteúdos abordados:

```bash
systemctl start
systemctl status
systemctl enable
ps
top
kill
ping
ip addr
ssh
scp
```

Objetivo da fase:

```text
Ensinar comandos usados em operação básica de servidores, acesso remoto e diagnóstico inicial.
```

---

### ✅ Fase 4 — Sala de Crise e Troubleshooting

Monitoramento, logs e diagnóstico.

Conteúdos abordados:

```bash
uptime
top
free -h
df -h
du -sh
/var/log
tail -f
journalctl -xe
journalctl -u
systemctl restart
```

Objetivo da fase:

```text
Introduzir pensamento de troubleshooting: observar, medir, investigar logs, agir e validar.
```

---

### ✅ Fase 5 — O Relatório Final do Caso

Revisão, fechamento e convite para a próxima etapa.

Conteúdos revisados:

```bash
pwd
ls
cd
chmod
systemctl status
top
ping
journalctl -u
causa raiz
continuar para Detetive Linux 2
```

Objetivo da fase:

```text
Consolidar os aprendizados e encaminhar o participante para o Detetive Linux 2 — A Fábrica em Produção.
```

---

## 🖼️ Screenshots


### Tela inicial

![Tela inicial](screenshots/tela-inicial.png)

### Escolha de fase

![Escolha de fase](screenshots/escolha-fase.png)

### Tela de missão

![Tela de missão](screenshots/missao.png)


---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Django**
- **SQLite**
- **HTML**
- **CSS**
- **Django Admin**

---

## 📁 Estrutura do projeto

```text
detetive-linux-fabrica/
├── manage.py
├── requirements.txt
├── README.md
├── INSTRUCOES.md
├── .gitignore
├── docs/
│   ├── TREINAMENTO_DETETIVE_LINUX.md
│   └── GABARITO.md
├── detetive_linux/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── game/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    ├── management/
    │   └── commands/
    │       └── seed_missions.py
    ├── static/
    │   └── game/
    │       └── css/
    │           └── style.css
    └── templates/
        └── game/
            ├── base.html
            ├── home.html
            ├── start.html
            ├── mission.html
            └── finished.html
```

---

## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Azevedo1996/detetive-linux-fabrica.git
```

```bash
cd detetive-linux-fabrica
```

---

### 2. Crie o ambiente virtual

No Linux/macOS:

```bash
python3 -m venv venv
```

No Windows:

```powershell
python -m venv venv
```

---

### 3. Ative o ambiente virtual

No Linux/macOS:

```bash
source venv/bin/activate
```

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

No Windows CMD:

```bat
venv\Scripts\activate
```

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Execute as migrações

```bash
python manage.py migrate
```

---

### 6. Carregue as missões

```bash
python manage.py seed_missions
```

Esse comando popula o banco com as missões do jogo.

---

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Django Admin

Para acessar o painel administrativo:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Depois acesse:

```text
http://127.0.0.1:8000/admin/
```

No admin é possível editar:

- missões;
- perguntas;
- respostas esperadas;
- respostas alternativas;
- exemplos de comando;
- explicações;
- recompensas;
- pontuação;
- sessões dos jogadores;
- histórico de respostas.

---

## 🧬 Modelo de missão

Cada missão possui campos como:

```python
{
    "phase": 1,
    "order": 1,
    "title": "Missão 1 — Onde estou?",
    "story": "História da missão",
    "question": "Pergunta exibida ao jogador",
    "expected_answer": "pwd",
    "aliases": "PWD",
    "command_example": "pwd",
    "explanation": "Explicação exibida após o acerto",
    "reward": "Evidência: Onde estou?",
    "points": 10,
}
```

---

## 🏆 Pontuação e recompensas

Cada missão possui pontuação definida no campo:

```python
points
```

Por padrão:

```text
10 pontos por missão
```

A última missão da fase final vale:

```text
20 pontos
```

As recompensas representam evidências ou selos coletados durante a investigação.

Exemplos:

```text
Evidência: Onde estou?
Evidência: Novo Funcionário
Evidência: Diário ao Vivo
Selo final: Próximo Caso
```

---

## 🧑‍🏫 Uso em treinamento

Sugestão de condução:

```text
1. Relembrar a Fantástica Fábrica do Linux
2. Explicar que agora o visitante virou detetive
3. Jogar uma fase por bloco
4. A cada acerto, reforçar o comando e a recompensa
5. Encerrar com a Fase 5
6. Convidar para o Detetive Linux 2
```

---

## ➡️ Próxima aventura recomendada

Ao concluir o jogo, o participante é convidado a continuar com:

# Detetive Linux 2 — A Fábrica em Produção

Essa próxima experiência aprofunda o aprendizado em Linux intermediário, incluindo:

```text
permissões avançadas
processos
serviços
rede
logs
automação
discos
segurança
recuperação
troubleshooting
```

---

## 🔗 Relacionamento com os outros projetos

### A Fantástica Fábrica do Linux

Primeira etapa da trilha. Ensina conceitos fundamentais e comandos básicos de forma leve e introdutória.

### Detetive Linux — O Mistério da Fábrica

Segunda etapa. Usa comandos básicos e intermediários iniciais para resolver missões investigativas.

### Detetive Linux 2 — A Fábrica em Produção

Terceira etapa. Avança para operação Linux intermediária e troubleshooting profissional.

---

## 📌 Comandos úteis do projeto

Rodar servidor:

```bash
python manage.py runserver
```

Carregar missões:

```bash
python manage.py seed_missions
```

Criar usuário administrador:

```bash
python manage.py createsuperuser
```

Executar migrações:

```bash
python manage.py migrate
```

---

## 🧹 Arquivos que não devem ir para o GitHub

O projeto deve ignorar arquivos como:

```text
venv/
__pycache__/
db.sqlite3
.env
*.pyc
.vscode/
.idea/
```

---

## 🔮 Melhorias futuras

Ideias para próximas versões:

- ranking dos participantes;
- modo professor;
- temporizador por pergunta;
- exportação de pontuação;
- tela de certificado simbólico;
- autenticação de jogadores;
- cadastro de turmas;
- dashboard de desempenho;
- integração com Docker;
- deploy em servidor Linux;
- ligação direta com o repositório do Detetive Linux 2.

---

## 📄 Licença

Este projeto pode ser distribuído sob a licença **MIT**.

Sugestão: adicione um arquivo `LICENSE` na raiz do projeto com o texto da licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por **Leonardo Azevedo** como material de apoio para treinamento Linux em formato interativo.

---

## ⭐ Apoie o projeto

Se este projeto ajudou em estudos, meetups ou treinamentos internos, considere deixar uma estrela no repositório.

```text
⭐ Star no GitHub ajuda outras pessoas a encontrarem o projeto.
```
