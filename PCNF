import nltk
from nltk import CFG, PCFG, ChartParser
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    NP -> DT N [0.6] | NP PP [0.4]
    PP -> P NP [1.0]
    DT -> 'the' [1.0]
    N -> 'cat' [0.4] | 'dog' [0.6]
    V -> 'chased' [1.0]
    P -> 'with' [1.0]
""")
parser = ChartParser(grammar)
sentence = "the cat chased the dog with the dog".split()
for tree in parser.parse(sentence):
    tree.pretty_print()
