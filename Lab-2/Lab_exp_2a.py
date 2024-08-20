import gymnasium as gym
import time

# Creating the Frozen Lake environment with custom parameters
env = gym.make(
    "FrozenLake-v1",
    render_mode="human",
    map_name="4x4",            # Optional argument to specify map size
    is_slippery=False,          # Optional argument to make the environment slippery
)

# Reset the environment to the starting state
state, _ = env.reset()
env.render()

# Example policy for demonstration purposes
def random_policy(state):
    return env.action_space.sample()

# Simulate the environment using the random policy
num_steps = 10  # Define the number of steps you want to simulate
for step in range(num_steps):
    action = random_policy(state)
    next_state, reward, terminated, truncated, info = env.step(action)
    env.render()
    time.sleep(0.5)  # Adding a delay for better visualization

    # Print detailed information at each step
    print(f"Step: {step + 1}")
    print(f"State: {state}")
    print(f"Action: {action}")
    print(f"Next State: {next_state}")
    print(f"Reward: {reward}")
    print(f"Terminated: {terminated}")
    print(f"Truncated: {truncated}")
    print(f"Info: {info}")
    print("---------")

    state = next_state
    if terminated or truncated:
        print(f"Episode finished after {step + 1} timesteps")
        break

env.close()
