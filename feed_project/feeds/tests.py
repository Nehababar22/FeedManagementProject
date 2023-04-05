from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
from feeds.models import Feed

# Create your tests here.
class Create_Feed_Test(APITestCase):       
    """ Create Feed Test Case """  

    def setUp(self):        
        """ Test case init data """  

        self.user_admin = User.objects.create(username='admintest',
        password='admintest@123',email='admin@gmail.com') 

        self.user_test = User.objects.create(username='test',
        password='test@123',email='test@gmail.com')

        self.user_demo = User.objects.create(username='demo',
        password='demo@123',email='demo@gmail.com')
             
    def test_super_user_can_create_feed(self):        
        """ super user can create feed """
     
        url=reverse('Feed-list')  
        data= {'title':'abc','content':'aab',
        'created_by':self.user_admin.id} 
        self.client.force_authenticate(self.user_admin)   
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
        
    def test_admin_user_can_create_feed(self):        
        """ admin user can create feed """
     
        url=reverse('Feed-list')  
        data= {'title':'njk','content':'njk',
        'created_by':self.user_test.id} 
        self.client.force_authenticate(self.user_test)    
        response=self.client.post(url,data,format='json') 
        self.assertEqual(response.status_code,201)
     
    def test_anonymous_user_can_create(self):        
        """ anonymous user can create """
     
        url=reverse('Feed-list')  
        data= {'title':'feed','content':'feed detail',
        'created_by':self.user_demo.id} 
        self.client.force_authenticate(self.user_demo)    
        response=self.client.post(url,data,format='json') 
        self.assertEqual(response.status_code,201)
 
        
class Read_Feed_Test(APITestCase):
    """ Read Feed Test Case"""
    
    def setUp(self):        
        """ Test case init data """   

        self.user = User.objects.create_superuser(username='Admin', 
        password='Admin@123', email='Admin@gmail.com')
        self.feed = Feed.objects.create(title='feed',content='feed api',
        created_by=self.user,created_at='2022-01-31',updated_at='2022-01-31') 
    
        self.adminuser = User.objects.create_superuser(username='test', 
        password='test@123', email='test@gmail.com')
        self.adminfeed = Feed.objects.create(title='abc',content='abc api',
        created_by=self.adminuser,created_at='2022-01-11',
        updated_at='2022-01-12') 

    def test_super_user_can_read_feed_list(self):
        """ super user can read feed list """
        
        url=reverse('Feed-list')
        self.client.force_authenticate(self.feed.created_by)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
     
    def test_super_user_can_read_feed_detail(self):
        """ super user can read feed detail """
        
        url=reverse('Feed-detail',args=[self.feed.created_by.id])
        self.client.force_authenticate(self.feed.created_by)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_admin_user_can_read_feed_detail(self):
        """ admin user can read feed detail """
        
        url=reverse('Feed-detail',args=[self.adminfeed.created_by.id])
        self.client.force_authenticate(self.adminfeed.created_by)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_anonymous_user_can_read_feed_detail(self):
        """ anonymous user can read feed detail """
        
        url=reverse('Feed-detail',args=[self.adminfeed.created_by])
        response=self.client.get(url)
        self.assertEqual(response.status_code,403)
     

class Feed_Update_Test(APITestCase): 
    """ update feed Test Case"""  
    
    def setUp(self):        
        """ Test case init data """   

        self.fgh_user = User.objects.create(username='fgh', 
        password='fgh@123', email='fgh@example.com') 
        self.fgh_feed = Feed.objects.create(title='fgh',
        content='fgh',created_by=self.fgh_user) 

        self.jkl_user = User.objects.create(username='jkl', 
        password='jkl@123', email='jkl@example.com') 
        self.jkl_feed = Feed.objects.create(title='jkl',
        content='jkl',created_by=self.jkl_user) 
    
    def test_super_user_can_update_feed(self):
        """ super user can update feed """
       
        url=reverse('Feed-detail', args=[self.fgh_feed.id])
        data = {'title':'lmn','content':'lmn',
        'created_by':self.fgh_user.id}  
        self.client.force_authenticate(self.fgh_user)     
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)
     
    def test_admin_user_can_update_feed(self):
        """ admin user can update feed """
       
        url=reverse('Feed-detail', args=[self.jkl_feed.id])
        data = {'title':'lmn','content':'lmn',
        'created_by':self.jkl_user.id}  
        self.client.force_authenticate(self.jkl_user)     
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)
    
    def test_anonymous_user_cannot_update(self):
        """ anonymous user cannot update """
       
        url=reverse('Feed-detail', args=[self.jkl_feed.id])
        data = {'title':'lmn','content':'lmn',
        'created_by':self.jkl_user.id}    
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,403)
   

class Feed_Delete_Test(APITestCase): 
    """ delete Feed Test Case"""  

    def setUp(self):        
        """ Test case init data """   

        self.acb_user = User.objects.create_superuser(username='acb', 
        password='acb@123', email='acb@example.com')  
        self.acb_feed = Feed.objects.create(title='acb',content='acb',
        created_by=self.acb_user) 

        self.asd_user = User.objects.create(username='asd', 
        password='asd@123', email='asb@example.com')  
        self.asd_feed = Feed.objects.create(title='asb',content='asb',
        created_by=self.asd_user) 

    def test_super_user_can_delete_feed(self):
        """ superuser can delete feed """
        
        self.client.force_authenticate(self.acb_user)
        url=reverse('Feed-detail', args=[self.acb_user.id])
        response = self.client.delete(url,self.acb_user.id,format='json')
        self.assertEqual(response.status_code,204)
      
    def test_admin_user_can_delete_feed(self):
        """ admin user can delete feed """
        
        self.client.force_authenticate(self.asd_user)
        url=reverse('Feed-detail', args=[self.asd_feed.id])
        response = self.client.delete(url,self.asd_feed.id,format='json')
        self.assertEqual(response.status_code,204)

    def test_anonymous_user_cannot_delete_feed(self):
        """ anonymous user cannot delete feed """
        
        url=reverse('Feed-detail', args=[self.asd_feed.id])
        response = self.client.delete(url,self.asd_feed.id,format='json')
        self.assertEqual(response.status_code,403)
    
