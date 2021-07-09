from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/studies')
def studies():
    return render_template('studies.html')

@app.route('/message', methods=['POST'])
def message():
    if request.method == 'POST':

        ### lectura de datos del formulario ###
        nombre = str(request.form['nombre'])
        email = str(request.form['email'])
        mensaje = str(request.form['mensaje'])

        gmailaddress = "web.mail.sebpin@gmail.com"
        gmailpassword = "WebSite1!"
        mailto = "pinto7lopez7@gmail.com"
        msg = "My name is {}, my email is {} and my message is {}".format(nombre, email, mensaje)
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , msg)
        mailServer.quit()

        return render_template('message.html')
        


if __name__ == '__main__':
    app.run(debug=True)