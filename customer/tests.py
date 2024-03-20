# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Customer, Plan
from rest_framework import status
from datetime import datetime, timedelta
from django.urls import reverse
from .models import Plan
from datetime import datetime, timedelta, time
# tests.py
class CustomerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {
            'name': 'John Doe',
            'dob': '1990-01-01',
            'email': 'john@example.com',
            'adhar_number': '123456789012',
            'assigned_mobile_number': '9876543210'
        }
        self.plan_data = {
            'plan_name': 'Platinum365',
            'plan_cost': '499',
            'validity_days': '365',
            'plan_status': 'Active'
        }

    def test_create_customer(self):
        response = self.client.post('/mobility/customers/', self.customer_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_plan(self):
        response = self.client.post('/mobility/plans/', self.plan_data, format='json')
        print(response)
        self.assertEqual(response.status_code, 201)

    def test_renew_plan(self):
        # Create a plan object for testing
        plan = Plan.objects.create(
            expiry_date=datetime.now() + timedelta(days=30),  # Set expiry date to 30 days from now
            plan_status='Inactive',
            plan_cost=0,  # Provide a default value for plan_cost
            validity_days=30  # Provide a default value for validity_days
        )

        # Define the data for renewing the plan
        renewal_date = '2024-04-01'
        plan_status = 'Active'
        plan_id = plan.id

        # Prepare the request data
        renew_data = {
            'renewal_date': renewal_date,
            'plan_status': plan_status,
            'plan_id': plan_id,
        }

        # Call the renew plan API endpoint
        url = reverse('customer:renew-plan')
        response = self.client.post(url, renew_data, format='json')

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the plan was renewed successfully
        self.assertEqual(response.data['message'], 'Plan renewed successfully')

        # Check that the plan expiry date is updated
        renewed_plan = Plan.objects.get(id=plan_id)
        
        # Compare renewed_plan.expiry_date with today's date
        self.assertTrue(renewed_plan.expiry_date > datetime.now().date())

    def test_upgrade_downgrade_plan(self):
        # Create an existing plan object for testing
        existing_plan = Plan.objects.create(
            plan_name='Silver90',
            plan_cost=199,
            validity_days=90,
            plan_status='Active'
        )

        # Define the data for upgrading/downgrading the plan
        existing_plan_name = 'Silver90'
        new_plan_name = 'Gold180'
        plan_cost = 299
        validity_days = 180
        plan_status = 'Active'
        plan_id = existing_plan.id

        # Prepare the request data
        upgrade_downgrade_data = {
            'existing_plan_name': existing_plan_name,
            'new_plan_name': new_plan_name,
            'plan_cost': plan_cost,
            'validity_days': validity_days,
            'plan_status': plan_status,
            'plan_id': plan_id,
        }

        # Call the upgrade/downgrade plan API endpoint
        url = reverse('customer:upgrade-downgrade-plan')
        response = self.client.post(url, upgrade_downgrade_data, format='json')

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the plan was upgraded/downgraded successfully
        self.assertEqual(response.data['message'], 'Plan upgraded/downgraded successfully')

        # Check that the plan details are updated
        updated_plan = Plan.objects.get(id=plan_id)
        
        # Check that the plan details are updated correctly
        self.assertEqual(updated_plan.plan_name, new_plan_name)
        self.assertEqual(updated_plan.plan_cost, plan_cost)
        self.assertEqual(updated_plan.validity_days, validity_days)
        self.assertEqual(updated_plan.plan_status, plan_status)