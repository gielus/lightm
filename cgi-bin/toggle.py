#!/usr/bin/env python
print 'Content-Type: text/html\n\n'
import os
import cgi
import time
import lightm

arg = cgi.FieldStorage()

toggle = arg.getvalue("toggle")

if toggle == "BANK":
	print lightm.toggle( "BANK" )

elif toggle == "KAST":
	print lightm.toggle ( "KAST" )
	
elif toggle == "LED":
	print lightm.toggle ( "LED" )

elif toggle == "ALL":
	print lightm.toggle ( "LED" )
	print lightm.toggle ( "KAST" )
	print lightm.toggle ( "BANK" )
