from flask import Flask, render_template,request
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)

app.config.from_object('config.Config')
mail = Mail(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/email', methods = ['POST'])
def email():
	name = str(request.form['name'])	
	email = str(request.form['email'])	
	phone = str(request.form['phone'])	
	messageForm = str(request.form['message'])	

	message_text = '''Voce recebeu uma nova mensagem por meio do formulario
					  \ncontido em seu portfólio.
					  \n\nEstes são os detalhes da mensagem:
					  \n\nName: '''+ name+'''\n\nEmail: '''+ email+'''\n\nPhone: '''+ phone+'''
					  \n\nMessage:\n'''+ messageForm+''' '''

	message = Message('new_portifolio_message', 
					  sender = 'paulohenrique.luz@hotmail.com',
					  recipients = ['paulohenrique.luz@hotmail.com'])
	message.body = message_text

	mail.send(message)
	
	return '', 200	

if __name__ == '__main__':
	app.run(debug = True)