from django.shortcuts import render

def indexView(request):
    my_dict={'insert_content':'Welcome to the homepage'}
    return render(request,'index.html',context=my_dict)

def loginView(request):
    return render(request,'login.html')   


def authView(request):
    uname=request.post['uname']
    upass=request.post['upass']
    user=(uname,upass,)
    return render(request,'index.html',{'user':user})
