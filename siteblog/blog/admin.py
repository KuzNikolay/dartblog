from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True  # в админке позволяет добавлять посты на основе предыдущих, кнопка сохранить
    # как новый пост
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'author', 'get_photo', 'views')  #
    # Поля в просмотре статей
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tags',)
    readonly_fields = ('created_at', 'views', 'get_photo')  # Поля в редакторе поста только для
    # просмотра
    fields = ('title', 'slug', 'category', 'tags', 'content', 'author', 'photo', 'get_photo',
              'views', 'created_at',)  # Поля в редакторе поста

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
