Start developing:
-source venv/bin/activate
-export DEVELOPMENT_MODE="True"
-export DEBUG="True"

Start local web server: 
?python manage.py makemigrations
?python manage.py migrate
-python manage.py runserver

Retrieve code running in live environment:
-git pull (retrieves code)

Push your code to the live environment
-git pull (retrieves code)
-git add . (add all your editted files to the change)
-git commit -m "GEEF HIER JE VERANDERING EEN NAAM" (Create a change/give it a name)
-git push (push code to live environment)









Setup project:
Update:                 sudo apt-get update

Install virtual env:    pip install virtualenv
Create virtual env:     python -m venv venv
Activate virtual env:   source venv/bin/activate

Install libpq-dev:      sudo apt-get install libpq-dev
Install requirements:   pip install -r requirements.txt



VSCODE SETUP:
Install Python debugger and Django extensions
Create a launch.json file with a Django debug configuration

Add the following virtual env variables to launch.json:
"env": {
            "DEVELOPMENT_MODE": "True",
            "DEBUG": "True",
            "SECRET_KEY": "DJANGO_SECRET_KEY",
        }



If you want to run a django command, load env variables manually:
source venv/bin/activate
export DEVELOPMENT_MODE="True"
export DEBUG="True"
python manage.py [command]



GIT:
Be in dev branch:   git branch
    If not:         git checkout dev        

Push code:          git pull
                    git push      

Undo remote commit: git reset HEAD^ --hard
                    git push -f