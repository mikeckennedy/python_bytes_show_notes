import os
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: Pass the file name for the source transcript txt file.")
        sys.exit(-1)

    file = sys.argv[1]
    out_file = os.path.expanduser(
        os.path.join(
            '~/Desktop',
            os.path.basename(file)
        )
    )
    print("Files:")
    print("Reading source file: ", file)
    print("Exported version at: ", out_file)

    fin = open(file, 'r', encoding='utf-8')
    fout = open(out_file, 'w', encoding='utf-8')

    with fin, fout:
        time = "0:00"
        for line in fin:
            if is_time(line):
                time = get_time_text(line)
            elif line and line.strip():
                text = f"{time} {line.strip()}\n\n"
                fout.write(text)
                # print(text)


def is_time(line: str) -> bool:
    if not line or not line.strip():
        return False

    parts = line.split(':')
    if not parts:
        return False

    return all(p.strip().isnumeric() for p in parts)


def get_time_text(line: str) -> str:
    if ':' not in line:
        raise Exception(f"Text doesn't seem to be a time: {line}")

    parts = line.split(':')

    hour_text = "0"
    min_text = "0"
    sec_text = "0"

    if len(parts) == 3:
        hour_text = parts[0].strip()
        min_text = parts[1].strip()
        sec_text = parts[2].strip()
    elif len(parts) == 2:
        min_text = parts[0].strip()
        sec_text = parts[1].strip()
    elif len(parts) == 1:
        sec_text = parts[0].strip()

    return f"{hour_text.zfill(2)}:{min_text.zfill(2)}:{sec_text.zfill(2)}"


if __name__ == '__main__':
    main()
