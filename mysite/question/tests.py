from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

class ModelTest(TestCase):

    def test_exam_annoymously(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        # client = Client()
        # response = client.post('/login/', {'username': 'a2', 'password': 'a'})

        # print (response.status_code)

        # response = client.get('/question/questionset/10/')


        # response = self.client.get(reverse('question:question_set' , args=[1]))
        # self.assertEqual(response.status_code, 200)


        # response = self.client.get(reverse('question:exam_result' , args=[1]))

        response = self.client.get(reverse('question:result' , args=[1]))
        # response = self.client.get("/question/questionset/10/result/")
        # response = client.get("/question/questionset/10/result/")

        # self.assertEqual(response.status_code, 200)



        # self.assertEqual(response.status_code, 200)

