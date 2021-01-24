from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import csv
#import pandas as pd
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Gopi'})

def datatable(request,file):
    #file = name
    csv_fp = open(f'csv_upload_files/{file}', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'result.html', {'data' : out, 'headers' : headers})

def upload(request):
    if request.method == 'POST':
        uploaded_file =request.FILES['csv_file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        name = uploaded_file.name
        if name:
            extension = name.split('.')[-1]
            if extension != 'csv':
                raise ValidationError("File type not supported")
        
        #df = pd.read_csv("csv_upload_files/"+name)
        #filters = 
        print(name)
        datatable(request,name)
    return render(request,'upload.html')

