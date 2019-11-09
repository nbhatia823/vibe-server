import os

class Config:
	HOST = 'ec2-174-129-253-140.compute-1.amazonaws.com'
	DATABASE = 'd9ku25a2bulpk2'
	USERNAME = 'bvxxebjsjrhphb'
	PASSWORD = '596f67861a11f2d606078c579ee8aa2f8c8855297aff08e3d0a3f60d1b0f8eed'
	PORT = '5432'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'