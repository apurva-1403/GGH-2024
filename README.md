# GGH-2024
Optimization of the design of a Network-on-Chip (NOC) for System-on-Chip (SoC) architectures

## Time complexity:

* Parse_interface_monitor_output: O(n)
* calculate_average_latency: O(n)
* calculate_bandwidth: O(n)
* process_simulator_output: O(n)
*  **Overall Time Complexity:** O(n)
  
Since all the dominant operations have the same time complexity (O(n)), the overall time complexity of the code is: O(n)
This indicates that the execution time of the code grows linearly with the size of the simulator output data.

## Design Document for RL: Using Reinforcement Learning for Simulator Output Analysis Optimization
This document outlines a design for using reinforcement learning (RL) to optimize the parameters used in processing simulator output.

### RL Framework

**States:**

* The state will be represented by a dictionary containing information about the current processing stage:
    * `trace`: The current trace generated by `parse_interface_monitor_output`.
    * `data_width`: The current data width value.
    * Additional parameters to be optimized in the future.

**Actions:**

* The agent can take the following actions:
    * Update `data_width`: Choose a new value from a predefined set of possible data width values.
    * Do nothing: Maintain the current state.

**Rewards:**

* The reward function will be designed to encourage the agent to find a configuration that balances two objectives:
    * **Minimize average latency:** This can be achieved by increasing the data width (assuming wider data paths allow for faster transfers).
    * **Maximize bandwidth:** This can be achieved by finding the optimal data width that allows for efficient data transfer without wasting resources with excessively wide paths.

**Possible RL Algorithm:**

* **Actor-Critic (A3C):** This is a well-suited algorithm for this scenario because it combines the strengths of both policy-based (actor) and value-based (critic) approaches. The actor learns the optimal action (data width adjustment) to take in a given state, while the critic evaluates the long-term value of those actions. A3C is efficient for handling continuous state spaces (like the potential addition of future parameters) and allows for parallel learning which can be beneficial for this type of problem.

### Implementation Considerations

* **Environment:** The environment will consist of the simulator output processing functions (`parse_interface_monitor_output`, `calculate_average_latency`, and `calculate_bandwidth`). The agent interacts with this environment by providing actions (data width adjustments) and receives rewards based on the calculated latency and bandwidth.
* **Reward Function Design:** The reward function needs careful design to achieve the desired balance between minimizing latency and maximizing bandwidth. This may involve weighted combinations of the calculated values or functions based on specific performance targets.
* **Hyperparameter Tuning:** The A3C algorithm itself has hyperparameters (learning rate, discount factor, etc.) that will need to be tuned for optimal performance in this specific scenario.

### Benefits of using RL

* **Automatic Optimization:**  The RL agent can learn the optimal configuration for processing simulator output data, adapting to different workloads and scenarios.
* **Flexibility:** The framework allows for easy integration of additional parameters for optimization in the future.

### Limitations

* **Computational Cost:** Training an RL agent can be computationally expensive, requiring a significant number of iterations through the simulator output processing functions.
* **Exploration vs. Exploitation:**  The agent needs to balance exploring different data width values (exploration) with exploiting the knowledge gained so far (exploitation) to find the optimal configuration.

This design document proposes a framework for using RL to optimize the parameters used in processing simulator output data. By combining A3C with a well-designed reward function, the agent can learn to balance minimizing latency and maximizing bandwidth. This approach offers automatic optimization and flexibility for future parameter considerations, but requires careful consideration of computational costs and exploration/exploitation trade-offs.
