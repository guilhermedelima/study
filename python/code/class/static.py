#!/usr/bin/python3

import abc, enum

class DocParser( metaclass=abc.ABCMeta ):
	class DocParserType( enum.Enum ):
		XML_PARSER = 1
		TXT_PARSER = 2

	def __init__( self, filename ):
		self.filename = filename
		self.data = None

	@abc.abstractmethod
	def parse( self ):
		raise NotImplementedError

	@abc.abstractmethod
	def get_content( self ):
		raise NotImplementedError

	@classmethod
	def GetInstance( cls, parser_type, *args, **kwargs ):
		if parser_type == cls.DocParserType.XML_PARSER:
			return XmlParser( *args, **kwargs )
		elif parser_type == cls.DocParserType.TXT_PARSER:
			return TxtParser( *args, **kwargs )
		else:
			return None


class XmlParser( DocParser ):
	def __init__( self, *args, **kwargs ):
		super().__init__( *args, **kwargs )

	def parse( self ):
		print( 'Parsing Xml file:', self.filename )
		self.data = 'FAKE XML CONTENT FROM: ' + self.filename

	def get_content( self ):
		return self.data


class TxtParser( DocParser ):
	def __init__( self, *args, **kwargs ):
		super().__init__( *args, **kwargs )

	def parse( self ):
		print( 'Parsing Txt File:', self.filename )
		self.data = 'FAKE TXT CONTENT FROM: ' + self.filename

	def get_content( self ):
		return self.data


if __name__ == '__main__':
	txt_parser = DocParser.GetInstance( parser_type = DocParser.DocParserType.XML_PARSER, filename = 'sample.txt' )
	xml_parser = DocParser.GetInstance( parser_type = DocParser.DocParserType.XML_PARSER, filename = 'sample.xml' )

	txt_parser.parse()
	print( txt_parser.get_content() )

	xml_parser.parse()
	print( xml_parser.get_content() )
