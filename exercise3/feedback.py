import smtplib, os

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, formataddr
from email.header import Header
from flask import Flask, request, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/feedback/', methods=['POST', 'GET'])
def feedback():
    def to_sender(toaddress, content):
        print(2)
        fromaddress = "andy193.study@gmail.com"
        toaddress
        password = "01284376896"
        subject = "Copy of your feedback"
        content
        sender
        msg = MIMEMultipart()
        msg['From'] = fromaddress
        msg['To'] = toaddress
        msg['Subject'] = subject
        msg.attach(MIMEText(content))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(fromaddress, password)
        s.sendmail(fromaddress, toaddress, msg.as_string())
        s.quit()
        return "The copy of feedback has been sent to the sender"

    def to_owner(sender, content):
        fromaddress = "andy193.study@gmail.com"
        toaddress = "keodepchai@gmail.com"
        password = "01284376896"
        subject = "Feedback from client"
        content
        sender 
        author = formataddr((str(Header(sender)), "andy193.study@gmail.com"))
        msg = MIMEMultipart()
        msg['From'] = author
        msg['To'] = toaddress
        msg['Subject'] = subject
        msg.attach(MIMEText(content))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(fromaddress, password)
        s.sendmail(fromaddress, toaddress, msg.as_string())
        s.quit()
        return "The feedback has been sent to the owner"

    if request.method == 'POST':       
        content = request.form['message']
        sender = request.form['client_mail']
        to_sender(sender, content)
        to_owner(sender, content)        
    return render_template('index.html')

@app.route('/thanks/')
def thanks():
    return "Your feedback has been sent. A copy of your feedback also is being sent to your email address Thanks for your feedback"

if __name__ == "__main__":
    app.run(debug=True)
