def copy_file(command: str) -> None:
    part = command.split()
    if len(part) != 3 or part[0] != "cp" or part[1] == part[2]:
        return
    try:
        with open(part[1], "r") as src, open(part[2], "w") as copy:
            for line in src:
                copy.write(line)
    except FileNotFoundError:
        return
