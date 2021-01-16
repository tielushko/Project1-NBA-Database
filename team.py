class Team:
	def __init__(self, team_id, location, name, league):
		self.team_id = team_id
		self.location = location
		self.name = name
		self.league = league

	def __repr__(self):
		return "{0:<10} {1:<10} {2:<10} {3:<10}".format(self.team_id, self.location, self.name, self.league)

