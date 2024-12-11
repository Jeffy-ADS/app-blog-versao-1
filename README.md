# Guia para Executar o Projeto Blog

Este guia irá orientá-lo sobre como configurar e executar o projeto **Blog** desenvolvido em Django e Python.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes itens instalados em sua máquina:

1. **Python 3.8+**
2. **Pip (gerenciador de pacotes do Python)**
3. **Virtualenv** (opcional, mas recomendado para isolar o ambiente do projeto)
4. **Django** (será instalado durante a configuração do ambiente)
5. **Git** (caso deseje clonar o repositório)

---

## **1. Clonar o Repositório (opcional)**

Caso o projeto esteja hospedado no GitHub, você pode cloná-lo usando o seguinte comando:

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
```

Entre na pasta do projeto:

```bash
cd NOME_DO_REPOSITORIO
```

---

## **2. Criar um Ambiente Virtual**

Para criar um ambiente virtual e instalar as dependências:

```bash
python -m venv venv
```

Ative o ambiente virtual:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

---

## **3. Instalar as Dependências**

Com o ambiente virtual ativo, instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não esteja disponível, instale o Django manualmente:

```bash
pip install django
```

---

## **4. Configurar o Banco de Dados**

Execute as migrações para criar o banco de dados local:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **5. Criar um Superusuário**

Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções para definir um nome de usuário, e-mail e senha.

---

## **6. Iniciar o Servidor Local**

Execute o servidor de desenvolvimento para acessar o blog:

```bash
python manage.py runserver
```

O servidor estará disponível em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **7. Testar o Projeto**

1. Abra o navegador e acesse a URL do servidor local.
2. Faça login no painel administrativo (opcional) em: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
3. Explore as funcionalidades do blog, como criação de posts e gerenciamento de usuários.

---

## **8. Finalizar o Ambiente Virtual**

Ao terminar, desative o ambiente virtual:

```bash
deactivate
```

---

## **Dicas Finais**

- Certifique-se de que todas as dependências estejam instaladas corretamente.
- Consulte a documentação do Django para aprofundar seus conhecimentos: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- Caso tenha dúvidas, me avise! Posso ajudar a personalizar o guia ou resolver problemas específicos.
