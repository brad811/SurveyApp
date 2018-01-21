from django.contrib import admin

from .models import Question, QuestionChoice, QuestionGuestResponse

class QuestionChoiceInline(admin.StackedInline):
  model = QuestionChoice
  extra = 2

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['text']}),
  ]
  inlines = [QuestionChoiceInline]

admin.site.register(Question, QuestionAdmin)

from .models import QuestionChoice
admin.site.register(QuestionChoice)

from .models import QuestionGuestResponse
admin.site.register(QuestionGuestResponse)
