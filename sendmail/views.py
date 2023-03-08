from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from backend_api import settings

@csrf_exempt
def contactmail(request):
    if request.method == 'POST':
        name = request.POST['name'] or '--*--'
        phone = request.POST['phone'] or '--*--'
        email = request.POST['email'] or '--*--'
        message = request.POST['message'] or '--*--'
        job = request.POST['job'] or '--*--'
        company = request.POST['company'] or '--*--'
        reason = request.POST['reason'] or '--*--'
        # recipient_list = [request.POST.get('to_email')]
        if name and email and phone and message:
          admin_deliver = "Hello, Sales team \n" + ' ' +  '\n' + name + ' just reached out to us through our contact form, check the response below: \n' + ' ' + '\n' + 'Name: \n' + name + '\n' + ' ' + '\n' + 'Email: \n' + email + '\n' + ' ' + '\n' + 'Phone: \n' + phone +  '\n' + ' ' + '\n' + 'Job: \n' + job + '\n' + ' ' + '\n' + 'Company: \n' + company + '\n' + ' ' + '\n' + 'Reason: \n' + reason + '\n' + ' ' + '\n' + 'Message: \n' + message
          admin_subject = "New Contact Form Entry From " + name
          user_deliver = "Hey there " + name + "," + '\n' + '\n' + "Thanks for reaching out to us - we're always excited to hear from people who love our products and services as much as we do!" + '\n' + '\n' + "We promise to get back to you within 24 hours (or less!) with more information on how we can help. In the meantime, feel free to keep sending us your burning questions - we're here to help you out however we can." + '\n' + '\n' + "Thanks for choosing AfriLight Technologies Ltd - we can't wait to show you what we have got in store." + '\n' + '\n' + "Best regards, \nGbenga Daniels." 
          user_subject = name + ", Your Details Have Been Submitted"
          site_title = "Smatforms"
          send_mail(
            admin_subject,
            admin_deliver,
            settings.DEFAULT_FROM_EMAIL,
            ['demo@smatforms.ng'],
            fail_silently= False
        )

          send_mail(
            user_subject,
            user_deliver,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently= False
        )
        return JsonResponse({'message': 'Email sent successfully'})
    else:
      return JsonResponse({'Message': 'You need to make a post request'})    







@csrf_exempt
def pricingmail(request):
    if request.method == 'POST':
        name = request.POST['name'] or '--*--'
        phone = request.POST['phone'] or '--*--'
        email = request.POST['email'] or '--*--'
        job = request.POST['job'] or '--*--'
        company = request.POST['company'] or '--*--'
        plan = request.POST['plan'] or '--*--'
        # recipient_list = [request.POST.get('to_email')]
        if name and email and phone and plan:
          admin_deliver = "Hello, \n" + ' ' +  '\n' + name + ' is willing to subscribe to our ' + plan + ' package, check the response below: \n' + ' ' + '\n' + 'Name: \n' + name + '\n' + ' ' + '\n' + 'Email: \n' + email + '\n' + ' ' + '\n' + 'Phone: \n' + phone +  '\n' + ' ' + '\n' + 'Job: \n' + job + '\n' + ' ' + '\n' + 'Company: \n' + company + '\n' + ' ' + '\n' + 'Package Selected: \n' + plan
          admin_subject = "New Subscription Package Form Entry From " + name
          user_deliver = "Hey there " + name + "," + '\n' + '\n' + "Thanks for your interest in our " + plan + " Package - we're always excited to hear from people who love our products and services as much as we do!" + '\n' + '\n' + "We promise to get back to you within 24 hours (or less!) with more information on how we can help. In the meantime, feel free to keep sending us your burning questions - we're here to help you out however we can." + '\n' + '\n' + "Thanks for choosing AfriLight Technologies Ltd - we can't wait to show you what we have got in store." + '\n' + '\n' + "Best regards, \nGbenga Daniels." 
          user_subject = "You Are Getting Close"
        
          send_mail(
            admin_subject,
            admin_deliver,
            settings.DEFAULT_FROM_EMAIL,
            ['apehg@smatforms.ng'],
            fail_silently= False
        )

          send_mail(
            user_subject,
            user_deliver,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently= False
        )
        return JsonResponse({'message': 'Email sent successfully'})
    else:
      return JsonResponse({'Message': 'You need to make a post request'})    
