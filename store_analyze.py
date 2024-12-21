#### SALAL KHAN (202307216)| ASSIGNMENT:II

import sys, os, shutil
import multiprocessing
import time


def get_encoding(file_path):
    with open(file_path, "rb") as file:
        first_bytes = file.read(4)

    if first_bytes[:2] == b"\xFF\xFE":
        return "utf-16-le"
    else:
        return "utf-8"


def fixed(values):
    line = ""

    for value in values:
        line += str(value).ljust(20, "x")

    return line


def delimited(values):
    line = ""

    for i, value in enumerate(values):
        line += value + ("$" if i < len(values) - 1 else "")

    return line


def offset(values):
    line = ""

    index = 12

    for value in values:
        line += str(index)
        index += len(value)

    line += "".join(values)

    return line


def get_fixed_attributes(line):
    values = []

    for i in range(0, 119, 20):
        values.append(int(line[i : i + 19].replace("x", "")))

    return values


def get_delimited_attributes(line):
    values = []

    splitted_values = line.split("$")

    for splitted_value in splitted_values:
        values.append(int(splitted_value))

    return values


def get_offset_attributes(line):
    values = []

    line = line.rstrip("\n")

    indexes = [int(line[i : i + 2]) for i in range(0, len(line), 2)]

    for i in range(0, 6):
        start = i

        end = "END"

        if i < 5:
            end = i + 1

        first_offset = int(indexes[start])
        last_offset = int(indexes[end] if end != "END" else len(line))

        values.append(int(line[first_offset:last_offset]))

    return values


def get_pages_attribute(pages, method_name, method, index):
    print(pages, method_name, method, index)

    attribute_list = []
    sum = 0

    for page in pages:
        f = open("./" + method_name + "/" + page, "r")

        start = 1 if method_name == "Offset" else 0

        for line in f.readlines()[start:]:
            attribute = method(line)[int(index)]
            attribute_list.append(attribute)
            sum += attribute

        f.close()

    return [sum / len(attribute_list), len(attribute_list)]


def get_attribute(method_name, method, index, number_of_processes):
    sum = 0
    lengths = 0

    pages = []

    for dir, dirnames, pages in os.walk("./" + method_name):
        pages = pages

    pool = multiprocessing.Pool(processes=int(number_of_processes))

    sums = pool.starmap(
            get_pages_attribute, [([page], method_name, method, index) for page in pages]
        )

    for avg, length in sums:
        sum += avg
        lengths += length

    print(index + " average: ", sum / (lengths / 500))


# Creates three directories
def create_dirs():
    print("Creating directories")

    if os.path.exists("./Offset"):
        shutil.rmtree("./Offset")

    os.mkdir("./Offset")

    if os.path.exists("./Fixed"):
        shutil.rmtree("./Fixed")

    os.mkdir("./Fixed")

    if os.path.exists("./Delimited"):
        shutil.rmtree("./Delimited")

    os.mkdir("./Delimited")


def store(dataset_path):
    print("Reading dataset")

    try:
        dataset = open(dataset_path, "r", encoding=get_encoding(dataset_path))

        fixed_lines = []
        delimited_lines = []
        offset_lines = []

        for line in dataset.readlines():
            values = line.rstrip("\n").split(",")[1:]

            fixed_lines.append(fixed(values))
            delimited_lines.append(delimited(values))
            offset_lines.append(offset(values))

        no_pages = len(fixed_lines) / 500

        for page_no in range(0, int(no_pages)):
            print("Writing page no:", page_no)

            fixed_page = open("./Fixed/page_" + str(page_no) + ".txt", "x")
            delimited_page = open("./Delimited/" + "page_" + str(page_no) + ".txt", "x")
            offset_page = open("./Offset/" + "page_" + str(page_no) + ".txt", "x")

            page_offset = page_no * 500

            offset_page.write(str(len(delimited_lines[0].split("$"))) + ",2\n")

            for fixed_line, delimited_line, offset_line in zip(
                fixed_lines[page_offset : page_offset + 500],
                delimited_lines[page_offset : page_offset + 500],
                offset_lines[page_offset : page_offset + 500],
            ):
                fixed_page.write(fixed_line + "\n")
                delimited_page.write(delimited_line + "\n")
                offset_page.write(offset_line + "\n")

    except Exception as e:
        print("Error: ", e)


def analyze(method, index_of_attribute, number_of_processes):
    print("analyzed")

    if method == "Fixed":
        get_attribute(method, get_fixed_attributes, index_of_attribute, number_of_processes)
    elif method == "Delimited":
        get_attribute(method, get_delimited_attributes, index_of_attribute, number_of_processes)
    elif method == "Offset":
        get_attribute(method, get_offset_attributes, index_of_attribute, number_of_processes)
    else:
        print("Invalid attribute please try <Fixed|Delimited|Offset>")


if __name__ == "__main__":
    start_time = time.time()

    command = sys.argv[1]
    dataset_path_or_method = sys.argv[2]

    if command == "store":
        create_dirs()
        store(dataset_path_or_method)

    if command == "analyze":
        index_of_attribute = sys.argv[3]
        number_of_processes = sys.argv[4]

        analyze(dataset_path_or_method, index_of_attribute, number_of_processes)

    print("Process took: ", time.time() - start_time)


