from os import environ

class Config:
#	SECRET_KEY = environ.get('SECRET_KEY') or 'hard to guess string'
	MAIL_SERVER = 'smtp.office365.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USE_SSL= False
	MAIL_USERNAME = environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
