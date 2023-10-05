from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from monte_carlo_simulation.models import Trial
from monte_carlo_simulation.serializers import TrialSerializer


@api_view(['GET', 'POST', 'DELETE'])
def trial_list(request):
    # GET list of trials, POST a new trial DELETE all trials
    if request.method == 'GET':
        trials = Trial.objects.all()
        trials_serializer = TrialSerializer(
            trials, many=True)
        return JsonResponse(trials_serializer.data, safe=False)
    elif request.method == 'POST':
        trials_data = JSONParser().parse(request)
        trials_serializer = TrialSerializer(
            data=trials_data)
        if trials_serializer.is_valid():
            trials_serializer.save()
            return JsonResponse(trials_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(trials_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Trial.objects.all().delete()
        return JsonResponse({'message': f'{count} trials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def trial_detail(request, pk):
    # find trial by pk (id)
    try:
        trial = Trial.objects.get(pk=pk)
    except Trial.DoesNotExist:
        return JsonResponse({'message': 'The trial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        trial_serializer = TrialSerializer(trial)
        return JsonResponse(trial_serializer.data)
    elif request.method == 'PUT':
        trial_data = JSONParser().parse(request)
        trial_serializer = TrialSerializer(
            trial, data=trial_data)
        if trial_serializer.is_valid():
            trial_serializer.save()
            return JsonResponse(trial_serializer.data)
        return JsonResponse(trial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        trial.delete()
        return JsonResponse({'message': 'Trial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
