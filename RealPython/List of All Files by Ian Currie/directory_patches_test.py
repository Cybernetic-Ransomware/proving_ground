import pathlib
from typing import Generator


SKIP_DIRS = ["temp", "temporary_files", "logs"]

files_folder = pathlib.Path("E:\LARPy - RPG\Zew Cthulhu")
print('Main path:')
print(files_folder)


def separation() -> None:
    print('*' * 20)


def return_direct() -> None:
    #
    # for f in list(files_folder.iterdir()):
    #     print(f)

    separation()
    print('Folders:')
    [print(f) for f in list(files_folder.iterdir()) if f.is_dir()]
    separation()
    print('Files directly in:')
    [print(f) for f in list(files_folder.iterdir()) if f.is_file()]


def return_all() -> None:
    separation()
    print('All folders:')
    [print(f) for f in list(files_folder.rglob("*")) if f.is_dir()]
    separation()
    print('All files:')
    [print(f) for f in list(files_folder.rglob("*")) if f.is_file()]


def return_sufix(suffix: str='*', keyword: str='*') -> None:
    separation()
    print('All folders:')
    [print(f) for f in list(files_folder.rglob(f"*{keyword}*")) if f.is_dir() and set(f.parts).isdisjoint(SKIP_DIRS)]
    separation()
    print('All files:')
    [print(f) for f in list(files_folder.rglob(f"*{keyword}*.{suffix}")) if f.is_file() and set(f.parts).isdisjoint(SKIP_DIRS)]


def return_all_items(root: pathlib.Path, exclude: list=None) -> Generator[str, None, None]:
    """
    :param root: a root to a folder tree
    :param exclude: a list of folder names, that won't be checked during recursive search
    :return: generator to iterate files paths through all folders names except those given by exclude parameter
    """

    if exclude is None:
        exclude = []

    for item in root.iterdir():
        if item.name in exclude:
            continue
        yield item
        if item.is_dir():
            yield from return_all_items(item)


if __name__ == '__main__':
    # return_direct()
    # return_all()
    return_sufix(suffix='pdf', keyword='yellow')
    # return_sufix(keyword='1')
    # [print(f) for f in (list(return_all_items(files_folder, SKIP_DIRS)))]
    # print(list(return_all_items(files_folder, SKIP_DIRS)))
