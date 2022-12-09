from myApp.serializers import MoviesLibrarySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myApp.models import MoviesLibraryModel
from myApp.utils  import covert_json_to_python_data


@csrf_exempt
def post_movie_details(request):
    """ Based on User (client) request, validate and create record in DB
    and sends acknowledgment to user
    """
    if request.method == 'POST':
        queryset = MoviesLibraryModel.objects.values('name')
        list_queryset = list(queryset)
        for movie_name in list_queryset:
            if covert_json_to_python_data(request)['name'] == movie_name['name']:
                response_to_client = {'response': 'The Movie Detail Already Exists'}
                return JsonResponse(response_to_client, safe=True)

        serialized_data = MoviesLibrarySerializer(data=covert_json_to_python_data(request))
        if serialized_data.is_valid():
            serialized_data.save()
            response_to_client = {'response': 'Data Saved in DB'}
            return JsonResponse(response_to_client, safe=True)
        return JsonResponse(serialized_data.errors, safe=False)


def get_movie_details(request):
    """ Based on request from user send requested data through
    HTTPResponse
    """
    if request.method == 'GET':
        received_id = covert_json_to_python_data(request).get('id', None)
        if received_id is not None:
            movie_details = MoviesLibraryModel.objects.get(id=received_id)
            deserialized_data = MoviesLibrarySerializer(movie_details)
            # json_response_data = JSONRenderer().render(deserialized_data.data)
            return JsonResponse(deserialized_data, safe=False)
        all_movie_details = MoviesLibraryModel.objects.all()
        all_deserialized_data = MoviesLibrarySerializer(all_movie_details, many=True)
        json_response = JSONRenderer().render(all_deserialized_data.data)
        return HttpResponse(json_response, content_type='application/json')


@csrf_exempt
def partial_update_movie_details(request):
    """ Take update response from user, update in db and sends
    acknowledgement to user
    """
    if request.method == 'PUT':
        received_update_id = covert_json_to_python_data(request).get('id', None)
        if received_update_id is not None:
            movie_details = MoviesLibraryModel.objects.get(id=received_update_id)
            serialized_data = MoviesLibrarySerializer(movie_details, data=covert_json_to_python_data(request), partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                response_to_client = {'response': 'User info updated'}
                json_response_data = JSONRenderer().render(response_to_client)
                return HttpResponse(json_response_data, content_type='application/json')
            error_response_to_client = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(error_response_to_client, content_type='application/json')


@csrf_exempt
def delete_movie_details(request):
    """ Based delete request from user, deletes the record from Db and
    sends acknowledgment
    """
    if request.method == 'DELETE':
        received_delete_id = covert_json_to_python_data(request).get('id', None)
        if received_delete_id is not None:
            movie_details = MoviesLibraryModel.objects.get(id=received_delete_id)
            movie_details.delete()
            response_to_client = {'response': 'Movie Details deleted'}
            json_response_data = JSONRenderer().render(response_to_client)
            return HttpResponse(json_response_data, content_type='application/json')

