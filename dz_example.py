def load_log_file(path):
    ...
    for line in file:
        try:
            parse_log_line(line)
        except ValueError | IndexError:
            continue

def parse_log_line(line):
    ...
    if ...:
        raise ValueError