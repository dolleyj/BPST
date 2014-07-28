from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from suggestion.models import Filetype, Tool, StandaloneTool, ErgatisTool, GalaxyTool, ToolFiletype
from forms import UserQueryForm, FiletypeForm, ToolForm, ToolFiletypeForm
from django.core.context_processors import csrf

import json



# Create your views here.

#def hello(request):
#	name = "Dustin"
#	return render_to_response('hello.html'), {'name':name})

def biotools(request):
	return render_to_response('biotools.html', {'tools': Tool.objects.all()})


def biotool(request, tool_id=1):
	return render_to_response('biotool.html', {'tool': Tool.objects.get(id=tool_id), 'toolfileype': ToolFiletype.objects.get(id=tool_id)})

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
			#u_formatname = request.session['user_formatname']
			u_formatname = request.POST.getlist('user_formatname')			
			
			#u_formatname = form.cleaned_data[]
			request.session['u_formatname'] = u_formatname
			
			


			
			return HttpResponseRedirect('/biotools/suggestion', u_formatname)#, {'tools': tools})
	else:
		form = UserQueryForm()

	args = {}
	args.update(csrf(request))
		
	args['form'] = form

	return render_to_response('user_query.html', args)


def suggestion(request, init_input=(), tools=()): #will also take the output of build_pipeline?!
	#passes the user's initial file selection from user_query view into this view
	init_input = request.session['u_formatname']
	
	#Gathers the tool id's that are entered as 'input' and take the selected filetype as input
	toolfiletype_inputs_list = ToolFiletype.objects.filter(io_type = "i").filter(filetype_id__in = init_input).values_list('tool_id') 
	#Returns the name(s) of the tool(s) that would accept user's selected filetype
	tools = Tool.objects.filter(id__in=toolfiletype_inputs_list).values_list('name', flat=True).order_by('name')
		
	return render_to_response('suggestion.html', {'tools': tools})






