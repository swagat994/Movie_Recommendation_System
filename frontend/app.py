import streamlit as st
import requests

# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# =====================================
# Custom CSS
# =====================================

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.movie-title {
    text-align: center;
    font-weight: bold;
    font-size: 16px;
    margin-top: 10px;
}

h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# Header
# =====================================

st.title("🎬 Movie Recommendation System")
st.markdown(
    "<center>Discover movies similar to your favorites</center>",
    unsafe_allow_html=True
)

st.divider()

# =====================================
# Backend URL
# =====================================

BACKEND_URL = "http://127.0.0.1:8000"

# =====================================
# Movie Input
# =====================================

movie_name = st.text_input(
    "Enter a movie name",
    placeholder="e.g. Avatar"
)

# =====================================
# Recommendation Button
# =====================================

if st.button("Get Recommendations", use_container_width=True):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:

        with st.spinner("Finding recommendations..."):

            response = requests.get(
                f"{BACKEND_URL}/recommend/{movie_name}"
            )

            data = response.json()

            if "error" in data:
                st.error(data["error"])

            else:

                recommendations = data["recommendations"]

                st.subheader(
                    f"Movies similar to '{movie_name}'"
                )

                cols = st.columns(5)

                for idx, movie in enumerate(recommendations):

                    with cols[idx]:

                        if movie["poster"]:
                            st.image(
                                movie["poster"],
                                use_container_width=True
                            )
                        else:
                            st.image(
                                "https://via.placeholder.com/300x450?text=No+Poster",
                                use_container_width=True
                            )

                        st.markdown(
                            f"""
                            <div class='movie-title'>
                                {movie['title']}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )