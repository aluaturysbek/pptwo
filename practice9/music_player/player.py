import pygame

class MusicPlayer:
    def __init__(self):
        # Playlist with WAV files
        self.playlist = ["music/track1.wav", "music/track2.wav"]
        self.current_track_index = 0
        self.is_playing = False
        self.mixer = pygame.mixer
        self.mixer.init()
        self.current_music = None

    def play(self):
        """Start or resume playing the current track."""
        if not self.is_playing:
            self.current_music = self.mixer.Sound(self.playlist[self.current_track_index])
            self.current_music.play()
            self.is_playing = True

    def stop(self):
        """Stop playing the current track."""
        if self.is_playing:
            self.current_music.stop()
            self.is_playing = False

    def next_track(self):
        """Skip to the next track in the playlist."""
        if self.is_playing:
            self.stop()
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        """Go back to the previous track in the playlist."""
        if self.is_playing:
            self.stop()
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        """Return the name of the current track."""
        return self.playlist[self.current_track_index].split("/")[-1]

    def get_progress(self):
        """Return the current progress of the track in seconds."""
        if self.is_playing:
            return self.current_music.get_length()  # Returns the length of the track
        return 0

    