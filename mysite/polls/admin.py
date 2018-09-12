from django.contrib import admin

# Register your models here.
# add 20180821 m_miyamoto
#from .models import Question
# chg 20180823 m_miyamoto
from .models import Choice, Question

# add 20180823 m_miyamoto
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# add 20180823 m_miyamoto
class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
# chg 20180823 m_miyamoto
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # add 20180823 m_miyamoto
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

#admin.site.register(Question)
# chg 20180823 m_miyamoto
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
