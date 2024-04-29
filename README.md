# Course Registration System

## Getting Started
This application uses MySQL as a primary database using a docker image.<br>
Download MySQL image: https://hub.docker.com/_/mysql<br>
Run it with the environment variable `MYSQL_ROOT_PASSWORD` that has the password of the root user.<br>
Execute this command in the container in order to run MySQL commands: 
```sh
mysql -u root -p
```
then enter the password which is set in the environment variables.<br>
Execute: 
```sh
CREATE DATABASE reg;
```
and use the name `reg` for the client connection.<br>
To start using the database and execute SQL queries, execute:
```sh
USE reg;
```

TODO: indexes, health check, pagination, swagger ui, custom errors page 