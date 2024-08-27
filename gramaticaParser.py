# Generated from gramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,7,2,0,7,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,5,0,2,1,0,0,0,2,
        3,5,1,0,0,3,4,5,25,0,0,4,5,5,18,0,0,5,1,1,0,0,0,0
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PROGRAM'", "'INTEGER'", "'BOOLEAN'", 
                     "'BEGIN'", "'END'", "'WHILE'", "'DO'", "'READ'", "'VAR'", 
                     "'FALSE'", "'TRUE'", "'WRITE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'~'", "<INVALID>", "';'", "'.'", "':'", 
                     "','", "'('", "')'", "':='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'//'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "INTEGER", "BOOLEAN", "BEGIN", 
                      "END", "WHILE", "DO", "READ", "VAR", "FALSE", "TRUE", 
                      "WRITE", "OPAD", "OPMULT", "OPLOG", "OPNEG", "OPREL", 
                      "PVIG", "PONTO", "DPONTOS", "VIG", "ABPAR", "FPAR", 
                      "ATRIB", "ID", "CTE", "CADEIA", "COMENTARIOS_LINHA", 
                      "WS" ]

    RULE_programa = 0

    ruleNames =  [ "programa" ]

    EOF = Token.EOF
    PROGRAM=1
    INTEGER=2
    BOOLEAN=3
    BEGIN=4
    END=5
    WHILE=6
    DO=7
    READ=8
    VAR=9
    FALSE=10
    TRUE=11
    WRITE=12
    OPAD=13
    OPMULT=14
    OPLOG=15
    OPNEG=16
    OPREL=17
    PVIG=18
    PONTO=19
    DPONTOS=20
    VIG=21
    ABPAR=22
    FPAR=23
    ATRIB=24
    ID=25
    CTE=26
    CADEIA=27
    COMENTARIOS_LINHA=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(gramaticaParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def PVIG(self):
            return self.getToken(gramaticaParser.PVIG, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = gramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(gramaticaParser.PROGRAM)
            self.state = 3
            self.match(gramaticaParser.ID)
            self.state = 4
            self.match(gramaticaParser.PVIG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





