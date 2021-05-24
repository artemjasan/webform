# webform
Web application in Django that allows you to fill in and save a form.

### Python version
- [Python 3.8.6](https://www.python.org/downloads/release/python-386/)

### Packages
- asgiref==3.3.4
- certifi==2020.12.5
- chardet==4.0.0
- Django==3.2.3
- idna==2.10
- lxml==4.6.3
- pkg-resources==0.0.0
- pytz==2021.1
- requests==2.25.1
- sqlparse==0.4.1
- style==1.1.0
- update==0.0.1
- urllib3==1.26.4

### Commands
#### First start
- Create the virtual environment for the project:
```shell
$ python3 -m venv venv
```
- Activate the virtual environment for the project:
```shell
$ source venv/bin/activate
```
- Update pip:
```shell
$ pip install update
```
- Install the requirements:
```shell
$ pip install -r requirements.txt
```
- CD into the project directory:
```shell
$ cd webform_project/
```
- Run migration. 
```shell
$ python manage.py migrate
```
- Create the admin-user. 
```shell
$ python manage.py createsuperuser
```
- Run the application. 
```shell
$ python manage.py runserver
```
#### Run tests
You can launch some unit tests for models, views, urls, forms.
```shell
$ python manage.py test
```