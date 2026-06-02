import sys

from mypass.commands import (
    init,
    add,
    list,
    search,
    delete,
    # copy,
)


def main():

    if len(sys.argv) < 2:
        print(
            """
Commands

mypass init
mypass add
mypass list
mypass delete <keyword>
mypass search <keyword>

Shortcut:
mypass <keyword>
"""
        )
        return

    command = sys.argv[1]

    if command == "init":
        init.run()

    elif command == "add":
        add.run()

    elif command == "list":
        list.run()

    # elif command == "copy":
    #
    #     if len(sys.argv) < 3:
    #         print(
    #             "Usage: mypass copy <keyword>"
    #         )
    #         return
    #
    #     copy.run(
    #         sys.argv[2]
    #     )

    elif command == "delete":

        if len(sys.argv) < 3:
            print(
                "Usage: mypass delete <keyword>"
            )
            return

        delete.run(
            sys.argv[2]
        )

    elif command == "search":

        if len(sys.argv) < 3:
            print(
                "Usage: mypass search <keyword>"
            )
            return

        search.run(
            sys.argv[2]
        )

    else:
        # Shortcut search
        search.run(command)
