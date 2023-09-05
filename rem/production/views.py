from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from production.models import BaseMonitoringObject
from django.shortcuts import render, get_object_or_404


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def my_html_view(request):
    productions = BaseMonitoringObject.objects.all()
    #data = {"message": "Hello, World!"}
    #return Response(data, template_name='production/my_template.html')


    context = {
            'productions': productions,
        }
    return render(request, 'production/my_template.html', context)