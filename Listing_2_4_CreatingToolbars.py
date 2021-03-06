import wx


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars', size=(300,200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        bmp = wx.Bitmap('documents.png', wx.BITMAP_TYPE_PNG)
        toolbar.AddTool(wx.NewIdRef(), "New", bmp)
        toolbar.AddTool(wx.NewIdRef(), "New", bmp)
        toolbar.Realize()
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewIdRef(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewIdRef(), "C&ut", "")
        menu2.Append(wx.NewIdRef(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewIdRef(), "&Options...", "Display options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)

if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()