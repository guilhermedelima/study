#!/usr/bin/python2

class person( object ):
	def __init__( self, name ):
		self._name = name

	# Create name property with getter only (docstring of getter can be used as property docstring)
	# Equals to:
	# def get_name( self ):
	# 	...
	# name = property( get_name )
	@property
	def name( self ):
		"""Property attribute which represents person's name"""
		print 'get name was called'
		return self._name

	# Call property.setter decorator method, which returns original name property with new setter method
	# Equals to
	# def set_name( self, name ):
	# 	...
	# name = name.setter( set_name )
	@name.setter
	def name( self, name ):
		print 'set name was called'
		self._name = name

	# Call property.deleter decorator method, which returns original name property with new deleter method
	# Equals to
	# def delete_name( self ):
	# 	...
	# name = name.deleter( delete_name )
	@name.deleter
	def name( self ):
		# Does not delete name, just empty it
		print 'delete name was called'
		self._name = 'Empty Name'


if __name__ == '__main__':
	p = person('Guilherme')

	print p.name

	p.name = 'Joao'

	print p.name

	del p.name

	print p.name

	# Docstring of 'name'
	print person.__dict__[ 'name' ].__doc__
