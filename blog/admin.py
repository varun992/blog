from django.contrib import admin

from .models import Blog, Comment


# Register your models here.

class CommentInLine(admin.TabularInline):
	model = Comment
	extra = 0


class BlogAdmin(admin.ModelAdmin):
	inlines = [
		CommentInLine,
	]


admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
