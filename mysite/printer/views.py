from django.shortcuts import render
import json
import subprocess
import base64
# Create your views here.
from django.http import HttpResponse

def runCmd(request):
    # Load File
    req_str = request.body.decode("utf-8")
    req_json = json.loads(req_str)
    req_file_byte = base64.b64decode(req_json["fileToPrint"])

    # Write File
    open('fileToPrint.txt', 'wb').write(req_file_byte)
    
    # Print File
    process = subprocess.run(['lp', 'fileToPrint.txt'], stdout=subprocess.PIPE, universal_newlines=True)
    # print(process.stdout)

    # Send Successful Response
    return HttpResponse('File sent to printer!')

def index(request):
    # return HttpResponse("Hit printer index")
    if(request.path == '/printer/print' and request.method == 'POST'):
        return runCmd(request)
    else:
        return HttpResponse('Humble pie')

    