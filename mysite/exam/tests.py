from django.test import TestCase
from .models import Mcq_Question
from django.test import Client
import unittest
import exam
from django.conf.urls import include
# # Create your tests here.

c = Client()

# def checkHomePage():
#     response = c.get('/exam/')
#     print(response.content)
#     print ("\n\n\n")

# checkHomePage()

# response = c.post('/exam/login/', {})

# response = c.get('/exam/home/')
# print(response.content)
# response.status_code
# print (response.status_code)
# print ("status_code is printed\n")
# response = c.post('/exam/login/', {'username': 'a3', 'password': 'a'}, follow=True)

response = c.get('/exam/myregistration/')
# print (response.content)
# # print ("printing redirect_chain \n")
# # print(response.redirect_chain)
# print ("printing client")
# print (response.client)
# # print ("\n\n\n\nprinting context: " + str(response.context))
# # c.login(username='a3', password='a')

# print ("\n\n\nprinting templates: " + str(response.templates))
# a = response.templates
# print ("printing file name: " + str(a[0].name))
# print ("printing file name: " + str(a[0].name))

# response = c.get('/exam/home/')
# #print(response.content)
# response.status_code
# print (response.status_code)
# print ("\n\n after login \n\n\n")
# response = c.get('/exam/home/')


# print ("\n\n\n\n")
# response.context['topic']
# print(response.context)

# c.logout()
# print ("\n\n after logout \n\n\n")
# response = c.get('/exam/home/')


#print ("\n\nprinting out view name {} " . format(response.resolver_match.func))
#assertEqual(response.resolver_match.func, exam.views.myregistration)
if (response.resolver_match.func == exam.views.result):
	print (".........views okay.......\n")
else:
	print ("................views dont match ........\n")




# class SimpleTest(unittest.TestCase):
#     def setUp(self):
#         # Every test needs a client.
#         self.client = Client()

#     def test_details(self):
#         # Issue a GET request.
#         response = self.client.get('/exam/myregistration/')

#         # Check that the response is 200 OK.
#         self.assertEqual(response.status_code, 200)

#         # Check that the rendered context contains 5 customers.
#         #self.assertEqual(len(response.context['customers']), 5)

#         print ("in test_details function")

#         self.assertEqual(response.resolver_match.func, exam.views.myregistration)
#         self.assertEqual(response.resolver_match.func, exam.views.result)