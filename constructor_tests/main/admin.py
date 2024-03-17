from django.contrib import admin

from .models import Tests, Questions, Choice, Result, Valuation, Categories # Quest, Rez, Cat

admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(Choice)
admin.site.register(Result)
admin.site.register(Valuation)
admin.site.register(Categories)
