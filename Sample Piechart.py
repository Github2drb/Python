import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 8))  # Adjust the figure size

# Create a pie chart
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# Add a title with alignment
ax.set_title('Distribution of Categories', loc='center', fontsize=16, pad=10)

# Add a legend with alignment
ax.legend(
    labels, 
    loc='best',  # 'best' automatically places the legend in the best location
    bbox_to_anchor=(1.05, 0.69),  # Position the legend outside the plot area
    fontsize=12, 
    title="Categories", 
    title_fontsize='8', 
    shadow=True
)

# Optionally, adjust subplot parameters
plt.subplots_adjust(left=0.1, right=0.4, top=1, bottom=0.5)  # Adjust the margins to make space for the legend

# Optional: Improve the appearance of the text in the pie chart
for text in texts:
    text.set_fontsize(8)
for autotext in autotexts:
    autotext.set_fontsize(8)

# Show the pie chart
plt.show()
