import curses
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

def main(stdscr):
    curses.curs_set(2)
    stdscr.clear() 
    stdscr.refresh() 

    stdscr.addstr("Digite o texto para análise léxica: ")
    curses.echo() 
    text = stdscr.getstr().decode() 
    try:
        lexer = CustomLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = gramaticaParser(stream)

        tree = parser.programa()
        stdscr.addstr("\n" + tree.toStringTree(recog=parser) + "\n")

        for token in stream.tokens:
            token_text = token.text
            token_type = lexer.symbolicNames[token.type]
            if ':' in token_text:
                tipo, atributo = token_text.split(":")
                stdscr.addstr(f"Token : {token_text}, Tipo: {tipo}, Atributo: {atributo}\n")
            else:
                stdscr.addstr(f"Token: {token_text}, Tipo: {token_type}\n")

        stdscr.addstr("Análise léxica concluída.\n")

    except LexicalError as e:
        stdscr.addstr(str(e) + "\n")

    except Exception as e:
        stdscr.addstr(f"Erro: {e}\n")

    stdscr.addstr("\nPressione qualquer tecla para continuar...")
    stdscr.getch()  # Esperar o usuário pressionar uma tecla

if __name__ == '__main__':
    curses.wrapper(main)
