# Inception on Heroku

Google's Inception Image Recognition as a Heroku API    
The model can detect 1000 Classes:  [ImageNet Link](http://image-net.org/challenges/LSVRC/2012/browse-synsets) or [Internet Archive Link](http://web.archive.org/web/20130405004914/http://image-net.org:80/challenges/LSVRC/2012/browse-synsets)

* [Python on Heroku](https://github.com/EN10/PythonHeroku)  
* [Image Recognition with Inception](https://github.com/EN10/SimpleInception)  
* [Node API](https://github.com/EN10/InceptionWebAPI)
* [Bash in Python](http://blog.nuventure.in/2014/09/04/executing-bash-commands-via-python)
* [Flask Query Strings](https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask)

#### Install

    sudo pip install heroku gunicorn flask tensorflow

**Setup Git**

    git init
    git add runtime.txt requirements.txt run.sh Procfile app.py  
    git commit -am "init"  
    
**Setup Heroku**

    heroku login
    heroku git:remote -a image001

**Push to Heroku**

    git push heroku master

**Run App Locally**

    export FLASK_APP=app.py
    flask run --host=0.0.0.0 --port=8080

**Test:**    

* Example cs50 URL:   http://heroku-eniof.cs50.io
* cs50 test:    http://heroku-eniof.cs50.io/?q=http://saxony-blue.com/data/out/86/5918348-image.jpg
* Heroku test:  https://image001.herokuapp.com/?q=http://saxony-blue.com/data/out/86/5918348-image.jpg