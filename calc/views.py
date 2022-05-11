from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import PersonalDetails, VaccinationDetails
from .mysqlpass import passwords
from datetime import date
import mysql.connector as sqlcon

from decouple import config

# Create your views here.
def index(request):

    if request.method=='POST':
        try:
            phone_no=int(request.POST['phone'])
            passwd=request.POST['passwd']
            mycon = sqlcon.connect(passwd=passwords.passw,host="localhost", user="root", database="Covid_Vaccination")
            mycursor = mycon.cursor()
            mycursor.execute("SELECT phone_no , pwd from Personal_Details WHERE phone_no={}".format(phone_no))
            data_out = mycursor.fetchall()
            print(data_out)
            for x in data_out:

                    if (x[0]==phone_no):

                        if (str(x[1])==passwd):
                            request.session['phone_no']=phone_no
                            return redirect('user_details')
                        else:
                            messages.info(request,'Incorrect password')
                            return redirect('index')


        except:

            messages.info(request, 'User not registered')
            return redirect('index')


    return render(request,'calc/sign-in-page.html')

def user_details(request):
    phone_no=request.session['phone_no']
    details_list = PersonalDetails.objects.filter(phone_no=phone_no)
    vaccination_status=VaccinationDetails.objects.get(phone_no=phone_no)
    detail = {'details':details_list,'vaccine':vaccination_status}
    return render(request,'calc/user_details.html', context = detail)
#edit
def signup(request):


        if request.method =='POST':
                name=request.POST['name']
                age=request.POST.get('age')
                gender=request.POST['gender']
                password=request.POST['password']
                phone_no=request.POST['phone_no']

                if PersonalDetails.objects.filter(phone_no=phone_no).exists():
                    messages.info(request,'User Already registered')
                    return redirect('signup')
                else:
                    mycon = sqlcon.connect(passwd=passwords.passw,host="localhost", user="root", database="Covid_Vaccination")
                    if mycon.is_connected():
                        print("Successfully connected")
                        cursor = mycon.cursor()


                        data_in = "INSERT INTO Personal_Details (name,phone_no,age,gender,pwd) VALUES ('{}', {}, {}, '{}', '{}')".format(name,phone_no,age,gender,password)
                        cursor.execute(data_in)
                        mycon.commit()

                        data_in_vd='INSERT INTO Vaccination_Details(phone_no) VALUES ({})'.format(phone_no)
                        cursor.execute(data_in_vd)
                        mycon.commit()
                        messages.info(request,'User Successfully Registered')
                        return redirect('index')

        return render(request,'calc/sign-up-page.html')



def vaccination(request):


        if request.method=='POST':
            reg_id=request.POST['regid']
            due_date=request.POST['date']
            time=request.POST['time']
            location=request.POST['location']
            phone_no=request.session['phone_no']
            mycon=sqlcon.connect(passwd=passwords.passw, host='localhost', user='root',database='Covid_Vaccination')
            cursor = mycon.cursor()
            data_in="UPDATE Vaccination_Details SET vaccination_id='{}' , date='{}', time='{}' , location='{}',booking_status='Booked' WHERE phone_no={}".format(reg_id,due_date,time,location,phone_no)
            cursor.execute(data_in)
            mycon.commit()
            return redirect('user_details')
        date_min=date.today()
        date_list={'date_min':date_min}
        return render(request,'calc/vaccination_details.html', context=date_list)


# def form_name_view(request):
#
#
#     return render(request,'calc/form_page.html',{'name':name})
