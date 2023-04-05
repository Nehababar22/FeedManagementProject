from django.contrib.auth.models import Group 

def add_default_group(sender,instance,created,**kwargs):
    """ signal for assign group for new user """
    
    if created: 
        group = Group.objects.get_or_create(name="Admin")
        instance.groups.add(group[0])
        


          