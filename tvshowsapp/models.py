from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def team_create_validate( self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors['titlereq'] = "Title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors['networkreq'] = "Network name should be at least 3 characters."
        
        if len(postData['release']) < 3:
            errors["releasereq"] = "Description should be at least 20 characters."
        return errors   

class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.TextField(max_length=255, null=True )
    release_date= models.DateField(max_length=255, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= ShowManager()
    

    
    