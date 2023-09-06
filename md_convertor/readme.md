## Markdown convertor

De tekst op de openbare website wordt gevoed door markdown bestanden. Het reviewen van de teksten die op deze website staan, gebeurt voornamelijk via *'wijzigingen bijhouden'* in een .docx bestand.

Deze Python package, inclusief bijbehorende instructie voor een pre-commit hook, zorgt ervoor dat er ALTIJD een .docx versie van *main.md* aanwezig is dat gedeeld kan worden met derden. De .docx wordt lokaal opgeslagen op *md_convertor/docx/*. Oude versies worden automatisch in een archief (*md_convertor/docx/archive/*) gezet.

Aub de bestaande code in *.git/hooks/pre-commit.sample* vervangen door het volgende. Vervolgens de bestandsnaam van *pre-commit.sample* veranderen naar *pre-commit*.


```bash
#!/bin/bash

:<< COMMENT
author: Wouter van Riel
date: 6 September 2023

Script detects files that are to be committed and filters for 'main.md' and files in folder 'media'.
If changes are detected 'main.md' is converted into a .docx file via a Python script.
COMMENT

# adopted from: https://davidwalsh.name/detect-changed-files-git
output=$({ git diff-index --name-only HEAD ; } | grep --regexp='main.md\|media/.*')

array=($output)

# check if nr of files in array is greater than 0. If yes, run main.py
if [ ${#array[@]} -gt 0 ]
then
  echo "Changes in main.md or media files detected. *.docx file will be updated."
  python md_convertor/main.py
fi
```
