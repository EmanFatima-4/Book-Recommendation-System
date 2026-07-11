import streamlit as st
import pandas as pd

# -------------------------
# Dataset (6+ books per genre)
# -------------------------
data = {
    "Title": [
        "Harry Potter", "The Hobbit", "Lord of the Rings", "Percy Jackson", "Game of Thrones", "Eragon",
        "Dune", "Ender's Game", "The Martian", "Foundation", "Neuromancer", "Ready Player One",
        "1984", "Brave New World", "Hunger Games", "Fahrenheit 451", "Divergent", "Maze Runner",
        "Da Vinci Code", "Angels & Demons", "Gone Girl", "Sherlock Holmes", "Girl with Dragon Tattoo", "Big Little Lies",
        "Atomic Habits", "Deep Work", "Power of Habit", "Think and Grow Rich", "Can't Hurt Me", "Subtle Art"
    ],
    "Author": [
        "J.K. Rowling", "Tolkien", "Tolkien", "Rick Riordan", "George R.R. Martin", "Christopher Paolini",
        "Frank Herbert", "Orson Scott Card", "Andy Weir", "Isaac Asimov", "William Gibson", "Ernest Cline",
        "George Orwell", "Aldous Huxley", "Suzanne Collins", "Ray Bradbury", "Veronica Roth", "James Dashner",
        "Dan Brown", "Dan Brown", "Gillian Flynn", "Arthur Conan Doyle", "Stieg Larsson", "Liane Moriarty",
        "James Clear", "Cal Newport", "Charles Duhigg", "Napoleon Hill", "David Goggins", "Mark Manson"
    ],
    "Genre": (
        ["Fantasy"] * 6 +
        ["Sci-Fi"] * 6 +
        ["Dystopian"] * 6 +
        ["Mystery"] * 6 +
        ["Self-help"] * 6
    ),
    "Rating": [
        4.5, 4.8, 4.9, 4.6, 4.7, 4.4,
        4.6, 4.5, 4.8, 4.7, 4.6, 4.5,
        4.8, 4.7, 4.6, 4.5, 4.7, 4.6,
        4.5, 4.8, 4.7, 4.6, 4.5, 4.8,
        4.7, 4.6, 4.5, 4.8, 4.7, 4.6
    ],
    "Image": [
        # Fantasy
        "https://covers.openlibrary.org/b/id/7984916-L.jpg",
        "https://covers.openlibrary.org/b/id/6979861-L.jpg",
        "https://covers.openlibrary.org/b/id/8231856-L.jpg",
        "https://covers.openlibrary.org/b/id/7888781-L.jpg",
        "https://covers.openlibrary.org/b/id/8463571-L.jpg",
        "https://covers.openlibrary.org/b/id/8305836-L.jpg",

        # Sci-Fi
        "https://covers.openlibrary.org/b/id/8101359-L.jpg",
        "https://covers.openlibrary.org/b/id/10594763-L.jpg",
        "https://covers.openlibrary.org/b/id/8370226-L.jpg",
        "https://covers.openlibrary.org/b/id/7222246-L.jpg",
        "https://covers.openlibrary.org/b/id/8311996-L.jpg",
        "https://covers.openlibrary.org/b/id/7888788-L.jpg",

        # Dystopian
        "https://covers.openlibrary.org/b/id/7222246-L.jpg",
        "https://covers.openlibrary.org/b/id/8775111-L.jpg",
        "https://covers.openlibrary.org/b/id/8370226-L.jpg",
        "https://covers.openlibrary.org/b/id/7222271-L.jpg",
        "https://covers.openlibrary.org/b/id/8442161-L.jpg",
        "https://covers.openlibrary.org/b/id/8311991-L.jpg",

        # Mystery
        "https://covers.openlibrary.org/b/id/8108691-L.jpg",
        "https://covers.openlibrary.org/b/id/8108701-L.jpg",
        "https://covers.openlibrary.org/b/id/8231991-L.jpg",
        "https://covers.openlibrary.org/b/id/8228691-L.jpg",
        "https://covers.openlibrary.org/b/id/8234561-L.jpg",
        "https://covers.openlibrary.org/b/id/8239991-L.jpg",

        # Self-help
        "https://covers.openlibrary.org/b/id/10594763-L.jpg",
        "https://covers.openlibrary.org/b/id/10423763-L.jpg",
        "https://covers.openlibrary.org/b/id/10958363-L.jpg",
        "https://covers.openlibrary.org/b/id/11194763-L.jpg",
        "https://covers.openlibrary.org/b/id/10794763-L.jpg",
        "https://covers.openlibrary.org/b/id/10294763-L.jpg",
    ]
}

df = pd.DataFrame(data)

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="BookFlix", page_icon="📚", layout="wide")

# -------------------------
# Header (Netflix Style)
# -------------------------

st.markdown("""
<style>

/* ---------- Main Background ---------- */
.stApp {
    background-color: #141414;
    color: white;
}

/* Main container */
.main {
    background-color: #141414;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#181818;
}

/* ---------- Titles ---------- */
.title{
    font-size:48px;
    font-weight:bold;
    color:#E50914;
    text-align:center;
}

.subtitle{
    font-size:20px;
    color:#d3d3d3;
    text-align:center;
    margin-bottom:30px;
}

/* ---------- Genre Dropdown ---------- */
label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

div[data-baseweb="select"] > div{
    background:#202020 !important;
    color:white !important;
    border:2px solid #E50914 !important;
    border-radius:10px;
}

div[data-baseweb="select"] span{
    color:white !important;
}

/* ---------- Book Cards ---------- */
.card{
    background:#1E1E1E;
    border-radius:15px;
    padding:15px;
    margin-bottom:25px;
    transition:0.3s;
    border:1px solid #333;
}

.card:hover{
    transform:scale(1.05);
    border:1px solid #E50914;
    box-shadow:0 0 20px rgba(229,9,20,.5);
}

/* Images */
img{
    border-radius:10px;
}

/* Text */
h1,h2,h3,h4,h5,h6,p{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'>📚 BookFlix</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>📖 Endless Stories. One Scroll Away</div>", unsafe_allow_html=True)

# -------------------------
# Genre Selection
# -------------------------
genre = st.selectbox("🎯 Choose Genre", df["Genre"].unique())

filtered = df[df["Genre"] == genre]

# -------------------------
# Netflix-style Grid
# -------------------------
st.markdown(
    f"<h2 style='color:white;'>🔥 {genre} Collection</h2>",
    unsafe_allow_html=True
)

cols = st.columns(3)

for i, row in filtered.iterrows():
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

       st.image(row["Image"], width="stretch")

        st.markdown(
    f"""
    <h3 style='color:white;text-align:center;'>
        📖 {row['Title']}
    </h3>

    <p style='color:#B3B3B3;text-align:center;'>
        👤 {row['Author']}
    </p>

    <p style='color:#FFD700;text-align:center;font-size:18px;font-weight:bold;'>
        ⭐ {row['Rating']} / 5
    </p>

    <p style='color:#E50914;text-align:center;'>
        🏷️ {row['Genre']}
    </p>
    """,
    unsafe_allow_html=True
)

        st.markdown("</div>", unsafe_allow_html=True)
