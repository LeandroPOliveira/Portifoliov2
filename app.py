import os
from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__)
app.secret_key = 'lambreta'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['email'],
    "MAIL_PASSWORD": os.environ['senha']
}

app.config.update(mail_settings)

mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )

        msg = Message(
            subject=f'{formContato.nome} enviou uma mensagem',
            sender=app.config.get('MAIL_USERNAME'),
            recipients=['leandro_lpo2@hotmail.com', app.config.get('MAIL_USERNAME')],
            body=f'''
            
            {formContato.nome} com o email {formContato.email}, te enviou a seguinte mensagem:
            
            {formContato.mensagem}        
                    '''
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)