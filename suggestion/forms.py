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

	toolfiletype = ToolFiletype.objects.filter(io_type = "i").values_list('filetype_id')
	user_formatname = forms.ModelChoiceField(label= "Select file type", queryset=Filetype.objects.filter(id__in=toolfiletype), empty_label=None)
	

#user_format = forms.ModelChoiceField(label='Choose a file format', queryset=Filetype.objects.values_list('format', flat=True).distinct(), empty_label=None)
	#user_variant = forms.ModelChoiceField(label="Let's be more specific...", queryset=Filetype.objects.values_list('variant', flat=True).distinct(), empty_label=None)
	#commented out because its repetitive of the 1st two
	#user_formatname = forms.ModelChoiceField(label='Most Specific...', queryset=ToolFiletype.objects.values_list('filetype', flat=True).filter(io_type = "i").distinct(), empty_label=None)

# ATTEMPT TO DYNAMICALLY FILTER 'variants' based on 'format' selection
# https://docs.djangoproject.com/en/dev/ref/models/querysets/#id4
	#user_formatvariant = forms.ModelChoiceField(label="Let's be more specific...", queryset=Filetype.objects.filter(format=user_fileformat).values_list('variant', flat=True), empty_label=None)


	
