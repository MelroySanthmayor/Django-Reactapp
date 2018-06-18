# Django-Reactapp
E-commerce site with Django rest framework and React js

Steps to run the project in your local machine 
1) After cloning the repo run npm install in the Frontend directory to install dependencies ,if Problems occur with
   ._parent.js file run yarn remove lodash and yarn add lodash@4.17.9
   
2) Open another terminal in the Shop_api folder and Run the command python manage.py makemigrations and after that
   runs successfully run Python manage.py migrate
   
3) Run the command python manage.py runserver to start the server at Localhost Port:8000  

4) Go to the terminal inside the Frontend folder and run the command npm run build ,frontend of the project is 
   served at Localhost port:3000

Status Of the Project: currently under development, handling JWT authentication feature and implementing redux.
