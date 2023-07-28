import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

if __name__ == '__main__':
  st.title(f'My First Streamlit App!')

  
  # Working with media
  st.header('Working with media')
  
  st.subheader('Image')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/media/st.image)')
  st.image('resources/image.jpg', width = 420)

  st.subheader('Audio')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/media/st.audio)')
  st.audio('resources/audio.mp3')

  st.subheader('Video')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/media/st.video)')
  st.video('resources/video.mp4')

  
  # Working with text
  st.header('Working with text')

  st.subheader('Write')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/write-magic/st.write)')
  st.write(1234)
  st.write('1 + 1 = ', 2)
  st.write('Hello, *World!* :sunglasses:')
  df_1 = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, np.nan, np.inf]})
  st.write(df_1)
  df_2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
  c = alt.Chart(df_2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
  st.write(c)
  
