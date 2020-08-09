# customermanagement
Django Rest Service

Django Application hosted on heroku with User and Activity Period prepopulated.

Custom Management Script to populate the User and his session activity to the models. Faker module is used to populate data

Steps to be Followed to run the application in Local.

1) Create a virtual environment. [virtualenv venv]
2) Requirements.txt files contains all the neccessary dependencies.
3) Run the server from local.
4) To add data run the script populate_data.py which has 2 function ( CreateUser and CreateActivityData )
    > Both takes single argument n (number of records to be created).
    
Heroku App:
URL: https://customermanagementdetails.herokuapp.com/customerdetails/

> I have removed Django build in static files and json is rendered in a default way.




