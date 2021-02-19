# Blog-Application System

Blog-Application System provides a way of creating and sharing of blogs using the given system. Users can follow or unfollow each others and based on the following users see the blogs on home screen of the system.

## Installation

`install.sh` will install all dependencies required to run this application which includes python 3, pip and other required packages which is defined in Pipfile.lock file. Additionally it will ask you for the permission to install the pacakges.

```bash
./install.sh
```

## Requirements

Python 3 and pipenv will be installed via `install.sh` file which is covered in Installation section. In ubuntu 20.04 python 3 is built-in package which is already installed in the system. For the case we are using `db.sqlite3` file to store the data. Additionally, we can also store the data in any other data storage applications such as relational databases, no-sql databases etc.

- Ubuntu 20.04
- Python 3.8
- Pipenv
- Sqlite3 Database
- Django Framework

## Run application

In order to run the django development server execute following commands which will starts the server at http://localhost:8000

**Note:** `pipenv shell` command activates the virtual environment.

```bash
cd blog
pipenv shell
python manage.py runserver
```

Output:

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 19, 2021 - 19:15:20
Django version 3.1.6, using settings 'blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Project Code Structure Overview

Project consists of 3 main applications i.e posts, follow and authentication. Each application is based on django directory & file structure. Same overview is presented below:

- **Pipfile** -> Pipenv configuration file
- **Pipfile.lock** -> Contains packages dependencies configuration and hashes
- **manage.py** -> Entry point of the application
- **models.py** -> Database schema defined in this file for each apps
- **views.py** -> APIs are defined in this module for each apps
- **usecases.py** -> All the use cases implemented by the application are defined in this file

- **settings.py** -> All the application configuration variables are placed in this file
- **db.sqlite3** -> Database file
