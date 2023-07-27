from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def my_html_view(request):
    data = {"message": "Hello, World!"}
    return Response(data, template_name='tool/my_template.html')