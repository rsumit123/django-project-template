from django.http import HttpResponse
from rest_framework.decorators import api_view
from .settings import BASE_DIR
from rest_framework.response import Response
import json
import os
import logging

logger = logging.getLogger('ai_health_backend')



def view_logs(request):
    # Default number of lines to display
    default_lines_to_display = 50

    # Check for a "lines" query parameter and use its value, or default to 50
    lines_to_display = int(request.GET.get('lines', default_lines_to_display))

    # Check for a "full" query parameter
    show_full_log = request.GET.get('full', 'false').lower() == 'true'

    with open('ai_health_logging.log', 'r') as log_file:
        if show_full_log:
            log_content = log_file.read()
        else:
            # Read the last 'lines_to_display' lines from the log file
            log_content = ''.join(log_file.readlines()[-lines_to_display:])

    return HttpResponse(log_content, content_type="text/plain")


@api_view(["GET"])

def get_json_schema(request):
    """Serve the docs json file, to display it in the swagger editor"""
    file_path = os.path.join(BASE_DIR, "docs/openapi-schema/api-schema.json")

    try:
        with open(file_path) as file:
            json_data = json.load(file)
            return Response(json_data, status=200)
    except FileNotFoundError:
        return Response({"error": "File not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)