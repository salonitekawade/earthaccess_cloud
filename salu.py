import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt

# Create a slider widget
slider = widgets.FloatSlider(min=0, max=10, step=0.1, description='Value:')

# Create a plot
def update_plot(value):
    x = np.linspace(0, 10, 100)
    y = np.sin(x * value)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interactive Plot')
    plt.show()

# Connect the slider to the plot update function
slider.observe(update_plot, 'value')

# Display the slider and plot
display(slider)