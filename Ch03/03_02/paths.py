def split_ext(path):
    i = path.rfind('.')
    return (path, '') if i == -1 else (path[:i], path[i:])


if __name__ == '__main__':
    root, ext = split_ext('app.py')
    print(f'{root=}, {ext=}')
