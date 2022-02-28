from django.contrib import admin
from .models import UserAll,UserMetaData,UserDocument,UserAccountFund
# Register your models here.
class UserAllDisplay(admin.ModelAdmin):
  list_display = ('id','fname','lname','phoneno','account_verfication','email_verfication','create_datetime')

class UserMetaDataDisplay(admin.ModelAdmin):
  list_display = ('id','user','ip','mac_address','os','device')

class UserDocumentDisplay(admin.ModelAdmin):
  list_display = ('id','user','pancard_image','pancard_number','additional_documents','additional_documents_number','additional_documents_image')

class UserAccountFundDisplay(admin.ModelAdmin):
  list_display = ('id','user','amount')

admin.site.register(UserAll, UserAllDisplay)
admin.site.register(UserMetaData, UserMetaDataDisplay)
admin.site.register(UserDocument, UserDocumentDisplay)
admin.site.register(UserAccountFund, UserAccountFundDisplay)