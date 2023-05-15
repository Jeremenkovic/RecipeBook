
# Recipe Book

A Django-based recipe book application using PostgreSQL.

## Prerequisites

- Python 3.x
- pip
- virtualenv

## Installation

1. Clone this repository and `cd` into the project folder.
2. Create and activate a virtual environment: python3 -m venv recipebook_env
source recipebook_env/bin/activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Create the PostgreSQL database and user:

CREATE DATABASE recipebook;
CREATE USER your_postgres_user WITH PASSWORD 'your_postgres_password';
GRANT ALL PRIVILEGES ON DATABASE recipebook TO your_postgres_user;


5. Apply the migrations:
python3 manage.py makemigrations
python3 manage.py migrate


6. Run the development server:
python3 manage.py runserver


API:
http://localhost:8000/api/recipes/
<img width="1440" alt="Screen Shot 2023-05-16 at 1 35 40 AM" src="https://github.com/Jeremenkovic/RecipeBook/assets/102044657/07fbcd5a-edb1-455f-9bc1-d6fb69ed3390">

http://localhost:8000/api/tags/
<img width="1440" alt="Screen Shot 2023-05-16 at 1 35 57 AM" src="https://github.com/Jeremenkovic/RecipeBook/assets/102044657/907d481d-96ef-40dd-8a50-9ce6ded760ba">


![0-02-05-425a8ef0a76ec70777be3e948f2ce8728efe25589cedfc2d054726c0a0b226a1_1c6db39085b7d1](https://github.com/Jeremenkovic/RecipeBook/assets/102044657/e138800a-d756-4ffc-b648-bc12eaee2b28)


![0-02-05-bbed42d48ea61830288cded0c1bdfa93340a561b0b3f77d23c353de276fed9f0_1c6db390ff0772](https://github.com/Jeremenkovic/RecipeBook/assets/102044657/3aee5c40-08e6-4a05-a8c3-375f8baf45fb)
