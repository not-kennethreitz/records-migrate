from records import Database
from records_migrate.adapters import MigrationAdapter

db = Database()
a = MigrationAdapter(db=db)
print(a.last_migration_applied)
# a.init()
# for file in a.load():
#     print(file)
