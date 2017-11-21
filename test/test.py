#!/usr/bin/env python
import unittest
import urllib2
import os
import threading
import subprocess
from subprocess import PIPE,STDOUT
from flask import Flask
app = Flask(__name__)
class FlaskTests(unittest.TestCase):
	def setUp(self):
		self.p = subprocess.Popen('python '+os.path.dirname(os.path.realpath(__file__))+"/../chat.py", shell = True, stdout = PIPE, stdin = PIPE, stderr = STDOUT)		
		self.app = app.test_client()
		self.app.testing = True
		for line in iter(self.p.stdout.readline, ''): 
			print line, # do something with the output here
		

	def test_home_status_code(self):
		result = urllib2.urlopen("http://localhost:5000/")
		self.assertEqual(result.code,200)
		
	def setDown(self):
		self.p.kill()
		
		
if __name__== '__main__':
	unittest.main()			
