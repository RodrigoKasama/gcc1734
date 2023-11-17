from environment import Environment

class CliffEnviroment(Environment):
    # Namespace(num_episodes=60000, env_name='CliffWalking-v0', decay_rate=0.0001, learning_rate=0.1, gamma=0.616)
	def __init__(self, env):
		super().__init__(env)
		"""
			There are 3 x 12 + 1 possible states. The player cannot be at the cliff, nor at the goal as the latter results in the end of the episode. What remains are all the positions of the first 3 rows plus the bottom-left cell.
			The observation is a value representing the player's current position as
   				current_row * nrows + current_col (where both the row and col start at 0).
			For example, the stating position can be calculated as follows: 3 * 12 + 0 = 36.
			The observation is returned as an int().
  		"""
		# self.env.state_id = 36 -> Posição inicial?
		# self.xstate = int(self.env.observation_space.n % 12)
		# self.ystate = int(self.env.observation_space.n / 12)
		
  
	def get_num_states(self):
		return self.env.observation_space.n

	def get_num_actions(self):
		return self.env.action_space.n

	def get_state_id(self, state):
    	# Área crítica   
		return state

	def get_random_action(self):
		return self.env.action_space.sample()
		pass
