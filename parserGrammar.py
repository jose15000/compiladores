# Generated from parserGrammar.g4 by ANTLR 4.13.2
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
        4,1,35,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,3,1,
        56,8,1,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,5,7,87,8,7,10,7,12,7,90,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,98,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,109,8,10,1,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,5,14,129,8,14,10,14,12,14,132,9,14,1,15,1,
        15,3,15,136,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,
        17,5,17,148,8,17,10,17,12,17,151,9,17,1,18,1,18,1,18,1,18,1,18,1,
        18,5,18,159,8,18,10,18,12,18,162,9,18,1,19,1,19,1,19,1,19,1,19,3,
        19,169,8,19,1,20,1,20,1,20,1,20,1,20,1,20,5,20,177,8,20,10,20,12,
        20,180,9,20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,188,8,21,10,21,12,
        21,191,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,203,8,22,1,22,0,4,34,36,40,42,23,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,0,1,2,0,2,3,30,30,203,0,46,1,
        0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,65,1,0,0,0,8,69,1,0,0,0,10,77,
        1,0,0,0,12,79,1,0,0,0,14,83,1,0,0,0,16,97,1,0,0,0,18,99,1,0,0,0,
        20,108,1,0,0,0,22,110,1,0,0,0,24,115,1,0,0,0,26,120,1,0,0,0,28,125,
        1,0,0,0,30,135,1,0,0,0,32,137,1,0,0,0,34,141,1,0,0,0,36,152,1,0,
        0,0,38,168,1,0,0,0,40,170,1,0,0,0,42,181,1,0,0,0,44,202,1,0,0,0,
        46,47,5,1,0,0,47,48,5,25,0,0,48,49,5,18,0,0,49,50,3,2,1,0,50,51,
        3,12,6,0,51,52,5,19,0,0,52,1,1,0,0,0,53,54,5,9,0,0,54,56,3,4,2,0,
        55,53,1,0,0,0,55,56,1,0,0,0,56,3,1,0,0,0,57,62,3,6,3,0,58,59,5,18,
        0,0,59,61,3,6,3,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,
        1,0,0,0,63,5,1,0,0,0,64,62,1,0,0,0,65,66,3,8,4,0,66,67,5,20,0,0,
        67,68,3,10,5,0,68,7,1,0,0,0,69,74,5,25,0,0,70,71,5,21,0,0,71,73,
        5,25,0,0,72,70,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,
        75,9,1,0,0,0,76,74,1,0,0,0,77,78,7,0,0,0,78,11,1,0,0,0,79,80,5,4,
        0,0,80,81,3,14,7,0,81,82,5,5,0,0,82,13,1,0,0,0,83,88,3,16,8,0,84,
        85,5,18,0,0,85,87,3,16,8,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,
        0,0,88,89,1,0,0,0,89,15,1,0,0,0,90,88,1,0,0,0,91,98,3,18,9,0,92,
        98,3,22,11,0,93,98,3,24,12,0,94,98,3,26,13,0,95,98,3,32,16,0,96,
        98,3,12,6,0,97,91,1,0,0,0,97,92,1,0,0,0,97,93,1,0,0,0,97,94,1,0,
        0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,17,1,0,0,0,99,100,5,31,0,0,100,
        101,3,34,17,0,101,102,5,32,0,0,102,103,3,16,8,0,103,104,3,20,10,
        0,104,19,1,0,0,0,105,106,5,33,0,0,106,109,3,16,8,0,107,109,1,0,0,
        0,108,105,1,0,0,0,108,107,1,0,0,0,109,21,1,0,0,0,110,111,5,6,0,0,
        111,112,3,34,17,0,112,113,5,7,0,0,113,114,3,16,8,0,114,23,1,0,0,
        0,115,116,5,8,0,0,116,117,5,22,0,0,117,118,3,8,4,0,118,119,5,23,
        0,0,119,25,1,0,0,0,120,121,5,12,0,0,121,122,5,22,0,0,122,123,3,28,
        14,0,123,124,5,23,0,0,124,27,1,0,0,0,125,130,3,30,15,0,126,127,5,
        21,0,0,127,129,3,30,15,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,29,1,0,0,0,132,130,1,0,0,0,133,136,3,
        34,17,0,134,136,5,27,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,31,
        1,0,0,0,137,138,5,25,0,0,138,139,5,24,0,0,139,140,3,34,17,0,140,
        33,1,0,0,0,141,142,6,17,-1,0,142,143,3,36,18,0,143,149,1,0,0,0,144,
        145,10,2,0,0,145,146,5,34,0,0,146,148,3,36,18,0,147,144,1,0,0,0,
        148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,35,1,0,0,0,151,
        149,1,0,0,0,152,153,6,18,-1,0,153,154,3,38,19,0,154,160,1,0,0,0,
        155,156,10,2,0,0,156,157,5,35,0,0,157,159,3,38,19,0,158,155,1,0,
        0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,37,1,0,0,
        0,162,160,1,0,0,0,163,164,3,40,20,0,164,165,5,17,0,0,165,166,3,40,
        20,0,166,169,1,0,0,0,167,169,3,40,20,0,168,163,1,0,0,0,168,167,1,
        0,0,0,169,39,1,0,0,0,170,171,6,20,-1,0,171,172,3,42,21,0,172,178,
        1,0,0,0,173,174,10,2,0,0,174,175,5,13,0,0,175,177,3,42,21,0,176,
        173,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        41,1,0,0,0,180,178,1,0,0,0,181,182,6,21,-1,0,182,183,3,44,22,0,183,
        189,1,0,0,0,184,185,10,2,0,0,185,186,5,14,0,0,186,188,3,44,22,0,
        187,184,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,
        190,43,1,0,0,0,191,189,1,0,0,0,192,193,5,16,0,0,193,203,3,44,22,
        0,194,195,5,22,0,0,195,196,3,34,17,0,196,197,5,23,0,0,197,203,1,
        0,0,0,198,203,5,25,0,0,199,203,5,26,0,0,200,203,5,11,0,0,201,203,
        5,10,0,0,202,192,1,0,0,0,202,194,1,0,0,0,202,198,1,0,0,0,202,199,
        1,0,0,0,202,200,1,0,0,0,202,201,1,0,0,0,203,45,1,0,0,0,14,55,62,
        74,88,97,108,130,135,149,160,168,178,189,202
    ]

class parserGrammar ( Parser ):

    grammarFileName = "parserGrammar.g4"

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
                      "WS", "STRING", "IF", "THEN", "ELSE", "OR", "AND" ]

    RULE_prog = 0
    RULE_decls = 1
    RULE_listDecl = 2
    RULE_declTip = 3
    RULE_listId = 4
    RULE_tip = 5
    RULE_cmdComp = 6
    RULE_listCmd = 7
    RULE_cmd = 8
    RULE_cmdIf = 9
    RULE_elseOpt = 10
    RULE_cmdWhile = 11
    RULE_cmdRead = 12
    RULE_cmdWrite = 13
    RULE_listW = 14
    RULE_elemW = 15
    RULE_cmdAtrib = 16
    RULE_expr = 17
    RULE_expr1 = 18
    RULE_expr2 = 19
    RULE_expr3 = 20
    RULE_expr4 = 21
    RULE_expr5 = 22

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "elseOpt", "cmdWhile", 
                   "cmdRead", "cmdWrite", "listW", "elemW", "cmdAtrib", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5" ]

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
    STRING=30
    IF=31
    THEN=32
    ELSE=33
    OR=34
    AND=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(parserGrammar.PROGRAM, 0)

        def ID(self):
            return self.getToken(parserGrammar.ID, 0)

        def PVIG(self):
            return self.getToken(parserGrammar.PVIG, 0)

        def decls(self):
            return self.getTypedRuleContext(parserGrammar.DeclsContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(parserGrammar.CmdCompContext,0)


        def PONTO(self):
            return self.getToken(parserGrammar.PONTO, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = parserGrammar.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(parserGrammar.PROGRAM)
            self.state = 47
            self.match(parserGrammar.ID)
            self.state = 48
            self.match(parserGrammar.PVIG)
            self.state = 49
            self.decls()
            self.state = 50
            self.cmdComp()
            self.state = 51
            self.match(parserGrammar.PONTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(parserGrammar.VAR, 0)

        def listDecl(self):
            return self.getTypedRuleContext(parserGrammar.ListDeclContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = parserGrammar.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 53
                self.match(parserGrammar.VAR)
                self.state = 54
                self.listDecl()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declTip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.DeclTipContext)
            else:
                return self.getTypedRuleContext(parserGrammar.DeclTipContext,i)


        def PVIG(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.PVIG)
            else:
                return self.getToken(parserGrammar.PVIG, i)

        def getRuleIndex(self):
            return parserGrammar.RULE_listDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListDecl" ):
                listener.enterListDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListDecl" ):
                listener.exitListDecl(self)




    def listDecl(self):

        localctx = parserGrammar.ListDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.declTip()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 58
                self.match(parserGrammar.PVIG)
                self.state = 59
                self.declTip()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclTipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listId(self):
            return self.getTypedRuleContext(parserGrammar.ListIdContext,0)


        def DPONTOS(self):
            return self.getToken(parserGrammar.DPONTOS, 0)

        def tip(self):
            return self.getTypedRuleContext(parserGrammar.TipContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_declTip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclTip" ):
                listener.enterDeclTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclTip" ):
                listener.exitDeclTip(self)




    def declTip(self):

        localctx = parserGrammar.DeclTipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declTip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.listId()
            self.state = 66
            self.match(parserGrammar.DPONTOS)
            self.state = 67
            self.tip()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.ID)
            else:
                return self.getToken(parserGrammar.ID, i)

        def VIG(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.VIG)
            else:
                return self.getToken(parserGrammar.VIG, i)

        def getRuleIndex(self):
            return parserGrammar.RULE_listId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListId" ):
                listener.enterListId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListId" ):
                listener.exitListId(self)




    def listId(self):

        localctx = parserGrammar.ListIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(parserGrammar.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 70
                self.match(parserGrammar.VIG)
                self.state = 71
                self.match(parserGrammar.ID)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(parserGrammar.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(parserGrammar.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(parserGrammar.STRING, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_tip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTip" ):
                listener.enterTip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTip" ):
                listener.exitTip(self)




    def tip(self):

        localctx = parserGrammar.TipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tip)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073741836) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdCompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(parserGrammar.BEGIN, 0)

        def listCmd(self):
            return self.getTypedRuleContext(parserGrammar.ListCmdContext,0)


        def END(self):
            return self.getToken(parserGrammar.END, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_cmdComp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdComp" ):
                listener.enterCmdComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdComp" ):
                listener.exitCmdComp(self)




    def cmdComp(self):

        localctx = parserGrammar.CmdCompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdComp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(parserGrammar.BEGIN)
            self.state = 80
            self.listCmd()
            self.state = 81
            self.match(parserGrammar.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.CmdContext)
            else:
                return self.getTypedRuleContext(parserGrammar.CmdContext,i)


        def PVIG(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.PVIG)
            else:
                return self.getToken(parserGrammar.PVIG, i)

        def getRuleIndex(self):
            return parserGrammar.RULE_listCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListCmd" ):
                listener.enterListCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListCmd" ):
                listener.exitListCmd(self)




    def listCmd(self):

        localctx = parserGrammar.ListCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.cmd()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 84
                self.match(parserGrammar.PVIG)
                self.state = 85
                self.cmd()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdIf(self):
            return self.getTypedRuleContext(parserGrammar.CmdIfContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(parserGrammar.CmdWhileContext,0)


        def cmdRead(self):
            return self.getTypedRuleContext(parserGrammar.CmdReadContext,0)


        def cmdWrite(self):
            return self.getTypedRuleContext(parserGrammar.CmdWriteContext,0)


        def cmdAtrib(self):
            return self.getTypedRuleContext(parserGrammar.CmdAtribContext,0)


        def cmdComp(self):
            return self.getTypedRuleContext(parserGrammar.CmdCompContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = parserGrammar.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmd)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.cmdIf()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.cmdWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.cmdRead()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.cmdWrite()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.cmdAtrib()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.cmdComp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(parserGrammar.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def THEN(self):
            return self.getToken(parserGrammar.THEN, 0)

        def cmd(self):
            return self.getTypedRuleContext(parserGrammar.CmdContext,0)


        def elseOpt(self):
            return self.getTypedRuleContext(parserGrammar.ElseOptContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_cmdIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdIf" ):
                listener.enterCmdIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdIf" ):
                listener.exitCmdIf(self)




    def cmdIf(self):

        localctx = parserGrammar.CmdIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(parserGrammar.IF)
            self.state = 100
            self.expr(0)
            self.state = 101
            self.match(parserGrammar.THEN)
            self.state = 102
            self.cmd()
            self.state = 103
            self.elseOpt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(parserGrammar.ELSE, 0)

        def cmd(self):
            return self.getTypedRuleContext(parserGrammar.CmdContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_elseOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseOpt" ):
                listener.enterElseOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseOpt" ):
                listener.exitElseOpt(self)




    def elseOpt(self):

        localctx = parserGrammar.ElseOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elseOpt)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(parserGrammar.ELSE)
                self.state = 106
                self.cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(parserGrammar.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def DO(self):
            return self.getToken(parserGrammar.DO, 0)

        def cmd(self):
            return self.getTypedRuleContext(parserGrammar.CmdContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)




    def cmdWhile(self):

        localctx = parserGrammar.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(parserGrammar.WHILE)
            self.state = 111
            self.expr(0)
            self.state = 112
            self.match(parserGrammar.DO)
            self.state = 113
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(parserGrammar.READ, 0)

        def ABPAR(self):
            return self.getToken(parserGrammar.ABPAR, 0)

        def listId(self):
            return self.getTypedRuleContext(parserGrammar.ListIdContext,0)


        def FPAR(self):
            return self.getToken(parserGrammar.FPAR, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_cmdRead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRead" ):
                listener.enterCmdRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRead" ):
                listener.exitCmdRead(self)




    def cmdRead(self):

        localctx = parserGrammar.CmdReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(parserGrammar.READ)
            self.state = 116
            self.match(parserGrammar.ABPAR)
            self.state = 117
            self.listId()
            self.state = 118
            self.match(parserGrammar.FPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(parserGrammar.WRITE, 0)

        def ABPAR(self):
            return self.getToken(parserGrammar.ABPAR, 0)

        def listW(self):
            return self.getTypedRuleContext(parserGrammar.ListWContext,0)


        def FPAR(self):
            return self.getToken(parserGrammar.FPAR, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_cmdWrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWrite" ):
                listener.enterCmdWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWrite" ):
                listener.exitCmdWrite(self)




    def cmdWrite(self):

        localctx = parserGrammar.CmdWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(parserGrammar.WRITE)
            self.state = 121
            self.match(parserGrammar.ABPAR)
            self.state = 122
            self.listW()
            self.state = 123
            self.match(parserGrammar.FPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemW(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.ElemWContext)
            else:
                return self.getTypedRuleContext(parserGrammar.ElemWContext,i)


        def VIG(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.VIG)
            else:
                return self.getToken(parserGrammar.VIG, i)

        def getRuleIndex(self):
            return parserGrammar.RULE_listW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListW" ):
                listener.enterListW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListW" ):
                listener.exitListW(self)




    def listW(self):

        localctx = parserGrammar.ListWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listW)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.elemW()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 126
                self.match(parserGrammar.VIG)
                self.state = 127
                self.elemW()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def CADEIA(self):
            return self.getToken(parserGrammar.CADEIA, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_elemW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemW" ):
                listener.enterElemW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemW" ):
                listener.exitElemW(self)




    def elemW(self):

        localctx = parserGrammar.ElemWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elemW)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 16, 22, 25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.expr(0)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(parserGrammar.CADEIA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdAtribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(parserGrammar.ID, 0)

        def ATRIB(self):
            return self.getToken(parserGrammar.ATRIB, 0)

        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_cmdAtrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAtrib" ):
                listener.enterCmdAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAtrib" ):
                listener.exitCmdAtrib(self)




    def cmdAtrib(self):

        localctx = parserGrammar.CmdAtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(parserGrammar.ID)
            self.state = 138
            self.match(parserGrammar.ATRIB)
            self.state = 139
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(parserGrammar.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def OR(self):
            return self.getToken(parserGrammar.OR, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = parserGrammar.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = parserGrammar.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 144
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 145
                    self.match(parserGrammar.OR)
                    self.state = 146
                    self.expr1(0) 
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(parserGrammar.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(parserGrammar.Expr1Context,0)


        def AND(self):
            return self.getToken(parserGrammar.AND, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = parserGrammar.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = parserGrammar.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 155
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 156
                    self.match(parserGrammar.AND)
                    self.state = 157
                    self.expr2() 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.Expr3Context)
            else:
                return self.getTypedRuleContext(parserGrammar.Expr3Context,i)


        def OPREL(self):
            return self.getToken(parserGrammar.OPREL, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_expr2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)




    def expr2(self):

        localctx = parserGrammar.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr2)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.expr3(0)
                self.state = 164
                self.match(parserGrammar.OPREL)
                self.state = 165
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.expr3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(parserGrammar.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(parserGrammar.Expr3Context,0)


        def OPAD(self):
            return self.getToken(parserGrammar.OPAD, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_expr3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr3" ):
                listener.enterExpr3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr3" ):
                listener.exitExpr3(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = parserGrammar.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = parserGrammar.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    self.match(parserGrammar.OPAD)
                    self.state = 175
                    self.expr4(0) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(parserGrammar.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(parserGrammar.Expr4Context,0)


        def OPMULT(self):
            return self.getToken(parserGrammar.OPMULT, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_expr4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr4" ):
                listener.enterExpr4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr4" ):
                listener.exitExpr4(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = parserGrammar.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = parserGrammar.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    self.match(parserGrammar.OPMULT)
                    self.state = 186
                    self.expr5() 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPNEG(self):
            return self.getToken(parserGrammar.OPNEG, 0)

        def expr5(self):
            return self.getTypedRuleContext(parserGrammar.Expr5Context,0)


        def ABPAR(self):
            return self.getToken(parserGrammar.ABPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def FPAR(self):
            return self.getToken(parserGrammar.FPAR, 0)

        def ID(self):
            return self.getToken(parserGrammar.ID, 0)

        def CTE(self):
            return self.getToken(parserGrammar.CTE, 0)

        def TRUE(self):
            return self.getToken(parserGrammar.TRUE, 0)

        def FALSE(self):
            return self.getToken(parserGrammar.FALSE, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_expr5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr5" ):
                listener.enterExpr5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr5" ):
                listener.exitExpr5(self)




    def expr5(self):

        localctx = parserGrammar.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr5)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(parserGrammar.OPNEG)
                self.state = 193
                self.expr5()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(parserGrammar.ABPAR)
                self.state = 195
                self.expr(0)
                self.state = 196
                self.match(parserGrammar.FPAR)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.match(parserGrammar.ID)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.match(parserGrammar.CTE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 200
                self.match(parserGrammar.TRUE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.match(parserGrammar.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        self._predicates[18] = self.expr1_sempred
        self._predicates[20] = self.expr3_sempred
        self._predicates[21] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




