import wx 
class Frame1(wx.Frame):
 def __init__(self,superior):
        wx.Frame.__init__(self, parent = superior, title = "Mouse Event", pos= (100,200), size= (500,500))
        self.panel = wx.Panel(self)
        #text1= wx.TextCtrl(self.panel, value = "Hello, World!", size = (200,100))
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick)
		
 def OnClick(self, event):
     posm = event.GetPosition()
     wx.StaticText(parent=self.panel, label="Hello World!", pos = (posm.x, posm.y))
	 
if __name__ == '__main__': 
    app =wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop() 