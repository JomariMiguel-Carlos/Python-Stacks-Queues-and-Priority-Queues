class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def