# myapp/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import PersonalInfo, Project

@register(PersonalInfo)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'bio', 'location', 'brand')

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'kind', 'propertys')

