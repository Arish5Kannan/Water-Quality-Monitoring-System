from django.shortcuts import render,redirect
from  django.http import JsonResponse,HttpResponse
import json
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login as auth_login,logout
import requests 
def getData(request):
    if request.method == 'GET':
        try :
            data = realtime.objects.latest('created_at')
            print(data)
            item = {
                'ph':f"{data.ph:.1f}",
                'conductivity':data.conductivity,
                'turbidity':data.turbidity,
                'temperature':data.temperature,
            }
            return JsonResponse({'items':item},status=200)
        except Exception as e:
            return JsonResponse({'error':'Failed to retrieve the data'},status=200)
        
            
def message_alert(request):
    if request.method == 'GET' and request.user.is_authenticated :
        try:
            # Ensure the user model has the required fields
            username = request.user.username
            contact_no = getattr(request.user, 'contact_no', None)  # Fetch contact field safely

            if not contact:
                return JsonResponse({'msg': 'Contact number not found for user.'}, status=200)

            # Send the message
            send_msg(contact, username)
            return JsonResponse({'msg': 'Message sent successfully to you!'}, status=200)
        except Exception as e:
            return JsonResponse({'msg': 'An error occurred while sending the message.', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'msg': 'Login to get Message alert'}, status=200)

def email_alert(request):
    if request.method == 'GET' and request.user.is_authenticated :
        try:
            email = request.user.email
            username = request.user.username
            send_html_email(email, username)  # Send the email
            return JsonResponse({'msg': 'Email sent successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'msg': 'An error occurred while sending the email.', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'msg': 'Login to get email alert'}, status=200)

        
def Logout(request):
    logout(request)
    return redirect("/")
def login(request):
    
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('Name')
        password = data.get('Password')

        user = authenticate(request, username=name, password=password)
        if user is None:
            return JsonResponse({'msg': 'Invalid credentials'}, status=200)
        
        auth_login(request, user)
        return JsonResponse({'msg': 'Login successful'}, status=200)
    
    return render(request, "login.html")
    
def collect_data(request):
    if request.method=="POST":
        data = json.load(request)
        ph = data['ph']
        temp = data['temp']
        conduct = data['conduct']
        turb = data['turb']
        phr = PHReading.objects.create(reading=ph)
        tempr = TemperatureReading.objects.create(reading=temp)
        conductr = ConductivityReading.objects.create(reading=conduct)
        turbr = TurbidityReading.objects.create(reading=turb)
        real_time = realtime.objects.create(ph=ph,temperature=temp,conductivity=conduct,turbidity=turb)
        print("Data stored successfully...")
    return HttpResponse(status=200)
from itertools import cycle

def index(request):
    realtimereading = realtime.objects.latest('created_at')

    # Fetch the latest 7 records for each parameter
    ph = PHReading.objects.order_by('-date', '-time')[:7]
    temp = TemperatureReading.objects.order_by('-date', '-time')[:7]
    cond = ConductivityReading.objects.order_by('-date', '-time')[:7]
    turb = TurbidityReading.objects.order_by('-date', '-time')[:7]

    # Prepare data in chronological order and ensure 7 records
    def pad_data(queryset, default_value=0, required_length=7):
        # Extract readings, reverse for chronological order
        readings = [item.reading for item in queryset[::-1]]
        # Pad the data if fewer than required_length records exist
        return readings + [default_value] * (required_length - len(readings))

    phr = pad_data(ph, default_value=7.0)  # Default pH is neutral
    tempr = pad_data(temp, default_value=25.0)  # Default temperature in Celsius
    condr = pad_data(cond, default_value=500.0)  # Default conductivity in µS/cm
    turbr = pad_data(turb, default_value=5.0)  # Default turbidity in NTU

    # Generate labels
    vx_ax = [f"{item.date.strftime('%b-%d')} {item.time.strftime('%H:%M')}" for item in ph[::-1]]

            
    return render(request, 'index.html', {
        'latest': realtimereading,
        'ph': phr,
        'labels':vx_ax,
        'temp': tempr,
        'cond': condr,
        'turb': turbr,
    })

def register(request):
    return render(request,'register.html')
def contact(request):
    return render(request,'contact.html')
def trackdata(request):
    datas = realtime.objects.all()
    return render(request,'trackdata.html',{'datas':datas})
def new_user(request):
    if request.method=='POST':
        try :
            data = json.load(request)
            username = data['Name']
            password = data['Password']
            email = data['Email']
            gender = data['Gender']
            phonenumber = data['Number']
            user =  User.objects.filter(username=username)
            if user.exists():
                return JsonResponse({'msg':'User already registered'},status=200)
            user = User.objects.create_user(username=username,email=email,contact_no=phonenumber,gender=gender)
            user.set_password(password)
            user.save()
            send_html_email(email,username)
            send_msg(phonenumber,username)
        except Exception as e:
            return JsonResponse({'msg':'Failed to register'},status=200)
        return JsonResponse({'msg':'Registration successful'},status=200)

def send_msg(contact,username):
    latest = realtime.objects.latest('created_at')
    url = 'https://wasapy.com/send-message'
    data = {
             'api_secret': 'aU0hnQaN7rSk2KMlQ5ycphtTkHnNlt8hwjxfY6g5FPkqybfGxhni1ohbLQD6jpBJ',
             'phone_number': f'+91{contact}',
            'message': f"""
🌊 *Water Quality Monitoring System Update*

Dear {username},

Here's your water quality report:

📌 pH Level: {latest.ph:.1f} (Optimal range: 6.5 - 8.5)
📌 Turbidity: {latest.turbidity:.0f} NTU
📌 Temperature: {latest.temperature:.0f}°C
📌 Conductivity: {latest.conductivity:.0f} µS/cm

💡 Kindly contact us, Dont Hesitate .


Stay safe and ensure water quality!

🔗 [Visit Dashboard](http://127.0.0.1:8000/trackdata)

Thank you,
*Aquanet Team*
    """,
             }

    response = requests.post(url, json=data)
    print(response.text)
def send_html_email(r,n):
    subject = 'Welcome to Our Service'
    message = '<span style="color:green;">Congratulations</span> <strong>Welcome to Aquanet!</strong>'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [r]
    html_message = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Water Quality Monitoring System</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f7fc;
            }}
            .email-container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }}
            .header {{
                background-color: #0099cc;
                padding: 20px;
                text-align: center;
                color: white;
            }}
            .header h1 {{
                margin: 0;
                font-size: 24px;
            }}
            .content {{
                padding: 20px;
                color: #333;
            }}
            .content h2 {{
                color: #0099cc;
            }}
            .button {{
                display: inline-block;
                background-color: #0099cc;
                color:#fff;
                padding: 12px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 20px;
            }}
            .footer {{
                background-color: #f1f1f1;
                text-align: center;
                padding: 10px;
                font-size: 14px;
                color: #888;
            }}
            .footer a {{
                color: #0099cc;
                text-decoration: none;
            }}
            @media only screen and (max-width: 600px) {{
                .email-container {{
                    width: 100% !important;
                    padding: 10px;
                }}
                .header h1 {{
                    font-size: 20px;
                }}
                .content h2 {{
                    font-size: 18px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1>Water Quality Monitoring System</h1>
            </div>
            <div class="content">
                <h2>Stay Informed About Water Quality!</h2>
                <p>Dear {n},</p>
                <p>We are excited to introduce our <strong>Water Quality Monitoring System</strong>, a cutting-edge solution designed to help you keep track of water quality in real time. Whether you're managing a water treatment facility, a local municipality, or simply concerned about your community's water safety, our system provides comprehensive and accurate data to ensure a safe environment for all.</p>
                <p>With our system, you can:</p>
                <ul>
                    <li>Monitor water quality parameters such as pH, turbidity, dissolved oxygen, and more.</li>
                    <li>Receive real-time alerts on water quality issues.</li>
                    <li>Generate detailed reports for compliance and environmental assessments.</li>
                </ul>
                <p>To learn more and explore the features of our Water Quality Monitoring System, visit our website:</p>
                <p><a href="http://127.0.0.1:8000/" class="button">Visit Our Website</a></p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Water Quality Monitoring System. All rights reserved.</p>
                <p>For inquiries, please <a href="mailto:arishkannan941@gmail.com">contact us</a>.</p>
            </div>
        </div>
    </body>
    </html>
    """
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    