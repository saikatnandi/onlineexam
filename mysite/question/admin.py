from django.contrib import admin

# Register your models here.
from .models import *

class Upload_Question_From_Excel_Admin(admin.ModelAdmin):
    review_template = 'exam/excelparsing.html'

    exclude = ('pub_date', 'edit_date')


    def save_model(self, request, obj, form, change):
        print ("*****in excel save method")
        print (obj)


		# form = ExcelForm(request.POST, request.FILES)
        print ("\n this is a post method \n")
        # if form.is_valid():
        #     print ("the form is valid\n")
        #     wb = openpyxl.load_workbook(request.FILES['file'])
        #     sheet = wb.get_sheet_by_name('Sheet1')
        #     print ("\n\n type of sheet is: " + str(type(sheet)))
        #     for row in range(1, 4):
        #         if ((sheet.cell(row=row, column=1).value) is None):
        #             print ("in if part: " + str(sheet.cell(row=row, column=1).value))
        #             break

        #         q = Mcq_Question(question_text=str(sheet.cell(row=row, column=1).value))
        #         #q = Mcq_Question(question_text="alamin is hungry now")
        #         q.save()
        #         c1 = str(sheet.cell(row=row, column=2).value)
        #         c2 = str(sheet.cell(row=row, column=3).value)
        #         c3 = str(sheet.cell(row=row, column=4).value)
        #         c4 = str(sheet.cell(row=row, column=5).value)

        #         a = str(sheet.cell(row=row, column=6).value)

        #         t1 = str(sheet.cell(row=row, column=7).value)
        #         t2 = str(sheet.cell(row=row, column=8).value)

        #         q.choice_a = c1
        #         q.choice_b = c2
        #         q.choice_c = c3
        #         q.choice_d = c4

        #         q.mcq_answer = a
        #         q.tag1 = t1
        #         q.tag2 = t2
        #         #q.tag3 = t3

        #         q.save()

        #         t3 = str(sheet.cell(row=row, column=9).value)





# admin.site.register(Upload_Question_From_Excel, Upload_Question_From_Excel_Admin)