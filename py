import subprocess as sp
packages = set()
with open("files.txt", "r") as f:
    line = f.readline()
    while line:
        package_str = ""
        items = line.split("-")
        for item in items:
            if item[0].isdigit():
                break
            package_str += item+"-"
        package_str = package_str.strip("-")
        packages.add(package_str)
        line = f.readline()
print(packages)
for pkg in packages:
    result = sp.run(["dnf", "install", pkg])
