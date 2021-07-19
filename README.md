# jubilant-doodle
projectDjango
Its a simple shopping web page that displays the list of customers using a graph
How to setup locally
# Requirements
Python3.7
pip3
virtualenv
# setup instructions
pull the project using git
   git clone https://github.com/naaadjeleyc/jubilant-doodle.git
create a virtualenv using virtualenv
   python -m pip install --upgrade pip
   pip install virtualenv
   virtualenv .venv
activate it
   source .venv/bin/activate
or activate Windows
   .venv/bin/activate.bat
install dependencies from the requirements.txt file
   pip install -r requirements.txt
migrate the database tables
   python manage.py migrate
start a development server using
   python manage.py runserver

 # Testing
 A simple unit test to test forms and views
