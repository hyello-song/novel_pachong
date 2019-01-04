# novel_scratcher
A simple Python3 console program simplifying the work of downloading your favourite novel online. It is still an unfinished project.
I hope to improve my Python skill through this project:)

（Licensed under GNU GPL V2)
This project is only for web technology testing. Please respect the copyright of novels' authors and obey the related laws and regulations. It provides **ABSOLUTELY NO WARRANTY**.
## Some tips
There are some definition in the directory *define*. You could write new definitions for other websites，whose format can be found in define/Template.py. Remember to import the definition as a Python module and add the index in *df*.

```Python
from define import snwx, biquge, leduwo, snwx_txt, kanunu, ADD
df = {'snwx':snwx, 'leduwo':leduwo, 'biquge':biquge, 'snwx_txt':snwx_txt, 'kanunu':kanunu, 'NEWITEM':NEWITEM}
```

The current way of saving is putting each chapter in individual files and gathering all the chapter in a single folder， while the old one save all the content in only one file. If you prefer the latter one, please turn to *main_old.py*.

