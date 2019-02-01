class Migration:
    def __init__(self, *, path, adapter):
        self.path = path
        self.adapter = adapter

    def __repr__(self):
        return f"<Migration path={self.path!r} len={len(self.text)}>"

    @property
    def text(self):
        """Returns the text of the query."""
        with open(self.path, 'r') as f:
            return f.read()
