from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Item
from django.core.mail import send_mail  

@login_required(login_url='login')
def additem(request):
    if request.method == 'POST':
        iname = request.POST['iname']
        prof = request.FILES['img']
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        img4 = request.FILES.get('img4')
        itag = request.POST['itag']
        sdisc = request.POST['sdis']
        ldisc = request.POST['ldis']
        price = request.POST['iprice']
        sdate=request.POST['s_date']
        omail = request.user.email

        item = Item(ownermail=omail,start_date=sdate,currentPrice=price,img1=img1,img2=img2,img3=img3,img4=img4,name=iname,profile=prof,tag=itag,short_description=sdisc,long_description=ldisc,basePrice=price)
        item.save()
        return redirect("home")
    else:
        return render(request,'additem.html')
@login_required(login_url='login')
def biditem(request):
    id=request.GET['id']
    item = Item.objects.get(id=id)
    lstatus="live"

    if item.status ==lstatus:
        return render(request,"biditem.html",{'item':item})
    else:
        return redirect("home")
@login_required(login_url='login')
def validate(request):
    value = request.GET.get('bidrs')
    
    iid = request.GET.get('iid')
    # print (iid)

    bidder = request.user
    bidderEmail = bidder.email
    # print (bidder.id)
    item_obj = Item.objects.get(id=iid)

    itemownerEmail = item_obj.ownermail

    if bidderEmail==itemownerEmail:
        return render(request,"notification.html")
    else:
        mail = item_obj.ownermail
        subject = "Online Bidding"  
        msg     = "Congratulations your item is bidded by "+bidder.email+", By INR rs = "+value+". Contact your buyer by email Thank You for using our app."
        to      = mail  
        res     = send_mail(subject, msg, "bidmafia007@gmail.com", [to])


        Item.objects.filter(id=iid).update(currentPrice=value)
        Item.objects.filter(id=iid).update(highest_bidder=bidder.id)
        return redirect("home")