## Dockerizing a Udemy course: Flask, Postgres, Nginx

This repo contains a REST API using Flask, which reads/writes to a Postgres database. 

The Flask API comes from a udemy course: [REST APIs with Flask and Python](https://www.udemy.com/course/rest-api-flask-and-python/)
by Jose Salvatierra

I created a docker-compose file to run all of the components in containers, for easy deployment on AWS EC2. After installing docker and docker-compose, run 'docker-compose up --build' in the project directory to start the application.

docker-compose.yml will create the following containers:

    1. Nginx server listening on port 80
    2. Flask API with uwsgi application server
    3. Postgresql database
    4. Adminer to monitor Postgres, listening on port 8080

### Getting Started
1. Clone this repo to your server (currenlty configured for ubuntu on EC2)
2. Run 'sh docker-install.sh'
3. From the project directory, run 'docker-compose up --build'
4. Send an api request to [server IP]
5. Monitor the database at [server IP]:8080

License: MIT