from django.db import models

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Promote(models.Model):
    promote_id = models.AutoField(primary_key=True)
    pub_date = models.DateField(auto_now_add=True)
    fullname = models.CharField(max_length=500)
    user_email =  models.CharField(max_length=100, default="")
    user_phone = models.CharField(max_length=100, default="")
    user_promote = models.CharField(max_length=500, default="")
    user_link = models.CharField(max_length=500, default="")
    website_1 = models.CharField(max_length=500, default="False")
    website_2 = models.CharField(max_length=500, default="False")
    page_1 = models.CharField(max_length=500, default="False")
    page_2 = models.CharField(max_length=500, default="False")
    user_image = models.ImageField(upload_to="promotehere1/images")
    user_moretext = models.CharField(max_length=4000,default="")
    user_add = models.CharField(max_length=4000,default="")

    def __str__(self):
        return self.fullname