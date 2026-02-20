from django.contrib import admin
from .models import PersonalInfo, Skills, Project, ContactMessage, ProjectImage, SocialLink
from modeltranslation.admin import TranslationAdmin
from import_export.admin import ImportExportModelAdmin


class ProfileAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'email']
    group_fieldsets = True 

class ProjectAdmin(TranslationAdmin):
    list_display = ['title', 'description']
    filter_horizontal = ['tech']
    group_fieldsets = True




@admin.register(PersonalInfo)
class PersonalInfoImportExport(ImportExportModelAdmin):
    pass




@admin.register(Skills)
class SkillsImportExport(ImportExportModelAdmin):
    pass



@admin.register(Project)
class ProjectImportExport(ImportExportModelAdmin):
    pass




@admin.register(ProjectImage)
class ProjectImageImportExport(ImportExportModelAdmin):
    pass




@admin.register(SocialLink)
class SocialLinkImportExport(ImportExportModelAdmin):
    pass





admin.site.register(ContactMessage)