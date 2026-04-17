import os


def copy_file(command: str) -> None:
    part = command.split()
    if len(part) != 3 or part[0] != "cp" or part[1] == part[2]:
        return
    src = part[1]
    dst = part[2]

    if os.path.basename(src) != src or os.path.basename(dst) != dst:
        return
    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
