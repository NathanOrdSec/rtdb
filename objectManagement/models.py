from django.db import models
from authentication.models import Users
from .storage_backends import *
# Create your models here.


class Status(models.Model):
    class Meta:
        permissions = (("can_mark_approved", "Set Approval Status"),)
    lastUpdated=models.DateTimeField(blank=True,auto_now=True)
    active=models.BooleanField(default=True)
    approved=models.BooleanField(default=False)
    banned=models.BooleanField(default=False)
    creator=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,related_name="user_creator", verbose_name='Creator')
    editor=models.ForeignKey(Users,on_delete=models.SET_NULL,null=True,related_name="user_editor", verbose_name='Editor')

class Socials(models.Model):
    sID=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='SID')
    twitter=models.URLField(max_length=255,blank=True,null=True,verbose_name="Twitter",default="")
    instagram=models.URLField(max_length=255,blank=True,null=True,verbose_name="Instagram",default="")
    youtube=models.URLField(max_length=255,blank=True,null=True,verbose_name="YouTube",default="")
    twitch=models.URLField(max_length=255,blank=True,null=True,verbose_name="Twitch",default="")
    reddit=models.URLField(max_length=255,blank=True,null=True,verbose_name="Reddit",default="")
    tiktok=models.URLField(max_length=255,blank=True,null=True,verbose_name="TikTok",default="")
    threads=models.URLField(max_length=255,blank=True,null=True,verbose_name="Threads",default="")
    spotify=models.URLField(max_length=255,blank=True,null=True,verbose_name="Spotify",default="")
    apple=models.URLField(max_length=255,blank=True,null=True,verbose_name="Apple Podcasts",default="")
    website=models.URLField(max_length=255,blank=True,null=True,verbose_name="Website",default="")
    email=models.EmailField(max_length=255,blank=True,null=True,verbose_name="Email",default="")
    other=models.CharField(max_length=255,blank=True,null=True,verbose_name="Other",default="")
    image=models.ImageField(upload_to="images/%Y/%m/%d/",null=True,storage=PublicMediaStorage(),max_length=255)
    
    @property
    def getLinks(self):
        return {"Twitter":self.twitter,
                "Instagram":self.instagram,
                "YouTube":self.youtube,
                "Twitch":self.twitch,
                "Reddit":self.reddit,
                "TikTok":self.tiktok,
                "Threads":self.threads,
                "Spotify":self.spotify,
                "Apple Podcasts":self.apple,
                "Website":self.website,
                "Other":self.other}

class Projects(models.Model):
    pID=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='PID')
    sID=models.ForeignKey(Socials,on_delete=models.CASCADE)
    projectName=models.CharField(max_length=255)
    projectDescription=models.TextField()
    projectStatus=models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)

class People(models.Model):
    hID=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='HID')
    firstname = models.CharField(max_length=255,blank=True,default='First Name')
    lastname = models.CharField(max_length=255,blank=True,default='Last Name')
    pronouns = models.CharField(max_length=255,blank=True)
    handle = models.CharField(max_length=255,blank=True)
    sID=models.ForeignKey(Socials,on_delete=models.CASCADE,null=True)
    pID=models.ManyToManyField(Projects)
    personStatus=models.ForeignKey(Status, on_delete=models.CASCADE,blank=True, null=True)