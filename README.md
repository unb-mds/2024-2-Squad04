# 2024-2-Squad04

## Descrição
Aplicação de Gerenciamento de inventário

---

### Pré-requisitos
1. Docker Engine (ou Docker desktop)

### Como Executar o Projeto e Começar a Desenvolver
1. Clone o repositório:
    ```Bash
    git clone https://github.com/unb-mds/2024-2-Squad04

2. Navegue até o diretório do projeto:
    ```Bash
    cd PROJECT

3. Crie um ambiente virtual:
    ```Bash
    python -m venv .venv
    .venv/scripts/activate
4. Instale as dependências:
    ```Bash
    pip install -r requirements.txt

5. Baixe a Docker Desktop (Docker Engine, linux) no site: 
    https://www.docker.com/products/docker-desktop/
    <br>

5. Crie .env com as variáveis do projeto na pasta /PROJECT
    <br>

6. Rode o container do docker-compose.yml
    ```Bash
    docker compose up -d

7. Aplique as migrações do banco de dados:
    ```Bash
    python manage.py migrate

8. Inicie o servidor de desenvolvimento
    ```Bash
    python manage.py runserver

Pronto! Assim está pronto para começar a desenvolver.