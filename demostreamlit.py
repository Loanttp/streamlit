# -*- coding: utf-8 -*-
"""demostreamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lByLe2JbqQg47Q58Cx3AMRYXmA8KGKtv
"""

pip install bokeh

!pip install streamlit # install the missing module
import streamlit as st

from bokeh.plotting import figure, show

# Our main plotting package (must have explicit import of submodules)
import bokeh.io
import bokeh.plotting

# Enable viewing Bokeh plots in the notebook
bokeh.io.output_notebook()

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]
#Next, update the title for your plot by changing the string for the title argument in the figure() function:

# create a new plot with a title and axis labels
p3 = figure(title="Multiple line example", x_axis_label='x', y_axis_label='y')
#Finally, add more calls to the line() function:

# add multiple renderers
p3.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
p3.line(x, y2, legend_label="Rate", color="red", line_width=2)
p3.line(x, y3, legend_label="Objects", color="green", line_width=2)

# show the results
show(p3)