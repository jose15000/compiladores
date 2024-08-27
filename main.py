from antlr4 import *

from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser

class LexicalError(Exception):
    def __init__(self, line, column, text):
        self.line = line
        self.column = column
        self.text = text
        super().__init__(self._format_message())

    def _format_message(self):
        return f"Erro léxico na linha {self.line}, coluna {self.column}: '{self.text}'"

class CustomLexer(gramaticaLexer):
    def notifyListeners(self, e):
        line = self._tokenStartLine
        column = self._tokenStartColumn
        text = self._input.getText(self._tokenStartCharIndex, self._input.index)
        raise LexicalError(line, column, text)

def main():
    try:
        text = input("> ")

        lexer = CustomLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = gramaticaParser(stream)

        tree = parser.programa()
        print(tree.toStringTree(recog=parser))

        for token in stream.tokens:
            token_text = token.text
            token_type = lexer.symbolicNames[token.type]
            
            if ':' in token_text:
                tipo, atributo = token_text.split(":")
                print(f"Token: {token_text}, Tipo: {tipo}, Atributo: {atributo}")
            else:
                print(f"Token: {token_text}, Tipo: {token_type}")

        print("Análise léxica concluída.")

    except LexicalError as e:
        print(e)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()
