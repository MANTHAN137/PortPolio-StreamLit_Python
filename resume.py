import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Manthan Dhole
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)


st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- VJTI mumbai 2nd year Student
- Strong Passion in ML and AI and also in DSA problem Solving

''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.youtube.com/channel/UCNw9-IMi_MfFrw83TC4Mx-A" target="_blank">Manthan Dhole</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disable" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')
st.markdown('''
- Join Entrance Exam(JEE) score : `96.32`%tile
- Maharashtra Common Entrace Test(Mhtcet) :`99.62`%tile
''')
txt('**B.Tech** Information Technology, *VJTI*, mumbai',
'2020-2024')
st.markdown('''
- Current GPA: `3.04`
''')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Java`,`C++`')
txt3('AppDev','`Flutter`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`')
txt3('Machine Learning', '`scikit-learn`')
###################


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/manthan-dhole-174548202/')
txt2('GitHub', 'https://github.com/MANTHAN137')
txt2('Instagram', 'https://www.instagram.com/3manthan137/')
txt2('EmailId ', 'indiakamanthan@gmail.com')

st.sidebar.title("Additional Info")
st.sidebar.info(
        "This an interactive streamlit app completely created with Python's latest library **streamlit** "
        "Do reach out to me on [LinkedIn](https://www.linkedin.com/in/manthan-dhole-174548202/) or "
        "at [Mail me](mailto:indiakamanthan@gmail.com) to know more. "
       )
