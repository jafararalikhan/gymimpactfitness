from django.contrib import admin
from home.models import Contact,Enrollment,MembershipPlan,Trainer
# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)