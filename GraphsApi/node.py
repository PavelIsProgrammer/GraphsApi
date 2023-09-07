class Node:
	def __init__(self, graph, x, y, name, inc):
		self.id = inc.get_next_id()
		self.graph = graph
		self.x = x
		self.y = y

	def get_json(self):
		return '{ "id": ' + str(self.id) + ', "graph": ' + str(self.graph) + ', "x": ' +str(self.x) + ', "y": ' + str(self.y) + '}'