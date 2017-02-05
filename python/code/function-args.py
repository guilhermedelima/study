#!/usr/bin/python2

def f( name, *args, **kwargs ):
	print 'Name :', name
	
	for i, val in enumerate( args ):
		print 'Arg {0} : {1}'.format( i, val )

	for k, v in kwargs.items():
		print 'Kwargs {0} : {1}'.format( k, v )

	print


# Only required arg
f( name="Guilherme" )

# Required arg (keyword arg can be used only after *args) + *args
f( "Guilherme", 'Arg1', 'Arg2' )

# Required arg + *args + **kwargs (kwargs cant contain name in this case, because it appears before *args)
f( "Guilherme", 'Arg1', 'Arg2', foo="lorem", bar="ipsum" )

# Same as above but using packing
f( "Guilherme", *('Arg1', 'Arg2'), **{ "foo" : "lorem", "bar" : "ipsum" } )

# Required arg + **kwargs (Ignore *args)
f( foo="lorem", bar="ipsum", name="Guilherme" )

# Same as above but using packing
f( **{ "foo" : "lorem", "bar" : "ipsum", "name" : "Guilherme" } )
