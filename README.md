README.MD

In this backend API work project, In this application, the New Aggregator is implemented to fetch the data from the two different APIs, the source of the data is Reddit and News API. The application works on both APIs fetching the results from the sources and returning the data in JSON format.
With some additional featuring in the work, I develop and implemented a function that takes any news to give in any user's favorite news. And also we can get the data from the specific user name and news id.

Prerequisite Tools:
Python == 3.8.5
Django==4.0.5
newsapi==0.1.1
newsapi_python==0.2.6
psaw==0.1.0


For the API work, we are using the POSTMAN interface to achieve the results as we directed.

Steps to Run the Program:
STEP 01: 
	 Clone this repo, and extract the files. 
git clone ( URL )
STEP 02: 
	Inside the folder, activate the Virtual Environment and Install the dependencies.
Run python3 -m venv <name_of_virtualenv>
source <name_of_virtualenv>/bin/activate
	Locate to the folder, where you see the requirement.txt file;
pip install -r requirement.txt
STEP 03:
	Run the Simple Command with manage.py
python manage.py runserver
Now, your program is running without any kind of issue or error.

STEP 04:
Open the POSTMAN, copy the local host link;
As shown in the image:


STEP 05:
For Part1 of the project;
Hit the request to get the result of a specific news topic like this;


For Part2 of the Project
When we hit the news, the database will hold the data for only 30 sec, and after this data will be removed.

For Part3 of the Project
For the specific news get the favorite news in the list, like;

For checking the specific list of a User's favorite news.



Here our desired results are shown in your database.

