## Summary:
The REST API is built using Python Django framework which is capable of filtering, grouping and sorting.
It uses simple page number based style that helps you manage the paginated data using page numbers
in the request query parameters.

Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system that is being stored and processed in a MySQL(relational) database.

It contains the below mentioned endpoint:
- a GET '/search'

## Project Structure (App Based):

```bash
AdjustTask/
├── README.md
├── .gitignore
└── adjust_task
├── Makefile
├── adjust_task
│ ├── __init__.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── apps
│ ├── __init__.py
│ ├── api
│ │ ├── __init__.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── filters.py
│ │ ├── management
│ │ │ └── commands
│ │ │ ├── __init__.py
│ │ │ └── init_db.py
│ │ ├── migrations
│ │ │ ├── 0001_initial.py
│ │ │ └── __init__.py
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── tests
│ │ │ ├── __init__.py
│ │ │ ├── test_models.py
│ │ │ └── test_views.py
│ │ ├── urls.py
│ │ └── views.py
│ └── pagination.py
├── conf
│ └── init.sql
├── data
│ └── dataset.csv
├── manage.py
└── requirements.txt
```

### Python Libraries/Frameworks used:
-  **django** - This is a Python-based open-source web framework that follows the model-template-view
architectural pattern.
-  **djangorestframework** - This is a powerful and flexible toolkit built on top of the Django web framework
for building REST APIs.
-  **django-filter** - This is a reusable Django application for allowing users to filter querysets
dynamically from URL parameters.
-  **mysqlclient** - MySQL database connector for Python.
-  **drf-yasg** - This is a Swagger generation tool provided by Django Rest Framework that allow you
to build API documentation.
-  **ddt** - Data-driven testing (DDT) is a parameterized testing that allow you to multiply one test case
by running it with different test data, and make it appear as multiple test cases.
-  **black** - This is Python code formatter that formats code adhering to PEP8 standards.

### Prerequisite
- Make sure you have Python and Mysql installed in your system :)

**Note:** Python 3.6.0 is used for the task.

### How to start application (using Virtual Environment)

- Clone the project using command:
```
git clone https://github.com/Rabia23/AdjustTask.git
```

- Setup mysql database (mac OS):
```
mysql -V (check version)
rabia@Rabias-MacBook-Pro adjust_task % mysql -V
mysql Ver 8.0.19 for osx10.15 on x86_64 (Homebrew)

mysql.server status (check the mysql status)
rabia@Rabias-MacBook-Pro adjust_task % mysql.server status
SUCCESS! MySQL running (9963)

mysql.server start (run the mysql server)
rabia@Rabias-MacBook-Pro adjust_task % mysql.server start
Starting MySQL
.. SUCCESS!

mysql.server stop (stop the mysql server)
rabia@Rabias-MacBook-Pro adjust_task % mysql.server stop
Shutting down MySQL
.. SUCCESS!

mysql -u root -p (login into mysql server)
rabia@Rabias-MacBook-Pro adjust_task % mysql -u root -p
Enter password: root

create databases and database user
mysql> source /Users/rabia/Downloads/AdjustTask/adjust_task/conf/init.sql (absolute path to init.sql file)

mysql> show databases;
mysql> select Host, User from mysql.user;
mysql> use adjustdb;
mysql> show tables; (it doesn't have any tables right now. We will create it later)
mysql> exit
```

- Create and activate the virtual environment:
```
python3 -m venv env
source env/bin/activate
```

- Go into the project directory:
```
cd adjust_task
```

- Install project requirements:
```
make install-requirements
```

- Create database tables:
```
make migrate
```

- Show database migrations:
```
make showmigrations
```

- Import data into database from csv file:
```
make init-db
```

- Run the application by the following command:
```
make start-server
```

### How to run django admin

- Create application super user:
```
make create-superuser
```

- Run the django admin by entering following command in the browser:
```
localhost:8080/admin
Enter the credentials that you have created above using command and you are good to go.
```

### How to run application unittests

- Run the command to run the all unittests of the application:
```
make tests
```

**Note:** The tests command uses the --keepdb option. It preserves the test database between test runs. It skips the create and destroy actions which can greatly decrease the time to run tests.
  
### Different ways to test the API

- How to test using Swagger UI:
	- Hit the url in the browser:
		```
		localhost:8080/api-docs/
		```

- How to test using CURL:
	- Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
		```
		curl -X GET "http://localhost:8080/api/search/?date_to=2017-06-01&groupby=channel%2Ccountry&annotate=impressions%2Cclicks&ordering=-clicks" -H  "accept: application/json"
		{"count":25,"next":"http://localhost:8080/api/search/?annotate=impressions%2Cclicks&date_to=2017-06-01&groupby=channel%2Ccountry&ordering=-clicks&page=2","previous":null,"results":[{"channel":"adcolony","country":"US","impressions":532608,"clicks":13089},{"channel":"apple_search_ads","country":"US","impressions":369993,"clicks":11457},{"channel":"vungle","country":"GB","impressions":266470,"clicks":9430},{"channel":"vungle","country":"US","impressions":266976,"clicks":7937},{"channel":"unityads","country":"US","impressions":215125,"clicks":7374},{"channel":"facebook","country":"DE","impressions":214725,"clicks":6282},{"channel":"google","country":"US","impressions":211378,"clicks":6252},{"channel":"chartboost","country":"US","impressions":158894,"clicks":4725},{"channel":"unityads","country":"GB","impressions":158933,"clicks":4635},{"channel":"chartboost","country":"GB","impressions":106261,"clicks":4181},{"channel":"google","country":"GB","impressions":106905,"clicks":4126},{"channel":"apple_search_ads","country":"GB","impressions":106416,"clicks":3701},{"channel":"unityads","country":"CA","impressions":105659,"clicks":3621},{"channel":"facebook","country":"US","impressions":105686,"clicks":3584},{"channel":"google","country":"FR","impressions":106165,"clicks":3252},{"channel":"chartboost","country":"FR","impressions":106530,"clicks":3155},{"channel":"facebook","country":"GB","impressions":105988,"clicks":3082},{"channel":"apple_search_ads","country":"DE","impressions":52777,"clicks":2096},{"channel":"chartboost","country":"DE","impressions":105990,"clicks":2072},{"channel":"unityads","country":"DE","impressions":54060,"clicks":1638}]}
		```
	- Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
		```
		curl -X GET "http://localhost:8080/api/search/?date_from=2017-05-01&date_to=2017-05-31&os=ios&groupby=date&annotate=installs&ordering=date" -H  "accept: application/json"
		{"count":15,"next":null,"previous":null,"results":[{"date":"2017-05-17","installs":755},{"date":"2017-05-18","installs":765},{"date":"2017-05-19","installs":745},{"date":"2017-05-20","installs":816},{"date":"2017-05-21","installs":751},{"date":"2017-05-22","installs":781},{"date":"2017-05-23","installs":813},{"date":"2017-05-24","installs":789},{"date":"2017-05-25","installs":875},{"date":"2017-05-26","installs":725},{"date":"2017-05-27","installs":712},{"date":"2017-05-28","installs":664},{"date":"2017-05-29","installs":752},{"date":"2017-05-30","installs":762},{"date":"2017-05-31","installs":685}]}
		```
	- Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
		```
		curl -X GET "http://localhost:8080/api/search/?date_from=2017-06-01&date_to=2017-06-01&country=US&groupby=os&annotate=revenue&ordering=-revenue" -H  "accept: application/json"
		{"count":2,"next":null,"previous":null,"results":[{"os":"android","revenue":"1205.21"},{"os":"ios","revenue":"398.87"}]}
		```
	- Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
		```
		curl -X GET "http://localhost:8080/api/search/?country=CA&groupby=channel&cpi=true&annotate=spend&ordering=-cpi" -H  "accept: application/json
		{"count":4,"next":null,"previous":null,"results":[{"channel":"facebook","spend":"1164.00","cpi":"2.07"},{"channel":"chartboost","spend":"1274.00","cpi":"2.00"},{"channel":"unityads","spend":"2642.00","cpi":"2.00"},{"channel":"google","spend":"999.90","cpi":"1.74"}]}
		```

- How to test using Postman collection:
	- import the attached postman collection in the postman application and start playing with the API.

### Equivalent mysql queries
```
mysql> select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from api_dataset where date <= '2017-06-01' group by channel, country order by clicks desc;

mysql> select date, sum(installs) from api_dataset where date between "2017-05-01" and  "2017-05-31" and os = "ios" group by date order by date;

mysql> select os, sum(revenue) as revenue_earned from api_dataset where date = "2017-06-01" and country = "US" group by os order by revenue_earned desc;

mysql> select channel, sum(spend) as spends, sum(spend)/sum(installs) as cpi from api_dataset where country="CA" group by channel order by cpi desc;
```

#### Things that are not included in the task due to time constraints and make the task easy to review from reviewer's perspective:
- API authentication is not added. The API endpoint is public.
- Data will be inserted once from csv file into database. If you want to insert it again, you need to truncate/delete the data from the table.
- Database credentials are directly added in the settings.py file. It should be confidential from security prespective.
- Python logs are being displayed on the console instead of file for the sake of simplicity.
- Only `sum` function is used in the annotate query.
