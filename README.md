## Guia de Instalação e Configuração

### Pré-requisitos

- Python 3.x instalado
- Poetry

> OBS: [Instação poetry](https://python-poetry.org/docs/#installation)

### Passo 1: Clonar o Repositório do projeto

```bash
git clone https://github.com/seu_usuario/nome_do_repositorio.git
```

### Passo 2: Instalação dos pacotes e criação da virtual env

Comandos designados à instalação dos pacotes requeridos do projeto, criação e ativação da virtual env para rodar o projeto.

```
cd nome_do_repositorio
poetry config settings.virtualenvs.in-project true
poetry install
poetry shell
```

> **OBS:** É importante que, apartir daqui, todos os comandos rodados internamente no django sejam rodados com a virtual env ativada! (`poetry shell`)

## Passo 3: Migrando o banco e fazendo dump dos dados

Rode os dois migrates em sequência, isso fará com que os arquivos de banco sejam criados.

```
poetry run python manage.py migrate
poetry run python manage.py migrate --database=test
```

## Passo 4: Fazendo dump dos dados contidos no csv para funcionamento da aplicação

O comando `dump_movie_data` irá percorrer o csv dos filmes requeridos para a aplicação e adicionar os itens ao banco de dados.

```
poetry run python manage.py dump_movie_data
```

## Passo 5: Rodando os testes de integração

Os dados do testes foram mockados.

```
poetry run python manage.py test
```

## Passo 6: Acesso ao endpoint da proposta

**/api/maxminwinnerinterval/** - Esse endpoint retorna, em um conjunto de dados json, o produtor com maior intervalo entre dois prêmios consecutivos, e o que
obteve dois prêmios mais rápido.

Endpoint proposto pelo desafio.

## Abaixo um guia de como utilizar os endpoints

**/api/movies/** - Lista de todos os filmes e criação de novos filmes (GET e POST)
**/api/movies/\<pk\>/** - Detalhes de um filme específico, atualização ou remoção do mesmo (substitua <pk> pelo ID do filme) (GET, PUT E DELETE)

**Estrutura para cadastro ou atualização de filmes:**<br>

```
{
    "title": "Movie",
    "year": 0000,
    "winner": false,
    "studios": ["Studio Name 1", "Studio Name 2"],
    "producers": ["Producer Name 1", "Producer Name 2]
}
```

/api/producers/ - Lista de todos os produtores e criação de novos produtores (GET E POST)
/api/producers/<pk>/ - Detalhes de um produtor específico, atualização ou remoção do mesmo (substitua <pk> pelo ID do produtor) (GET, PUT E DELETE)

**Estrutura para cadastro ou atualização de produtores:**<br>

```
{
    "name": "Producer Name"
}
```

/api/studios/ - Lista de todos os estúdios e criação de novos estudios
/api/studios/<pk>/ - Detalhes de um estúdio específico, atualização e remoção do mesmo (substitua <pk> pelo ID do estúdio) (GET, PUT E DELETE)

**Estrutura para cadastro ou atualização de produtores:**<br>

```
{
    "name": "Producer Name"
}
```
