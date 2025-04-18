import streamlit as st
import openai
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# Title and intro
st.title("📚 Book Comparison Tool (AI-Powered)")
st.markdown("Enter two book titles and authors, and let AI handle the rest.")

# Form to input titles and authors
with st.form("book_form"):
    st.subheader("Book 1")
    title1 = st.text_input("Title (Book 1)", "Your Untethered Voice")
    author1 = st.text_input("Author (Book 1)", "Tracy Rohrer Irons")

    st.subheader("Book 2")
    title2 = st.text_input("Title (Book 2)", "Becoming a Legacy Leader")
    author2 = st.text_input("Author (Book 2)", "Zana Kenjar")

    submitted = st.form_submit_button("Compare Books")

# OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_text_image(text):
    # Create a simple image from the comparison text
    width, height = 800, 1000
    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Split text into lines and wrap
    lines = []
    for line in text.split('\n'):
        while len(line) > 100:
            idx = line.rfind(' ', 0, 100)
            if idx == -1:
                idx = 100
            lines.append(line[:idx])
            line = line[idx:].lstrip()
        lines.append(line)

    y_text = 10
    for line in lines:
        draw.text((10, y_text), line, fill=(0, 0, 0), font=font)
        y_text += 15

    return image

if submitted:
    with st.spinner("Analyzing books with AI..."):
        prompt = f"""
Compare the following two books in terms of their similarities, differences, common themes, and complementary themes:

Book 1:
Title: {title1}
Author: {author1}

Book 2:
Title: {title2}
Author: {author2}

Include key aspects such as focus, tone, style, audience, and overall message. Present your findings in a detailed, thoughtful, blog-style analysis. Then, recommend 2-3 fiction and 2-3 non-fiction books a reader might enjoy based on the comparison — as a follow-up section titled: '📚 If You Liked These Books, You Might Also Like...'
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a literary analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1800
            )
            ai_output = response.choices[0].message.content

            st.markdown("## 📖 Comparison Analysis")
            st.markdown(f"""<div style='background-color:#f9f9f9;padding:15px;border-radius:10px;border:1px solid #ddd;'>
            <p style='font-family:sans-serif;font-size:16px;white-space:pre-wrap'>{ai_output}</p>
            </div>""", unsafe_allow_html=True)

            text_bytes = ai_output.encode('utf-8')
            st.download_button(
                label="📥 Download as Text File",
                data=text_bytes,
                file_name="book_comparison.txt",
                mime="text/plain"
            )

            img = create_text_image(ai_output)
            img_bytes = BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            st.download_button(
                label="🖼️ Download as Shareable Graphic (PNG)",
                data=img_bytes,
                file_name="book_comparison.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")
