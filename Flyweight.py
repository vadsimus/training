class Smile:
    _sprite = None

    def __init__(self, position, sprite):
        self.position = position
        if not self._sprite:
            self._sprite = sprite
        self.sprite = self._sprite


