from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

#from.signalsimportobject_viewed_signal
#from.utilsimportget_client_ip



#Createyourmodelshere.
POWER_CHOICES = (
    ('superuser','SUPERUSER'),
    ('admin', 'ADMIN'),
    ('content', 'CONTENT_MANAGER'),
    )
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address=models.CharField(max_length=200 )
    privilege=models.CharField(max_length=10,choices=POWER_CHOICES, default='Admin' )
    Country=models.CharField(max_length=200 )
    phonenumber=models.CharField(max_length=15 )

    def __int__(self):
        return self.id







COMPANY_CHOICES = (
    ('flintwood','FLINTWOOD'),
    ('biotech', 'BIOTECH'),
    ('bttitan','BTTITAN'),
    ('all','ALL'),
    ('none','NONE'),
)

USER_CHOICES = (
    ('buyer','BUYER'),
    ('Flintwood_supplier', 'FLINTWOOD SUPPLIER'),
    ('btsupplier', 'BTTITAN SUPPLIER'),
    ('biotec_supplier', 'BIOTEC SUPPLIER'),
)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address=models.CharField(max_length=200 )
    role=models.CharField(max_length=30 , choices=USER_CHOICES, default='buyer' )
    privilege=models.CharField(max_length=30 , choices=COMPANY_CHOICES, default='none' )
    Country=models.CharField(max_length=200 )
    phonenumber=models.CharField(max_length=15)
    Alternate_phonenumber=models.CharField(max_length=15, default='none')
    WeChat=models.CharField(max_length=15,  default='none')
    Skype=models.CharField(max_length=15,  default='none')
    
    Verified= models.BooleanField(default=False)
    

    def __int__(self):
        return self.id





class ClientSession(models.Model):
    Activeclient=models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address=models.CharField(max_length=220,blank=True,null=True)
    session_key=models.CharField(max_length=100,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    ended=models.BooleanField(default=False)

    def end_session(self):
        session_key=self.session_key
        ended=self.ended
        try:
            Session.objects.get(pk=session_key).delete()
            self.active=False
            self.ended=True
            self.save()
        except:
            pass
        return self.ended

#defpost_save_session_receiver(sender,instance,request,*args,**kwargs):
#ifcreated:
#ps=UserSession.objects.filter(user=instance.user).exclude(id=instance.id)
#foriinqs:
#i.end_session()

#post_save.connect(post_save_session_receiver,sender=UserSession)


