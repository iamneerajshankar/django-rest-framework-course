import io
from rest_framework.parsers import JSONParser


def covert_json_to_python_data(request):
    json_data_from_client = request.body
    stream_data = io.BytesIO(json_data_from_client)
    parsed_python_data = JSONParser().parse(stream_data)
    return parsed_python_data
