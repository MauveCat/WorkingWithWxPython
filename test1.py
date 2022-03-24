import wx

class MyApp(wx.App):
    def OnInit(self):
        pass
        return True


if __name__ == '__main__':
    myapp = MyApp()
    myapp.MainLoop()