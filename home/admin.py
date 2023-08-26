from django.contrib import admin
from home.models import Contact,Enrollment,MembershipPlan,Trainer,Gallery,Attendance
# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)
