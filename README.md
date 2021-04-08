# Challenge Account

Project that performs a consultation of the forecast of the time of the informed city, saves the research and makes the history of consultations available.

It also provides a documented API for a new query and query history.


# Stack

This project uses lot of stuff as:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/#installation)
- [DRF-YASG](https://github.com/axnsan12/drf-yasg)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Docker](https://docs.docker.com/get-docker/)



## Get started

Follow the steps below to run the project locally.

*Note that you will need to have [Docker](https://docs.docker.com/get-docker/) and [Python](https://www.python.org/downloads/) installed.*

Clone the project ...

```bash
git clone https://github.com/IgorVessali/challenge-weather.git
cd challenge-weather
```

Configure local ambient ...

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```

Up the containers ...

```bash
docker-compose up -d 
```

Execute the migrations in database ...

```bash
docker-compose exec web python manage.py migrate 
```

Create a super user to access the painel admin and end-points privates:

```bash
docker-compose exec web python manage.py createsuperuser
```


## Usage

- Navigate to [localhost:8000/](http://127.0.0.1:8000/) and see the OpenAPI documentation.
- Navigate to [localhost:8000/admin](http://127.0.0.1:8000/admin) and see the painel admin running.
- Navigate to [localhost:8000/docs](http://127.0.0.1:8000/docs) and see the OpenAPI specification.



## Unit Tests

The project has unit tests with 100% coverage ...

![coverage image](https://github.com/IgorVessali/challenge-weather/blob/main/img/covarege-account.png)



To run the tests run the command:

```bash
docker-compose exec web coverage run manage.py test   
```

To create the html with the results run the command:

```bash
docker-compose exec web coverage html   
```