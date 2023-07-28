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

  
  st.divider()


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
  
  st.subheader('Markdown')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.markdown)')
  st.markdown('Streamlit is **_really_ cool**.')
  st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
  st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

  st.subheader('Title')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.title)')

  st.subheader('Header')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.header)')

  st.subheader('Subheader')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.subheader)')

  st.subheader('Caption')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.caption)')
  st.caption('This is a string that explains something above.')
  st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

  st.subheader('Code')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.code)')
  code = '''
  class HelloWorld {
      public static void main(String[] args) {
          System.out.println("Hello, World!"); 
      }
  }
  '''
  st.code(code, language = 'java')

  st.subheader('Text')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.text)')
  st.text('This is some text.')

  st.subheader('Latex')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.latex)')
  st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
  ''')

  st.subheader('Divider')
  st.markdown('API Reference: [here](https://docs.streamlit.io/library/api-reference/text/st.divider)')


  st.divider()


  #   