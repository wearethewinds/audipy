from .PlayListItem import PlayListItem


class PlayList:
    def __init__(self):
        self.queue = []
        self.selected_index = None

    def queue(self, queue_item: PlayListItem):
        self.queue.append(queue_item)

    def dequeue(self, queue_item: PlayListItem):
        self.queue.remove(queue_item)

    def next(self):
        self.selected_index += 1
        return self.queue[self.selected_index]

    def set_at(self, index):
        self.selected_index = index
        return self.queue[self.selected_index]
