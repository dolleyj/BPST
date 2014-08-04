from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from suggestion.models import Filetype, Tool, StandaloneTool, ErgatisTool, GalaxyTool, ToolFiletype
from forms import UserQueryForm, FiletypeForm, ToolForm, ToolFiletypeForm
from django.core.context_processors import csrf


# Create your views here.

def biotools(request):
	#diplays tools loaded into the database
	return render_to_response('biotools.html', {'tools': Tool.objects.order_by('name')})


def biotool(request, tool_id=1):
	#displays the attributes of the selected tool
	toolfiletype = ToolFiletype.objects.filter(tool_id__in=tool_id)
	return render_to_response('biotool.html', {'tool': Tool.objects.get(id=tool_id), 'toolfileype': toolfiletype})


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
	#collects the user's query and stores it for use in 'suggestion' view
	if request.POST:
		form = UserQueryForm(request.POST)
		if form.is_valid():
			u_formatname = request.POST.getlist('user_formatname')			
			request.session['u_formatname'] = u_formatname
			
			return HttpResponseRedirect('/biotools/suggestion', u_formatname)
	else:
		form = UserQueryForm()

	args = {}
	args.update(csrf(request))
		
	args['form'] = form

	return render_to_response('user_query.html', args)


def suggestion(request, init_input=(), tools=()):
	#passes the user's initial file selection from user_query view into this view
	init_input = request.session['u_formatname']
	user_input = Filetype.objects.filter(id__in=init_input).values_list('name', flat=True)
	
	#Gathers the tool id's that are entered as 'input' and ONLY take the selected filetype as input
	toolfiletype_inputs_list = ToolFiletype.objects.filter(io_type = "i", required=False).filter(filetype_id__in = init_input).values_list('tool_id')

	#Returns the name(s) of the tool(s) that only need selected filetype to run
	tools = Tool.objects.filter(id__in=toolfiletype_inputs_list).values_list('name', flat=True).order_by('name')

	#Find additional possible filetypes could added to suggestion 
	add_tools = ToolFiletype.objects.filter(io_type="i", required=True).filter(filetype_id__in = init_input).values_list('tool_id')
	add_tool_names = Tool.objects.filter(id__in=add_tools).values_list('name', flat=True)

	#Gathers entries that require filetypes in addition to the selected filetype 
	toolfiletype_entries = ToolFiletype.objects.filter(io_type="i", required=True).exclude(filetype_id__in= init_input)

	return render_to_response('suggestion.html', {'user_input': user_input, 'tools': tools, 'add_tool_names': add_tool_names, 'toolfiletype_entries': toolfiletype_entries})






