from pylatexenc.latexwalker import LatexWalker, LatexEnvironmentNode, LatexMathNode, LatexCharsNode, LatexMacroNode

with open('./handwritten_dataset/easy/1.txt') as f: 
	latex = f.read()

walker = LatexWalker(latex)
nodes, pos, len_ = walker.get_latex_nodes(pos=0)

class divider:
	def __init__(self):
		self.out = []

	def divideNode(self, node):
		if type(node) == LatexEnvironmentNode:
			for i in node.nodelist:
				self.divideNode(i)

		elif type(node) == LatexMathNode:
			self. out.append(node.delimiters[0])
			for i in node.nodelist:
				self.divideNode(i)
			self.out.append(node.delimiters[1])

		elif type(node) == LatexCharsNode:
			self.out.append(("chars", node.chars))

		elif type(node) == LatexMacroNode:
			self.out.append((node.macroname, node.macroname))


yay = divider()

latexTab = []
for node in nodes:
	latexTab.append(yay.divideNode(node))

print(latexTab)

print("yay")