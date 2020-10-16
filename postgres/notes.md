docker build -t jstnck/bball-api_postgres .
docker run --rm -p '5432:5432' -e POSTGRES_PASSWORD=admin jstnck/bball-api_postgres 

https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
https://docs.sqlalchemy.org/en/13/core/pooling.html#pool-disconnects

use gosu to run commands as postgres user within continer
$ gosu postgres psql

\dt lists all tables in 'postgres' database


postgres docker images, data directory:
/var/lib/postgresql/data

hba conf file: SHOW hba_file;
/var/lib/postgresql/data/pg_hba.conf
can use pg_config 

psql $ \du 
lists roles in postgres - postgres needs to exist, and be a superuser

getting error of 'database postgres does not exist'
    but, it does, so maybe the user/role is not set...
    it could also be the sqlalchemy md5 issue


initdb needs the ../data folder to be empty at startup.
so we need ititdb to change from trust to md5, not in dockerfile?
    or find a way to do it after initdb runs.
    https://www.postgresql.org/docs/9.5/app-initdb.html
    **set with authmethod?**

    **https://stackoverflow.com/questions/29580798/docker-compose-environment-variables**