from environment import Environment

class FrozenLakeEnviroment(Environment):
	# Namespace(num_episodes=60000, env_name='FrozenLake-v1', decay_rate=0.0001, learning_rate=0.01, gamma=0.8)
	def __init__(self, env):
		super().__init__(env)
		"""
			The game starts with the player at location [0,0] of the frozen lake grid world with the goal located at far extent of the world e.g. [3,3] for the 4x4 environment.
            Holes in the ice are distributed in set locations when using a pre-determined map or in random locations when a random map is generated.
            The player makes moves until they reach the goal or fall in a hole.
            The lake is slippery (unless disabled) so the player may move perpendicular to the intended direction sometimes (see is_slippery).
  		"""
		self.penalty_value = 0	

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

	def get_penalty_value(self):
		return self.penalty_value
