from pathlib import Path

from convertor import markdown_to_docx,  arguments
from utilities import get_files_in_folder, move_file

from files_folders import DOCX_OUTPUT_LOC, DOCX_ARCHIVE_LOC, MAIN_MD_LOC, DOCX_FILE_NAME


if __name__ == "__main__":

    if files := get_files_in_folder(folder=DOCX_OUTPUT_LOC, suffix='.docx'):
        for file in files:
            new_file_name = Path(DOCX_ARCHIVE_LOC, file.name)
            move_file(src=file, dest=new_file_name)

    # Omzetten markdown naar format
    markdown_to_docx(src_file=MAIN_MD_LOC, dest_file=Path(DOCX_OUTPUT_LOC, DOCX_FILE_NAME), args=arguments)
