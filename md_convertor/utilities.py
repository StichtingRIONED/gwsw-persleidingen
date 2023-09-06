from pathlib import Path
from typing import List


def move_file(src: Path, dest: Path) -> None:
    """
    moves file or folder from source to destination
    :param src: source location
    :param dest: destination location
    :return: None
    """
    if not src.exists():
        raise FileExistsError('source file does not exist')

    src.rename(dest)


def get_files_in_folder(folder: Path, suffix: str = None) -> List[Path]:
    """
    lists all files in a given folder, optionaly with
    :param folder: folder to search in
    :param suffix: a single suffix to match in files
    :return:
    """
    if not folder.exists():
        raise FileNotFoundError('folder does not exist')

    files = folder.iterdir()
    files = [file for file in files if file.is_file()]
    if suffix is None:
        return files

    if not suffix.startswith('.'):
        suffix = f".{suffix}"

    return [file for file in files if file.suffix == suffix]
