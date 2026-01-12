import os

def replace_lines(filename, start, end, replacement):
    print(f"Updating {filename}, removing lines {start} to {end}")
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Python slicing: [start:end] includes start, excludes end.
    # 1-based "start" corresponds to index start-1.
    # 1-based "end" corresponds to index end-1.
    # We want to remove inclusive range [start, end].
    # So we keep [0 : start-1] and [end : ].
    
    new_lines = lines[:start-1] + [replacement + '\n'] + lines[end:]
    
    with open(filename, 'w') as f:
        f.writelines(new_lines)

replace_lines('index.html', 16, 579, '    <link rel="stylesheet" href="style.css">\n    <style>\n        body {\n            font-family: "Lalezar", cursive, "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;\n        }\n    </style>')
replace_lines('index_en.html', 12, 534, '    <link rel="stylesheet" href="style.css">\n    <style>\n        body {\n            font-family: "Courier New", Courier, monospace;\n        }\n    </style>')
