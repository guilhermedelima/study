#!/usr/bin/python

class A:
	def __init__( self, *args, **kwargs ):
		print( 'A __init__' )


class B( A ):
	def __init__( self, *args, **kwargs ):
		print( 'B __init__' )
		A.__init__( self, *args, **kwargs )


class C( A ):
	def __init__( self, *args, **kwargs ):
		print( 'C __init__' )
		A.__init__( self, *args, **kwargs )


class D( B, C ):
	def __init__( self, *args, **kwargs ):
		print( 'D __init__' )
		B.__init__( self, *args, **kwargs )
		C.__init__( self, *args, **kwargs )


d = D()
