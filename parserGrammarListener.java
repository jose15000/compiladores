// Generated from parserGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link parserGrammar}.
 */
public interface parserGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link parserGrammar#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(parserGrammar.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(parserGrammar.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#decls}.
	 * @param ctx the parse tree
	 */
	void enterDecls(parserGrammar.DeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#decls}.
	 * @param ctx the parse tree
	 */
	void exitDecls(parserGrammar.DeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#listDecl}.
	 * @param ctx the parse tree
	 */
	void enterListDecl(parserGrammar.ListDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#listDecl}.
	 * @param ctx the parse tree
	 */
	void exitListDecl(parserGrammar.ListDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#declTip}.
	 * @param ctx the parse tree
	 */
	void enterDeclTip(parserGrammar.DeclTipContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#declTip}.
	 * @param ctx the parse tree
	 */
	void exitDeclTip(parserGrammar.DeclTipContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#listId}.
	 * @param ctx the parse tree
	 */
	void enterListId(parserGrammar.ListIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#listId}.
	 * @param ctx the parse tree
	 */
	void exitListId(parserGrammar.ListIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#tip}.
	 * @param ctx the parse tree
	 */
	void enterTip(parserGrammar.TipContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#tip}.
	 * @param ctx the parse tree
	 */
	void exitTip(parserGrammar.TipContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmdComp}.
	 * @param ctx the parse tree
	 */
	void enterCmdComp(parserGrammar.CmdCompContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmdComp}.
	 * @param ctx the parse tree
	 */
	void exitCmdComp(parserGrammar.CmdCompContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#listCmd}.
	 * @param ctx the parse tree
	 */
	void enterListCmd(parserGrammar.ListCmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#listCmd}.
	 * @param ctx the parse tree
	 */
	void exitListCmd(parserGrammar.ListCmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmd}.
	 * @param ctx the parse tree
	 */
	void enterCmd(parserGrammar.CmdContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmd}.
	 * @param ctx the parse tree
	 */
	void exitCmd(parserGrammar.CmdContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmdIf}.
	 * @param ctx the parse tree
	 */
	void enterCmdIf(parserGrammar.CmdIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmdIf}.
	 * @param ctx the parse tree
	 */
	void exitCmdIf(parserGrammar.CmdIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmdWhile}.
	 * @param ctx the parse tree
	 */
	void enterCmdWhile(parserGrammar.CmdWhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmdWhile}.
	 * @param ctx the parse tree
	 */
	void exitCmdWhile(parserGrammar.CmdWhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmdRead}.
	 * @param ctx the parse tree
	 */
	void enterCmdRead(parserGrammar.CmdReadContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmdRead}.
	 * @param ctx the parse tree
	 */
	void exitCmdRead(parserGrammar.CmdReadContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmdWrite}.
	 * @param ctx the parse tree
	 */
	void enterCmdWrite(parserGrammar.CmdWriteContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmdWrite}.
	 * @param ctx the parse tree
	 */
	void exitCmdWrite(parserGrammar.CmdWriteContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#cmdAtrib}.
	 * @param ctx the parse tree
	 */
	void enterCmdAtrib(parserGrammar.CmdAtribContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#cmdAtrib}.
	 * @param ctx the parse tree
	 */
	void exitCmdAtrib(parserGrammar.CmdAtribContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(parserGrammar.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(parserGrammar.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#relExpr}.
	 * @param ctx the parse tree
	 */
	void enterRelExpr(parserGrammar.RelExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#relExpr}.
	 * @param ctx the parse tree
	 */
	void exitRelExpr(parserGrammar.RelExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#addExpr}.
	 * @param ctx the parse tree
	 */
	void enterAddExpr(parserGrammar.AddExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#addExpr}.
	 * @param ctx the parse tree
	 */
	void exitAddExpr(parserGrammar.AddExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#multExpr}.
	 * @param ctx the parse tree
	 */
	void enterMultExpr(parserGrammar.MultExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#multExpr}.
	 * @param ctx the parse tree
	 */
	void exitMultExpr(parserGrammar.MultExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpr(parserGrammar.UnaryExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#unaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpr(parserGrammar.UnaryExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link parserGrammar#listW}.
	 * @param ctx the parse tree
	 */
	void enterListW(parserGrammar.ListWContext ctx);
	/**
	 * Exit a parse tree produced by {@link parserGrammar#listW}.
	 * @param ctx the parse tree
	 */
	void exitListW(parserGrammar.ListWContext ctx);
}