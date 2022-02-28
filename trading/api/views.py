import random
import string
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from .serializer import ChangePasswordSerializer
from rest_framework import generics, permissions, mixins
from rest_framework.decorators import api_view, action, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from .models import UserAll,UserMetaData,UserDocument,UserAccountFund
from trading.settings import EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST_PASSWORD, EMAIL_HOST

# Create your views here.
def id_generator_user(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    key_generated = ''.join(random.choice(chars) for _ in range(size))

    do_exist = UserAll.objects.filter(id=key_generated).count()
    if do_exist > 0:
        key_generated = id_generator_user()

    return key_generated


class HelloView(APIView):

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)




@permission_classes([AllowAny])
@api_view(('POST',))
def register_user(request):
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    fname = request.POST.get('fname','')
    lname = request.POST.get('lname','')
    phoneno = request.POST.get('phoneno','')
    name = fname + ' ' +lname
    if User.objects.filter(username=email):
        return Response({"status": "Already Exists"})
    else:
        id = id_generator_user()
        user = User.objects.create_user(username=email, password=password,email=email,first_name=fname,last_name=lname)
        userall = UserAll.objects.create(id=id,user=user, phoneno=phoneno,fname=fname, lname=lname,email=email,name=name)

    response = {'status':'success'}
    return Response(response, status=status.HTTP_200_OK)  


@api_view(('POST',))
def delete_user(request):
    email = request.POST.get('email','')
    user = User.objects.filter(username=email).delete()
    response = {'status':'success'}
    return Response(response, status=status.HTTP_200_OK) 


@api_view(('POST',))
def upload_documents(request):
    user_id = request.POST.get('user_id','')
    pancard_image = request.FILES.get('pancard_image','')
    pancard_number = request.POST.get('pancard_number','')
    additional_documents = request.POST.get('additional_documents','')
    additional_documents_number = request.POST.get('additional_documents_number','')
    additional_documents_image = request.FILES.get('additional_documents_image','')
    userdocument = UserDocument.objects.create(user=UserAll.objects.get(id=user_id), pancard_image=pancard_image,pancard_number=pancard_number,additional_documents=additional_documents,additional_documents_number=additional_documents_number,additional_documents_image=additional_documents_image)
    response = {'status':'success'}
    return Response(response, status=status.HTTP_200_OK) 



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            msg = MIMEMultipart()
            msg['From'] = EMAIL_HOST_USER
            msg['To'] = EMAIL_HOST_USER
            msg['Subject'] = f'Personal site: {form_data["subject"]}'
            message = f'Name: {form_data["name"]}\n' \
                        f'Email address: {form_data["email_address"]}\n\n' \
                        f'{form_data["message"]}'
            msg.attach(MIMEText(message))
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.ehlo()
                server.starttls()
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                server.sendmail(EMAIL_HOST_USER, EMAIL_HOST_USER, msg.as_string())
            return HttpResponseRedirect('/thanks')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})




    
