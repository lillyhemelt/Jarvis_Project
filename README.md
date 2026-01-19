# Jarvis_Project
PROJECT: Jarvis Core
Author: Lilly Hemelt
Field: Artificial Intelligence/Neural Networks

Project Overview
Jarvis Core is a modular AI framework designed to simulate a cognitive assistant.
Unlike basic linear scripts this project utilizes PyTorch for neural network management and is built with a decoupled architecture to seperate sensory input from logical processing

System Architecture
The project id fivided into four primary cognitive modules:
Perception: Handles data ingestion and initial environmental analysis
Cognition: The "brain" of the system where decision-making logic resides
Expression: Manages the output layer and system feedback loops
Actions: Translates cognitive decisions into executable system commands

Technical Implication
Deep Learning Framework: Built using PyTorch with native support for CUDA acceleration to optimize tensor operations on compatible GPUs
NLP Pipeline: Feas a custo SimpleTokenizer to handle vocabulary mapping
and text-to-tensor conversation
Persistence: Implements state-saving and loading via .pth files, allowing for iterative training and model evaluation (model.eval())
