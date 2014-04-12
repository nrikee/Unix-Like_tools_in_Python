import sys
import os

if len ( sys.argv ) == 4:
	args = sys.argv [ 1: ]
else:
	print 'Usage: python rename.py [path]'
	sys.exit ( 0 )

path = '.'
filenames = os.listdir ( str ( path ) )

# Check some things
text = open ( args [ 0 ], 'r' ).read ( )
original_names = text.split ( '\n' )

text = open ( args [ 1 ], 'r' ).read ( )
new_names = text.split ( '\n' )

all_names = [ ]
all_names.extend ( original_names )
all_names.extend ( new_names )
if len ( all_names ) != len ( set ( all_names ) ):
	print 'Something is incorrect. Maybe duplicated names.'
	sys.exit ( 0 )

for pair in zip ( original_names, new_names ):
	if pair [ 0 ] in filenames:
		os.rename ( pair [ 0 ], pair [ 1 ] )
