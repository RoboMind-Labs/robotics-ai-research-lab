# Papers & References - Robotics AI Research Lab

## Essential Reading List

This document curates important papers, textbooks, and resources organized by research area and learning stage.

---

## Stage 1: Mathematical Foundations

### Linear Algebra & Matrices

**Textbooks:**
- Strang, G. (2016). "Linear Algebra and Its Applications" (5th ed.)
  - Best for intuition and practical understanding
  - Free online course: MIT 18.06 Linear Algebra

- Axler, S. (2015). "Linear Algebra Done Right" (3rd ed.)
  - Rigorous mathematical approach
  - Emphasizes concepts over computations

**Papers:**
- Golub, G. H., & Van Loan, C. F. (2013). "Matrix computations" (4th ed.)
  - Comprehensive reference for numerical linear algebra
  - Standard textbook in the field

### Coordinate Transformations & Kinematics

**Core References:**
- Craig, J. J. (2009). "Introduction to Robotics: Mechanics and Control" (3rd ed.)
  - Chapter 2-3: Spatial Descriptions and Transformations
  - Chapter 4-5: Manipulator Kinematics

- Lynch, K. M., & Park, F. C. (2017). "Modern Robotics"
  - Chapter 2: Configuration Space
  - Chapter 3: Rigid-Body Motions
  - Chapter 4: Forward Kinematics

### Optimization & Calculus

**Textbooks:**
- Boyd, S., & Vandenberghe, L. (2004). "Convex Optimization"
  - Definitive reference for optimization
  - Free PDF available online

- Nocedal, J., & Wright, S. J. (2006). "Numerical Optimization"
  - Gradient descent and related methods
  - Practical optimization algorithms

---

## Stage 2: Machine Learning Fundamentals

### Regression & Classification

**Core Textbooks:**
- Géron, A. (2019). "Hands-On Machine Learning" (2nd ed.)
  - Practical, implementation-focused
  - Chapters 4-5: Training Linear/Logistic Models

- Bishop, C. M. (2006). "Pattern Recognition and Machine Learning"
  - Comprehensive theoretical foundation
  - Chapter 3: Linear Models for Regression
  - Chapter 4: Linear Models for Classification

**Key Papers:**
- Nesterov, Y. (1983). "A method for solving the convex programming problem with convergence rate O(1/k²)"
  - Momentum in gradient descent
  - Nesterov momentum

### Optimization for Machine Learning

**Papers:**
- Kingma, D. P., & Ba, J. (2015). "Adam: A method for stochastic optimization"
  - Most widely used adaptive optimizer
  - PyTorch/TensorFlow default

- Ruder, S. (2016). "An overview of gradient descent optimization algorithms"
  - Comprehensive survey of optimization methods
  - Excellent review article

---

## Stage 3: Deep Learning

### Fundamentals

**Textbooks:**
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). "Deep Learning"
  - Standard deep learning textbook
  - Chapter 6: Deep Feedforward Networks
  - Chapter 7: Regularization

- LeCun, Y., Bengio, Y., & Hinton, G. E. (2015). "Deep Learning" (Nature Review)
  - Accessible overview of deep learning
  - Historical perspective

### Convolutional Neural Networks

**Landmark Papers:**
- LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). "Gradient-based learning applied to document recognition"
  - LeNet: First CNN for digit recognition
  - Foundation of modern deep learning

- Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet classification with deep convolutional neural networks"
  - AlexNet: Breakthrough in computer vision
  - Modern deep learning era begins

- He, K., Zhang, X., Ren, S., & Sun, J. (2016). "Deep residual learning for image recognition"
  - ResNet: Skip connections
  - Enabled training of very deep networks

### Recurrent Neural Networks

**Papers:**
- Hochreiter, S., & Schmidhuber, J. (1997). "Long short-term memory"
  - LSTM architecture
  - Solves vanishing gradient problem

- Cho, K., et al. (2014). "Learning phrase representations using RNN encoder-decoder for statistical machine translation"
  - GRU architecture
  - Gated recurrent units

---

## Stage 4: Computer Vision

### Image Processing & Features

**Textbooks:**
- Forsyth, D., & Ponce, J. (2012). "Computer Vision: A Modern Approach" (2nd ed.)
  - Comprehensive vision textbook
  - Chapters 1-4: Fundamentals

- Szeliski, R. (2010). "Computer Vision: Algorithms and Applications"
  - Practical implementation focus
  - Excellent for applied vision

### Deep Learning for Vision

**Key Papers:**
- Simonyan, K., & Zisserman, A. (2015). "Very deep convolutional networks for large-scale image recognition"
  - VGG networks: Architecture principles
  - Systematic network depth study

- Ren, S., He, K., Girshick, R., & Sun, J. (2016). "Faster R-CNN: Towards real-time object detection with region proposal networks"
  - Object detection foundation
  - Region-based CNN

### 3D Computer Vision

**Papers:**
- Hartley, R., & Zisserman, A. (2003). "Multiple view geometry in computer vision" (2nd ed.)
  - 3D reconstruction from images
  - Epipolar geometry and structure from motion

- Newcombe, R. A., et al. (2011). "KinectFusion: Real-time dense surface mapping and tracking"
  - Real-time 3D reconstruction
  - Sensor fusion for robotics

---

## Stage 5: Robotics Fundamentals

### Kinematics & Dynamics

**Core References:**
- Corke, P. I. (2017). "Robotics, Vision and Control" (2nd ed.)
  - MATLAB/Python implementations
  - Very practical approach
  - Chapters 1-4: Kinematics and Dynamics

### Forward Kinematics

**Papers:**
- Pieper, D. L. (1968). "The kinematics of manipulators under computer control"
  - Classical reference for forward kinematics
  - DH parameters foundation

- Hartenberg, R. S., & Denavit, J. (1955). "A kinematic notation for lower-pair mechanisms based on matrices"
  - Denavit-Hartenberg parameters
  - Standard in robotics

### Inverse Kinematics

**Papers:**
- Pieper, D. L., & Roth, B. (1969). "The kinematics of manipulators under computer control"
  - Analytical inverse kinematics
  - 6-DOF arm solutions

---

## Stage 6: Control Theory

### Fundamentals

**Textbooks:**
- Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2015). "Feedback Control of Dynamic Systems" (7th ed.)
  - Standard control textbook
  - PID and state-space control

- Ogata, K. (2010). "Modern Control Engineering" (5th ed.)
  - Rigorous control theory
  - Chapters 1-4: Basics and state-space

### Linear Quadratic Control

**Papers:**
- Kalman, R. E. (1960). "Contributions to the theory of optimal control"
  - Linear Quadratic Regulator (LQR)
  - Optimal control foundation

- Kwakernaak, H., & Sivan, R. (1972). "Linear optimal control systems"
  - Comprehensive LQR treatment
  - Reference textbook

---

## Stage 7: Motion Planning

### Path Planning Algorithms

**Papers:**
- Latombe, J. C. (1991). "Robot Motion Planning" (Kluwer)
  - Comprehensive planning textbook
  - Roadmaps and cell decomposition

- Kavraki, L. E., Svestka, P., Latombe, J. C., & Overmars, M. H. (1996). "Probabilistic roadmaps for path planning in high-dimensional configuration spaces"
  - PRM algorithm
  - Sampling-based planning foundation

- LaValle, S. M. (2006). "Planning algorithms" (Online book)
  - Rapidly-exploring random trees (RRT)
  - Comprehensive planning algorithms reference

### Trajectory Optimization

**Papers:**
- Schulman, J., et al. (2014). "Finding locally optimal, collision-free trajectories with sequential convex optimization"
  - CHOMP algorithm
  - Real-time trajectory optimization

---

## Stage 8: Reinforcement Learning

### Fundamentals

**Textbooks:**
- Sutton, R. S., & Barto, A. G. (2018). "Reinforcement Learning: An Introduction" (2nd ed.)
  - Definitive RL textbook
  - Chapter 3-4: MDPs, Bellman equations
  - Chapter 5-6: Monte Carlo and TD methods

- Russell, S. J., & Norvig, P. (2020). "Artificial Intelligence: A Modern Approach" (4th ed.)
  - Chapters 21-23: Learning and Reinforcement Learning

### Algorithms

**Papers:**
- Watkins, C. J., & Dayan, P. (1992). "Q-learning"
  - Q-learning algorithm
  - Model-free RL foundation

- Williams, R. J. (1992). "Simple statistical gradient-following algorithms for connectionist reinforcement learning"
  - REINFORCE algorithm
  - Policy gradient methods

- Konda, V. R., & Tsitsiklis, J. N. (2000). "Actor-critic algorithms"
  - Actor-critic framework
  - Advantage estimation

---

## Stage 9: Deep Reinforcement Learning

### Deep Q-Networks

**Papers:**
- Mnih, V., et al. (2013). "Playing Atari with Deep Reinforcement Learning"
  - DQN algorithm
  - Deep RL breakthrough paper

- Mnih, V., et al. (2015). "Human-level control through deep reinforcement learning"
  - DQN improvements (target networks, replay)
  - Nature publication

### Policy Gradient Methods

**Papers:**
- Schulman, G., Levine, S., Moritz, P., Jordan, M. I., & Abbeel, P. (2015). "Trust region policy optimization"
  - TRPO algorithm
  - Natural policy gradient

- Schulman, G., Wolski, F., Dhariwal, P., Radford, A., & Openai, K. (2017). "Proximal policy optimization algorithms"
  - PPO algorithm
  - Most practical deep RL method

- Mnih, V., et al. (2016). "Asynchronous methods for deep reinforcement learning"
  - A3C algorithm
  - Multi-worker training

---

## Stage 10: Robot Learning & Autonomous Systems

### Learning from Demonstration

**Papers:**
- Abbeel, P., & Ng, A. Y. (2004). "Apprenticeship learning via inverse reinforcement learning"
  - Inverse RL
  - Learning reward functions

- Bain, A., & Sammut, C. (1999). "A framework for behavioural cloning"
  - Behavior cloning
  - Direct imitation learning

### Robot Learning

**Papers:**
- Levine, S., et al. (2016). "End-to-End Training of Deep Visuomotor Policies"
  - Vision-based robot control
  - Learning from robot interaction data

- Finn, C., Abbeel, P., & Levine, S. (2017). "Model-agnostic meta-learning for fast adaptation of deep networks"
  - MAML for robot learning
  - Few-shot learning

- Tobin, J., Fong, R., Ray, A., Schneider, J., Zaremba, W., & Abbeel, P. (2017). "Domain randomization for transferring deep neural networks from simulation to the real world"
  - Sim-to-real transfer
  - Addressing domain gap

### Autonomous Systems

**Papers:**
- Thrun, S., Burgard, W., & Fox, D. (2005). "Probabilistic Robotics"
  - Comprehensive probabilistic methods
  - Localization, mapping, planning

- Khatib, O. (1986). "Real-time obstacle avoidance for manipulators and mobile robots"
  - Potential fields
  - Real-time planning

---

## Recommended Reading Order

### For New Learners
1. Strang's Linear Algebra course (MIT 18.06)
2. Corke's Robotics, Vision and Control (Chapters 1-4)
3. Géron's Hands-On Machine Learning
4. Goodfellow's Deep Learning textbook
5. Sutton & Barto's Reinforcement Learning

### For Roboticists
1. Craig's Introduction to Robotics
2. Lynch & Park's Modern Robotics
3. Thrun's Probabilistic Robotics
4. Sutton & Barto's Reinforcement Learning
5. Recent deep RL papers (Nature, NeurIPS)

### For Vision Researchers
1. Szeliski's Computer Vision
2. Hartley & Zisserman's Multiple View Geometry
3. Bishop's Pattern Recognition and Machine Learning
4. Krizhevsky et al. AlexNet paper
5. Recent vision papers (CVPR, ICCV)

---

## OpenAccess Resources

### Free Textbooks & Courses
- **MIT OpenCourseWare**: Linear Algebra (18.06), Circuits (6.002)
- **Stanford**: CS231N (CNN for Visual Recognition)
- **UC Berkeley**: CS294 (Deep Reinforcement Learning)
- **Boyd's Convex Optimization**: Free PDF available
- **Szeliski's Computer Vision**: Free PDF available
- **LaValle's Planning Algorithms**: Free PDF available

### Paper Access
- **arXiv.org**: Preprints of most recent papers
- **Google Scholar**: Search and find papers
- **Papers With Code**: Implementation guides for papers
- **Semantic Scholar**: AI-powered paper search

---

## Citation Guidelines

### Citing This Lab
```bibtex
@misc{robotics_ai_lab,
  title={Robotics AI Research Lab},
  author={Your Name},
  year={2024},
  howpublished={\url{https://github.com/yourusername/robotics-ai-research-lab}}
}
```

### Reference Format
Use IEEE or ACM format for consistency. Examples:

**Journal Article:**
[1] Author(s), "Title," Journal, vol. #, no. #, pp. pp, Month Year.

**Conference Paper:**
[2] Author(s), "Title," in Proceedings of Conference, City, Country, Month Year.

**Book:**
[3] Author(s), Title, Edition ed. Publisher, Year.

---

**Last Updated**: 2024-09-04  
**Collection Status**: Core papers curated  
**Next Update**: As new papers are explored
