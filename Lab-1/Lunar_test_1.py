import gymnasium as gym

# First, we create our environment called LunarLander-v2
env = gym.make("LunarLander-v2",render_mode="human")
# Then we reset this environment
observation, info = env.reset()
env.render()
for _ in range(200):
  # Take a random action
  action = env.action_space.sample()
  print("Action taken:", action)

  # Do this action in the environment and get
  # next_state, reward, terminated, truncated and info
  observation, reward, terminated, truncated, info = env.step(action)

  # If the game is terminated (in our case we land, crashed) or truncated (timeout)
  if terminated or truncated:
      # Reset the environment
      print("Environment is reset")
      observation, info = env.reset()

env.close()