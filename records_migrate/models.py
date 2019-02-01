class Migration:
    def __init__(self, *, path, adapter):
        self.path = path
        self.adapter = adapter

    def __repr__(self):
        return f"<Migration path={self.path!r}>"

    def queries(self):
        for _ in os.walk(self.path):
            print(_)

    def text(self):
        """Returns the text of the query."""
        with open(self.path, 'r') as f:
            return f.read()
