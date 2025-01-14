from timeit import default_timer as timer
import numpy as np
import pickle
from environment import Environment

class QLearningAgentTabular:

	def __init__(self, 
              env: Environment,
              decay_rate,
              learning_rate,
              gamma):

		self.env = env

		self.q_table = np.zeros((env.get_num_states(), env.get_num_actions()))
		print(f"self.q_table.shape: {self.q_table.shape}")
		
		# self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
		self.epsilon = 1.0
		self.max_epsilon = 1.0
		self.min_epsilon = 0.01
		self.decay_rate = decay_rate
		self.learning_rate = learning_rate
		self.gamma = gamma # discount rate
		self.epsilons_ = []
	
	def choose_action(self, state, is_in_exploration_mode=True):
		exploration_tradeoff = np.random.uniform(0, 1)

		if is_in_exploration_mode and exploration_tradeoff < self.epsilon:
		# exploration
			action = np.random.randint(self.env.get_num_actions())    
		else:
		# exploitation (taking the biggest Q value for this state)
			action = np.argmax(self.q_table[state, :])
		
		return action

	def update(self, state, action, reward, next_state):
		'''
		Apply update rule Q(s,a):= Q(s,a) + lr * [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
		'''
		self.q_table[state, action] = self.q_table[state, action] + self.learning_rate * (reward + self.gamma * np.max(self.q_table[next_state, :]) - self.q_table[state, action])

	def train(self, num_episodes: int):
		rewards_per_episode = []

		start_time = timer()  # Record the start time

		for episode in range(num_episodes):
	
			terminated = False
			truncated = False

			state, _ = self.env.reset()
			# print("Curr state:", state)
			state_id = self.env.get_state_id(state)
			# print("Curr state_id:", state_id)
			state = state_id

			rewards_in_episode = []
			
			total_penalties = 0
			legends_actions={0:"UP", 1:"Right", 2:"Down", 3:"Left",}
			while not (terminated or truncated):
				
				# print(f"state: {state}")
				action = self.choose_action(state)
				# print(f"Action to take: {legends_actions.get(action)}")
				
				# transição
				new_state, reward, terminated, truncated, info = self.env.step(action)
				# print("New state:", new_state)
				# print("New state_id:", new_state, "\n")
				# input("")
				new_state_id = self.env.get_state_id(new_state)
				new_state = new_state_id
				assert (not truncated)
				
				# Avaliar com o professor - por que -1? a recompensa no blackjack é -1, por exemplo
				if reward == self.env.get_penalty_value():
					total_penalties += 1

				self.update(state, action, reward, new_state)

				if (terminated or truncated):
					# Reduce epsilon to decrease the exploration over time
					self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * np.exp(-self.decay_rate * episode)
					self.epsilons_.append(self.epsilon)

				state = new_state
					
				rewards_in_episode.append(reward)
			# input("")
			mean_reward = np.mean(rewards_in_episode)
			rewards_per_episode.append(mean_reward)

			if episode % 1000 == 0:
				end_time = timer()  # Record the end time
				execution_time = end_time - start_time
				n_actions = len(rewards_in_episode)
				print(f"Stats for episode {episode}/{num_episodes}:") 
				print(f"\tNumber of actions: {n_actions}")
				print(f"\tMean reward: {mean_reward:#.2f}")
				print(f"\tExecution time: {execution_time:.2f}s")
				print(f"\tTotal penalties: {total_penalties}")
				start_time = end_time

		return rewards_per_episode

	def save(self, filename):
		# open a file, where you ant to store the data
		file = open(filename, 'wb')

		# dump information to that file
		pickle.dump(self, file)

		# close the file
		file.close()

	@staticmethod
	def load_agent(filename):
		# open a file, where you stored the pickled data
		file = open(filename, 'rb')

		# dump information to that file
		agent = pickle.load(file)

		return agent
