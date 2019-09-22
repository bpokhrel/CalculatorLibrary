# project_storm

## To run

Install virtualenv

Then:

virtualenv -p /usr/bin/python2.7 venv

source venv/bin/activate

pip install -r req.txt

env FLASK_APP=hello.py flask run

## Remember to freeze libraries

pip freeze > req.txt
