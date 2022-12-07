from myApp.serializer import UserInfoSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myApp.models import UserInfoModel
from myApp.utils  import covert_json_to_python_data


@csrf_exempt
def post_user_info(request):
    """ Based on User (client) request, validate and create record in DB
    and sends acknowledgment to user
    """
    if request.method == 'POST':
        serialized_data = UserInfoSerializer(data=covert_json_to_python_data(request))
        if serialized_data.is_valid():
            serialized_data.save()
            response_to_client = {'response': 'Data Saved in DB'}
            json_response = JSONRenderer().render(response_to_client)
            return HttpResponse(json_response, content_type='application/json')
        json_error_response = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_error_response, content_type='application/json')


def get_user_info(request):
    """ Based on request from user send requested data through
    HTTPResponse
    """
    if request.method == 'GET':
        received_id = covert_json_to_python_data(request).get('id', None)
        if received_id is not None:
            user_info = UserInfoModel.objects.get(id=received_id)
            deserialized_data = UserInfoSerializer(user_info)
            json_response_data = JSONRenderer().render(deserialized_data)
            return HttpResponse(json_response_data, content_type='application/json')
        all_user_info = UserInfoModel.objects.all()
        print(f"Object received from DB {all_user_info}")
        all_deserialized_data = UserInfoSerializer(all_user_info, many=True)
        json_response = JSONRenderer().render(all_deserialized_data.data)
        return HttpResponse(json_response, content_type='application/json')


@csrf_exempt
def partial_update_user_info(request):
    """ Take update response from user, update in db and sends
    acknowledgement to user
    """
    if request.method == 'PUT':
        received_update_id = covert_json_to_python_data(request).get('id', None)
        print(f'Received ID from client {received_update_id}')
        if received_update_id is not None:
            user_info = UserInfoModel.objects.get(id=received_update_id)
            serialized_data = UserInfoSerializer(user_info, data=covert_json_to_python_data(request), partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                response_to_client = {'response': 'User info updated'}
                json_response_data = JSONRenderer().render(response_to_client)
                return HttpResponse(json_response_data, content_type='application/json')
            error_response_to_client = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(error_response_to_client, content_type='application/json')


@csrf_exempt
def delete_user_info(request):
    """ Based delete request from user, deletes the record from Db and
    sends acknowledgment
    """
    if request.method == 'DELETE':
        received_delete_id = covert_json_to_python_data(request).get('id', None)
        if received_delete_id is not None:
            user_info = UserInfoModel.objects.get(id=received_delete_id)
            user_info.delete()
            response_to_client = {'response': 'User info deleted'}
            json_response_data = JSONRenderer().render(response_to_client)
            return HttpResponse(json_response_data, content_type='application/json')

