from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalDetails, VaccinationDetails

# import mysql.connector as sqlcon

from decouple import config

# Create your views here.
def index(request):

    return render(request,'calc/sign-in-page.html')


def user_details(request):
    details_list = PersonalDetails.objects.all()
    detail = {'details':details_list}
    return render(request,'calc/user_details.html', context = detail)

def signup(request):


        if request.method =='POST':
                name=request.POST['name']
                age=request.POST.get('age')
                gender=request.POST['gender']
                password=request.POST['password']
                phone_no=request.POST['phone_no']
                mycon = sqlcon.connect(passwd='',host="localhost", user="root", database="Covid_Vaccination")
                if mycon.is_connected():
                    print("Successfully connected")
                    cursor = mycon.cursor()


                    data_in = "INSERT INTO Personal_Details (name,phone_no,age,gender,pwd) VALUES ('{}', {}, {}, '{}', '{}')".format(name,phone_no,age,gender,password)
                    cursor.execute(data_in)
                    mycon.commit()

                print(name,age,gender,password,phone_no)
        return render(request,'calc/sign-up-page.html')





# def form_name_view(request):
#
#
#     return render(request,'calc/form_page.html',{'name':name})
