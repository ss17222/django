# from django.test import TestCase
# from django.urls import reverse, resolve
# from mild.views import *
# #from django.core.urlresolvers import resolve, reverse
# from django.test import client



# class TestUrls(TestCase):
#    # def signup_client(self):
#    #    self.client = client()

#    def test_signup_url_is_resolved(self):
#       response = self.client.get(reverse('mild:signup'))
#       self.assertEqual(response.status_code, 200)

      
      

#    # def signupd_client(self):
#    #    self.client = client()

#    # def test_signupd_url_is_resolved(self):

#    #    response = self.client.post('mild:signup',{ "email": "ss17222@gmail.com",
#    #          "fname": "sumit",
#    #          "lname": "singh", 
#    #          "dob"  : "27-11-1996",
#    #          "phone_number" : "9801407745",
#    #          "password" : "secret",
#    #          "confirm" : "secret"})
#    #    self.assertEqual(response.status_code,302)


   

    
#    def test_login_url_is_resolved(self):

       
#       response = self.client.get(reverse('mild:login'))
#       self.assertEqual(response.status_code, 200)
#    # def test_logind_url_is_resolved(self):
        
#    #    response = self.client.post(reverse('mild:login',{'email':'ss17222@gmail.com', 'password': '123456789'}))
#    #    self.assertEqual(response.status_code, 302)
    
    


#    def test_logout_url_is_resolved(self):
       
#       response = self.client.get(reverse('mild:logout'))
#       self.assertEqual(response.status_code, 200)
    
#    def test_forgot_url_is_resolved(self):
      
#       response = self.client.get(reverse('mild:forgot'))
#       self.assertEqual(response.status_code, 200)

   
#    def test_activate_url_is_resolved(self):
      
#       response = self.client.get(reverse('mild:activate', kwargs= {'uid':1}))
#       self.assertEqual(response.status_code, 200)

#    def test_forgoten_url_is_resolved(self):
      
#       response = self.client.get(reverse('mild:forgoten', kwargs= {'uid':1}))
#       self.assertEqual(response.status_code, 200)


#    def test_dashboard_url_is_resolved(self):
      
#       response = self.client.get(reverse('mild:dashboard'))
#       self.assertEqual(response.status_code, 302)

    
    
    
    
    
    

