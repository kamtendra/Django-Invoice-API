# Django Invoice API

This project implements a simple Django API using Django Rest Framework to manage invoices and associated details.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django-invoice-api.git
   cd django-invoice-api
   ```

2. Install the dependencies 

   ```bash
   pip install -r requirements.txt
   ```   

3. Apply database migrations
   
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```  

## Usage

1. Run the development server:
   
   ```bash
   python manage.py runserver
   ``` 

   The API will be available at http://127.0.0.1:8000/api/

## API Endpoints

GET /api/invoices/: List all invoices.

GET /api/invoices/<int:pk>/: Retrieve a specific invoice.

POST /api/invoices/: Create a new invoice.

PUT /api/invoices/<int:pk>/: Update a specific invoice.

DELETE /api/invoices/<int:pk>/: Delete a specific invoice.

GET /api/invoices-details/: List all invoice details.

GET /api/invoices-details/<int:pk>/: Retrieve a specific invoice detail.

POST /api/invoices-details/: Create a new invoice detail.

PUT /api/invoices-details/<int:pk>/: Update a specific invoice detail.

DELETE /api/invoices-details/<int:pk>/: Delete a specific invoice detail.

## Testing 

Run the test suite:

```bash
python manage.py test

```