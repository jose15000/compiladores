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
        4,1,32,172,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,3,0,47,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,
        1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,
        70,8,4,10,4,12,4,73,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,
        84,8,7,10,7,12,7,87,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,95,8,8,1,9,1,
        9,1,9,1,9,1,9,3,9,102,8,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,15,1,15,1,16,1,16,1,16,5,16,131,8,16,10,16,12,16,134,9,16,
        1,17,1,17,1,17,5,17,139,8,17,10,17,12,17,142,9,17,1,18,1,18,1,18,
        5,18,147,8,18,10,18,12,18,150,9,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,3,19,162,8,19,1,20,1,20,1,20,5,20,167,8,20,10,
        20,12,20,170,9,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,0,1,1,0,2,3,169,0,42,1,0,0,0,2,51,1,0,0,
        0,4,54,1,0,0,0,6,62,1,0,0,0,8,66,1,0,0,0,10,74,1,0,0,0,12,76,1,0,
        0,0,14,80,1,0,0,0,16,94,1,0,0,0,18,96,1,0,0,0,20,103,1,0,0,0,22,
        106,1,0,0,0,24,111,1,0,0,0,26,116,1,0,0,0,28,121,1,0,0,0,30,125,
        1,0,0,0,32,127,1,0,0,0,34,135,1,0,0,0,36,143,1,0,0,0,38,161,1,0,
        0,0,40,163,1,0,0,0,42,43,5,1,0,0,43,44,5,28,0,0,44,46,5,21,0,0,45,
        47,3,2,1,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,3,12,
        6,0,49,50,5,22,0,0,50,1,1,0,0,0,51,52,5,9,0,0,52,53,3,4,2,0,53,3,
        1,0,0,0,54,59,3,6,3,0,55,56,5,21,0,0,56,58,3,6,3,0,57,55,1,0,0,0,
        58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,5,1,0,0,0,61,59,1,0,
        0,0,62,63,3,8,4,0,63,64,5,23,0,0,64,65,3,10,5,0,65,7,1,0,0,0,66,
        71,5,28,0,0,67,68,5,24,0,0,68,70,5,28,0,0,69,67,1,0,0,0,70,73,1,
        0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,9,1,0,0,0,73,71,1,0,0,0,74,
        75,7,0,0,0,75,11,1,0,0,0,76,77,5,4,0,0,77,78,3,14,7,0,78,79,5,5,
        0,0,79,13,1,0,0,0,80,85,3,16,8,0,81,82,5,21,0,0,82,84,3,16,8,0,83,
        81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,15,1,0,0,
        0,87,85,1,0,0,0,88,95,3,18,9,0,89,95,3,22,11,0,90,95,3,24,12,0,91,
        95,3,26,13,0,92,95,3,28,14,0,93,95,3,12,6,0,94,88,1,0,0,0,94,89,
        1,0,0,0,94,90,1,0,0,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,0,0,0,
        95,17,1,0,0,0,96,97,5,13,0,0,97,98,3,30,15,0,98,99,5,14,0,0,99,101,
        3,16,8,0,100,102,3,20,10,0,101,100,1,0,0,0,101,102,1,0,0,0,102,19,
        1,0,0,0,103,104,5,15,0,0,104,105,3,16,8,0,105,21,1,0,0,0,106,107,
        5,6,0,0,107,108,3,30,15,0,108,109,5,7,0,0,109,110,3,16,8,0,110,23,
        1,0,0,0,111,112,5,8,0,0,112,113,5,25,0,0,113,114,3,8,4,0,114,115,
        5,26,0,0,115,25,1,0,0,0,116,117,5,12,0,0,117,118,5,25,0,0,118,119,
        3,40,20,0,119,120,5,26,0,0,120,27,1,0,0,0,121,122,5,28,0,0,122,123,
        5,27,0,0,123,124,3,30,15,0,124,29,1,0,0,0,125,126,3,32,16,0,126,
        31,1,0,0,0,127,132,3,34,17,0,128,129,5,20,0,0,129,131,3,34,17,0,
        130,128,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,
        133,33,1,0,0,0,134,132,1,0,0,0,135,140,3,36,18,0,136,137,5,16,0,
        0,137,139,3,36,18,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,1,0,
        0,0,140,141,1,0,0,0,141,35,1,0,0,0,142,140,1,0,0,0,143,148,3,38,
        19,0,144,145,5,17,0,0,145,147,3,38,19,0,146,144,1,0,0,0,147,150,
        1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,37,1,0,0,0,150,148,1,
        0,0,0,151,152,5,19,0,0,152,162,3,38,19,0,153,154,5,25,0,0,154,155,
        3,30,15,0,155,156,5,26,0,0,156,162,1,0,0,0,157,162,5,28,0,0,158,
        162,5,29,0,0,159,162,5,11,0,0,160,162,5,10,0,0,161,151,1,0,0,0,161,
        153,1,0,0,0,161,157,1,0,0,0,161,158,1,0,0,0,161,159,1,0,0,0,161,
        160,1,0,0,0,162,39,1,0,0,0,163,168,3,30,15,0,164,165,5,24,0,0,165,
        167,3,30,15,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,
        169,1,0,0,0,169,41,1,0,0,0,170,168,1,0,0,0,11,46,59,71,85,94,101,
        132,140,148,161,168
    ]

class parserGrammar ( Parser ):

    grammarFileName = "parserGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PROGRAM'", "'INTEGER'", "'BOOLEAN'", 
                     "'BEGIN'", "'END'", "'WHILE'", "'DO'", "'READ'", "'VAR'", 
                     "'FALSE'", "'TRUE'", "'WRITE'", "'IF'", "'THEN'", "'ELSE'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'~'", "<INVALID>", 
                     "';'", "'.'", "':'", "','", "'('", "')'", "':='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "INTEGER", "BOOLEAN", "BEGIN", 
                      "END", "WHILE", "DO", "READ", "VAR", "FALSE", "TRUE", 
                      "WRITE", "IF", "THEN", "ELSE", "OPAD", "OPMULT", "OPLOG", 
                      "OPNEG", "OPREL", "PVIG", "PONTO", "DPONTOS", "VIG", 
                      "ABPAR", "FPAR", "ATRIB", "ID", "CTE", "CADEIA", "COMENTARIOS_LINHA", 
                      "WS" ]

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
    RULE_cmdElse = 10
    RULE_cmdWhile = 11
    RULE_cmdRead = 12
    RULE_cmdWrite = 13
    RULE_cmdAtrib = 14
    RULE_expr = 15
    RULE_relExpr = 16
    RULE_addExpr = 17
    RULE_multExpr = 18
    RULE_unaryExpr = 19
    RULE_listW = 20

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "cmdElse", "cmdWhile", 
                   "cmdRead", "cmdWrite", "cmdAtrib", "expr", "relExpr", 
                   "addExpr", "multExpr", "unaryExpr", "listW" ]

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
    IF=13
    THEN=14
    ELSE=15
    OPAD=16
    OPMULT=17
    OPLOG=18
    OPNEG=19
    OPREL=20
    PVIG=21
    PONTO=22
    DPONTOS=23
    VIG=24
    ABPAR=25
    FPAR=26
    ATRIB=27
    ID=28
    CTE=29
    CADEIA=30
    COMENTARIOS_LINHA=31
    WS=32

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
            self.state = 42
            self.match(parserGrammar.PROGRAM)
            self.state = 43
            self.match(parserGrammar.ID)
            self.state = 44
            self.match(parserGrammar.PVIG)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 45
                self.decls()


            self.state = 48
            self.cmdComp()
            self.state = 49
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(parserGrammar.VAR)
            self.state = 52
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
            self.state = 54
            self.declTip()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 55
                self.match(parserGrammar.PVIG)
                self.state = 56
                self.declTip()
                self.state = 61
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
            self.state = 62
            self.listId()
            self.state = 63
            self.match(parserGrammar.DPONTOS)
            self.state = 64
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
            self.state = 66
            self.match(parserGrammar.ID)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 67
                self.match(parserGrammar.VIG)
                self.state = 68
                self.match(parserGrammar.ID)
                self.state = 73
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
            self.state = 74
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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
            self.state = 76
            self.match(parserGrammar.BEGIN)
            self.state = 77
            self.listCmd()
            self.state = 78
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
            self.state = 80
            self.cmd()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 81
                self.match(parserGrammar.PVIG)
                self.state = 82
                self.cmd()
                self.state = 87
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
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.cmdIf()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.cmdWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.cmdRead()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.cmdWrite()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.cmdAtrib()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
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


        def cmdElse(self):
            return self.getTypedRuleContext(parserGrammar.CmdElseContext,0)


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
            self.state = 96
            self.match(parserGrammar.IF)
            self.state = 97
            self.expr()
            self.state = 98
            self.match(parserGrammar.THEN)
            self.state = 99
            self.cmd()
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 100
                self.cmdElse()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(parserGrammar.ELSE, 0)

        def cmd(self):
            return self.getTypedRuleContext(parserGrammar.CmdContext,0)


        def getRuleIndex(self):
            return parserGrammar.RULE_cmdElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdElse" ):
                listener.enterCmdElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdElse" ):
                listener.exitCmdElse(self)




    def cmdElse(self):

        localctx = parserGrammar.CmdElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(parserGrammar.ELSE)
            self.state = 104
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
        self.enterRule(localctx, 22, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(parserGrammar.WHILE)
            self.state = 107
            self.expr()
            self.state = 108
            self.match(parserGrammar.DO)
            self.state = 109
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
            self.state = 111
            self.match(parserGrammar.READ)
            self.state = 112
            self.match(parserGrammar.ABPAR)
            self.state = 113
            self.listId()
            self.state = 114
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
            self.state = 116
            self.match(parserGrammar.WRITE)
            self.state = 117
            self.match(parserGrammar.ABPAR)
            self.state = 118
            self.listW()
            self.state = 119
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
        self.enterRule(localctx, 28, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(parserGrammar.ID)
            self.state = 122
            self.match(parserGrammar.ATRIB)
            self.state = 123
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
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
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


        def OPREL(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.OPREL)
            else:
                return self.getToken(parserGrammar.OPREL, i)

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
        self.enterRule(localctx, 32, self.RULE_relExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.addExpr()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 128
                self.match(parserGrammar.OPREL)
                self.state = 129
                self.addExpr()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 34, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.multExpr()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 136
                self.match(parserGrammar.OPAD)
                self.state = 137
                self.multExpr()
                self.state = 142
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
        self.enterRule(localctx, 36, self.RULE_multExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.unaryExpr()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 144
                self.match(parserGrammar.OPMULT)
                self.state = 145
                self.unaryExpr()
                self.state = 150
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

        def ID(self):
            return self.getToken(parserGrammar.ID, 0)

        def CTE(self):
            return self.getToken(parserGrammar.CTE, 0)

        def TRUE(self):
            return self.getToken(parserGrammar.TRUE, 0)

        def FALSE(self):
            return self.getToken(parserGrammar.FALSE, 0)

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
        self.enterRule(localctx, 38, self.RULE_unaryExpr)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(parserGrammar.OPNEG)
                self.state = 152
                self.unaryExpr()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(parserGrammar.ABPAR)
                self.state = 154
                self.expr()
                self.state = 155
                self.match(parserGrammar.FPAR)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(parserGrammar.ID)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.match(parserGrammar.CTE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.match(parserGrammar.TRUE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
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
        self.enterRule(localctx, 40, self.RULE_listW)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.expr()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 164
                self.match(parserGrammar.VIG)
                self.state = 165
                self.expr()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





