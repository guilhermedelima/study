#!/usr/bin/python2

# Descritpor to add name to some instance
class name_descriptor( object ):

	def __init__( self ):
		pass

	def __get__( self, obj, klass ):
		# Called from class scope
		if not obj:
			return 'Default class name is: ' + klass.__name__

		# Add '_name' attr to obj when its not exist yet
		if not hasattr( obj, '_name' ):
			obj._name = 'Empty Name'

		return obj._name

	def __set__( self, obj, value ):
		# Only will be called from instance
		obj._name = value


# Client class which uses descriptor
class person( object ):
	
	name = name_descriptor()

	def __init__( self ):
		pass


if __name__ == '__main__':

	print person.name

	p = person()

	print p.name

	p.name = 'Guilherme'

	print p.name
