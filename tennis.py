Score = ["0", "15", "30", "40"]



class Game(object):
	"""a Tennis Game between two players: A and B"""
	def __init__(self):
		self.score_A = 0
		self.score_B = 0

	def increase_score_player_A(self):
            self.score_A += 1

	def increase_score_player_B(self):
            self.score_B += 1

	def get_score(self):
		if (self.score_A <= 3 and self.score_B <= 3
			and not(self.score_A == 3 and self.score_B == 3)):
			return Score[self.score_A] + " - " + Score[self.score_B]
		elif (self.score_A - self.score_B >= 2):
			return "Player1 wins"
		elif (self.score_A - self.score_B == 1):
			return "advantage Player1"
		elif (self.score_A - self.score_B == 0):
			return "deuce"
		elif (self.score_A - self.score_B == -1):
			return "advantage Player2"
		elif (self.score_A - self.score_B <= -2):
			return "Player2 wins"

if __name__ == '__main__':
	pass