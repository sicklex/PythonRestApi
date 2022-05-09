<h1 align="center">Health App</h1>

<h2>About<h2>

<p>Api para cadastrar usuarios</p>

<h3>Comandos necessarios para rodar aplicação<h3>

```python
docker-compose up --build -d # para iniciar o container
docker-compose exec web python manage.py migrate #para executar as migrations
```

# Tecnologias usadas

<ul>
  <li>
  <a href="https://www.python.org/">Python</a>
  </li>
  <li>
  <a href="https://www.djangoproject.com/">Django</a>
  </li>
  <li>
  <a href="https://www.postgresql.org/">PostgreSQL</a>
  </li>
  <li>
    <a href="https://www.docker.com/">Docker</a>
  </li>
</ul>


## Pré-requisitos

* Ter instalado `<Docker>`
* Para testar a api você precisara de um swoftware de teste como `<PostMan>`


# Endpoints

## Caso o docker já estiver rodando, você pode copiar e colar o código o link abaixo no seu software de teste:

<ul>
<li>
    [get{id}]: http://127.0.0.1:8000/health/patient/id
</li>

<li>
    [POST]: http://127.0.0.1:8000/health/patient/create
</li>

<li>
    [PUT]: http://127.0.0.1:8000/health/patient/update/1
</li>

<li>
    [DELETE]: http://127.0.0.1:8000/health/patient/delete/1
</li>

## Login Endpoint
<li>
    [POST]:  http://127.0.0.1:8000/health/login
</li>
</ul>



## Body Requests

### POST

```
{
    "name": "nome",
    "Data_de_Nascimento": "1994-06-21"
}
```

## PUT

```
{
    "name": "novo nome",
    "Data_de_Nascimento": "nova data"
}
```

## POST Login

```
{
    "username": "usuario",
    "password": "senha"
}
```


## Framework usado

### Framework Django
<p>
    Escolhi o framework Django pois achei que ele é mais facil de organizar e manter criei. Com ele criei um modelo de dados para o paciente e um modelo de dados para o login de usuario. E também pude com facilidade criar um CRUD para o paciente.
</p>





