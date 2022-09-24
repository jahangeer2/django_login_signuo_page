from distutils.log import error
from multiprocessing.sharedctypes import Value
from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def loginaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',passwd='alamjhangeer2@',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,Value in d.items():
            if key=="email":
                em=Value
            if key=="password":
                pwd=Value
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t== ():
            return render(request,'erorr.html')
        else:
            return render(request,"welcom.html")
        m.commit()
    return render(request,'login.html')
