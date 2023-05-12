# Reactive-means-in-the-Iterated-Prisoner-s-Dilemma

These files contain all of the necessary python code to replicate the results presented in our paper "Reactive means in the Iterated Prisoner's Dilemma". A brief explanation of each file is contained in this ReadME.

# Player_Functions.py
This file contains functions for calculating all of the functions of interest including their compliments given a player's probability of cooperating after their opponent defected, a player's probability of cooperating after their opponent cooperated, an opponent's probability of cooperating after the player defected, and an opponent's probability of cooperating after the player cooperated.

# Plot_Processing.py
This file contains a function for generating the heat maps shown in Figures 1,2, and 3 in the paper.

# Sandbox.py
This file can be run to calculate different statistics about the reactive means for each of the functions of interest.

# Statistics_Functions.py
This file contains functions for calculating different statistics given a function (or functions) using integrate in the scipy package.

# Test_Code.py
This file is a workspace that can be run to test that the functions in mean_Player_Functions.py and naive_mean_Player_Functions.py are functioning correctly.  

# mean_Player_Functions.py
This file contains functions for calculating all of the reactive means given a player's probability of cooperating after their opponent defected and a player's probability of cooperating after their opponent cooperated. The formulas used are those obtained from analytical solutions. 

# naive_Statistics_Functions.py
This file contains functions for calculating different statistics given a function (or functions) overa discrete space.

# naive_mean_Player_Functions.py
This file contains functions for calculating all of the reactive means given a player's probability of cooperating after their opponent defected and a player's probability of cooperating after their opponent cooperated using integrate in the scipy package. 
