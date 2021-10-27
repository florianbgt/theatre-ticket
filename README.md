# Tickets app

## Simple tickets app using Django and Nuxt.js

This app allow you to assign seats to groups and retrieve tickets

## Dependencies

The only dependencies needed to run this app are Docker and Docker Compose

## Usage

To use this app:

- Clone this repository
- Run the following command `docker-compose up`

A sqlite database will automatically be created and populated, migrations will be applied and a superuser will be created.

The Django rest API is served here: http://tickets.localhost/api/

You can log into the admin page (http://tickets.localhost/api/admin/) using the admin user (user: admin, password: testpass123)

The Nuxt Universal app is served here: http://tickets.localhost/