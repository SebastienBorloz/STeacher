from pylatexenc.latexwalker import (
    LatexWalker, LatexEnvironmentNode, LatexMacroNode,
    LatexCharsNode, LatexGroupNode, LatexMathNode
)

def extract_latex_tokens_flat(latex_str):
    walker = LatexWalker(latex_str)
    nodes, _, _ = walker.get_latex_nodes()

    def flatten_node(node):
        if isinstance(node, LatexCharsNode):
            text = node.chars.strip()
            return [text] if text else []

        elif isinstance(node, LatexMacroNode):
            tokens = [f"\\{node.macroname}"]
            if node.nodeargd:
                for arg in node.nodeargd.argnlist:
                    tokens.extend(flatten_node(arg))
            return tokens

        elif isinstance(node, LatexGroupNode):
            tokens = []
            for subnode in node.nodelist:
                tokens.extend(flatten_node(subnode))
            return tokens

        elif isinstance(node, LatexEnvironmentNode):
            tokens = [f"\\begin{{{node.envname}}}"]
            for subnode in node.nodelist:
                tokens.extend(flatten_node(subnode))
            tokens.append(f"\\end{{{node.envname}}}")
            return tokens

        elif isinstance(node, LatexMathNode):
            tokens = ["$"]
            for subnode in node.nodelist:
                tokens.extend(flatten_node(subnode))
            tokens.append("$")
            return tokens

        return []

    tokens = []
    for node in nodes:
        tokens.extend(flatten_node(node))

    return tokens



with open('./handwritten_dataset/easy/5.txt') as f: 
	latex_input = f.read()

parsed = extract_latex_tokens_flat(latex_input)
from pprint import pprint
pprint(parsed)
