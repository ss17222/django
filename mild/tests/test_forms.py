# from django.test import TestCase
# from mild.forms import SignUpForm



# class TestSignUpForm(TestCase):


#     def test_SignUp_Form(self):

#         invalid_data = {
#             "email": "ss17222@gmail.com",
#             "fname": "sumit",
#             "lname": "singh", 
#             "dob"  : "27-11-1996",
#             "phone_number" : "9801407745",
            
            


#     }
#         form = SignUpForm(data=invalid_data)
#         form.is_valid()
#         self.assertTrue(form.errors)


#         valid_data = {
#            "email": "ss17222@gmail.com",
#             "fname": "sumit",
#             "lname": "singh", 
#             "dob"  : "27-11-1996",
#             "phone_number" : "9801407745",
#             "password" : "secret",
#             "confirm" : "secret"

            
#     }
#         form = SignUpForm(data=valid_data)
#         form.is_valid()
#         self.assertFalse(form.errors)

