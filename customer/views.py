# views.py
from rest_framework import viewsets
from .models import Customer, Plan
from .serializers import CustomerSerializer, PlanSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Plan  # Import your Plan model

@api_view(['POST'])
def renew_plan(request):
    # Get renewal date and plan status from the request data
    renewal_date = request.data.get('renewal_date')
    plan_status = request.data.get('plan_status')
    
    # Assuming renewal_date is in ISO 8601 format (e.g., '2024-04-01')
    # Convert renewal_date to a datetime object
    renewal_datetime = datetime.strptime(renewal_date, '%Y-%m-%d')
    
    # Calculate the new expiry date (e.g., renew for 1 year)
    new_expiry_date = renewal_datetime + timedelta(days=365)
    
    # Update plan status to 'Active'
    new_plan_status = 'Active'
    
    # Update the plan in the database
    try:
        plan = Plan.objects.get(id=request.data.get('plan_id'))  # Assuming you have a 'plan_id' field in the request data
        plan.expiry_date = new_expiry_date
        plan.status = new_plan_status
        plan.save()  # Save the changes to the database
        return Response({'message': 'Plan renewed successfully', 'new_expiry_date': new_expiry_date.strftime('%Y-%m-%d')}, status=status.HTTP_200_OK)
    except Plan.DoesNotExist:
        return Response({'error': 'Plan not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def upgrade_downgrade_plan(request):
    # Get data for upgrading/downgrading the plan from the request data
    existing_plan_name = request.data.get('existing_plan_name')
    new_plan_name = request.data.get('new_plan_name')
    plan_cost = request.data.get('plan_cost')
    validity_days = request.data.get('validity_days')
    plan_status = request.data.get('plan_status')
    
    # Retrieve the existing plan from the database
    try:
        existing_plan = Plan.objects.get(plan_name=existing_plan_name)
    except Plan.DoesNotExist:
        return Response({'error': 'Existing plan does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # Update the plan attributes with the new values
    existing_plan.plan_name = new_plan_name
    existing_plan.plan_cost = plan_cost
    existing_plan.validity_days = validity_days
    existing_plan.plan_status = plan_status
    
    # Save the updated plan
    existing_plan.save()
    
    # Assuming you want to return a success response
    return Response({'message': 'Plan upgraded/downgraded successfully'}, status=status.HTTP_200_OK)