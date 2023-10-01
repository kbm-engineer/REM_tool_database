from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from production.models import BaseMonitoringObject
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
import subprocess
import os


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def test_html(request):
    productions = BaseMonitoringObject.objects.all()
    context = {
            'productions': productions,
        }
    return render(request, 'production/test_html.html', context)
