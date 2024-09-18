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
        4,1,33,164,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,3,0,45,8,0,1,0,1,0,1,0,1,1,1,1,4,1,52,8,1,11,1,12,1,
        53,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,66,8,4,10,4,12,4,
        69,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,80,8,7,10,7,12,7,
        83,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,91,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,99,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,
        15,3,15,125,8,15,1,16,1,16,1,16,5,16,130,8,16,10,16,12,16,133,9,
        16,1,17,1,17,1,17,5,17,138,8,17,10,17,12,17,141,9,17,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,154,8,18,1,19,1,
        19,1,19,5,19,159,8,19,10,19,12,19,162,9,19,1,19,0,0,20,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,1,1,0,2,4,163,0,40,
        1,0,0,0,2,49,1,0,0,0,4,55,1,0,0,0,6,58,1,0,0,0,8,62,1,0,0,0,10,70,
        1,0,0,0,12,72,1,0,0,0,14,76,1,0,0,0,16,90,1,0,0,0,18,92,1,0,0,0,
        20,100,1,0,0,0,22,105,1,0,0,0,24,110,1,0,0,0,26,115,1,0,0,0,28,119,
        1,0,0,0,30,121,1,0,0,0,32,126,1,0,0,0,34,134,1,0,0,0,36,153,1,0,
        0,0,38,155,1,0,0,0,40,41,5,1,0,0,41,42,5,29,0,0,42,44,5,22,0,0,43,
        45,3,2,1,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,3,12,
        6,0,47,48,5,23,0,0,48,1,1,0,0,0,49,51,5,10,0,0,50,52,3,4,2,0,51,
        50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,3,1,0,0,
        0,55,56,3,6,3,0,56,57,5,22,0,0,57,5,1,0,0,0,58,59,3,8,4,0,59,60,
        5,24,0,0,60,61,3,10,5,0,61,7,1,0,0,0,62,67,5,29,0,0,63,64,5,25,0,
        0,64,66,5,29,0,0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,9,1,0,0,0,69,67,1,0,0,0,70,71,7,0,0,0,71,11,1,0,0,0,72,
        73,5,5,0,0,73,74,3,14,7,0,74,75,5,6,0,0,75,13,1,0,0,0,76,81,3,16,
        8,0,77,78,5,22,0,0,78,80,3,16,8,0,79,77,1,0,0,0,80,83,1,0,0,0,81,
        79,1,0,0,0,81,82,1,0,0,0,82,15,1,0,0,0,83,81,1,0,0,0,84,91,3,18,
        9,0,85,91,3,20,10,0,86,91,3,22,11,0,87,91,3,24,12,0,88,91,3,26,13,
        0,89,91,3,12,6,0,90,84,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,90,87,
        1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,17,1,0,0,0,92,93,5,14,0,0,
        93,94,3,28,14,0,94,95,5,15,0,0,95,98,3,16,8,0,96,97,5,16,0,0,97,
        99,3,16,8,0,98,96,1,0,0,0,98,99,1,0,0,0,99,19,1,0,0,0,100,101,5,
        7,0,0,101,102,3,28,14,0,102,103,5,8,0,0,103,104,3,16,8,0,104,21,
        1,0,0,0,105,106,5,9,0,0,106,107,5,26,0,0,107,108,3,8,4,0,108,109,
        5,27,0,0,109,23,1,0,0,0,110,111,5,13,0,0,111,112,5,26,0,0,112,113,
        3,38,19,0,113,114,5,27,0,0,114,25,1,0,0,0,115,116,5,29,0,0,116,117,
        5,28,0,0,117,118,3,28,14,0,118,27,1,0,0,0,119,120,3,30,15,0,120,
        29,1,0,0,0,121,124,3,32,16,0,122,123,5,21,0,0,123,125,3,32,16,0,
        124,122,1,0,0,0,124,125,1,0,0,0,125,31,1,0,0,0,126,131,3,34,17,0,
        127,128,5,17,0,0,128,130,3,34,17,0,129,127,1,0,0,0,130,133,1,0,0,
        0,131,129,1,0,0,0,131,132,1,0,0,0,132,33,1,0,0,0,133,131,1,0,0,0,
        134,139,3,36,18,0,135,136,5,18,0,0,136,138,3,36,18,0,137,135,1,0,
        0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,35,1,0,0,
        0,141,139,1,0,0,0,142,143,5,20,0,0,143,154,3,36,18,0,144,145,5,26,
        0,0,145,146,3,28,14,0,146,147,5,27,0,0,147,154,1,0,0,0,148,154,5,
        29,0,0,149,154,5,30,0,0,150,154,5,12,0,0,151,154,5,11,0,0,152,154,
        5,31,0,0,153,142,1,0,0,0,153,144,1,0,0,0,153,148,1,0,0,0,153,149,
        1,0,0,0,153,150,1,0,0,0,153,151,1,0,0,0,153,152,1,0,0,0,154,37,1,
        0,0,0,155,160,3,28,14,0,156,157,5,25,0,0,157,159,3,28,14,0,158,156,
        1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,39,1,
        0,0,0,162,160,1,0,0,0,11,44,53,67,81,90,98,124,131,139,153,160
    ]

class parserGrammar ( Parser ):

    grammarFileName = "parserGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PROGRAM'", "'INTEGER'", "'BOOLEAN'", 
                     "'STRING'", "'BEGIN'", "'END'", "'WHILE'", "'DO'", 
                     "'READ'", "'VAR'", "'FALSE'", "'TRUE'", "'WRITE'", 
                     "'IF'", "'THEN'", "'ELSE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'", "'.'", 
                     "':'", "','", "'('", "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "INTEGER", "BOOLEAN", "STRING", 
                      "BEGIN", "END", "WHILE", "DO", "READ", "VAR", "FALSE", 
                      "TRUE", "WRITE", "IF", "THEN", "ELSE", "OPAD", "OPMULT", 
                      "OPLOG", "OPNEG", "OPREL", "PVIG", "PONTO", "DPONTOS", 
                      "VIG", "ABPAR", "FPAR", "ATRIB", "IDENTIFIER", "CTE", 
                      "STRING_LITERAL", "COMMENT", "WS" ]

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
    RULE_cmdWhile = 10
    RULE_cmdRead = 11
    RULE_cmdWrite = 12
    RULE_cmdAtrib = 13
    RULE_expr = 14
    RULE_relExpr = 15
    RULE_addExpr = 16
    RULE_multExpr = 17
    RULE_unaryExpr = 18
    RULE_listW = 19

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "cmdWhile", "cmdRead", 
                   "cmdWrite", "cmdAtrib", "expr", "relExpr", "addExpr", 
                   "multExpr", "unaryExpr", "listW" ]

    EOF = Token.EOF
    PROGRAM=1
    INTEGER=2
    BOOLEAN=3
    STRING=4
    BEGIN=5
    END=6
    WHILE=7
    DO=8
    READ=9
    VAR=10
    FALSE=11
    TRUE=12
    WRITE=13
    IF=14
    THEN=15
    ELSE=16
    OPAD=17
    OPMULT=18
    OPLOG=19
    OPNEG=20
    OPREL=21
    PVIG=22
    PONTO=23
    DPONTOS=24
    VIG=25
    ABPAR=26
    FPAR=27
    ATRIB=28
    IDENTIFIER=29
    CTE=30
    STRING_LITERAL=31
    COMMENT=32
    WS=33

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

        def IDENTIFIER(self):
            return self.getToken(parserGrammar.IDENTIFIER, 0)

        def PVIG(self):
            return self.getToken(parserGrammar.PVIG, 0)

        def cmdComp(self):
            return self.getTypedRuleContext(parserGrammar.CmdCompContext,0)


        def PONTO(self):
            return self.getToken(parserGrammar.PONTO, 0)

        def decls(self):
            return self.getTypedRuleContext(parserGrammar.DeclsContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(parserGrammar.PROGRAM)
            self.state = 41
            self.match(parserGrammar.IDENTIFIER)
            self.state = 42
            self.match(parserGrammar.PVIG)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 43
                self.decls()


            self.state = 46
            self.cmdComp()
            self.state = 47
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

        def listDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.ListDeclContext)
            else:
                return self.getTypedRuleContext(parserGrammar.ListDeclContext,i)


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
            self.state = 49
            self.match(parserGrammar.VAR)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.listDecl()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==29):
                    break

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

        def declTip(self):
            return self.getTypedRuleContext(parserGrammar.DeclTipContext,0)


        def PVIG(self):
            return self.getToken(parserGrammar.PVIG, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.declTip()
            self.state = 56
            self.match(parserGrammar.PVIG)
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
            self.state = 58
            self.listId()
            self.state = 59
            self.match(parserGrammar.DPONTOS)
            self.state = 60
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.IDENTIFIER)
            else:
                return self.getToken(parserGrammar.IDENTIFIER, i)

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
            self.state = 62
            self.match(parserGrammar.IDENTIFIER)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 63
                self.match(parserGrammar.VIG)
                self.state = 64
                self.match(parserGrammar.IDENTIFIER)
                self.state = 69
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
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
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
            self.state = 72
            self.match(parserGrammar.BEGIN)
            self.state = 73
            self.listCmd()
            self.state = 74
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
            self.state = 76
            self.cmd()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 77
                self.match(parserGrammar.PVIG)
                self.state = 78
                self.cmd()
                self.state = 83
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.cmdIf()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.cmdWhile()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.cmdRead()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.cmdWrite()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.cmdAtrib()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
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

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.CmdContext)
            else:
                return self.getTypedRuleContext(parserGrammar.CmdContext,i)


        def ELSE(self):
            return self.getToken(parserGrammar.ELSE, 0)

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
            self.state = 92
            self.match(parserGrammar.IF)
            self.state = 93
            self.expr()
            self.state = 94
            self.match(parserGrammar.THEN)
            self.state = 95
            self.cmd()
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 96
                self.match(parserGrammar.ELSE)
                self.state = 97
                self.cmd()


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
        self.enterRule(localctx, 20, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(parserGrammar.WHILE)
            self.state = 101
            self.expr()
            self.state = 102
            self.match(parserGrammar.DO)
            self.state = 103
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
        self.enterRule(localctx, 22, self.RULE_cmdRead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(parserGrammar.READ)
            self.state = 106
            self.match(parserGrammar.ABPAR)
            self.state = 107
            self.listId()
            self.state = 108
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
        self.enterRule(localctx, 24, self.RULE_cmdWrite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(parserGrammar.WRITE)
            self.state = 111
            self.match(parserGrammar.ABPAR)
            self.state = 112
            self.listW()
            self.state = 113
            self.match(parserGrammar.FPAR)
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

        def IDENTIFIER(self):
            return self.getToken(parserGrammar.IDENTIFIER, 0)

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
        self.enterRule(localctx, 26, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(parserGrammar.IDENTIFIER)
            self.state = 116
            self.match(parserGrammar.ATRIB)
            self.state = 117
            self.expr()
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

        def relExpr(self):
            return self.getTypedRuleContext(parserGrammar.RelExprContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = parserGrammar.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.relExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.AddExprContext)
            else:
                return self.getTypedRuleContext(parserGrammar.AddExprContext,i)


        def OPREL(self):
            return self.getToken(parserGrammar.OPREL, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_relExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)




    def relExpr(self):

        localctx = parserGrammar.RelExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.addExpr()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 122
                self.match(parserGrammar.OPREL)
                self.state = 123
                self.addExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.MultExprContext)
            else:
                return self.getTypedRuleContext(parserGrammar.MultExprContext,i)


        def OPAD(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.OPAD)
            else:
                return self.getToken(parserGrammar.OPAD, i)

        def getRuleIndex(self):
            return parserGrammar.RULE_addExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)




    def addExpr(self):

        localctx = parserGrammar.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.multExpr()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 127
                self.match(parserGrammar.OPAD)
                self.state = 128
                self.multExpr()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.UnaryExprContext)
            else:
                return self.getTypedRuleContext(parserGrammar.UnaryExprContext,i)


        def OPMULT(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.OPMULT)
            else:
                return self.getToken(parserGrammar.OPMULT, i)

        def getRuleIndex(self):
            return parserGrammar.RULE_multExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpr" ):
                listener.enterMultExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpr" ):
                listener.exitMultExpr(self)




    def multExpr(self):

        localctx = parserGrammar.MultExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.unaryExpr()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 135
                self.match(parserGrammar.OPMULT)
                self.state = 136
                self.unaryExpr()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPNEG(self):
            return self.getToken(parserGrammar.OPNEG, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(parserGrammar.UnaryExprContext,0)


        def ABPAR(self):
            return self.getToken(parserGrammar.ABPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(parserGrammar.ExprContext,0)


        def FPAR(self):
            return self.getToken(parserGrammar.FPAR, 0)

        def IDENTIFIER(self):
            return self.getToken(parserGrammar.IDENTIFIER, 0)

        def CTE(self):
            return self.getToken(parserGrammar.CTE, 0)

        def TRUE(self):
            return self.getToken(parserGrammar.TRUE, 0)

        def FALSE(self):
            return self.getToken(parserGrammar.FALSE, 0)

        def STRING_LITERAL(self):
            return self.getToken(parserGrammar.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return parserGrammar.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)




    def unaryExpr(self):

        localctx = parserGrammar.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryExpr)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(parserGrammar.OPNEG)
                self.state = 143
                self.unaryExpr()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(parserGrammar.ABPAR)
                self.state = 145
                self.expr()
                self.state = 146
                self.match(parserGrammar.FPAR)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(parserGrammar.IDENTIFIER)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(parserGrammar.CTE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.match(parserGrammar.TRUE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.match(parserGrammar.FALSE)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 7)
                self.state = 152
                self.match(parserGrammar.STRING_LITERAL)
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


    class ListWContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(parserGrammar.ExprContext,i)


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
        self.enterRule(localctx, 38, self.RULE_listW)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.expr()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 156
                self.match(parserGrammar.VIG)
                self.state = 157
                self.expr()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





