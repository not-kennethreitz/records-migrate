"""
Naval Fate.

Usage:
  records-migrate check
  records-migrate new
  records-migrate apply
  records-migrate schema

Options:
  -h --help      Show this screen.
  --version      Show version.
  --db=<db_url>  Database to connect to [default: $DATABASE_URL].
"""

import os
import sys

# import crayons
from docopt import docopt

def puts_error(msg, exit_code=False):
    if exit_code is True:
        exit_code = 1

    # msg = f"{str(crayons.red('Error'))}: {msg}"
    msg = f"Error: {msg}"
    print(msg, file=sys.stderr)

    if isinstance(exit_code, int):
        sys.exit(exit_code)


def main():
    args = docopt(doc=__doc__)

    do_check = args['check']
    do_new = args['new']
    do_apply = args['apply']
    do_schema = args['schema']

    # Prepare database_url.
    if "--db" not in args:
        try:
            args["--db"] = os.environ["DATABASE_URL"]
        except KeyError:
            puts_error("Either --db or $DATABASE_URL must be provided!", exit_code=1)


    if do_check:
        pass

    elif do_new:
        pass

    elif do_apply:
        pass

    elif do_schema:
        pass

if __name__ == "__main__":
    main()
