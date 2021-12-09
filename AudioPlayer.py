from vlc import MediaPlayer
import os


class AudioPlayer:

    song_dir = os.getcwd() + '\songs'
    current_index = 0
    
    def __init__(self) -> None:
        self.music_files = [f for f in os.listdir(self.song_dir) if os.path.isfile(os.path.join(self.song_dir, f))]
        self.player = self.set_player()

    def set_player(self, *args):
        if args:
            return MediaPlayer(args[0])
        return MediaPlayer()

    def play_song(self):
        song_to_play = self.song_dir + "\\" + self.music_files[self.current_index]
        self.player = self.set_player(song_to_play)
        self.player.play()

    def go_next(self):
        self.current_index += 1
        self.current_index = self.current_index % len(self.music_files)
        self.stop()
        self.play_song()

    def go_back(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.music_files) - 1
        self.stop()
        self.play_song()

    def stop(self):
        self.player.stop()
