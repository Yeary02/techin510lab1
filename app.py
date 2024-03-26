import streamlit as st

st.set_page_config(
    page_title="Yeary - Master of Science in Technology Innovation",
    page_icon="🌕",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

# Profile picture and basic information
col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.image('profile.png', caption='Yeary')

with col2:
    st.markdown("""
    # Yeary Yuan (She/Her)
    
    - **Education:** Current MSTI student
    """)

# About section
st.markdown("## About")
st.write("""
a brief paragraph about yourself, your professional interests, and what you're passionate about.
""")

# Education section
st.markdown("## Education")
st.write("""
- **Degree:** Bachelor’s in Informatics (DS, HCI)
- **Degree:** Master’s Technology Innovation
""")

# Work Experience section
st.markdown("## Work Experience")
st.write("""
- **Position:** GIX student
  - Being a student.
""")

# Hobbies and Interests section
st.markdown("## Hobbies and Interests")
st.write("""
Hiking, 
Sleeping
""")

# Interesting Projects section
st.markdown("## Interesting Projects")
st.write("""
- [Project 1](https://www.google.com) - My 1st project.
- [Project 2](https://www.google.com) - My 2nd project.
- [Project 3](https://www.google.com) - My 3rd project.
""")