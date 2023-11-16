import wx

from .frames import MainFrame


class App(wx.App):
    main_frame: MainFrame

    def __init__(self):
        super().__init__(redirect=True, filename='{{ cookiecutter.project_slug }}.log', useBestVisual=True)

        self.main_frame = MainFrame(None)

    def Run(self):
        self.main_frame.Show(True)

        self.MainLoop()
