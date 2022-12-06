from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from myApp.serializer import UserInfoSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myApp.models import UserInfoModel


"""" View to perform create operation """
@csrf_exempt
def post_user_info(request):
    if request.method == 'POST':
        json_data_from_client = request.body
        stream_data = io.BytesIO(json_data_from_client)
        parsed_python_data = JSONParser().parse(stream_data)
        serialized_data = UserInfoSerializer(data=parsed_python_data)
        if serialized_data.is_valid():
            serialized_data.save()
            response_to_client = {'response': 'Data Saved in DB'}
            json_response = JSONRenderer().render(response_to_client)
            return HttpResponse(json_response, content_type='application/json')
        json_error_response = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_error_response, content_type='application/json')


def get_user_info(request):
    if request.method == 'GET':
        json_data_from_client = request.body
        stream_data = io.BytesIO(json_data_from_client)
        parsed_python_data = JSONParser().parse(stream_data)
        received_id = parsed_python_data.get('id', None)
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


