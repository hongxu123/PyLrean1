# --*-- coding:utf-8 --*--
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, '我的世界', size=(300, 300))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        txt = wx.StaticText(panel, -1, '我是非常好的人!!', (200, 200))
        sizer.Add(txt, 0, wx.Top | wx.LEFT, 50)
        self.Centre()


app = wx.App()
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
