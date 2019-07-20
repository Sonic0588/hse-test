### Create local database and its user:
* `sudo -u postgres psql -c "create user hseuser with login password 'hsepass' superuser;"`
* `sudo -u postgres psql -c "create database hsetest owner hseuser encoding = 'UTF8';"`
