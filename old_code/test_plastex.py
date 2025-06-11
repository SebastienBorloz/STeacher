from plasTeX.TeX import TeX
from plasTeX.Base.LaTeX.Math import text
import json

tex = TeX()

with open('./handwritten_dataset/easy/1.txt') as f: 
	latex = f.read()

tex.input(latex)
doc = tex.parse()


class element:
	def __init__(self, type, content):
		self.type = type
		self.content = content
		self.children = []

class parser:
	def __init__(self):
		self.flat = []
		self.OH = self.divideNodeBetter(doc.childNodes[11])
		#print(OH)
		self.flattenTree(self.OH)
		print("yay")

	def divideNodeBetter(self, node):
		try:
			e = element(str(type(node)), node.childrenSource)
			for i in node.childNodes:
				e.children.append(self.divideNodeBetter(i))
		except:
			e = element(str(type(node)), node)

		return e

	def flattenTree(self, tree):
		for child in tree.children:
			if len(child.children) == 0:
				self.flat.append(child.content)
			else:
				for el in child.children:
					self.flattenTree(el)


p = parser()

print(p.flat)

print("yay")