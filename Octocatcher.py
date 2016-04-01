# -*- coding: utf-8 -*-
import json
import sys
import urllib
# import commands
import random

f = open( 'Octodex.json' )
Octodex = f.read()
f.close()

baseUrl = 'https://octodex.github.com/images/'
Octodex = json.loads( Octodex )

argv = sys.argv

if len( argv ) > 1 :
    if argv[1] == 'random' :
        random.shuffle( Octodex )
        # commands.getoutput( 'wget ' + baseUrl + Octodex[0] )
        urllib.urlretrieve( baseUrl + Octodex[0], Octodex[0] )
        print Octodex[0].split( '.' )[0] + ' captured !!'
    elif argv[1] == 'all' :
        for var in range( 0, len( Octodex ) ) :
            # commands.getoutput( 'wget ' + baseUrl + Octodex[var] )
            urllib.urlretrieve( baseUrl + Octodex[var], Octodex[var] )
        print 'all captured !!'
    else :
        print 'Huh ??'
else :
    print 'Huh ??'
