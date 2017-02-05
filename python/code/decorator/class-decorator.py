#!/usr/bin/python2

# Decorate some user function
# This decorator returns a new callable object (implements __call__)
class printer_decorator:
	def __init__( self, user_function ):
		self.f = user_function

	# Similar to C++ functor
	def __call__( self, *args, **kwargs ):
		self.f( *args, **kwargs )


# Sugar usage of decorator
# Equals to
# def print_user( ... ):
# 	...
# print_user = printer_decorator( print_user )
@printer_decorator
def print_user( name, *args ):
	print 'User :', name
	print '-------------------'
	for item in args:
		print item,
	print


# Using new decorated object as function
print_user( 'Guilherme', 'Unb', 'Brasilia' )
