# portfolio_app.py
import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="Kowshik's Portfolio", page_icon="💼", layout="wide")

# --- Load assets ---
profile_pic = Image.open("your_photo.jpg")  # Replace with your photo
resume_file = "Kowshik_Resume.pdf"          # Add your resume here

# --- Sidebar ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title("Kowshik BH")
    st.markdown("CSE Student | Web Developer | ML Enthusiast")
    st.download_button("📄 Download Resume", resume_file)
    st.markdown("📫 kobh22cs@cmrit.ac.in")
    st.markdown("[GitHub](https://github.com/Kowshik-bh18)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/kowshik-bh-0b750b309)")

# --- Main Sections ---
st.title("💼 Welcome to My Portfolio")

# Introduction
st.subheader("🚀 About Me")
st.write("""
I'm a Computer Science student at CMRIT, Bengaluru, passionate about building scalable solutions using Web Development, Machine Learning, and Cloud Technologies. 
""")

# Skills
st.subheader("🛠️ Skills")
st.write("""
- **Languages:** Python, Java, JavaScript, HTML, CSS  
- **Frameworks:** Django, React (Basic), Streamlit  
- **Tools & Cloud:** Git, Linux, GCP, Docker  
- **Areas of Interest:** Web Apps, LLMs, Cloud Infrastructure
""")

# Projects
st.subheader("📂 Projects")
projects = {
    "🏨 Hostel Management System": "A full-stack Django-based system to handle hostel data.",
    "🛒 E-commerce Website": "Frontend+Backend store with secure login, cart, and payments.",
    "🔐 Password Validation Tool": "Script to test and rate password strength with suggestions.",
    "🧠 LLM-based UI Research": "Research on AI-Driven UI for learning platforms (2025 Seminar).",
    "🎮 Logic Game Suite": "Django-based multi-game logic training web suite."
}
for project, desc in projects.items():
    st.markdown(f"**{project}**: {desc}")

# Contact
st.subheader("📬 Get in Touch")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thank you! Your message has been sent.")

# Footer
st.markdown("---")
st.markdown("© 2025 Kowshik BH. Made with ❤️ using Streamlit.")

# Optional: Add background music or animation using HTML/CSS (advanced)
