"""
Pipelines – an effective use of generators


Create an application to do the following linux command using a generator
# cat lines.txt | grep spam | sed 's/spam/bacon/g'
bacon
bacon bacon
bacon bacon bacon
"""
from os import path


def cat(filename):
    with open(filename) as lines:
        for line in lines:
            yield line


def grep(lines, search):
    for line in lines:
        if search in line:
            yield line


def replace(lines, search, replace):
    for line in lines:
        yield line.replace(search, replace)


file_path = path.join(
    path.dirname(__file__),
    'resources',
    'lines.txt'
)

search_keyword = 'spam'
replace_keyword = 'bacon'

# ============= Full version ============
lines_generator = cat(file_path)
matched_lines_generator = grep(lines_generator, search_keyword)
replaced_lines_generator = replace(matched_lines_generator, search_keyword, replace_keyword)

for replace_line in replaced_lines_generator:
    print(replace_line)

# ============ Short version =============
for replaced_line in replace(
        grep(
            cat(file_path),
            search_keyword
        ),
        search_keyword, replace_keyword):
    print(replaced_line)
