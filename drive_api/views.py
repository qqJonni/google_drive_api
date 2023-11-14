from django.shortcuts import render

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def create_and_upload_file(file_name='name.txt', file_content='data'):

    try:
        drive = GoogleDrive(gauth)

        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(file_content)
        my_file.Upload()

        return f'File {file_name} was uploaded!'
    except Exception as ex:
        return 'Got some trouble. Check your code please'


def index(request):
    file_name = request.POST.get('file_name')
    file_content = request.POST.get('file_content')

    result = create_and_upload_file(file_name=file_name, file_content=file_content)
    context = {'upload_result': result}

    return render(request, 'index.html', context)
