from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
from django.contrib.auth.models import Group 

# Create your tests here.
class Create_User_Test(APITestCase):  
    """ Create User Test Case"""  
      
    def test_super_user_can_create(self):        
        """ super user can create """
        
        url=reverse('user-list')
        data = {'username':'admin','email':'admin@gmail.com',
                'password':'admin@123','first_name':'admin1',
                'last_name':'admin2'}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
    
    def test_admin_user_can_create(self):
        """ admin user can create """
        
        url=reverse('user-list')
        data = {'username':'demo','email':'demo@gmail.com',
                'password':'demo@123','first_name':'demo1',
                'last_name':'demo2'}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
            
    def test_anonymous_user_can_create(self):
        """ anonymous user can create """
        
        url=reverse('user-list')
        data = {'username':'klm','email':'klm@gmail.com',
                'password':'klm@123','first_name':'klm1',
                'last_name':'klm2'}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
        
class Read_User_Test(APITestCase):
    """ Read User Test Case"""
    
    def setUp(self):        
        """ Test case init data """  
        
        self.superuser = User.objects.create_superuser(username='Admin',
        email='Admin@gmail.com',password='Admin@123',first_name='Admin1',
        last_name='Admin2')

        self.adminuser = User.objects.create(username='test',
        email='test@gmail.com',password='test@123',first_name='test1',
        last_name='test2') 
        group_name = "Admin"
        self.admingroup = Group.objects.get(name=group_name)
        self.admingroup.save()

        self.user = User.objects.create(username='vnm',email='vnm@gmail.com',
        password='vnm@123',first_name='vnm1',last_name='vnm2') 
        
    def test_super_user_can_read_user_list(self):
        """ super user can read user list """
        
        url=reverse('user-list')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
               
    def test_super_user_can_read_user_detail(self):        
        """ super user can read user detail """
        
        self.client.force_authenticate(self.superuser)
        url=reverse('user-detail',args=[self.superuser.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_admin_user_can_read_user_detail(self):
        """ admin user can read user detail """

        self.adminuser.groups.add(self.admingroup)
        self.client.force_authenticate(self.adminuser)
        url=reverse('user-detail',args=[self.adminuser.id]) 
        response=self.client.get(url,format='json') 
        self.assertEqual(response.status_code,200)
     
    def test_anonymous_user_cannot_read_user_detail(self):
        """ anonymous user cannot read user detail """
        
        url=reverse('user-detail',args=[self.user.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
   
         
class User_Update_Test(APITestCase): 
    """ Update User Test Case"""  
    
    def setUp(self):
        """ Test case init data """  
        
        self.superuser = User.objects.create_superuser(username='nik',
        email='nikita@gmail.com',password='nikita@123',first_name='nikita',
        last_name='kamble')  
       
        self.admin_user = User.objects.create(username='priyank',
        email='priyanka@gmail.com',password='priyanka@123',first_name='priyanka',
        last_name='bhosale')  
               
        self.user_nm1 = User.objects.create(username='himangi',
        email='himangi@gmail.com',password='himangi@123',first_name='him',
        last_name='doke')
                                         
    def test_super_user_can_update_user(self):
        """ super user can update user """
       
        url=reverse('user-detail', args=[self.superuser.id])
        data = {'username':'xyz','email':'xyz@gmail.com',
        'password':'xyz@123','first_name':'xyz1','last_name':'xyz2'}
        self.client.force_authenticate(self.superuser)
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)
               
    def test_admin_user_can_update_user(self):
        """ admin user can update user"""
           
        url=reverse('user-detail', args=[self.admin_user.id])
        data = {'username':'lmn','email':'lmn@gmail.com',
        'password':'lmn@123','first_name':'lmn1','last_name':'lmn2'}
        self.client.force_authenticate(self.admin_user)
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)
         
    def test_anonymous_user_cannot_update_user(self):
        """ anonymous user cannot update user """
           
        url=reverse('user-detail', args=[self.user_nm1.id])
        data = {'username':'jkl','email':'jkl@gmail.com',
        'password':'jkl@123','first_name':'jkl1','last_name':'jkl2'}
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,404)
    
                
class User_Delete_Test(APITestCase):
    """ Delete User Test Case"""  
    
    def setUp(self): 
        """ Test case init data """  
        
        self.superuser= User.objects.create_superuser(username='example',
        email='example@gmail.com',password='example@123',first_name='ex1',
        last_name='ex2')
        
        self.adminuser = User.objects.create(username='pqr',
        email='pqr@gmail.com',password='pqr@123',first_name='pqr1',
        last_name='pqr2')
                                            
        self.user_nm2 = User.objects.create(username='pranali',
        email='pranali@gmail.com',password='pranali@123',first_name='pranali',
        last_name='more')
                                               
    def test_super_user_can_delete(self):
        """ superuser can Delete """
        
        self.client.force_authenticate(self.superuser)
        url=reverse('user-detail', args=[self.superuser.id])
        response = self.client.delete(url,self.superuser.id,format='json')
        self.assertEqual(response.status_code,204)
                      
    def test_admin_user_cannot_delete_user(self):
        """ admin user cannot delete user """
            
        url=reverse('user-detail', args=[self.adminuser.id])
        response = self.client.delete(url,self.adminuser.id,format='json')
        self.assertEqual(response.status_code,404)
    
    def test_anonymous_user_cannot_delete_user(self):
        """ admin user cannot delete user  """
            
        url=reverse('user-detail', args=[self.user_nm2.id])
        response = self.client.delete(url,self.user_nm2.id,format='json')
        self.assertEqual(response.status_code,404)


class Read_Group_Test(APITestCase):
    """ Read Group Test Case"""
    
    def setUp(self):        
        """ Test case init data """  

        group_name = "Admin"
        self.group = Group(name=group_name)
        self.group.save()
        self.user = User.objects.create_user(username="test", 
        email="test@test.com", password="test")

        self.user_demo = User.objects.create_user(username="demotest", 
        email="demotest@test.com", password="pass@123")

    def test_super_user_can_read_group_list(self):
        """ super user can read group list """
        
        url=reverse('group-list')
        self.client.force_authenticate(self.user)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_admin_user_can_read_group_list(self):
        """ admin user can read group list """
        
        url=reverse('group-list')
        self.client.force_authenticate(self.user_demo)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_anonymous_user_cannot_read_group_list(self):
        """ anonymous user cannot read group list """
        
        url=reverse('group-list')
        response=self.client.get(url)
        self.assertEqual(response.status_code,403)
   
