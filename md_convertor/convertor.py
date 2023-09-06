from pathlib import Path
from typing import List

import pypandoc

from files_folders import DOCX_METADATA_FILE, DOCX_TEMPLATE_FILE


def markdown_to_docx(src_file: Path, dest_file: Path, args: List[str]):
    """
    converts a .md file to a docx file
    :param src_file: source file to convert
    :param dest_file: destination file
    :param args: additional Pandoc arguments
    :return: None
    """
    try:
        pypandoc.convert_file(
            source_file=src_file,
            to='docx',
            format='md',
            outputfile=dest_file,
            extra_args=args)

        print(f"File is successfully converted to '{dest_file.as_posix()}'.")
    except Exception as e:
        print(f"An error occured as follows: {e}")


# list of additional pandoc arguments
arguments = [
    # path to metadata file
    '--metadata-file', DOCX_METADATA_FILE,
    # path to word template
    '--reference-doc', DOCX_TEMPLATE_FILE,
    # markdown extension
    '-f', "gfm+yaml_metadata_block+implicit_figures+footnotes",
    # highlight style for code blocks.
    '--highlight-style', 'pygments',
    # Maak het resulterende bestand een standalone document zonder externe
    # afhankelijkheden.
    '--standalone',
    # Gebruik de "listings" -omgeving voor opmaak van codeblokken.
    '--listings',
    # resolutie voor afbeeldingen
    '--dpi=300',
    # hoogste niveau van divisie van het leidende document
    '--top-level-division=chapter',
    # Parameter configureert een boek- of rapportstijl
    '-V', 'book=True',
    # eenzijdig afdrukken
    '-V', 'classoption=oneside',
    #  taal in van het gegenereerde document
    '-V', 'lang=nl-NL'
]
