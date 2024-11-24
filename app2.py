from flask import Flask, request, render_template
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError
import smtplib
from email.message import EmailMessage
import random

lol = Flask(__name__)

@lol.route('/')
def form():
    return render_template('email.html')

@lol.route('/otpemail',methods=['POST'])
def otpverify():
    otp=''
    for i in range(6):
        otp=otp+str(i)

    ##
    email=request.form.get('email')
    print(email)
    otpr=request.form.get('otp')

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login('hperumalla.21@gmail.com','zsun dnpq afud itvs')

    mes=EmailMessage()
    mes['Subject']="OTP for Mikoshi!"
    mes['TO']=email
    mes['From']='hperumalla.21@gmail.com'
    mes.set_content('YOur OTP for a safe bitcoi wallet is: '+otp)


    server.send_message(mes)

    # if otpr==otp:
    #     return render_template('otpverified.html')
    # else:
    #     return render_template('fail.html')

otpverify()