# EpicEvents

Epic Events is an event management and consulting company that meets the needs of start-ups wanting to organize "epic parties"

Epic Events customer relationship management software is a secure application that will allow you to manage upcoming events, customers and their contracts


<li><a href="#requirements">Requirements</a></li>
<li><a href="#gitbash">Gitbash</a></li>
<li><a href="#installation-on-windows">Installation on Windows</a></li>
<li><a href="#installation-on-linux">Installation on Linux</a></li>
<li><a href="#installation-on-mac">Installation on Mac</a></li>
<li><a href="#setup-the-application">Setup The Application</a></li>
<li><a href="#postman-documentation">POSTMAN Documentation</a></li>


## Requirements
```bash
Python 3.9.0
```
## Gitbash
You have to clone the deposit with this command on gitbash :
```
git clone https://github.com/Papiex/EpicEvent/
```

## Installation on Windows
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
- if you use PowerShell :
``` env/Scripts/activate.ps1```
- if you use CMD or terminal that supports __.bat__ :
``` env/Scripts/activate.bat```

## Installation on Linux
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Installation on Mac
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Libraries
__This program need some libraries, for installing them, use this command (in your virtual env) :__

*View requirements.txt to know which library/version is used*

- ```pip3 install -r requirements.txt``` | Windows : ```pip install -r requirements.txt```


## Setup The Application

After you have setup the environment and installed all requirements :

__1- Install PGAdmin and setup postgre database :__

- Go to https://www.pgadmin.org/download/ and install pgadmin according to your os
- Setup your master password in pgadmin
- Setup your username and password like this : ```username : postgres password : test```
- Create database and give this name : ```epicevent```

_The settings in django are pre-configured with this identifiers_

__2- Naviguate to Epic-Events\Epic_Event_APP\ an run this management commands in orders :__

- ```python manage.py set_groups_permissions```

_set group permission will create group permission for the saler, gestion and support user_

- ```python manage.py create_testing_users```

_this command create testings users, check below for identifiers_

### Testing Accounts Identifiers

ADMIN USER (can login to admin panel) :

Username ```admin_user```

Password ```motdepasse78```

GESTION USER (can login to admin panel):

Username ```gestion_user```

Password ```motdepasse78```

SALER USER :

Username ```saler_user```

Password ```motdepasse78```

SUPPORT USER :

Username ```support_user```

Password ```motdepasse78```

## POSTMAN Documentation

Except the admin user (only for admin panel), all request on endpoints need to be executed with POSTMAN

The documentation and all endpoints can be found here :