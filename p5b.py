import matplotlib.pyplot as plt
import pandas as pd

# Read dataset
data = pd.read_csv("daily_routine.csv")

# Extract columns
days = data['Days']
eating = data['Eating']
sleeping = data['Sleeping']
working = data['Working']
playing = data['Playing']

# -------- Subplot 1: Stack Plot --------
plt.subplot(2, 1, 1)
plt.stackplot(days, eating, sleeping, working, playing,
              labels=['Eating', 'Sleeping', 'Working', 'Playing'])
plt.title('Daily Routine (Stack Plot)')
plt.xlabel('Days')
plt.ylabel('Hours')
plt.legend(loc='upper left')

# -------- Subplot 2: Line Plot --------
plt.subplot(2, 1, 2)
plt.plot(days, eating, marker='o', label='Eating')
plt.plot(days, sleeping, marker='s', label='Sleeping')
plt.plot(days, working, marker='^', label='Working')
plt.plot(days, playing, marker='d', label='Playing')

plt.title('Daily Routine (Line Plot)')
plt.xlabel('Days')
plt.ylabel('Hours')
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()