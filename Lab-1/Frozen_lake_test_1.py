import gymnasium as gym

# Create the FrozenLake environment
env = gym.make("FrozenLake-v1", is_slippery=True,render_mode="human")

# Number of episodes
num_episodes = 10

for episode in range(num_episodes):
    state = env.reset()[0]
    done = False
    steps = 0
    
    while not done:
        action = env.action_space.sample()  # Take a random action
        next_state, reward, done, truncated, info = env.step(action)
        print(f"Episode: {episode+1}, Step: {steps+1}, State: {state}, Action: {action}, Next State: {next_state}, Reward: {reward}, Done: {done}")
        state = next_state
        steps += 1

env.close()
