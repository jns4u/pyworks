class	MyFrame(wx.Frame):
	def	__init__(self,	parent,	title=""):
		super(MyFrame,	self).__init__(parent,	title=title)
		
		#	Set	an	application	icon
		self.SetIcon(wx.Icon("appIcon.png"))
		
		#	Set	the	panel
		self.panel	=	wx.Panel(self)

class	MyApp(wx.App):
	def	OnInit(self):
		self.frame	=	MyFrame(None,	title="Main	Frame")
		self.frame.Show()
		return	True

