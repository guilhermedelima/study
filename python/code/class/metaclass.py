#!/usr/bin/python

class mymeta( type ):
	@classmethod
	def __prepare__( metaclass, name, bases, **kwargs ):
		print( 'mymeta.__prepare__' )
		return {}
	
	def __new__( metaclass, name, bases, namespace, **kwargs ):
		print( 'mymeta.__new__' )
		return super().__new__( metaclass, name, bases, namespace, **kwargs )

	def __init__( metaclass, name, bases, namespace, **kwargs ):
		print( 'mymeta.__init__' )
		super().__init__( name, bases, namespace, **kwargs )

	def __call__( classobject, *args, **kwargs ):
		print( "mymeta.__call__" )

		obj = super().__call__( *args, **kwargs )
		obj.hide = 'Hide parameter created by metaclass'

		return obj


print( '--- Before class definition ---' )

class base( metaclass=mymeta ):
	print( 'Class body is been executed from exec()' )

	def __new__( klass, *args, **kwargs ):
		print( 'base.__new__' )
		return super().__new__( klass )

	def __init__( self, x, y ):
		print( 'base.__init__' )
		self.x = x
		self.y = y

print( '--- After class definition ---' )

print()

print( '--- Before instance object ---' )

b = base( 2, 3 )

print( '--- After instance object ---' )

print()

print( 'Object dict = ', b.__dict__ )
