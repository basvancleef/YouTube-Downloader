from pytube import YouTube, Playlist
import os

playlist_url = input('Enter playlist url:\n>>>')
playlist = Playlist(playlist_url)

for video in playlist.videos:
    yt = YouTube(
        video.watch_url)

    # TODO Use bypass_age_gate() function to update the vid_info by bypassing the age gate.
    video = yt.streams.filter(only_audio=True).first()
    destination = './Downloads'

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")
