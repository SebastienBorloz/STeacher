from pylatexenc.latexwalker import LatexWalker, LatexEnvironmentNode, LatexMathNode
from sympy.parsing.latex import parse_latex
from sympy import simplify


def extract_math_nodes(latex_code):
    walker = LatexWalker(latex_code)
    nodes, pos, _ = walker.get_latex_nodes(pos=0)

    def walk_and_collect_math(nodes):
        expressions = []
        for node in nodes:
            if isinstance(node, LatexMathNode):
                #math_code = latex_code[node.pos:node.pos_end]
                math_content = node.latex_verbatim()
                expressions.append(math_content)
            elif hasattr(node, 'nodelist') and node.nodelist:
                expressions += walk_and_collect_math(node.nodelist)
            elif isinstance(node, LatexEnvironmentNode):
                expressions += walk_and_collect_math(node.nodelist)
        return expressions

    return walk_and_collect_math(nodes)

def parse_with_sympy(expressions):
    for i, expr in enumerate(expressions, start=1):
        print(f"\nExpression {i}: {expr}")
        try:
            parsed = parse_latex(expr)
            print(f"Parsed: {parsed}")
            simplified = simplify(parsed)
            print(f"Simplified: {simplified}")
        except Exception as e:
            print(f"Erreur de parsing SymPy : {e}")



latex_code = test.dataset["easy"][0]["text"]
print("Extraction des expressions mathématiques LaTeX...")
expressions = extract_math_nodes(latex_code)
print(f"{len(expressions)} expression(s) trouvée(s).")
parse_with_sympy(expressions)