import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np


class gym_4LocationsEnv(gym.Env):
    """
    Observation:
        Type: Box(4)
        Num	Observation                 Min         Max
        0	Location A                   0           10
        1	Location B                   0           10
        2	Location C                   0           10
        3	Location D                   0           10
        4   k                            0           10
    Actions:
        Type: Discrete(2)
        Num	Action
        0	Push cart to the left
        1	Push cart to the right
    """


    def __init__(self):

        self.visited =[]

        self.action_space = spaces.Discrete(2)
        self.observation_space = None

        self.xAxisSize = 0
        self.timer = 0

        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.k = 0

        self.seed()
        self.viewer = None
        self.state = None


        self.steps_beyond_done = None
    def inputParameters(self, aa, bb, cc, dd, kInput, timerInput, maxAxis):
        self.xAxisSize = maxAxis
        self.timer = timerInput
        self.observation_space = spaces.Box(0, self.xAxisSize, dtype=np.float32)
        self.a = aa
        self.b = bb
        self.c = cc
        self.d = dd
        self.k = kInput

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        state = self.state
        A ,B ,C ,D ,k = state
        self.time -= 1

        i f(k == A):
            reward =1
            self.visited.append(A)
        elif (k == B):
            reward = 1
            self.visited.append(B)
        elif (k == C):
            reward = 1
            self.visited.append(C)
        elif (k == D):
            reward = 1
            self.visited.append(D)
        else:
            reward = -1
        self.state = (A, B, C, D, k)

        for i in range(0, len(self.visited)):
            if (self.visited[i] == A):
                for j in range(i + 1, len(self.visited)):
                    if (self.visited[j] == B):
                        for k in range(j + 1, len(self.visited)):
                            if (self.visited[k] == C):
                                for l in range(k + 1, len(self.visited)):
                                    if (self.visited[l] == D):
                                        done = true

        if ((A not in self.visited and B not in self.visited and C not in self.visited and D not in self.visited) or (
                self.timer == 0)):
            done = false

        if done:
            reward = 1.0
        elif done == false:
            reward = 0
        elif self.steps_beyond_done is None:
            self.steps_beyond_done = 0
            reward = 1.0
        else:
            if self.steps_beyond_done == 0:
                logger.warn(
                    "You are calling 'step()' even though this environment has already returned done = True. You should always call 'reset()' once you receive 'done = True' -- any further steps are undefined behavior.")
            self.steps_beyond_done += 1
            reward = 0.0

        return np.array(self.state), reward, done, {}

    def reset(self):
        self.state = self.np_random.uniform(low=0, high=self.k, size=(4,))
        self.steps_beyond_done = None
        return np.array(self.state)

    def render(self, mode='human'):
        return None

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
