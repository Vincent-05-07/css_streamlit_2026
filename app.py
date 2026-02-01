import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Student Profile",
    page_icon="🎓",
    layout="centered"
)

# ---------- Background & sidebar styling ----------
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #eef2ff 0%, #ffffff 100%);
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e5e7eb 0%, #f9fafb 100%);
        border-right: 1px solid #d1d5db;
    }

    /* Sidebar text slightly darker */
    section[data-testid="stSidebar"] * {
        color: #111827;
    }

    /* Make sidebar profile image round and consistent */
    .profile-pic {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Headings size */
    .stMarkdown h1 { font-size: 30px; }
    .stMarkdown h2 { font-size: 22px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## 🎓 Student")
    st.markdown("**Programme:** Bachelor of Information and Communication Technology")
    st.markdown("**Background:** Information & Communication Networks")
    st.markdown("---")

    st.markdown("### Focus Areas")
    st.markdown("""
    - Computer Networks  
    - Data Communication  
    - Cybersecurity  
    - Data Analysis  
    - Machine Learning  
    """)

    st.markdown("---")
    st.markdown("### Contact")
    st.write("📧 Email: vincentmatemu2002@gmail.com")
    st.write("📱 Number: 060-651-3009")
    st.markdown("---")

    st.markdown("### Profile photo")
    st.image(
        "IMG_20250220_164738.jpg"
    )
    st.markdown("---")

# ---------- Main ----------
st.title("👨‍🎓 Student Portfolio")

st.header("About Me")
st.markdown("""
I am **Vincent Matemu Mthuke**, an **Honours student** with a background in **Information and Communication Networks**.  
My undergraduate studies provided strong foundations in **computer networks, data communication, and systems**, and I am currently expanding my skills through **research, data analysis, and applied computing projects**.

My academic interests focus on how **data, networks, and intelligent systems** can be combined to solve real-world problems.
""")

st.header("Academic Background")
st.markdown("""
- **Honours Degree (Current):** Computing / Information Technology  
- **Bachelor’s Degree:** Information and Communication Networks  
- **Core Skills:**  
  - Network design and analysis  
  - Python programming  
  - Data analysis & visualization  
  - Database systems  
""")

# ---------- Projects ----------
st.header("Projects & Coursework")

projects = pd.DataFrame({
    "Project": [
        "Work Integrated Learning (WIL)",
        "Network Traffic Analysis (Competition)",
        "Driver Behaviour Analysis (Competition)",
        "Data Visualization Dashboard",
        "ETL Pipeline for Movie Dataset"
    ],
    "Description": [
        "Work Integrated Learning project: produced a website and an Android app as part of placement/work integration.",
        "Analyzed network traffic patterns to detect anomalies; project submitted to a competition.",
        "Analyzed driving behaviour using sensor data; competition entry with performance metrics.",
        "Built interactive dashboards using Streamlit to explore datasets and KPIs.",
        "Cleaned and transformed raw movie data for analysis (ETL)."
    ],
    "Tools / Notes": [
        "Website (HTML/CSS/JS/Flask) + Android app (Kotlin/React Native). Add links below.",
        "Python, Wireshark, Scapy — competition entry.",
        "Python, NumPy, Matplotlib, sensor data processing — competition entry.",
        "Streamlit, Pandas, Plotly",
        "Python, Pandas"
    ]
})

st.dataframe(projects, use_container_width=True)

st.markdown("#### Work Integrated Learning — details")
st.markdown("""
- **What:** Built a website and an Android app as part of the WIL project.  
- **Website:** Add your website URL in the line below (edit this cell or add it to the repo).
- **Android app:** Add Google Play / APK / repo link below when ready.
""")

# ---------- Skills ----------
st.header("Technical Skills Overview")

skills = pd.DataFrame({
    "Skill": ["Python", "Networking", "Data Analysis", "Databases", "Web Development"],
    "Level": [4, 4, 5, 3, 3]
})

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("**Highlighted skill**")
    st.metric("Data Analysis proficiency (1–5)", "5")
with col2:
    st.markdown(" ")

chart = alt.Chart(skills).mark_bar(size=40).encode(
    x=alt.X("Skill:N", title="Skill"),
    y=alt.Y("Level:Q", title="Proficiency (1–5)", scale=alt.Scale(domain=[0, 5])),
    tooltip=["Skill", "Level"]
).properties(width=700, height=420)

st.altair_chart(chart, use_container_width=True)

# ---------- Research ----------
st.header("Research Interests")
st.markdown("""
- Network performance and optimization  
- Data-driven decision making  
- Cybersecurity and intrusion detection  
- Applied machine learning in networked systems  
""")

st.write("---")

