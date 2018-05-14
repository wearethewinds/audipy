from pyglet import media
from playlist.PlayListItem import PlayListItem


class FilePlayer:

    def __init__(self):
        self.player = media.Player()

        self.player.play()

    def play(self):
        self.player.play()

    def prepare(self, play_list_item: PlayListItem):
        self.player.queue(play_list_item.resource)

    def pause(self):
        self.player.pause()
