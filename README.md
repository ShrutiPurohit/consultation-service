# consultation-service
A web-based medical consultation service

## Working of the Web Application:

  1. A user has to login to use the application. If he/she is using the web application for the first time, then he/she should first register. It does not allow to register if the username and password is not unique.
  2. After logging in, the user can send a new consultation request or view his/her history of all consultation requests sent by him.
  3. If the logged in user is the assistant (the person in charge of handling online consultation requests), then he/she is redirected to a personalised home page, which has special functionalities exclusive for the assistant. The functionalities are :
      a) Viewing all consultation requests made.
      b) Viewing all consultation requests made on the basis of specific tags.
      c) Conveying the appropriate diagnosis given by the medical practitioner to the patient, by updating the consultation request.

### Membership:
Django authentication system: Django authentication provides both authentication and authorization together.
We have used django.contrib.auth.views module for the login and logout views.

Home page has two links:
  1. Login
  2. Register

## Functionalities:
    1.    To register onto the web application: register/ 
Enter username, email id and password through a form. Username and email should be unique, if not registration fails.

    2.    To login: login/
Using django authentication system, django.contrib.auth.views.login.
Enter username and password to login.

    3.    To logout: logout/
Using django authentication system, django.contrib.auth.views.logout.

### Functionalities of User:

    1.    To view history: /history
Displays all consultation requests made by the logged-in user and their current status.

### Functionalities of Assistant:

Home page of Assistant: /homeassist

Contains the following functionalities:

    1.    To view all requests: /allcases
Displays all transaction requests that have been made with their details.

    2.    To view all requests with particular tags: casetag/tag
Home page of assistant displays various tags. When he/she clicks on the particular tag, then all consultation requests relevant to that tag are displayed.

    3.    To update the requests with the prescribed diagnosis: update/caseid
When a consultation request is displayed to the assistant, he/she is provided with the functionality to update each request so as to fill or update the diagnosis that was prescribed by the doctor for that particular request. If he/she clicks the update link, then it redirects to a form where he/she can post the diagnosis message.
