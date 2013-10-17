'''
Created on Sep 22, 2013

@author: mayank
'''
from pyGoogleTrendsCsvDownloader import pyGoogleTrendsCsvDownloader
r = pyGoogleTrendsCsvDownloader('username', 'password')
r.get_csv(geo='US-NY',hl='en-US',q='obamacare,affordable')
    

