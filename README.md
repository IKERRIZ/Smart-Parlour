## Adore Parlour
I s a beauty application.

## Description
This is an open palour website that gives information about beauty and treatments. A user can only create an account and sign into it when they want to view, comment and like an exciting image. The site supports uploading images,liking and commenting on images as well as following other users. Logged in users can view photos uploaded by other users in the home page of app.

## Link to deployed site
https://parlour-riz.herokuapp.com/

## Set Up and Installations
----------------------------
### Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
## Clone the Repo
Run the following command on the terminal: git clone github.com/IKERRIZ/parlour.git && cd parlour

## Activate virtual environment
Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
psql
CREATE DATABASE parlour;
## .env file
Create .env file and paste paste the following filling where appropriate:

- SECRET_KEY = '<Secret_key>'
- DBNAME = 'parlour'
- USER = '<Username>'
- PASSWORD = '<password>'
- DEBUG = True

- EMAIL_USE_TLS = True
- EMAIL_HOST = 'smtp.gmail.com'
- EMAIL_PORT = 587
- EMAIL_HOST_USER = '<your-email>'
- EMAIL_HOST_PASSWORD = '<your-password>'

## Run initial Migration
python3.6 manage.py makemigrations parlour
python3.6 manage.py migrate
## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8800

 ## Known bugs
Like functionality not well implemented

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- Heroku
- Postgresql
## Support and contact details
Contact me for further help/support

License
Copyright (c) ikerriz