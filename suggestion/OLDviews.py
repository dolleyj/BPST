from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from suggestion.models import Biotool, Datatype, Filetype, ToolFiletype
from forms import BiotoolForm, DatatypeForm, FiletypeForm, ToolFiletypeForm
from forms import UserdatafileForm
from django.core.context_processors import csrf

# Create your views here.

#def hello(request):
#	name = "Dustin"
#	return render_to_response('hello.html'), {'name':name})

def biotools(request):
	return render_to_response('biotools.html', {'biotools': Biotool.objects.all()})


def biotool(request, biotool_id=1):
	return render_to_response('biotool.html', {'biotool': Biotool.objects.get(id=biotool_id)})

def add_biotool(request):
	if request.POST:
	   form = BiotoolForm(request.POST, request.FILES)
	   if form.is_valid():
		form.save()

		return HttpResponseRedirect('/biotools/all')
	else:
	   form = BiotoolForm()

	args = {}
	args.update(csrf(request))
	
	args['form'] = form

	return render_to_response('add_biotool.html', args)

def upload_user_data(request):
	if request.POST:
		form = UserdatafileForm(request.POST)
		if form.is_valid():
			form.save()
			#file_format_type(request.POST['user_datatype', 'user_datasubtype', 'user_fileformat'])
			#build_pipeline(...., Biotool)
			return HttpResponseRedirect('/biotools/suggestion')
	else:
		form = UserdatafileForm()

	args = {}
	args.update(csrf(request))
		
	args['form'] = form

	return render_to_response('upload_user_data.html', {'form': form})

#def file_format_type(user_datatype, user_datasubtype, user_fileformat):
'''
Taking the user's input, determine the file format AND data type. 
'''

#def build_pipeline(args from file_format_type, Biotool):
'''
Take results (file format & data type from Function 'file_format_type') and biotool database. Based upon the results find the biotools compatiable.
''' 

def suggestion(request):
	return render_to_response('suggestion.html')






