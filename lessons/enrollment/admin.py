from django.contrib import admin
from .models import Subject
from .models import Student

# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'quota', 'enrolled_students')
    search_fields = ('name',)
    fieldsets = (
        ('Info', {
            'fields': (
                ('name',),
                ('quota', ),
                ('enrolled_students',),
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created'),
                ('modified')
            ),
        }),
    )
    readonly_fields = ('enrolled_students', 'created', 'modified')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'subject')
    search_fields = ('first_name', 'last_name', 'email', 'subject__name')
    fieldsets = (
        ('Info', {
            'fields': (
                ('first_name',),
                ('last_name', ),
                ('email',),
                ('phone_number',),
                ('subject',),
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created'),
                ('modified')
            ),
        }),
    )
    readonly_fields = ('created', 'modified')
