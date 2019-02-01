import os

from .models import Migration

class MigrationAdapter:
    def __init__(self, db, *, _dir="migrations", default_format="{:06d}"):
        # Make path of dir absolute.
        _dir = os.path.abspath(_dir)

        # Create the migration directory, if it doesn't exist
        os.makedirs(_dir, exist_ok=True)

        # The migrations directory.
        self.migrations_dir = _dir

        # The database.
        self.db = db

    @property
    def files(self):
        """Returns a list of file names in the migrations directory, in order."""
        def gen():
            for root, dirs, files in os.walk(self.migrations_dir, topdown=True, followlinks=True):
                for _file in files:
                    # Yield the file name.
                    yield f"{root}{os.path.sep}{_file}"

        return [g for g in gen()]

    def load(self):
        def gen():
            for _file in self.files:
                yield Migration(path=_file, adapter=self)

        return [g for g in gen()]

    def query(self, query):
        return self.db.query(query)

    @property
    def last_migration_applied(self):
        raise NotImplementedError
