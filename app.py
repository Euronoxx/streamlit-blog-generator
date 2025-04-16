import streamlit as st
from pathlib import Path
import markdown
from datetime import datetime

# Load custom CSS for GitHub-style
css_path = Path(__file__).parent / "templates" / "github_style.css"
with open(css_path, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📝 GitHub-Style Blog Generator")
# Blog Title
title = st.text_input("Blog Title", placeholder="Enter your blog title here...")

# Markdown Content
content = st.text_area("Write your post in Markdown:", height=300)

# Live Preview
st.subheader("🔍 Live Preview")
if content:
    html = markdown.markdown(content, extensions=["fenced_code", "codehilite"])
    st.markdown(html, unsafe_allow_html=True)
else:
    st.info("Start typing above to see preview here.")

# Save Blog
if st.button("💾 Save Blog Post"):
    if title and content:
        filename = f"posts/{title.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.md"
        with open(filename, "w") as f:
            f.write(f"# {title}\n\n{content}")
        st.success(f"Blog saved as `{filename}`")
    else:
        st.warning("Please enter a title and content.")
