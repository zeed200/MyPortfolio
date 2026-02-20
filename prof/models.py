from django.db import models

class PersonalInfo(models.Model):
    brand = models.CharField(max_length=3, null=True, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150) 
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=150)
    cv = models.FileField(upload_to='cv/', blank=True)

    class Meta:
        verbose_name = "البيانات الشخصية"
        verbose_name_plural = "البيانات الشخصية"

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=70, null=True, blank=True)
    image = models.ImageField(upload_to='project/tech/', null=True, blank=True) 

    class Meta:
        verbose_name = "مهارة"
        verbose_name_plural = "المهارات"

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    propertys = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='projects/main')
    live = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    tech = models.ManyToManyField(Skills, related_name='projects')
    created_at = models.DateField()

    class Meta:
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"

    def __str__(self):
        return self.title    

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/gallery/') 

    class Meta:
        verbose_name = "صور المشاريع"
        verbose_name_plural = "صور المشروع"

    def __str__(self):
        return f'{self.project.title} - {self.image.name}'

class Experience(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)          
    end_date = models.DateField(blank=True, null=True) 

    class Meta:
        verbose_name = "الخبرات"
        verbose_name_plural = "الخبرة"

    def __str__(self):
        return self.company

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(
        max_length=50,
        help_text="مثال: fa-github"
    )

    class Meta:
        verbose_name = "وسيلة الأتصال"
        verbose_name_plural = "وسائل التواصل"

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "الرسالة" 
        verbose_name_plural = "الرسائل"
        ordering = ['-created_at']

    def __str__(self):
        return self.email
