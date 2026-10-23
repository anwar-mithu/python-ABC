#a module is a python file containeing functions or other code. importing lets one file use code from another file.
# %%
import statistics

latency = [0.1, 0.2, 0.3, 0.4, 0.5]

print("Mean latency:", statistics.mean(latency))
print(f"Median Latency:{statistics.median(latency)} ")
# %%
#create a database of latency of 100 random numbers between 0 and 1. Use the statistics module to calculate the mean and median of the latency values.
#value shoule be in three decimal places. Use the random module to generate the random numbers.
import random
latency = [random.uniform(0, 1) for data in range(1000)]
latency = [round(x, 3) for x in latency]
print("Mean latency:", statistics.mean(latency))
print(f"Median Latency:{statistics.median(latency)} ")
#how to run this code in the terminal
#answer: python learn_by_gpt/mod_imp.py
# %%
from statistics import mean, median
time = [0.1, 0.2, 0.3, 0.4, 0.5]
print("Mean time:", mean(time))
print(f"Median time: {median(time)}")

# %%
