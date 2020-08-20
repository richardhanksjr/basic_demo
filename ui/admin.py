# from django.contrib import admin
# from ui.models import Post
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
#
#
# class PostsInline(admin.StackedInline):
#     model = Post
#
#
# class UserAdmin(AuthUserAdmin):
#     inlines = [PostsInline]
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
#
# admin.site.register(Post)