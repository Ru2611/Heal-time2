from django.shortcuts import render
import requests
from spotipy.oauth2 import SpotifyClientCredentials
# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        response=requests.get('https://api.spotify.com/v1/search?q='+artist_uri+'&type=track&market=ES&limit=10&offset=5',headers={'Authorization': "Bearer BQDu3aKyVTIzE-hPB6SC-54BJxMPs34OB4_VZxSGSwZJyqnIC_P3LEA2_bt0D4oDSmZm1wbWyYVj_S6yb8i64rpdRotjm4RPVmdepb5gD4xRfa_KDk_y08KTC5_LAJdFYd9QZLIRIsQL0-BoKwFmjtJSJDaQjFoPg2w11EZmQWzRpF8q7HE0PLSQjy0wE76GyBg"}).json()
        # print(response['tracks']['items'][0]['album'])
        # print(response['tracks']['items'][0]['album']['images'][0]['url'])
        final_result=response['tracks']['items']
        return render(request,'base.html',{"results":final_result})

    # for track in results['tracks'][:10]:
        # print('track    : ' + track['name'])
        # print('audio    : ' + track['preview_url'])
        # print('cover art: ' + track['album']['images'][0]['url'])
        # print()
    return render(request,'base.html')


