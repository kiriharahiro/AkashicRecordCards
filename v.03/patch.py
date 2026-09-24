import sys

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    bad_str = "label: 'Today's Theme'"
    good_str = "label: \"Today's Theme\""
    
    if bad_str in content:
        content = content.replace(bad_str, good_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed quote in {filepath}')
    else:
        print(f'Not found in {filepath}')

patch_file('build_html_en.py')
