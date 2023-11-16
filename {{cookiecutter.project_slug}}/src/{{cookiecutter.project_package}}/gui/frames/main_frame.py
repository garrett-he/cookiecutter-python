import wx


class MainFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title='{{ cookiecutter.project_name }}')
        self.Centre()
