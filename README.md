# Bachelor Semester Project 3

This project contains a website created with Django 3.1.1, Python 3.7, HTML 5 and CSS combined with the library Bootstrap 4.

## Installation

Using the package manager [pip](https://pip.pypa.io/en/stable/):

If a virtual environment is required, create and activate it by executing the following lines in the terminal:
```bash
python3 -m venv venv
source venv/bin/activate
```
Then, upgrade **pip** and install all the requirements:
```bash
pip3 install --upgrade pip
pip3 install --no-cache-dir -r requirements.txt
```

The project uses the database PostgreSQL which has to be downloaded [here](https://www.postgresql.org/download/) in order to create a database for the website (I would recommand to download the [Postgres App](https://postgresapp.com/)).

## Usage

To run the webiste on your local machine:
- Open the Postgres App and create a server and a database
- Open the Porject and go to the directory "GoodnessGroceries_Project" in the main folder
- Open the python file "settings.py" and scroll down to "DATABASES", there you have to change the settings such that it corresponds to your created databse
- Open the terminal and go to the folder where the project is located (the "manage.py" file should be located in this folder)
- Being in this folder in the terminal, run the command ``` python3 manage.py runserver``` (The database server has to be running)
- The server is now running on your local host, to access the webiste go to some browser (Chrome was used for developping) and go to http://localhost:8000/, this will redirect you to your local host with the port 8000 where the webiste is running
