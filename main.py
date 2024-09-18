import sys
from antlr4 import *
from lexerGrammar import lexerGrammar
from parserGrammar import parserGrammar

class LexicalError(Exception):
    def __init__(self, line, column, text):
        self.line = line
        self.column = column
        self.text = text
        super().__init__(self._format_message())

    def _format_message(self):
        return f"Erro léxico na linha {self.line}, coluna {self.column}: '{self.text}'"

class CustomLexer(lexerGrammar):
    def notifyListeners(self, e):
        line = self._tokenStartLine
        column = self._tokenStartColumn
        text = self._input.getText(self._tokenStartCharIndex, self._input.index)
        raise LexicalError(line, column, text)

def main():

    if len(sys.argv) != 2:
        print("Usage: python test_grammar.py <input_file>")
        exit(1)

    print("> ")
    text = sys.argv[1]

    try:
        lexer = CustomLexer(FileStream(text))
        stream = CommonTokenStream(lexer)
        parser = parserGrammar(stream)

        tree = parser.prog()
        print("\nÁrvore de Análise Sintática:")
        print(tree.toStringTree(recog=parser))

        print("\nTokens:")
        for token in stream.tokens:
            token_text = token.text
            token_type = lexer.symbolicNames[token.type]
            if ':' in token_text:
                tipo, atributo = token_text.split(":")
                print(f"Token: {token_text}, Tipo: {tipo}, Atributo: {atributo}")
            else:
                print(f"Token: {token_text}, Tipo: {token_type}")

        print("\nAnálise léxica concluída.")

    except LexicalError as e:
        print(f"\nErro léxico: {e}")

    except Exception as e:
        print(f"\nErro geral: {e}")

if __name__ == '__main__':
    main()
