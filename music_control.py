import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import cv2
import numpy as np

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

def control_spotify(action):
    devices = sp.devices()
    if not devices['devices']:
        print("No active Spotify device found.")
        return

    device_id = devices['devices'][0]['id']
    playback = sp.current_playback()

    if action == "Play/Pause":
        if playback and playback['is_playing']:
            sp.pause_playback(device_id=device_id)
        else:
            sp.start_playback(device_id=device_id)
    elif action == "Next Track":
        sp.next_track(device_id=device_id)
    elif action == "Volume Up":
        sp.volume(80, device_id=device_id)
    elif action == "Volume Down":
        sp.volume(30, device_id=device_id)

def get_current_track_info():
    playback = sp.current_playback()
    if playback and playback['item']:
        track_name = playback['item']['name']
        artists = ", ".join([artist['name'] for artist in playback['item']['artists']])
        album_art_url = playback['item']['album']['images'][1]['url']
        response = requests.get(album_art_url)
        album_art = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
        return track_name, artists, album_art
    return None, None, None
