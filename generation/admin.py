from django.contrib import admin
from generation.models import Generation, Student


class GenerationAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Generation, GenerationAdmin)
admin.site.register(Student, StudentAdmin)
