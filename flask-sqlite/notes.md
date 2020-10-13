docker build -t jstnck/bball-api_flask-sqlite .

docker run --rm -p '8080:8080' jstnck/bball-api_flask-sqlite 


NEXT STEPS - FIX APP USING
https://github.com/schoolofcode-me/stores-rest-api.git

seems like we need a run.py to run db.init_app(app) 
sqlalchemy seems to want this...

