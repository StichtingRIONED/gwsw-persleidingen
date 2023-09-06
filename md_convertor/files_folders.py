from pathlib import Path
from datetime import datetime


MAIN_MD = 'main.md'

BASE_LOC = Path(__file__).parent.absolute()
MAIN_MD_LOC = Path(BASE_LOC.parent, MAIN_MD)
DOCX_OUTPUT_LOC = Path(BASE_LOC, 'docx')
DOCX_ARCHIVE_LOC = Path(DOCX_OUTPUT_LOC, 'archive')

DT = datetime.now().strftime('%Y-%m-%d_%H%M%S')
DOCX_FILE_NAME = f"GWSW-Persleidingen_{DT}.docx"

DOCX_TEMPLATE_FILE = Path(BASE_LOC, 'templates', 'template.docx')
DOCX_METADATA_FILE = Path(BASE_LOC, 'templates', 'metadata_docx.yaml')
