import streamlit as st

st.set_page_config(
    page_title="Yeary - Master of Science in Technology Innovation",
    page_icon="😀",
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
    - **Research Interest:** GenAI
    """)

# About section
st.markdown("## About")
st.write("""
I'm Yeary Yuan, a Master of Science in Technology Innovation (MSTI) student and a technology enthusiast with a strong interest in Generative AI (GenAI). My academic journey and passion for tech innovation drive me to explore the potential of AI in revolutionizing digital interaction and creativity. Committed to bridging the gap between innovative technology and practical application, I continuously seek out new trends and challenges in the tech world, aiming to make a significant impact on society through technology.
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
Throughout my internships, I've had the opportunity to explore various aspects of technology, from AI and algorithms to product development and digital marketing. My contributions have included streamlining workflows, enhancing data analysis, and engaging in market research, each experience enriching my understanding and application of technology in real-world scenarios. These roles have nurtured my skills in critical thinking, collaboration, and adaptability, preparing me for future challenges and opportunities in the tech industry.
""")

# Hobbies and Interests section
st.markdown("## Hobbies and Interests")
st.write("""
- **Technology Exploration**: Passionate about discovering and experimenting with the latest tech trends and tools, especially in the realm of AI and machine learning.
- **Coding Projects**: Enjoy dedicating time to personal coding projects, which allows me to apply theoretical knowledge in practical settings, and continuously improve my programming skills.
- **Reading**: Avid reader of both tech-related literature and fiction, finding joy in expanding my knowledge and immersing myself in different worlds and perspectives.
- **Outdoor Activities**: Love spending time outdoors, whether it's hiking, cycling, or simply taking a walk in nature, appreciating the balance it brings to my tech-focused life.
- **Photography**: Amateur photographer with a keen interest in capturing the beauty of everyday moments and landscapes, exploring the interplay of light and shadow.
- **Music**: Enthusiastic about exploring diverse music genres and occasionally dabbling in music production as a creative outlet.
""")

# Interesting Projects section
st.markdown("## Interesting Projects")
st.write("""
- **Mindful - AI-powered Personal Assistant**: Served as Project Lead for Mindful, an initiative aimed at enhancing daily productivity through AI. This project focused on developing a personal assistant that leverages natural language processing and machine learning to offer personalized task management and insights.

- **SitRight not Left! - Ergonomic Health Tech Solution**: As the Tech Lead, I contributed to designing a solution that uses machine learning to promote healthy sitting postures. This project combined hardware sensors and software analytics to alert users about their posture in real time, encouraging healthier habits.

- **PetMeet IOS App - Full Stack Developer**: Developed an iOS app aimed at pet owners, facilitating a social network for pet meetups and interactions. My role encompassed handling both front-end and back-end development, ensuring a seamless user experience and efficient data management.

- **Time Traveler - Web Developer**: Participated in creating an educational web application that allows users to explore historical events in an interactive timeline. My contributions focused on front-end development, utilizing JavaScript and React to create an engaging and informative experience.
""")