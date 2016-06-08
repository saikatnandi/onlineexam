from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.test import *

from .views import *
from qa1.models import *
from django.core.management import call_command
from django.db import connections







# class CustomTestCase(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         super(CustomTestCase, cls).setUpClass()
#         connections['replica']._orig_cursor = connections['replica'].cursor
#         connections['replica'].cursor = connections['default'].cursor

#     @classmethod
#     def tearDownClass(cls):
#         connections['replica'].cursor = connections['replica']._orig_cursor
#         super(CustomTestCase, cls).tearDownClass()



# def urls()


class SimpleTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     call_command('loaddata', 'backup.json', verbosity=0)

    def setUp(self):
        # Every test needs access to the request factory.
        
        # self.q = Question_Set(question_set_text="Test Question Set")
        # self.q.save()
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')

    def test_anonymoususer(self):
        # Create an instance of a GET request.

        # print ("****** test details method")

        request = self.factory.get('/question/questionset/2/result/0/')

        # # Recall that middleware are not supported. You can simulate a
        # # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()


        # Test my_view() as if it were deployed at /customer/details
        response = result(request,1,0)
        # Use this syntax for class-based views.
        # response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 200)




  
    def test_registered_user(self):
        request = self.factory.get('/')
        request.user =  User.objects.get(username='a20')




        # Test my_view() as if it were deployed at /customer/details
        response = result(request,1,0)
        self.assertEqual(response.status_code, 200)


        response = result(request,17,0)
        self.assertEqual(response.status_code, 302)





    def test_admin(self):
        request = self.factory.get('/')
        request.user =  User.objects.get(username='admin')


        # Test my_view() as if it were deployed at /customer/details
        response = result(request,1,0)
        self.assertEqual(response.status_code, 200)


        response = result(request,17,0)
        self.assertEqual(response.status_code, 200)




