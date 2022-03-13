# level1

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(re.findall('\w|\.|\_|\-', new_id))

    for i in sorted(re.findall('\.+', new_id), reverse=True):
        new_id = new_id.replace(i, '.')

    new_id = new_id.strip('.')

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >=16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id)<=2:
        new_id += new_id[-1]

    return new_id
