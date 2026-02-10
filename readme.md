
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
```
2. **Create a virtual environment and activate it:**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux / Mac
source venv/bin/activate
```
3. **Install dependencies:**
**Install all required packages.**
```bash
pip install -r requirements.txt
```
4. **Create a .env file in the root folder.**
**THEN: Copy variables from .env.example and update them as needed.**
```bash
Example .env:

DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=learning_django
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```
5. **Create the PostgreSQL database:**

6. **CREATE DATABASE learning_django;**
**Run migrations:**
```bash
python manage.py migrate
```
7. **Create a superuser (for Django admin):**
```bash
python manage.py createsuperuser
```
8. **Run the development server:**
```bash
python manage.py runserver
```
      
