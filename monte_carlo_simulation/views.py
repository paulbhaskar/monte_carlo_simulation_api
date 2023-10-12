# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response

from monte_carlo_simulation.models import Trial
from monte_carlo_simulation.serializers import TrialSerializer


@api_view(['GET', 'POST', 'DELETE'])
def trial_list(request):
    # GET list of trials, POST a new trial DELETE all trials
    if not (request.GET.get('page') and request.GET.get('page_size')):
        return JsonResponse({"message": "Please pass the following query params: page, page_size"})
    elif request.method == 'GET':
        page = int(request.GET['page'])
        page_size = int(request.GET['page_size'])
        offset = (page - 1) * page_size
        trials = Trial.objects.skip(offset).limit(page_size)
        return Response(json.loads(trials.to_json()))
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
        return Response(json.loads(trial.to_json()))
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
