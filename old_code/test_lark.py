from lark import Lark

latex_grammar = r"""
start: (element | TEXT)+

element: command
       | environment
       | group
       | math_env

command: "\\" CNAME options? arguments*

environment: "\\begin" "{" CNAME "}" (element | TEXT)* "\\end" "{" CNAME "}"

group: "{" (element | TEXT)* "}"

arguments: group
option_content: /[^\[\]]+/
options: "[" option_content "]"

math_env: "\\[" /(.|\n)*?/"\\]"     -> display_math
        | "\\(" /(.|\n)*?/"\\)"     -> inline_math

%import common.CNAME
%import common.WS_INLINE
%ignore WS_INLINE

TEXT: /[^\\{}\[\]]+/
"""

parser = Lark(latex_grammar)

with open('./handwritten_dataset/easy/1.txt') as f: 
	latex = f.read()


tree = parser.parse(latex)
print(tree.pretty())