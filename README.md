# Records-Migrate: a migration system for Records

A migration system for the [Records](https://github.com/kennethreitz/records) Python library.

## Intented Usage

    $ records-migrate check
    all migrations appear to be applied!

    $ records-migrate new
    Created file migrations/0003.sql. Feel free to add a suffix to the file name.

    $ records-migrate apply
    Applied migration 3/5...
