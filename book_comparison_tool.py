import streamlit as st

# Streamlit app for comparing two books
st.title("📚 Book Comparison Tool")

st.markdown("Enter details for two books to see a comparison of their themes, tone, and focus.")

# Form inputs
with st.form("book_form"):
    st.subheader("Book 1")
    title1 = st.text_input("Title (Book 1)", "Your Untethered Voice")
    author1 = st.text_input("Author (Book 1)", "Tracy Rohrer Irons")
    focus1 = st.text_input("Focus (Book 1)", "Reclaiming personal voice and truth")
    tone1 = st.text_input("Tone (Book 1)", "Reflective and healing")
    style1 = st.text_input("Style (Book 1)", "Memoir-infused, emotional narrative")
    audience1 = st.text_input("Audience (Book 1)", "Those reclaiming self after silence or self-doubt")
    themes1 = st.text_area("Themes (Book 1, comma-separated)", "authenticity, courage, resilience, inner alignment")
    comp1 = st.text_area("Complementary Elements (Book 1, comma-separated)", "Rediscovering voice, Resilience, Overcoming doubt")

    st.subheader("Book 2")
    title2 = st.text_input("Title (Book 2)", "Becoming a Legacy Leader")
    author2 = st.text_input("Author (Book 2)", "Zana Kenjar")
    focus2 = st.text_input("Focus (Book 2)", "Intentional leadership and legacy")
    tone2 = st.text_input("Tone (Book 2)", "Visionary and strategic")
    style2 = st.text_input("Style (Book 2)", "Framework-driven, motivational")
    audience2 = st.text_input("Audience (Book 2)", "Emerging and established leaders")
    themes2 = st.text_area("Themes (Book 2, comma-separated)", "authenticity, courage, leadership, impact")
    comp2 = st.text_area("Complementary Elements (Book 2, comma-separated)", "Applying vision in leadership, Influence cultivation, Purpose-driven strategy")

    submitted = st.form_submit_button("Compare Books")

if submitted:
    book1 = {
        "title": title1,
        "author": author1,
        "focus": focus1,
        "tone": tone1,
        "style": style1,
        "audience": audience1,
        "themes": [t.strip() for t in themes1.split(",")],
        "complementary": [c.strip() for c in comp1.split(",")]
    }
    
    book2 = {
        "title": title2,
        "author": author2,
        "focus": focus2,
        "tone": tone2,
        "style": style2,
        "audience": audience2,
        "themes": [t.strip() for t in themes2.split(",")],
        "complementary": [c.strip() for c in comp2.split(",")]
    }

    # Comparison logic
    def bullet_list(items):
        return "\n".join([f"- {item}" for item in items])

    shared_themes = list(set(book1['themes']) & set(book2['themes']))
    similarities = [
        "Both focus on personal growth or transformation",
        "Encourage authenticity and empowerment",
        "Authors speak from personal experience",
        "Appeal to audiences seeking meaning or purpose"
    ]
    if shared_themes:
        similarities.append(f"Shared themes: {', '.join(shared_themes)}")

    st.markdown("## 🔗 Similarities")
    st.markdown(bullet_list(similarities))

    st.markdown("## 🔍 Differences")
    st.markdown(f"""
    | Aspect | {book1['title']} | {book2['title']} |
    |--------|--------------------------|-----------------------------|
    | **Focus** | {book1['focus']} | {book2['focus']} |
    | **Tone** | {book1['tone']} | {book2['tone']} |
    | **Style** | {book1['style']} | {book2['style']} |
    | **Audience** | {book1['audience']} | {book2['audience']} |
    """)

    st.markdown("## 🎯 Common Elements & Themes")
    st.markdown(bullet_list(shared_themes) if shared_themes else "None explicitly shared.")

    st.markdown("## 🤝 Complementary Elements & Themes")
    comp_pairs = zip(book1['complementary'], book2['complementary'])
    comp_table = "| Book 1 | Book 2 |\n|--------|--------|\n"
    for a, b in comp_pairs:
        comp_table += f"| {a} | {b} |\n"
    st.markdown(comp_table)