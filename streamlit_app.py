import streamlit as st

if __name__ == '__main__':
  st.title(f'My First Streamlit App!')
  
  # Working with media
  st.header('Working with media')
  
  st.subheader('Images')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/media/st.image)')
  st.image('resources/image.jpg', width = 250)

  st.subheader('Audio')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/media/st.audio)')
  st.audio('resources/audio.mp3')
