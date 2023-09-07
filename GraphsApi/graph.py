class Graph:
	def __init__(self, name, inc):
    		self.id = inc.get_next_id()
    		self.name = name

	def get_json(self):
    		return '{ "id": ' + str(self.id) + ', "name": "' + self.name+ '" }'