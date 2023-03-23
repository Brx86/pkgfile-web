import re, subprocess


def pkgfile(pkg):
    try:
        out_bytes = subprocess.check_output(["pkgfile", "-v", pkg])
    except subprocess.CalledProcessError as e:
        print(f"Error: pkgfile returned {e.returncode}")
        return
    return out_bytes.decode("utf-8")


def safename(text):
    NOTALLOW = r"[^a-zA-Z0-9\+_.-]"
    if re.compile(NOTALLOW).findall(text):
        text = re.sub(NOTALLOW, "", text)
    return text


def handle_output(file_name, text):
    pkg_dict, pkg_list = dict(), list()
    for line in text.splitlines():
        info = line.split()
        if info[0] not in pkg_dict:
            pkg_dict[info[0]] = [info[1], [info[2]]]
        else:
            pkg_dict[info[0]][1].append(info[2])

    for file, desc in pkg_dict.items():
        repo, name = file.split("/")
        pkg_list.append(
            {"name": name, "ver": desc[0], "repo": repo, "path": "<br>".join(desc[1])}
        )

    return {"status": "ok", "filename": file_name, "data": pkg_list}


def run(file_input):
    file_name = safename(file_input)
    text = pkgfile(file_name)
    if text:
        return handle_output(file_name, text)
    else:
        return {
            "status": "error",
            "filename": file_name,
            "data": "No package provides the file.",
        }


if __name__ == "__main__":
    import sys

    file_input = "atestfile"
    print(run(sys.argv[1]))
