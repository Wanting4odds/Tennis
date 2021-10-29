Project for Homework from Smartodds
==================================

The homework using Python + Django + MySQL.

### For CI strategy: We can use Jenkins.
Add a new job on Jenkins: 
The main step:
```
1. git clone the repository
2. run lint to check syntax and test cases
3. setup notification of email or chat channel(Ex: Microsoft Teams), once Jenkins build fails, 
   we can find errors immediately.
```

## How to deploy ##
> Run `docker-compose up`to aggregates the output of each container


## How to import .xls data ##
>  1. Visit <http://0.0.0.0:8080>
>  2. Select '.xls' file at local
>  3. Click on 'Upload' Button

## How to GET all info ##

> `curl -v http://0.0.0.0:8080/result/`

Or

> Visit <http://0.0.0.0:8080/result/>


Or

> Visit <http://0.0.0.0:8080/admin/>

## How to GET info by id ##

> `curl -v http://0.0.0.0:8080/result/{id}`

Or

> Visit <http://0.0.0.0:8080/result/{id}>

## How to POST info ##

> `curl -d {data} http://0.0.0.0:8080/result/`

Or

> Visit <http://0.0.0.0:8080/result/>

## How to DELETE info ##

> `curl -X DELETE http://0.0.0.0:8080/result/{id}`

Or

> Visit <http://0.0.0.0:8080/result/{id}>

## Running tests ##
> `python3 manage.py test`
