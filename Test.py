'''
Created on Sep 22, 2013

@author: mayank
'''
import csv
from pyGTrends import pyGTrends
connector = pyGTrends('username','password')
connector.download_report( 
                      ( "obama" )
                    , date = "2013-09"
                                , geo = "US-NY"
                                , scale = "1"
                 )

connector.writer( "search_query_name.csv" )
data = connector.csv( section='Main' ).split('\n')
csv_reader = csv.reader( data )
print "completed"

#trendsReport?hl=en-US&q=obama&date=today%207-d&cmpt=q&content=1
