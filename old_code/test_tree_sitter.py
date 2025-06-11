from tree_sitter import Language, Parser

# Compile the grammar (à faire une seule fois)
Language.build_library(
    'build/latex.so',
    ['tree-sitter-latex']
)

# Charger le langage compilé
LATEX_LANGUAGE = Language('build/latex.so', 'latex')
parser = Parser()
parser.set_language(LATEX_LANGUAGE)

with open('./handwritten_dataset/easy/1.txt') as f: 
	latex_code = f.read()

tree = parser.parse(bytes(latex_code, "utf8"))

def extract_tokens(node, source):
    if node.child_count == 0:
        return [(node.type, source[node.start_byte:node.end_byte].decode())]
    else:
        tokens = []
        for child in node.children:
            tokens += extract_tokens(child, source)
        return tokens

tokens = extract_tokens(tree.root_node, bytes(latex_code, "utf8"))
for t in tokens:
    print(t)
