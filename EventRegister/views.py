from django.shortcuts import render
from .models import Register
from django.utils.crypto import get_random_string


# Create your views here.


def submit(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        identification = request.FILES['id']
        reg_type = request.POST['type']
        if reg_type == 'self':
            no_ticket = 1
        else:
            no_ticket = request.POST['no_ticket']

        reg_id = get_reg_id()

        registered = Register(reg_id=reg_id, fullname=fullname, mobile=mobile, email=email,
                              identification=identification, reg_type=reg_type, no_ticket=no_ticket)
        registered.save()
        registration_id = registered.reg_id

        context = {'reg_id': registration_id}
        return render(request, 'thankyou.html', context)


def get_reg_id():
    reg_id = get_random_string(8).upper()
    registers = Register.objects.all()
    for register in registers:
        if register.reg_id == reg_id:
            get_reg_id()
        else:
            continue
    return reg_id
