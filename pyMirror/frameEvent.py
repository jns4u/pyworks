import wx

class	MyApp(wx.App):
	def	OnInit(self):
		#self.frame	=	wx.Frame(None,	title="Binding	Events")
		self.frame	=	MyFrame(None,	title="Main	Frame")

		#	Bind	to	events	we	are	interested	in
		self.frame.Bind(wx.EVT_SHOW,	self.OnFrameShow)
		self.frame.Bind(wx.EVT_CLOSE,	self.OnFrameExit)
					
		#	Show	the	frame
		self.frame.Show()
		return	True

	def	OnFrameShow(self,	event):
		theFrame	=	event.EventObject
		print("Frame	(%s)	Shown!"	%	theFrame.Title)
		event.Skip()
	
	def	OnFrameExit(self,	event):
		theFrame	=	event.EventObject
		print("Frame	(%s)	is	closing!"	%	theFrame.Title)
		event.Skip()

class	MyFrame(wx.Frame):
	def	__init__(self,	parent,	title=""):
		super(MyFrame,	self).__init__(parent,	title=title)
		
		#	Set	an	application	icon
		self.SetIcon(wx.Icon("usingBitmaps.png"))
		
		#	Set	the	panel
		self.panel	=	wx.Panel(self)

if	__name__	==	"__main__":
	app	=	MyApp(False)
	app.MainLoop()
