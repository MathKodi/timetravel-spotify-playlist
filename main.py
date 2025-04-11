import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# =============== 1. Configurações e autenticação ===============
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

data = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
playlist_name = f"{data} Billboard 100"
header = {"User-Agent": "Mozilla/5.0"}

# =============== 2. Scraping da Billboard ===============
response = requests.get(f"https://www.billboard.com/charts/hot-100/{data}/", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("li h3", class_="c-title")
songs_list = []
for song in songs:
    if len(songs_list) < 100:
        text = song.getText().strip()
        songs_list.append(text)
    else:
        break

print("📻 Músicas extraídas da Billboard:", len(songs_list))
# =============== 3. Autenticando com Spotipy ===============
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
print("👤 Spotify User ID:", user_id)

# =============== 4. Buscar URIs das músicas ===============
def get_spotify_uri(track_name, year):
    query = f"track:{track_name} year:{year}"
    results = sp.search(q=query, limit=1, type='track')
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    return None

songs_with_uris = []
year = data.split("-")[0]
for song in songs_list:
    uri = get_spotify_uri(song, year)
    if uri:
        songs_with_uris.append(uri)
        print(f"✔️ Found URI for '{song}'")
    else:
        print(f"❌ Not found on Spotify: {song}")

print(f"\n🎧 Total de músicas encontradas no Spotify: {len(songs_with_uris)}")

# =============== 5. Criar playlist e adicionar músicas ===============
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"Top 100 da Billboard em {data}"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_with_uris)

print(f"✅ Playlist '{playlist_name}' criada com {len(songs_with_uris)} músicas.")
