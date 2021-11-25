from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from .models import Category


@admin.register(Category)
class CategoryDraggableMPTTAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'move_element')
    list_display_links = ('move_element',)

    def move_element(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,
        )

    move_element.short_description = 'move element'
    