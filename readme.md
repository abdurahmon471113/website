
# Website Project

## Project Overview
This is a Django project with a user app and template folder.  
It uses PostgreSQL as the database and `.env` for environment variables.  

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/abdurahmon471113/website.git
cd website
Create a virtual environment and activate it:

python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux / Mac
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Setup environment variables:

Create a .env file in the root folder.

Copy variables from .env.example and update them as needed.

Example .env:

DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=learning_django
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
Create the PostgreSQL database:

CREATE DATABASE learning_django;
Run migrations:

python manage.py migrate
Create a superuser (for Django admin):

python manage.py createsuperuser
Run the development server:

python manage.py runserver
