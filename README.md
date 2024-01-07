## OrderManagement - Django Dashboard App
This Django project, named OrderManagement, includes a powerful app called OrderApp designed to manage and analyze customer orders efficiently. The app provides a comprehensive dashboard that displays key metrics and insights related to orders and customers.
## Dashboard Features:
## Total Orders:
- Displays the total count of unique orders within the specified date range.

## Total Customers:
- Shows the total number of unique customers.

## Average Order Value:
- Calculates and presents the average order value based on the total order records.

## Date Filtering:
- Provides basic date filtering options to narrow down data based on a specified start and end date.

## How to Use:
- Clone the repository named OrderManagement to your local machine.
- git clone https://github.com/kksain/OrderManagement.git

## Set Up Virtual Environment:
- Create and activate a virtual environment within the project directory.
-cd OrderManagement
-python -m venv venv
-venv\Scripts\activate

## Install Dependencies:
- pip install -r requirements.txt
  
## Run Migrations:
- python manage.py migrate

## Create Superuser (Admin):
- python manage.py createsuperuser

## Run the Development Server:
- python manage.py runserver
