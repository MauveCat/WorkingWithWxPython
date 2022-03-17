import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Moving widgets around", size=(300,300))
        panel = wx.Panel(self)
        self.button = wx.Button(panel, -1, 'Button', size=(100,50), pos=(10,10))
        self.button.Bind(wx.EVT_LEFT_DOWN, self.OnPanelClick)

    def OnPanelClick(self, event):
        self.button.SetPosition((event.x, event.y))



if __name__ == '__main__':

    app = wx.App()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()
