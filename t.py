from records_migrate.adapters import MigrationAdapter

a = MigrationAdapter(db=None)
for file in a.load():
    print(file)
