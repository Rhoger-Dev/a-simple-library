# pylint: disable=all

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.ui_libro import app

if __name__ == "__main__":
    app.mainloop()