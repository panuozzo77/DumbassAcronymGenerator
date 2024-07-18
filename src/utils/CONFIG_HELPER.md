## How to setup config.ini

This file contains configurations for the application, here's the guide:

config.ini **MUST** be in `utils/` folder. 
- [numbers] section specifies the number of words to search for in PDFs.
- [paths] section allows customization of the PDF directory path.
- [database] section is optional and provides settings for database connections.

```ini
[numbers]
; Specifies the number of words to search for in PDFs for each letter.
; Default value is set to 15.
num_words_to_search = 15

[paths]
; If no other paths have been inserted into config.ini ensure that PDF documents are placed in the `dumbassAcronym/pdfs/` directory for usage. 
; Path to the directory containing PDFs.
; Example: directory_path = /path/to/your/pdfs/
directory_path =

[database]
; Database connection settings. These fields are optional unless you plan to use the analyzer/ code folder.
; Replace placeholders with actual values.
username = <your db username goes here>
ip = <your db IP goes here>
password = <your password goes here>
database = <the name of the schema>
```