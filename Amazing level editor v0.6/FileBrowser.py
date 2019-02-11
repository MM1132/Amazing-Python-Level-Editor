import glob, os
from Button import Button
class FileBrowser:
    # This is fileBrowser....
    # File browser is used for creating buttons for all the save files in 'saves' folder
    def __init__(self, folder, extension, pos):
        gap = 50
        files = glob.glob(folder + "*" + extension)
        self.elements = [Button(os.path.basename(files[i])[:-4], files[i], [pos[0], pos[1] + gap * i]) for i in range(len(files))]
    def render(self, window):
        for i in self.elements:
            i.render(window)