# LAB - Class 33

## Project: Authentication and Production Server

## Author: Eric Mungai Kinuthia

## About 

This project implements a basic Django API with CRUD methods available and  JWT Authentication.

## Links and Resources

[Gunicorn](https://gunicorn.org/)

[Whitenoise](http://whitenoise.evans.io/en/stable/django.html)

## Setup

PORT=http://127.0.0.1:8000/

DATABASE_URL=http://127.0.0.1:8000/api/v1/movies

## How to initialize

`docker-compose up`
`docker-compose run web python manage.py makemigrations`
`docker-compose run web python manage.py migrate`
`docker-compose run web python manage.py createsuperuser`

## Steps to manually test using Thunderclient

Obtain the API endpoint URL for the token endpoint i.e `http://127.0.0.1:8000/api/token/`

Use the Thunderclient to send a `POST request` to the token endpoint.

Include the necessary authentication credentials in the request `BODY` i.e. the username and password.

Example 
```
{"username":"user","password":"pass"}
```

Send the request and receive the response. 

The response should contain information about the token, including its value and any associated metadata.

Both the `access token` and the `refresh token` are in the response.

