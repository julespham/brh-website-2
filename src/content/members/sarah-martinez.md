---
name: "Sarah Martinez"
role: "AI/ML Research Scientist"
card-graphic-builtin: "code"
card-text: "CODE"
featured: true
skills: ["PyTorch", "Python", "Deep Learning", "Research"]
github: "sarah-ml"
linkedin: "sarahmartinez"
projects: ["Robot Learning Lab", "Manipulation RL"]
---

# Sarah Martinez - AI/ML Research Scientist

MIT Computer Science PhD specializing in **reinforcement learning for robotic manipulation**. Sarah leads our weekly machine learning study group and helps members integrate AI into their robotics projects.

## Research Focus

Sarah's research at MIT focuses on enabling robots to learn complex manipulation tasks through interaction with their environment:

- **Sample-efficient reinforcement learning** for robotic tasks
- **Sim-to-real transfer** for training policies in simulation
- **Multi-task learning** for generalizable robot behaviors

## Teaching & Mentorship

### Weekly ML Study Group
Every Tuesday evening, Sarah runs study sessions covering:
- Deep reinforcement learning fundamentals
- Computer vision for robotics
- Neural network architectures for control

```python
# Example RL training code Sarah teaches
import torch
import gym

class RobotPolicyNetwork(torch.nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Linear(state_dim, 256),
            torch.nn.ReLU(),
            torch.nn.Linear(256, action_dim)
        )
    
    def forward(self, state):
        return self.network(state)
```

## Community Impact

Sarah has helped over 20 members integrate machine learning into their projects, from computer vision for drone navigation to predictive maintenance for manufacturing equipment.

### Notable Student Projects
- Autonomous trash sorting robot using computer vision
- Predictive failure detection for 3D printers
- Gesture-controlled robotic arm using deep learning

## Publications

- "Sample-Efficient Robot Learning via Model-Based RL" - ICRA 2024
- "Bridging Sim-to-Real Gap in Manipulation" - RSS 2023
- "Multi-Task Learning for Robotic Assembly" - IROS 2023