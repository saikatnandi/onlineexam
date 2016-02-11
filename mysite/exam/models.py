from django.db import models

class Mcq_Question(models.Model):
   
    question_text = models.CharField(max_length=200)   
    choice_a =  models.CharField(max_length=200) 
    choice_b =  models.CharField(max_length=200) 
    choice_c =  models.CharField(max_length=200) 
    choice_d =  models.CharField(max_length=200) 

    mcq_answer = models.CharField(max_length=200)       

    def __str__(self):
    	return self.question_text








# class Mcq_Choice(models.Model):
#     mcq_question = models.ForeignKey(Mcq_Question,  on_delete=models.CASCADE)
#     mcq_choice_text = models.CharField(max_length=200)
#     id = models.AutoField(primary_key=True)
   
#     def __str__(self):
#     	return self.mcq_choice_text


# class Mcq_Answer(models.Model):
#     mcq_question = models.OneToOneField(
#         Mcq_Question,
#         on_delete=models.CASCADE,
        
#     )
#     mcq_choice = models.OneToOneField(Mcq_Choice)
    
   
#     def __str__(self):
#     	return "alamin"

