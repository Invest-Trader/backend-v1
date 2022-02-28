from django.db import models
import uuid
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.auth.models import User
from model_utils import Choices
from model_utils.fields import StatusField
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
# Create your models here.



class UserAll(models.Model):
    id = models.CharField(max_length=6, primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=15)
    name = models.CharField(max_length=15,default='')
    email = models.EmailField(max_length=100)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    day = models.CharField(blank=True,null=True,default='',max_length=3)
    month = models.CharField(blank=True,null=True,default='',max_length=3)
    year = models.CharField(blank=True,null=True,default='',max_length=5)
    STATUS = ((0,'NOT_PROVIDED'),(1,'MALE'),(2, 'FEMALE'),(3, 'OTHER'))
    gender = models.PositiveSmallIntegerField(choices=STATUS,blank=True,null=True,default=0)
    create_datetime = models.DateTimeField(auto_now_add=True)
    STATUS_ACCOUNT_VERIFICATION = ((0,'VERIFIED'),(1,'NOT VERIFIED'),(2, 'IN PROCESS'),(3, 'BLOCKED'))
    account_verfication = models.PositiveSmallIntegerField(choices=STATUS_ACCOUNT_VERIFICATION,blank=True,null=True,default=1)
    STATUS_EMAIL_VERIFICATION = ((0,'VERIFIED'),(1,'NOT VERIFIED'))
    email_verfication = models.PositiveSmallIntegerField(choices=STATUS_EMAIL_VERIFICATION,blank=True,null=True,default=1)
    def __str__(self):
        return str(self.user.username) + " " + self.name

class UserMetaData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(UserAll, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20,blank=True,null=True)
    mac_address = models.CharField(max_length=50,blank=True,null=True)
    os = models.CharField(max_length=50,blank=True,null=True)
    device = models.CharField(max_length=50,blank=True,null=True)

class UserDocument(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(UserAll, on_delete=models.CASCADE)
    pancard_image = models.ImageField(upload_to='images/pancard/', blank=True)
    pancard_number = models.CharField(max_length=11,blank=True,null=True)
    STATUS_DOCUMENTS = ((0,'AADHAR CARD'),(1,'PASSPORT'),(2,'DRIVING LICENSE'),(3,'OTHER'))
    additional_documents = models.PositiveSmallIntegerField(choices=STATUS_DOCUMENTS,blank=True,null=True,default=0)
    additional_documents_number = models.CharField(max_length=18,blank=True,null=True)
    additional_documents_image = models.ImageField(upload_to='images/documents/', blank=True)


class UserAccountFund(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(UserAll, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True,null=True)

class OrderTransactions(model.Model):
    user = models.ForeignKey(UserAll, on_delete=models.CASCADE)
    transaction_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    TRANSACTION_DOCUMENTS = ((0,'CRYPTO'),(1,'STOCK'),(2,'INDICES'),(3,'OTHER'))
    transaction_order =  models.PositiveSmallIntegerField(choices=TRANSACTION_DOCUMENTS,blank=True,null=True)
    transaction_order_quantity = model.FloatField()
    transaction_order_price = model.FloatField()
    TRANSACTION_ACTION = ((0,'BUY'),(1,'SELL'))
    transaction_order_action = models.PositiveSmallIntegerField(choices=TRANSACTION_ACTION,blank=True,null=True)
    TRANSACTION_TYPE = ((0,'LIMIT'),(1,'INSTANT BUY'),(2,'INSTANT SELL'),(3,'OTHER'))
    transaction_order_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE,blank=True,null=True)
    transaction_total_amount = model.FloatField()
    transaction_timestamp = model.DateTimeField(auto_now_add=True)
    transaction_status = models.BooleanField()
    transaction_is_wallet_type = models.BooleanField()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )







