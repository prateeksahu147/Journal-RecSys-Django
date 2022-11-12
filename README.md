# RecSys-Django-Application

## Content-based recommendation system
* Content-based recommendation systems recommend items to a user by using the similarity of items. This recommender system recommends products or items based on their description or features. It identifies the similarity between the products based on their descriptions. It also considers the user’s previous history in order to recommend a similar product.



## Data 
1. Download "data" folder from [here](www.google.com) and past into "server" folder.

## Run App

1. Installing virtualenv
- python3 -m pip install --user virtualenv/

2. Creating a virtual environment at root folder
- python3 -m venv env

3. Activating a virtual environment
- source env/bin/activate

4. install packages using pip according to the requirements.txt
- pip install -r server/requirements.txt

5. Go to "server" folder and Run Django Application
- python manage.py runserver 

6. Use this URL for Journal Recommendation System
- http://127.0.0.1:8000/journal
- Note : Local host "127.0.0.1:8000" may be different as per local machine
