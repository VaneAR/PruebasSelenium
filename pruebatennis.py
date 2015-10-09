
import tennis
import unittest

class TestTennisGame(unittest.TestCase):
	def setUp(self):
		self.g = tennis.Game();

	def test_score_0_0(self):
		self.assertEqual(self.g.get_score(), '0 - 0')

	def test_score_15_0(self):
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), '15 - 0')
	
	def test_score_0_15(self):
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), '0 - 15')

	def test_score_15_15(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), '15 - 15')

	def test_score_30_15(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), '30 - 15')
	
	def test_score_15_30(self):
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), '15 - 30')
	

	def test_score_30_30(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), '30 - 30')

	def test_score_40_30(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), '40 - 30')
		
	def test_score_30_40(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), '30 - 40')

	def test_score_deuce(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'deuce')

	def test_score_advantage_A(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), 'advantage Player1')

	def test_score_advantage_B(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'advantage Player2')

	

	def test_A_wins(self):
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.g.increase_score_player_A()
		self.assertEqual(self.g.get_score(), 'Player1 wins')

	def test_B_wins(self):
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.g.increase_score_player_B()
		self.assertEqual(self.g.get_score(), 'Player2 wins')



if __name__ == '__main__':
	unittest.main()