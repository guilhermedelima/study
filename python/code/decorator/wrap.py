#!/usr/bin/python2

from functools import wraps

# Decorator which returns new decorated function
def printer_decorator( user_function ):

	# Decorate new function with original values (__name__, __doc__) from user function
	@wraps( user_function )
	def wrapper_function( *args, **kwargs ):
		print 'Decorated Function'
		user_function( *args, **kwargs )

	return wrapper_function


# Decorates some function
@printer_decorator
def show_user( name ):
	"""Simple docstring from a dumb function"""

	print 'User name is', name


# Just uses function
show_user( name='Guilherme' )

# Show user function parameters
print "user function name: %s\nuser function docs: %s" % ( show_user.__name__, show_user.__doc__ )
