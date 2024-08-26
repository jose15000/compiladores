# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass



del gramaticaParser