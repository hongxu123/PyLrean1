import wx

class MyFrame(wx.Frame):
  def __init__(self,parent):
    frame = wx.Frame.__init__(self, parent, title="用户登录系统", pos=(100,100), size=(300,300))
  
  
if __name__ == "__main__":
  app = wx.App()
  frame = MyFrame(None)
  frame.Show()
  app.MainLoop()
