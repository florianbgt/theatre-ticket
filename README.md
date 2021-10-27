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

The Nuxt app is server side rendered (on hard refresh, great for SEO!) and is hydrated to become a SPA after and provide a smooth user experience

## To improve

It would be great to implement the assign seat algorithm API endpoint in a async way.

Indeed, this API endpoint takes time to complete. It would be nicer for the user to have this task done in the background, return a task ID and polling url, and have a polling in the frontend to retrieve the results once available from the polling url using the task id.

I have never done such thing and I unfortunately run out of time to try such implementation.
However, here is what I would try to do: https://testdriven.io/blog/django-and-celery/