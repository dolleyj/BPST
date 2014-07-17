from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from suggestion.models import Filetype, Tool, StandaloneTool, ErgatisTool, GalaxyTool, ToolFiletype
from forms import UserQueryForm, FiletypeForm, ToolForm, ToolFiletypeForm
from django.core.context_processors import csrf



# Create your views here.

#def hello(request):
#	name = "Dustin"
#	return render_to_response('hello.html'), {'name':name})

def biotools(request):
	return render_to_response('biotools.html', {'biotools': Tool.objects.all()})


def biotool(request, biotool_id=1):
	return render_to_response('biotool.html', {'biotool': Tool.objects.get(id=id)})

def add_biotool(request):
	if request.POST:
	   form = ToolForm(request.POST, request.FILES)
	   if form.is_valid():
		form.save()

		return HttpResponseRedirect('/biotools/all')
	else:
	   form = ToolForm()

	args = {}
	args.update(csrf(request))
	
	args['form'] = form

	return render_to_response('add_biotool.html', args)

def user_query(request):
	if request.POST:
		form = UserQueryForm(request.POST)
		if form.is_valid():
			# helped out a lot: https://docs.djangoproject.com/en/dev/topics/forms/#field-data
			user_format = form.cleaned_data['user_format']
			user_formatvariant = form.cleaned_data['user_formatvariant']
			
			#file_format_type(request.POST['user_format', 'user_formatvariant', 'user_formatname'])
			#build_pipeline(...., Tool)
			return HttpResponseRedirect('/biotools/suggestion')
	else:
		form = UserQueryForm()

	args = {}
	args.update(csrf(request))
		
	args['form'] = form

	return render_to_response('user_query.html', {'form': form})

#def file_format_type(request?!, user_format, user_fileformat):
'''
Taking the user's input, determine the file format AND data type. 
'''

def build_pipeline(args from file_format_type, Tool):
'''
Take user's input from 'user_query' and find the 1st compatiable tool. Then using that tool's output as NEW
"user input" find the next tool and store it with the 1st. Repeat until done?!
''' 

def suggestion(request): #will also take the output of build_pipeline?!
	return render_to_response('suggestion.html')






