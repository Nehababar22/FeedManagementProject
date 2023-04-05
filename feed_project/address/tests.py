from django.urls import reverse
from rest_framework.test import APITestCase
from address.models import Address
from users.models import User

# Create your tests here.
class Create_Address_Test(APITestCase):      
    """ Create address Test Case """  
    
    def setUp(self):        
        """ Test case init data """   
        self.user = User.objects.create(username='abc', 
        password='abc@123', email='abc@example.com')

        self.user_nm = User.objects.create(username='pqr',
        password='pqr@123', email='pqr@example.com')

        self.user_xyz = User.objects.create(username='xyz', 
        password='xyz@123', email='xyz@example.com')

    def test_super_user_can_create_address(self):        
        """ super user can create address """
        
        url=reverse('address-list')  
        data = {'street':'abc','city':'aab',
        'state':'maharashtra','country':'india','user':self.user.id}   
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
    
    def test_admin_user_can_create_address(self):        
        """ admin user can create address """

        url=reverse('address-list')  
        data = {'street':'pqr','city':'ppur',
        'state':'maharashtra','country':'india','user':self.user_nm.id}   
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
       
    def test_anonymous_user_can_create_address(self):        
        """ anonymous user can create address """

        url=reverse('address-list')  
        data = {'street':'xyz','city':'solapur',
        'state':'maharashtra','country':'india','user':self.user_xyz.id}   
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)

      
class Read_Address_Test(APITestCase):
    """ Read User Test Case"""
    
    def setUp(self):        
        """ Test case init data """   

        self.user = User.objects.create_superuser(username='admin',
        password='admin@123', email='admin@example.com')  
        self.address = Address.objects.create(street='FC Road',
        city='Pune',state='Maharashtra',country='India',user=self.user) 

        self.user_nm = User.objects.create_user(username='test',
        password='test@123', email='test@example.com') 
        self.user_address = Address.objects.create(street='MG Road',
        city='Ppur',state='Maharashtra',country='India',user=self.user_nm) 

    def test_super_user_can_read_address_list(self):
        """ super user can read address list """
        
        url=reverse('address-list')
        response=self.client.get(url)
        self.assertEqual(self.address.user, self.user)
        self.assertEqual(response.status_code,200)     

    def test_super_user_can_read_address_detail(self):        
        """ super user can read address detail """
        
        self.client.force_authenticate(self.address.user)
        url=reverse('user-detail',args=[self.address.user.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    
    def test_admin_user_can_read_address_detail(self):        
        """ admin user can read address detail """
        
        self.client.force_authenticate(self.address.user)
        self.assertEqual(self.user_address.user, self.user_nm)
        url=reverse('user-detail',args=[self.user_address.user.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_anonymous_user_cannot_read_address_detail(self):
        """ anonymous user cannot read address detail  """
        
        url=reverse('address-detail',args=[self.user_address.user.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)


class Address_Update_Test(APITestCase): 
    """ Update Address Test Case"""  
    
    def setUp(self):        
        """ Test case init data """  

        self.demo_user = User.objects.create_superuser(username='acb', 
        password='acb@123', email='acb@example.com')  
        self.demo_address = Address.objects.create(street='FC Road',
        city='Pune',state='Maharashtra',country='India',user=self.demo_user) 

        self.dfg_user = User.objects.create(username='dfg', 
        password='dfg@123', email='dfg@example.com')  
        self.dfg_address = Address.objects.create(street='SB Road',
        city='Pune',state='Maharashtra',country='India',user=self.dfg_user) 

    def test_super_user_can_update_address(self):
        """ super user can update address """
       
        url=reverse('address-detail', args=[self.demo_address.id])
        data = {'street':'lmn','city':'mumbai',
        'state':'Maharashtra','country':'India',
        'user':self.demo_user.id}   
        self.client.force_authenticate(self.demo_user)     
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)

    def test_admin_user_can_update_address(self):
        """ admin user can update address """
       
        url=reverse('address-detail', args=[self.dfg_address.id])
        data = {'street':'mnp','city':'Mumbai',
        'state':'Maharashtra','country':'India',
        'user':self.dfg_user.id}   
        self.client.force_authenticate(self.dfg_user)     
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)
        
    def test_anonymous_user_cannot_update_address(self):
        """ anonymous user can update address """
       
        url=reverse('address-detail', args=[self.dfg_address.id])
        data = {'street':'xyz','city':'Delhi',
        'state':'Maharashtra','country':'India',
        'user':self.dfg_user.id}     
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,404)

  
class Address_Delete_Test(APITestCase): 
    """ Delete Address Test Case"""  

    def setUp(self):        
        """ Test case init data """   
    
        self.superuser = User.objects.create_superuser(username='klm', 
        password='klm@123', email='klm@example.com')  
        self.superuser_address = Address.objects.create(street='ABC Road',
        city='Solapur',state='Maharashtra',country='India',user=self.superuser) 

        self.adminuser = User.objects.create_user(username='hjk', 
        password='hjk@123', email='hjk@example.com')  
        self.admin_address = Address.objects.create(street='ABC Road',
        city='Solapur',state='Maharashtra',country='India',user=self.adminuser) 

    def test_super_user_can_delete_address(self):
        """ superuser can delete address """
        
        self.client.force_authenticate(self.superuser)
        url=reverse('address-detail', args=[self.superuser.id])
        response = self.client.delete(url,self.superuser.id,format='json')
        self.assertEqual(response.status_code,204)
    
    def test_admin_user_cannot_delete_address(self):
        """ admin user cannot delete address """
        
        url=reverse('address-detail', args=[self.admin_address.id])
        response = self.client.delete(url,self.admin_address.id,format='json')
        self.assertEqual(response.status_code,404)

    def test_anonymous_user_cannot_delete(self):
        """ anonymous user cannot delete address """
        
        self.client.force_authenticate(self.adminuser)
        url=reverse('address-detail', args=[self.admin_address.id])
        response = self.client.delete(url,self.admin_address.id,format='json')
        self.assertEqual(response.status_code,403)
    
