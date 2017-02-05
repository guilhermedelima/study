#!/usr/bin/python2

# Decorate some user function
# This decorator returns a new function
def printer_decorator( user_function ):

	# Create a new functions and return it
	# Use *args and **kwargs to pass anything to user_function
	def wrapper( *args, **kwargs ):
		print 'Decorator Function'
		user_function( *args, **kwargs )

	return wrapper;


# Sugar usage of decorator
# Equals to:
# def print_user( ... ):
# 	...
# print_user = printer_decorator( print_user )
@printer_decorator
def print_user( name, end, **kwargs ):
	print 'User :', name
	print 'End  :', end
	print '----------------------'
	for k, v in kwargs.items():
		print k, ":", v
	print


# Using new decorated function
print_user( name="Guilherme", end="Aguas Claras", CPF="036.671.101-62", RG="2842618-MG" )
