import gym
from gym import error, spaces, utils
from gym.utils import seeding

class RLEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		# self.observation_space = spaces.Box(low=np.array([0,-8,0]), high=np.array([60,0,5]), dtype=float)
		self.observation_space = spaces.Box(low=0, high=10, shape=(25,)) # observation_space = Continuous space of 25 parameters
		self.action_space = spaces.Discrete(20)                          # action_space = Set of 20 discrete actions
 
	def step(self, action):
		pass
		return 0
	
	def reset(self):
		pass
		return 0







