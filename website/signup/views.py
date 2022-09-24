from multiprocessing.sharedctypes import Value
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def signupaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='alamjhangeer2@',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,Value in d.items():
            if key=="first_name":
                fn=Value
            if key=="last_name":
                ln=Value
            if key=="sex":
                s=Value
            if key=="email":
                em=Value
            if key=="password":
                pwd=Value
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,'signup.html')
