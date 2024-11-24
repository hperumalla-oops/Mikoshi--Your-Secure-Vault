from flask import Flask, request, render_template
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError
import smtplib
from email.message import EmailMessage
import random

lol = Flask(__name__)

otp=''


@lol.route('/')
def form():
    return render_template('email.html')

@lol.route('/otpemail',methods=['POST'])
def sendemail():
    global otp
    for i in range(6):
        otp=otp+str(random.randint(0,9))

    ##
    email=request.form.get('email')
    print(email)

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login('hperumalla.21@gmail.com','zsun dnpq afud itvs')

    mes=EmailMessage()
    mes['Subject']="OTP for Mikoshi!"
    mes['TO']=email
    mes['From']='hperumalla.21@gmail.com'
    mes.set_content('YOur OTP for a safe bitcoi wallet is: '+otp)


    server.send_message(mes)

@lol.route('/otpverify', methods=['POST'])

def otpverify():

    global otp  # Use the global OTP for verification
    otpr = request.form.get('otp')  

    if otp == otpr:
        return render_template('otpverified.html')
        otp=""
    else:
        return render_template('fail.html')  # OTP is incorrect



if __name__ == "__main__":
    lol.run(debug=True)