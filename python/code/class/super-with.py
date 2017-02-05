#!/usr/bin/python

class A:
	def __init__( self, name ):
		print( 'A __init__' )
		self.name = name


class B( A ):
	def __init__( self, age, *args, **kwargs ):
		print( 'B __init__' )

		super().__init__( *args, **kwargs )
		self.age = age


class C( A ):
	def __init__( self, end, *args, **kwargs ):
		print( 'C __init__' )

		super().__init__( *args, **kwargs )
		self.end = end


class D( B, C ):
	def __init__( self, ddd, *args, **kwargs ):
		print( 'D __init__' )

		super().__init__( *args, **kwargs )
		self.ddd = ddd


B( name='Guilherme', age=21 )

print()

C( name='Guilherme', end="Águas Claras" )

print()

D( name = 'Guilherme', age=21, end="Aguas Claras", ddd='061' )

print()

o = D( "061", name = 'Guilherme', age=21, end="Aguas Claras" )

print( o.__dict__ )
