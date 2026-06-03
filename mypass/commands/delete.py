import sys

from mypass.commands import (
    init,
    setup,
    add,
    list,
    search,
    show,
    delete
)


def main():

    if len(sys.argv) < 2:
        print(
            """
mypass setup
mypass init
mypass add
mypass list
mypass search <keyword>
mypass show <name>
mypass delete <name>
"""
        )
        return

    command = sys.argv[1]

    if command == "setup":
        setup.run()

    elif command == "init":
        init.run()

    elif command == "add":
        add.run()

    elif command == "list":
        list.run()

    elif command == "search":
        search.run(
            sys.argv[2]
        )

    elif command == "show":
        show.run(
            sys.argv[2]
        )

    elif command == "delete":
        delete.run(
            sys.argv[2]
        )

    else:
        search.run(command)