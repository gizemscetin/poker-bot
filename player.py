from deck import Card
# Player attributes are:
# 2 Pocket cards
# hand : 5 Best cards after river
# Small-0 or Big-1 blind
# Stack
# TBC...

class Action:
	def __init__(self, no):
		self.index_ = no
	def __str__(self):
		if self.index_ == 0:
			return "check-0"
		if self.index_ == 1:
			return "call-1"
		if self.index_ == 2:
			return "bet-2"
		if self.index_ == 3:
			return "raise-3"	
		if self.index_ == 4:
			return "fold-4"
		return ""
			
	__repr__ = __str__
	
	def __eq__(self, other):
	# Override the default Equals behavior
		if isinstance(other, self.__class__):
			return (self.index_ == other.index_)
		return False
	
# Action Set : {check-0, call-1, bet-2, raise-3, fold-4}
# State Set : {pre-flop 0, flop 1, turn 2, river 3}
S1 = [Action(1), Action(3), Action(4)]
S2 = [Action(0), Action(2), Action(4)]
S3 = [Action(1), Action(4)]
SE = []

class Player:
	def __init__(self, id, stack = 20):
		self.id_ = id
		self.pocket_cards_ = []
		self.stack_ = stack
		self.action_history_ = []
		self.last_action_ = None
		self.blind_type_ = 0
		self.raise_ctr_ = 0
		
	def __str__(self):
		return "Player " + str(self.id_) + " : " + str(self.stack_)
		
	__repr__ = __str__
		
	def set_blind(self, blind):
		self.blind_type_ = blind
		if blind == 0:
			self.stack_ -= 1
		elif blind == 1:
			self.stack_ -= 2
			
	def set_cards(self, cards):
		self.pocket_cards_ = cards
		
	def show_cards(self):
		print("Player " + str(self.id_) + " : " + str(self.pocket_cards_))
		
	def print_last_action(self):
		s = "Player " + str(self.id_)
		if self.last_action_.index_ == 0:
			s += " checked."
		if self.last_action_.index_ == 1:
			s +=  " called."
		if self.last_action_.index_ == 2:
			s +=  " bet."
		if self.last_action_.index_ == 3:
			s +=  " raised."	
		if self.last_action_.index_ == 4:
			s +=  " folded."
		print(s+"\n")
		
	def act(self, state, last_action):
		# TO DO  :  Check if the player has enough stack to raise or bet or call
		actions = self.find_allowed_actions(state, last_action)
		
		if len(actions) == 0:
			self.last_action_ = None
		else:
			print(actions)		
			# Ask for I/O input
			self.last_action_ = Action(int(input("Player " + str(self.id_) + " : ")))
			# TO DO  :  Check if the input is legit
		
	def lost(self):
		if self.stack_ <= 0:
			return True
			
	def decrease_stack(self, action, amount = 1):
		if action.index_ == 1 or action.index_ == 2 or action.index_ == 3:
			self.stack_ -= amount
			return True
		return False
	
	def increase_stack(self, amount):
		self.stack_ += amount
		
	def find_allowed_actions(self, state, last_action):
		# find possible actions given the state
			
		# Action Set : {check-0, call-1, bet-2, raise-3, fold-4}
		
		if last_action == None:
			if state == 0: 	 # Pre-flop
				return S1
			return S2
		
		if self.blind_type_ == 0 and last_action.index_ == 0:
			return SE
		if last_action.index_ == 0:
			return S2
		if last_action.index_ == 4:
			return SE
		if last_action.index_ == 2:
			return S1
		
		if not state == 0 and last_action.index_ == 1:
			return SE
		if not state == 0 and last_action.index_ == 3:
			return S3
	
		# For the pre-flop, if the last action was Call (1):
		# the possible action sets can be: S2, SE
		# Handle S2 case by changing that first Call to Check (0)
		if last_action.index_ == 1:
			return SE
		
		# For the pre-flop, if the last action was Raise (3):
		# the possible action sets can be: S1, S3
		# Handle S1 case by changing that first Raise to Bet (2)
		if last_action.index_ == 3:
			return S3
				
					
				
	def add_action_history(self, action):
		self.action_history_.append(action)
				
			
			
				
		
	
		
	
	