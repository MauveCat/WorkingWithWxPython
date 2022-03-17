import wx

class MenuEvent(wx.Frame):
    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, 'Menus', size=(300,300))
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuItem = menu1.Append(-1, "&Exit")
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItem)

    def OnCloseMe(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frame = MenuEvent(None, -1)
    frame.Show()
    app.MainLoop()