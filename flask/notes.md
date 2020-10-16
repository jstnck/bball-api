docker exec -it 1b8a3d25c84a bash


#### example
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/DBNAME"


make use of 
\conninfo
in posgres container

want database 'postgres' as user 'posgres' via socket(?) in /var/run/postgresql at port 5432

socket may be hostname (locally would create a socket to the directory, in docker it points to host?)

