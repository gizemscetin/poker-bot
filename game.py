import math
from player import Player, Action
from dealer import Dealer

				
# Action Set : {check-0, call-1, bet-2, raise-3, fold-4}
# State Set : {pre-flop 0, flop 1, turn 2, river 3}
			
class Game:
	def __init__(self, player_cnt = 2):
		self.players_ = []

		for i in range(player_cnt):
			self.players_.append(Player(i+1))

		self.pot_ = 0
		self.winner_ = None
	
	def __str__(self):
		return "\n\t[Pot : " + str(self.pot_) + "]\n"
				
	def play_one_state(self, state_type):			
		last_action = None
		player_turn = 0
		
		while not last_action == Action(4): 	# While not FOLD
			# Switch player
			player = self.players_[player_turn % 2]
			player.act(state_type, last_action) 	# 0 for pre-flop
			
			if player.last_action_ == None:
				# no more turns left, so go to the next state
				# deal the next community cards
				break
			
			player.print_last_action()
			
			# Update the new last action
			last_action = player.last_action_
			player.add_action_history(last_action)
			
			# Update the current stack according to the action
			if player.decrease_stack(last_action):
			# Update the current pot according to the action
				self.pot_ += 1
			
			# Handle 2 special cases here!!! 
			# Call -> Check and Raise -> Bet
			if player_turn == 0:
				if last_action.index_ == 1:
					last_action.index_ = 0
				elif last_action.index_ == 3:
					last_action.index_ = 2
				
			#Update the counter
			player_turn += 1
			
			if last_action == Action(4):
				self.winner_ = self.players_[player_turn % 2] # other player won
				return False
		return True
			
	def play_one_round(self):
		dealer = Dealer()				# Create new dealer for every round
		self.pot_ = 3					# Clear the pot by setting it to small + big blinds
		
		self.players_[0].set_blind(0)	# Player 0 is always small blind
		self.players_[1].set_blind(1)	# Player 1 is always big blind
		self.show_game_status()
		
		if self.play_one_state(0): 	# pre-flop
			dealer.deal_flop()
			self.show_game_status()
			if self.play_one_state(1): 	# pre-turn
				self.show_game_status()
				dealer.deal_turn()
				if self.play_one_state(1): 	# pre-river
					dealer.deal_river()
		

		# Find the winner of the round
		if not self.winner_ == None:
			self.winner_.increase_stack(self.pot_)
		#else: # User winner.py
			#self.winner_.increase_stack(self.pot_)
		self.show_game_status()
		
	def start(self):
		game_end = False
		round_cnt = 0
		
		while round_cnt < 3 and not game_end:
			print("\n----------------------------------\n")
			self.play_one_round()
			print("\n----------------------------------\n")
			#self.show_game_status()
			
			# Before going into the next round, do a few things!
			# Check game over conditions:
			for player in self.players_:
				if player.lost():
					game_end = True
			
			# Switch players for the next round:
			players = self.players_.reverse()
			
			round_cnt += 1
					
	def show_game_status(self):
		print(self)
		print(self.players_)			# Show player status
		print()
						
G = Game()
G.start()
