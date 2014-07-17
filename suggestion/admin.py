from django.contrib import admin

from suggestion.models import Filetype, Tool, StandaloneTool, ErgatisTool, GalaxyTool, ToolFiletype

# Register your models here.

admin.site.register(Filetype)
admin.site.register(Tool)
admin.site.register(StandaloneTool)
admin.site.register(ErgatisTool)
admin.site.register(GalaxyTool)
admin.site.register(ToolFiletype)
