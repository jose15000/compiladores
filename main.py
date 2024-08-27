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
        msg = self._formatMessage(self.line, self.column, self.text)
        raise LexicalError(self.line, self.column, self.text)

    def _formatMessage(self, line, column, text):
        return f"Erro léxico na linha {line}, coluna {column}: '{text}'"

def main():
    try:
        text = input("> ")

        lexer = CustomLexer(InputStream(text))

        stream = CommonTokenStream(lexer)

        parser = gramaticaParser(stream)

        tree = parser.programa()

        print(tree.toStringTree(recog=parser))

        print("Análise léxica concluída.")

    except LexicalError as e:
        print(e)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()