from django.contrib import admin
from .models import BlogPost,  Comment, Image
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else 'No Image'

    image_preview.short_description = 'Image Preview'


admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Image, ImageAdmin)
# Register your models here.
