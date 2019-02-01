# Records-Migrate: a migration system for Records

A migration system for the [Records](https://github.com/kennethreitz/records) Python library.

## Intented Usage

Assuming `DATABASE_URL` is set:

    $ records-migrate check
    all migrations appear to be applied!

    $ records-migrate new
    Created file migrations/0003.sql. Feel free to add a suffix to the file name.

    $ records-migrate apply
    Applied migration 3/5...

## Considerations

- Don't base migration order on file creation time, as Heroku strips the data on deploy.
