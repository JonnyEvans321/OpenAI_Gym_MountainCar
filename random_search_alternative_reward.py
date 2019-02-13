import gym
import numpy as np
import random

max_steps=500
max_iterations=10000
play_mode=False #set whether we want to watch every iteration play out

def train_episode(env, play):
	observation = env.reset()
	total_distance = None
	done=False
	action_memory=[]
	while done==False:
		#randomly select whether to press left, right or nothing at each step	 
		action = random.randint(0,2)
		
		action_memory.append(action)
		#play the iteration if in play mode
		if play:
			env.render()
		#take a step to find the observation and current distance after the action
		observation, distance, done, info = env.step(action)

		#observation[0] is the distance the cart is to the right. If this is greater than it has been before, update it.
		if total_distance is None or observation[0]>total_distance:
			total_distance=observation[0]
	return total_distance,action_memory

def test_episode(actions):
	env.reset()
	env._max_episode_steps = max_steps
	
	done=False
	i=0
	while done==False:
		#play the action recorded from the episode with the best distance
		env.render()
		observation, distance, done, info = env.step(actions[i])		
		i+=1
		
if __name__ == '__main__':
	# use gym environment: MountainCar-v0
	# https://github.com/openai/gym/wiki/MountainCar-v0
	env = gym.make('MountainCar-v0')
	env._max_episode_steps = max_steps
	  
	best_distance = None
	for x in range(max_iterations):	 
		#run an epsiode and record the distance gained
		total_distance,action_memory = train_episode(env,play_mode)
		#if its better than the previous best distance, save the params and distance value
		if best_distance==None or total_distance > best_distance:
			best_distance = total_distance
			best_action_memory=action_memory
			print('Episode: ',x,' Best distance:',best_distance)
			
		#stop training early if it reaches the flag
		if best_distance>0.6:
			print('Course completed!')
			break
			
	#%% play the best model
	for i in range(10):
		test_episode(best_action_memory)
	test_episode(best_action_memory)