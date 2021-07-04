
import config




class PlexSong:

    def __init__(self,synology_file):
        self.song = synology_file # class SynologyFile
        self.video = None    

    def add_video(self, synology_file):
        self.video = synology_file

    def __str__(self):
        if self.video != None:
            return f'plex name: {self.song.name}[{self.song.ext}]\nplex video: {self.video.name} [{self.video.ext}]\nplex dir: {self.song.dir}'
        else:
            return f'plex name: {self.song.name} [{self.song.ext}]\nplex video: {self.video}\nplex dir: {self.song.dir}'

