from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import PersonalInfo, Skills, Project, SocialLink, ContactMessage

def home(request):
    profile = PersonalInfo.objects.first()
    skills = Skills.objects.all()
    projects = Project.objects.prefetch_related('tech', 'images').all()
    social = SocialLink.objects.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'socials': social,
    }

    
    return render(request, 'prof/index.html', context)


def get_project_details(request, pk):
    try:
        project = Project.objects.get(id=pk)
        tech_list = [t.name for t in project.tech.all()]
        images_list = [img.image.url for img in project.images.all()]
        features_list = project.propertys.split('-') if project.propertys else []

        data = {
            'success': True,
            'title': project.title,
            'subtitle': project.kind, 
            'description': project.description,
            'tech': tech_list,
            'features': features_list,
            'github': project.github,
            'live': project.live,
            'images': images_list
        }
        return JsonResponse(data)
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Project not found'}, status=404)
    


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message')
        
        if not name or not email or not message:
            messages.error(request, 'يرجى ملء جميع الحقول المطلوبة.')
            return redirect('prof:home')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(
            request, 
            'تم إرسال رسالتك بنجاح! سأقوم بالرد عليك في أقرب وقت ممكن.'
        )
        
        return redirect('prof:home')
    
    return redirect('prof:home')
