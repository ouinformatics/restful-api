from django.shortcuts import render
#from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly,AllowAny
from rest_framework.views import APIView
#from ccelery.q import QueueTask, list_tasks, task_docstring
#from models import Run_model
from rest_framework.renderers import JSONRenderer, JSONPRenderer
#from renderer import QueueRunBrowsableAPIRenderer
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser
#from util import trim
#from rest_framework.authtoken.models import Token
#from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator
#task = list_tasks()['available_tasks']
#from rest_framework.viewsets import ModelViewSet
#from serializer import FileUploadSerializer
import os
from dockertask import docker_task
rom subprocess import Popen, PIPE
class CheckMapFile(APIView):
    permission_classes = ( IsAuthenticatedOrReadOnly,)

    def __init__(self, *args, **kwargs):
        self.docker_cmd = "validate_mapping_file.py -m %s -o %s "
        self.docker_opts = "-v /data:/data"
        self.docker_container = "qiime_env"
        
        super(CheckMapFile, self).__init__(*args, **kwargs)

    def post(self, request,filename=None,format=None):
        if filename:
            p = Popen(['md5sum', filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate()
            resultDir = os.path.join("/data/tmp", output.split()[0])
            os.makedirs(resultDir)
        else:
            raise('Please provide map file filename')
        docker_cmd = self.docker_cmd % (filename,resultDir)
        result = docker_task(docker_name=self.docker_container,docker_opts=self.docker_opts,docker_command=docker_cmd,id=output.split()[0])
        return Response({
            'MapFile': filename,
            'resultDir': resultDir 
        })

# Create your views here.
"""
class FileUploadView(APIView):

    permission_classes =(AllowAny,)
    parser_classes = (MultiPartParser, FormParser,)
    #parser_classes = (FileUploadParser,)
    renderer_classes = (JSONRenderer,)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FileUploadView, self).dispatch(request, *args, **kwargs)

    def get_username(self, request):
        username = "guest"
        if request.user.is_authenticated():
            username = request.user.username
        return username

    def post(self, request, format=None):
    	resultDir = os.path.join("/data/tmp", self.get_username(request))
	try:
    	    os.makedirs(resultDir)
	except:
	    pass
	result={}
	for key,value in request.FILES.iteritems():
	    filename= value.name
	    local_file = "%s/%s" % (resultDir,filename)
	    self.handle_file_upload(request.FILES[key],local_file)
	    result[key]=local_file
	return Response(result)
    def handle_file_upload(self,f,filename):
	if f.multiple_chunks():
	    with open(filename, 'wb+') as temp_file:
                for chunk in f.chunks():
                    temp_file.write(chunk)
	else:
	    with open(filename, 'wb+') as temp_file:
	        temp_file.write(f.read())

"""
