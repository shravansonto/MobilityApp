# MobilityApp
MobilityApp

# Mobility Project

This project is a Django-based RESTful API for managing customers and their subscription plans.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- Django
- Django REST Framework

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/shravansonto/MobilityApp.git

2. cd MobilityApp
    pip install -r requirements.txt

3. Apply database migrations:
 python manage.py migrate

4. Run the development server:
    python manage.py runserver

API Endpoints
http://localhost:8000/mobility/customers/: CRUD operations for managing customers.
http://localhost:8000/mobility/plans/: CRUD operations for managing subscription plans.
http://localhost:8000/mobility/renew-plan/: API endpoint for renewing a subscription plan.
http://localhost:8000/mobility/upgrade-downgrade-plan/: API endpoint for upgrading/downgrading a subscription plan.

