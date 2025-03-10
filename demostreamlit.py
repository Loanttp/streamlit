pip install streamlit
import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app.')
streamlit run my_app.py


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
