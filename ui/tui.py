from ui.ui import UI
import json


class Display(UI):
    def show(self):
        print(json.dumps(self.result, indent=2, sort_keys=True))
