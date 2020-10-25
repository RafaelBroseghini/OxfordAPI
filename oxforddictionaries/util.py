import json


def dump_json(_object, _file_name='tmp.json'):
    with open(_file_name, "w") as _outfile:
        json.dump(_object, _outfile)


def read_json(_file_name='tmp.json'):
    with open(_file_name, 'r') as _infile:
        return json.load(_infile)
