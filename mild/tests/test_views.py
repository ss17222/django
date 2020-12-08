# from django.test import TestCase, Client
# from django.urls import reverse
# from mild.models import MyUser, MyUserManagement



# class Test_views(TestCase):

#     def setUp(self):
#         self.client = Client()

#     def test_signup(self):
#         response = self.client.get(reverse('mild:signup'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response,'home.html')

#     def test_login(self):
#         response = self.client.get(reverse('mild:login'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response,'login.html')

#     def test_forgot(self):
#         response = self.client.get(reverse('mild:forgot'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response,'forgot.html')

    
#     def test_logout(self):
#         response = self.client.get(reverse('mild:logout'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response,'login.html')

    

 
