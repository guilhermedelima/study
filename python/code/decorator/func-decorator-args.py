#!/usr/bin/python2

from functools import wraps

# Decorator factory that receives args, creates a decorator and return it
# Must return a reference to some decorator ( class type or function )
def printer_decorator( filename ):

	# Decorator that will be returned and used to decorate user function
	def _printer_decorator( user_function ):

		# Wrapper function that will replace original one
		@wraps( user_function )
		def wrapper_function( *args, **kwargs ):
			print 'Trace decorator, log to', filename
			user_function( *args, **kwargs )

		return wrapper_function

	return _printer_decorator


# Sugar usage of decorator with args
# Equals to
# def F( ... ):
# 	...
# F = printer_decorator( 'stdin' )( F )
@printer_decorator( 'stdin' )
def user_func( name ):
	"""Some docstring from simple user function"""
	print 'User function called by', name


# Using new decorated function
user_func( name='Guilherme' )

print

# Show user function information __name__, __doc__
print 'user function info: {}'.format( ( user_func.__name__, user_func.__doc__ ) )
