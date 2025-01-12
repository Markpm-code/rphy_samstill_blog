from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at')
#     readonly_fields = ('image_preview',)

#     def image_preview(self, obj):
#         return f'<img src="{obj.image.url}" width="100">' if obj.image else 'No Image'
#     image_preview.allow_tags = True

# admin.site.register(Post, PostAdmin)
admin.site.register(Post)
admin.site.register(Comment)
