class Link:
	def __init__(self, a, b, inc):
		self.id = inc.get_next_id()
		self.a = a
		self.b = b

	def get_json(self):
		return '{ "id": ' + str(self.id) + ', "a": ' + str(self.a) + ', "b": ' + str(self.b) + ' }'