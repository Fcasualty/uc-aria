#uc-aria description page
# uc-aria #

uc-aria is a web2py mini-app for testing aria functionality. uc-aria feeds into uc-multilingual which commbines uc-aria with multi-lingual functionality.

This project was started by a soon to be named non-profit dedicated to promoting fair access.

Christopher Steel
Project Manager

# Notes #

We aim to make uc-aria as "modular" as possible. In this case modular means that uc-aria's functionality should be separated out from the rest of the application in order to allow it's eventual installation as a "plugin"

So we might end up with something like...

  * models/db\_aria.py

  * controllers/aria.py

  * views/aria/index.html

  * views/menu/aria\_aria\_menu.html

  * static/aria.cas