#!/usr/bin/env python
import unittest
import urllib2
import os
import threading
from flask import Flask
 
app = Flask(__name__)
class FlaskTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
       
    def test_home_status_code(self):
        result = urllib2.urlopen("http://localhost:5000/")
        self.assertEqual(result.code,200)
       
    def setDown(self):
        pass       
       
if __name__== '__main__':
    unittest.main()	
