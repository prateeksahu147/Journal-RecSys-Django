# RecSys-Django-Application

## Content-based recommendation system
* A Content-based recommendation system suggests items to a user by evaluating the similarity between them. This type of recommender system focuses on the characteristics or attributes of the products being recommended, and it uses the descriptions of these items to identify similarities. Additionally, the user's past behavior and preferences may also be taken into account to provide more personalized recommendations.



## Data 
1. Download "data" folder from [here](www.google.com) and past into "server" folder.

## Run App

1. Install virtual env
- python3 -m pip install --user virtualenv/

2. Create a virtual environment at the root folder
- python3 -m venv env

3. Activate the virtual environment
- source env/bin/activate

4. install packages using pip according to the requirements.txt
- pip install -r server/requirements.txt

5. Go to "server" folder and Run Django Application
- python manage.py runserver 

6. Use this URL for Journal Recommendation System
- http://127.0.0.1:8000/journal
- Note : Local host "127.0.0.1:8000" may be different as per local machine
