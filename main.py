from antlr4 import *

from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser



text = input(">")

lexer = gramaticaLexer(InputStream((text)))

stream = CommonTokenStream(lexer)

parser = gramaticaParser(stream)

tree = parser.programa()

print(tree.toStringTree(recog=parser))