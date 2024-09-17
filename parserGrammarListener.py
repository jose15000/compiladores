# Generated from parserGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .parserGrammar import parserGrammar
else:
    from parserGrammar import parserGrammar

# This class defines a complete listener for a parse tree produced by parserGrammar.
class parserGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by parserGrammar#prog.
    def enterProg(self, ctx:parserGrammar.ProgContext):
        pass

    # Exit a parse tree produced by parserGrammar#prog.
    def exitProg(self, ctx:parserGrammar.ProgContext):
        pass


    # Enter a parse tree produced by parserGrammar#decls.
    def enterDecls(self, ctx:parserGrammar.DeclsContext):
        pass

    # Exit a parse tree produced by parserGrammar#decls.
    def exitDecls(self, ctx:parserGrammar.DeclsContext):
        pass


    # Enter a parse tree produced by parserGrammar#listDecl.
    def enterListDecl(self, ctx:parserGrammar.ListDeclContext):
        pass

    # Exit a parse tree produced by parserGrammar#listDecl.
    def exitListDecl(self, ctx:parserGrammar.ListDeclContext):
        pass


    # Enter a parse tree produced by parserGrammar#declTip.
    def enterDeclTip(self, ctx:parserGrammar.DeclTipContext):
        pass

    # Exit a parse tree produced by parserGrammar#declTip.
    def exitDeclTip(self, ctx:parserGrammar.DeclTipContext):
        pass


    # Enter a parse tree produced by parserGrammar#listId.
    def enterListId(self, ctx:parserGrammar.ListIdContext):
        pass

    # Exit a parse tree produced by parserGrammar#listId.
    def exitListId(self, ctx:parserGrammar.ListIdContext):
        pass


    # Enter a parse tree produced by parserGrammar#tip.
    def enterTip(self, ctx:parserGrammar.TipContext):
        pass

    # Exit a parse tree produced by parserGrammar#tip.
    def exitTip(self, ctx:parserGrammar.TipContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdComp.
    def enterCmdComp(self, ctx:parserGrammar.CmdCompContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdComp.
    def exitCmdComp(self, ctx:parserGrammar.CmdCompContext):
        pass


    # Enter a parse tree produced by parserGrammar#listCmd.
    def enterListCmd(self, ctx:parserGrammar.ListCmdContext):
        pass

    # Exit a parse tree produced by parserGrammar#listCmd.
    def exitListCmd(self, ctx:parserGrammar.ListCmdContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmd.
    def enterCmd(self, ctx:parserGrammar.CmdContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmd.
    def exitCmd(self, ctx:parserGrammar.CmdContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdIf.
    def enterCmdIf(self, ctx:parserGrammar.CmdIfContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdIf.
    def exitCmdIf(self, ctx:parserGrammar.CmdIfContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdElse.
    def enterCmdElse(self, ctx:parserGrammar.CmdElseContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdElse.
    def exitCmdElse(self, ctx:parserGrammar.CmdElseContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdWhile.
    def enterCmdWhile(self, ctx:parserGrammar.CmdWhileContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdWhile.
    def exitCmdWhile(self, ctx:parserGrammar.CmdWhileContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdRead.
    def enterCmdRead(self, ctx:parserGrammar.CmdReadContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdRead.
    def exitCmdRead(self, ctx:parserGrammar.CmdReadContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdWrite.
    def enterCmdWrite(self, ctx:parserGrammar.CmdWriteContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdWrite.
    def exitCmdWrite(self, ctx:parserGrammar.CmdWriteContext):
        pass


    # Enter a parse tree produced by parserGrammar#cmdAtrib.
    def enterCmdAtrib(self, ctx:parserGrammar.CmdAtribContext):
        pass

    # Exit a parse tree produced by parserGrammar#cmdAtrib.
    def exitCmdAtrib(self, ctx:parserGrammar.CmdAtribContext):
        pass


    # Enter a parse tree produced by parserGrammar#expr.
    def enterExpr(self, ctx:parserGrammar.ExprContext):
        pass

    # Exit a parse tree produced by parserGrammar#expr.
    def exitExpr(self, ctx:parserGrammar.ExprContext):
        pass


    # Enter a parse tree produced by parserGrammar#relExpr.
    def enterRelExpr(self, ctx:parserGrammar.RelExprContext):
        pass

    # Exit a parse tree produced by parserGrammar#relExpr.
    def exitRelExpr(self, ctx:parserGrammar.RelExprContext):
        pass


    # Enter a parse tree produced by parserGrammar#addExpr.
    def enterAddExpr(self, ctx:parserGrammar.AddExprContext):
        pass

    # Exit a parse tree produced by parserGrammar#addExpr.
    def exitAddExpr(self, ctx:parserGrammar.AddExprContext):
        pass


    # Enter a parse tree produced by parserGrammar#multExpr.
    def enterMultExpr(self, ctx:parserGrammar.MultExprContext):
        pass

    # Exit a parse tree produced by parserGrammar#multExpr.
    def exitMultExpr(self, ctx:parserGrammar.MultExprContext):
        pass


    # Enter a parse tree produced by parserGrammar#unaryExpr.
    def enterUnaryExpr(self, ctx:parserGrammar.UnaryExprContext):
        pass

    # Exit a parse tree produced by parserGrammar#unaryExpr.
    def exitUnaryExpr(self, ctx:parserGrammar.UnaryExprContext):
        pass


    # Enter a parse tree produced by parserGrammar#listW.
    def enterListW(self, ctx:parserGrammar.ListWContext):
        pass

    # Exit a parse tree produced by parserGrammar#listW.
    def exitListW(self, ctx:parserGrammar.ListWContext):
        pass



del parserGrammar