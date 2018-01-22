# Inception on Heroku

Google's Inception Image Recognition as a Heroku API

* [Python on Heroku](https://github.com/EN10/PythonHeroku)  
* [Image Recognition with Inception](https://github.com/EN10/SimpleInception)  
* [Node API](https://github.com/EN10/InceptionWebAPI)
* [Bash in Python](http://blog.nuventure.in/2014/09/04/executing-bash-commands-via-python)
* [Flask Query Strings](https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask)



#### Install

    sudo pip install heroku gunicorn flask tensorflow

**Setup Git **

    git init
    git add requirements.txt Procfile run.sh app.py  
    git commit -am "init"  
    
**Setup Heroku**

    heroku login
    heroku git:remote -a image001

**Push to Heroku**

    git push heroku master

**Run App Locally**

    export FLASK_APP=app.py
    flask run --host=0.0.0.0 --port=8080
    
Example cs50 URL:   http://heroku-eniof.cs50.io

Query Test: http://heroku-eniof.cs50.io/?q=http://saxony-blue.com/data/out/86/5918348-image.jpg