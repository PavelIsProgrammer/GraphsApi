class Increment:
	def __init__(self, id):
		self.id = id

	def get_next_id(self):
		id = self.id
		self.id += 1
		return id