import streamlit as st
import pickle
import requests
from streamlit_lottie import st_lottie
import json


# Load Lottie animation 
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Apply inline CSS
def apply_css():
    st.markdown("""
    <style>
        .movie-card {
            border-radius: 10px;
            padding: 10px;
            transition: transform 0.2s;
            margin-bottom: 20px;
        }
        .movie-card:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .movie-poster {
            border-radius: 8px;
            width: 100%;
            height: auto;
            margin-bottom: 8px;
        }
        .movie-title {
            font-weight: 600;
            text-align: center;
            font-size: 14px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .stSelectbox div[data-baseweb="select"] {
            border-radius: 8px !important;
        }
    </style>
    """, unsafe_allow_html=True)


# Initialize session state
if 'recommended' not in st.session_state:
    st.session_state.recommended = False


@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


# Apply CSS
apply_css()

# App Header
st.title('🎬 CineMatch AI')
st.subheader('Discover Your Next Favorite Movie')

# Load animation from URL (no local file needed)
lottie_url = "https://assets1.lottiefiles.com/packages/lf20_5tkzkblw.json"
lottie_movie = load_lottieurl(lottie_url)
if lottie_movie:
    st_lottie(lottie_movie, speed=1, height=200, key="initial")

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🔍 Search or select a movie you like:",
    movie_list,
    index=None,
    placeholder="Start typing to search..."
)

# Recommendation button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    recommend_btn = st.button('✨ Get Recommendations', use_container_width=True)

if recommend_btn and selected_movie:
    with st.spinner('Finding perfect matches for you...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        st.session_state.recommended = True

if st.session_state.recommended:
    st.success(f"Because you liked **{selected_movie}**, you might enjoy:")

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
            <div class="movie-card">
                <img src="{recommended_movie_posters[i]}" class="movie-poster">
                <div class="movie-title">{recommended_movie_names[i]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### Not happy with the results?")
    st.button("Try another movie", on_click=lambda: st.session_state.update({'recommended': False}))

# Footer

st.markdown("""
<div class="footer">
    <div class="footer-container">
        <p class="footer-text">Powered by TMDB API | Made with Streamlit</p>
        <div class="developer-badge">
            <p class="developer-text">👩‍💻 Developed by <span class="developer-name">Shubhangi Katariyar</span></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)