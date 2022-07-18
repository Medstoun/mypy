import re
from typing import Iterator, List, Any


def build_query(cmd: str, val: str, file_list: Iterator) -> List[Any]:
    if cmd == 'filter':
        res = list(filter(lambda x: val in x, file_list))
        return res
    if cmd == 'map':
        res = list([x.split()[int(val)] for x in file_list])
        return res
    if cmd == 'unique':
        res = list(set(file_list))
        return res
    if cmd == 'sort':
        reverse = val == 'desc'
        res = list(sorted(file_list, reverse=reverse))
        return res
    if cmd == 'limit':
        res = list(file_list)[:int(val)]
        return res
    if cmd == 'regex':
        regex = re.compile(val)
        res = list(filter(lambda x: regex.search(x), file_list))
        return res
    return []
