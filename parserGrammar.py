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
        4,1,32,147,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,1,1,1,3,1,39,8,1,1,2,1,2,1,
        2,5,2,44,8,2,10,2,12,2,47,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,56,
        8,4,10,4,12,4,59,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,70,
        8,7,10,7,12,7,73,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,89,8,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,121,8,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,132,8,14,10,14,12,
        14,135,9,14,1,15,1,15,1,15,1,15,1,15,5,15,142,8,15,10,15,12,15,145,
        9,15,1,15,0,1,28,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,
        1,1,0,2,3,149,0,32,1,0,0,0,2,38,1,0,0,0,4,40,1,0,0,0,6,48,1,0,0,
        0,8,52,1,0,0,0,10,60,1,0,0,0,12,62,1,0,0,0,14,66,1,0,0,0,16,80,1,
        0,0,0,18,82,1,0,0,0,20,90,1,0,0,0,22,95,1,0,0,0,24,100,1,0,0,0,26,
        105,1,0,0,0,28,120,1,0,0,0,30,136,1,0,0,0,32,33,5,1,0,0,33,34,5,
        28,0,0,34,35,5,21,0,0,35,1,1,0,0,0,36,37,5,9,0,0,37,39,3,4,2,0,38,
        36,1,0,0,0,38,39,1,0,0,0,39,3,1,0,0,0,40,45,3,6,3,0,41,42,5,21,0,
        0,42,44,3,6,3,0,43,41,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,
        1,0,0,0,46,5,1,0,0,0,47,45,1,0,0,0,48,49,3,8,4,0,49,50,5,23,0,0,
        50,51,3,10,5,0,51,7,1,0,0,0,52,57,5,28,0,0,53,54,5,24,0,0,54,56,
        5,28,0,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,9,1,0,0,0,59,57,1,0,0,0,60,61,7,0,0,0,61,11,1,0,0,0,62,63,5,4,
        0,0,63,64,3,14,7,0,64,65,5,5,0,0,65,13,1,0,0,0,66,71,3,16,8,0,67,
        68,5,21,0,0,68,70,3,16,8,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,
        0,0,71,72,1,0,0,0,72,15,1,0,0,0,73,71,1,0,0,0,74,81,3,18,9,0,75,
        81,3,20,10,0,76,81,3,22,11,0,77,81,3,24,12,0,78,81,3,26,13,0,79,
        81,3,12,6,0,80,74,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,0,80,77,1,0,
        0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,17,1,0,0,0,82,83,5,13,0,0,83,
        84,3,28,14,0,84,85,5,14,0,0,85,88,3,16,8,0,86,87,5,15,0,0,87,89,
        3,16,8,0,88,86,1,0,0,0,88,89,1,0,0,0,89,19,1,0,0,0,90,91,5,6,0,0,
        91,92,3,28,14,0,92,93,5,7,0,0,93,94,3,16,8,0,94,21,1,0,0,0,95,96,
        5,8,0,0,96,97,5,25,0,0,97,98,3,8,4,0,98,99,5,26,0,0,99,23,1,0,0,
        0,100,101,5,12,0,0,101,102,5,25,0,0,102,103,3,30,15,0,103,104,5,
        26,0,0,104,25,1,0,0,0,105,106,5,28,0,0,106,107,5,27,0,0,107,108,
        3,28,14,0,108,27,1,0,0,0,109,110,6,14,-1,0,110,111,5,19,0,0,111,
        121,3,28,14,6,112,113,5,25,0,0,113,114,3,28,14,0,114,115,5,26,0,
        0,115,121,1,0,0,0,116,121,5,28,0,0,117,121,5,29,0,0,118,121,5,11,
        0,0,119,121,5,10,0,0,120,109,1,0,0,0,120,112,1,0,0,0,120,116,1,0,
        0,0,120,117,1,0,0,0,120,118,1,0,0,0,120,119,1,0,0,0,121,133,1,0,
        0,0,122,123,10,9,0,0,123,124,5,20,0,0,124,132,3,28,14,10,125,126,
        10,8,0,0,126,127,5,16,0,0,127,132,3,28,14,9,128,129,10,7,0,0,129,
        130,5,17,0,0,130,132,3,28,14,8,131,122,1,0,0,0,131,125,1,0,0,0,131,
        128,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,
        29,1,0,0,0,135,133,1,0,0,0,136,137,3,28,14,0,137,138,5,25,0,0,138,
        139,5,24,0,0,139,143,3,28,14,0,140,142,5,26,0,0,141,140,1,0,0,0,
        142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,31,1,0,0,0,145,
        143,1,0,0,0,10,38,45,57,71,80,88,120,131,133,143
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
    RULE_cmdWhile = 10
    RULE_cmdRead = 11
    RULE_cmdWrite = 12
    RULE_cmdAtrib = 13
    RULE_expr = 14
    RULE_listW = 15

    ruleNames =  [ "prog", "decls", "listDecl", "declTip", "listId", "tip", 
                   "cmdComp", "listCmd", "cmd", "cmdIf", "cmdWhile", "cmdRead", 
                   "cmdWrite", "cmdAtrib", "expr", "listW" ]

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
            self.state = 32
            self.match(parserGrammar.PROGRAM)
            self.state = 33
            self.match(parserGrammar.ID)
            self.state = 34
            self.match(parserGrammar.PVIG)
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
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 36
                self.match(parserGrammar.VAR)
                self.state = 37
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
            self.state = 40
            self.declTip()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 41
                self.match(parserGrammar.PVIG)
                self.state = 42
                self.declTip()
                self.state = 47
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
            self.state = 48
            self.listId()
            self.state = 49
            self.match(parserGrammar.DPONTOS)
            self.state = 50
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
            self.state = 52
            self.match(parserGrammar.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 53
                self.match(parserGrammar.VIG)
                self.state = 54
                self.match(parserGrammar.ID)
                self.state = 59
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
            self.state = 60
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
            self.state = 62
            self.match(parserGrammar.BEGIN)
            self.state = 63
            self.listCmd()
            self.state = 64
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
            self.state = 66
            self.cmd()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 67
                self.match(parserGrammar.PVIG)
                self.state = 68
                self.cmd()
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
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.cmdIf()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.cmdWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.cmdRead()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.cmdWrite()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.cmdAtrib()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
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
            self.state = 82
            self.match(parserGrammar.IF)
            self.state = 83
            self.expr(0)
            self.state = 84
            self.match(parserGrammar.THEN)
            self.state = 85
            self.cmd()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(parserGrammar.ELSE)
                self.state = 87
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
            self.state = 90
            self.match(parserGrammar.WHILE)
            self.state = 91
            self.expr(0)
            self.state = 92
            self.match(parserGrammar.DO)
            self.state = 93
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
            self.state = 95
            self.match(parserGrammar.READ)
            self.state = 96
            self.match(parserGrammar.ABPAR)
            self.state = 97
            self.listId()
            self.state = 98
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
            self.state = 100
            self.match(parserGrammar.WRITE)
            self.state = 101
            self.match(parserGrammar.ABPAR)
            self.state = 102
            self.listW()
            self.state = 103
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
        self.enterRule(localctx, 26, self.RULE_cmdAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(parserGrammar.ID)
            self.state = 106
            self.match(parserGrammar.ATRIB)
            self.state = 107
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

        def OPNEG(self):
            return self.getToken(parserGrammar.OPNEG, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(parserGrammar.ExprContext,i)


        def ABPAR(self):
            return self.getToken(parserGrammar.ABPAR, 0)

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

        def OPREL(self):
            return self.getToken(parserGrammar.OPREL, 0)

        def OPAD(self):
            return self.getToken(parserGrammar.OPAD, 0)

        def OPMULT(self):
            return self.getToken(parserGrammar.OPMULT, 0)

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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 110
                self.match(parserGrammar.OPNEG)
                self.state = 111
                self.expr(6)
                pass
            elif token in [25]:
                self.state = 112
                self.match(parserGrammar.ABPAR)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(parserGrammar.FPAR)
                pass
            elif token in [28]:
                self.state = 116
                self.match(parserGrammar.ID)
                pass
            elif token in [29]:
                self.state = 117
                self.match(parserGrammar.CTE)
                pass
            elif token in [11]:
                self.state = 118
                self.match(parserGrammar.TRUE)
                pass
            elif token in [10]:
                self.state = 119
                self.match(parserGrammar.FALSE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = parserGrammar.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 123
                        self.match(parserGrammar.OPREL)
                        self.state = 124
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = parserGrammar.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 126
                        self.match(parserGrammar.OPAD)
                        self.state = 127
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = parserGrammar.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 129
                        self.match(parserGrammar.OPMULT)
                        self.state = 130
                        self.expr(8)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def ABPAR(self):
            return self.getToken(parserGrammar.ABPAR, 0)

        def VIG(self):
            return self.getToken(parserGrammar.VIG, 0)

        def FPAR(self, i:int=None):
            if i is None:
                return self.getTokens(parserGrammar.FPAR)
            else:
                return self.getToken(parserGrammar.FPAR, i)

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
        self.enterRule(localctx, 30, self.RULE_listW)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expr(0)
            self.state = 137
            self.match(parserGrammar.ABPAR)
            self.state = 138
            self.match(parserGrammar.VIG)
            self.state = 139
            self.expr(0)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.match(parserGrammar.FPAR) 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self._predicates[14] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




