import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Image Processing Web Demo",
    page_icon=":eye:",
    layout="wide",
)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# bootstrap 4 collapse example
components.html(
    """
    <style>
      * {
          margin: 0;
          padding: 0;
          font-family: Arial, Helvetica, sans-serif;
      }
      .header {
         font-size: 40px;
         text-align: center;
      }
    </style>
    <div class="header">
      The CVU Need
      <a href="localhost:8501/about">About us<a/>
    </div>
    """,
    height=200,
)

# st.write("# Welcome to Streamlit! 👋")

# st.sidebar.success("Select a demo above.")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )

# import streamlit as st
# import numpy as np

# with st.container():
#    st.write("This is inside the container")

#    # You can call any Streamlit command, including custom components:
#    st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")