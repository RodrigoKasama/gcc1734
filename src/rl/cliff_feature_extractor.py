import numpy as np
from feature_extractor import FeatureExtractor

class Actions:
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

class CliffFeatureExtractor(FeatureExtractor):
	__actions_one_hot_encoding = {
			Actions.UP:     np.array([1,0,0,0]),
			Actions.RIGHT:  np.array([0,1,0,0]),
			Actions.DOWN:   np.array([0,0,1,0]), 
			Actions.LEFT:	np.array([0,0,0,1]) 
	}

	def __init__(self, env):
		'''
		Initializes the TaxiFeatureExtractor object. 
		It adds feature extraction methods to the features_list attribute.
		'''
		self.env = env
		self.features_list = []
		self.features_list.append(self.f0)
		# self.features_list.append(self.f1)
		# self.features_list.append(self.f2)

	def get_num_features(self):
		'''
		Returns the number of features extracted by the feature extractor.
		'''
		return len(self.features_list) + self.get_num_actions()

	def get_num_actions(self):
		'''
		Returns the number of actions available in the environment.
		'''
		return len(self.get_actions())

	def get_action_one_hot_encoded(self, action):
		'''
		Returns the one-hot encoded representation of an action.
		'''
		return self.__actions_one_hot_encoding[action]

	def is_terminal_state(self, state):
		if state == 47:
			return True
		return False

	def get_actions(self):
		'''
		Returns a list of available actions in the environment.
		'''
		return [Actions.UP, Actions.RIGHT, Actions.LEFT, Actions.DOWN]
	
  
	def get_features(self, state, action):
		'''
		Takes a state and an action as input and returns the feature vector for that state-action pair. 
		It calls the feature extraction methods and constructs the feature vector.
		'''
		feature_vector = np.zeros(len(self.features_list))
		for index, feature in enumerate(self.features_list):
			feature_vector[index] = feature(state, action)

		action_vector = self.get_action_one_hot_encoded(action)
		feature_vector = np.concatenate([feature_vector, action_vector])

		return feature_vector

	def f0(self, state, action):
		'''
		This is just the bias term.
		'''
		return 1.0

	def f1(self, state, action):
		cliff_zone = [i for i in range(37, 45)]

		if any(next_state in cliff_zone for next_state in (state + 12, state + 1, state - 1)):
			return 1
		else: 
			return 0
 
	# def f2(self, state, action):
	# 	goal = [3,11]

	# 	man = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
	# 	xstate = int(state / 12)
	# 	ystate = state % 12
	# 	print(state)
	# 	print((xstate, ystate))
	# 	print(man((xstate, ystate), goal))
	# 	input()
	# 	return man((xstate, ystate), goal)
