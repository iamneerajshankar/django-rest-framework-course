import io
from rest_framework.parsers import JSONParser


def covert_json_to_python_data(request):
    json_data_from_client = request.body
    print(f"Raw Data from client {json_data_from_client}")
    stream_data = io.BytesIO(json_data_from_client)
    parsed_python_data = JSONParser().parse(stream_data)
    print(f"Parsed python data from client {parsed_python_data}")
    return parsed_python_data
