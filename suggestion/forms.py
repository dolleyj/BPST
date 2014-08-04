from django import forms
from models import Filetype, Tool, StandaloneTool, ErgatisTool, GalaxyTool, ToolFiletype




class FiletypeForm(forms.ModelForm):
	class Meta:
		model = Filetype
		fields = ('name', 'format', 'variant', 'spec_url')

class ToolForm(forms.ModelForm):
	class Meta:
		model = Tool
		fields = ('name', 'version', 'primary_site', 'publication', 'files' )

class ToolFiletypeForm(forms.ModelForm):
	class Meta:
		model = ToolFiletype
		fields = ('tool', 'description', 'filetype', 'required', 'io_type')



class UserQueryForm(forms.Form):
	'''Form for collecting user's input'''

	#displays filetypes that are INPUT for a tool(s)
	toolfiletype = ToolFiletype.objects.filter(io_type = "i").values_list('filetype_id')
	user_formatname = forms.ModelChoiceField(label= "Select file type", queryset=Filetype.objects.filter(id__in=toolfiletype), empty_label=None)
		
