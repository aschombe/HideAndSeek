This project is a machine learning hide and seek experiment.
The goal is to train two different agents to play hide and seek against each other.
The hiders and seekers are trained in a 2D environment with a top-down view.
The hiders are trained to hide behind objects and the seekers are trained to find the hiders.
The hiders are trained to maximize their survival time and the seekers are trained to minimize the survival time of the hiders.

The main file for training is simulate.py.
It generates a models folder, with subfolders named for time of execution.
Inside of those subfolders are a hider and seeker model for every 10th generation starting with the 0th.
