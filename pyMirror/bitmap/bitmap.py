#!/usr/bin/env python
import	wx

class	ImagePanel(wx.Panel):
	def	__init__(self,	parent):
		super(ImagePanel,	self).__init__(parent)
		theBitmap	=	wx.Bitmap("usingBitmaps.png")
		self.bitmap	=	wx.StaticBitmap(self,	bitmap=theBitmap)

class	MyFrame(wx.Frame):
	def	__init__(self,	parent,	title=""):
		super(MyFrame,	self).__init__(parent,	title=title)
		self.panel	=	ImagePanel(self)

class	MyApp(wx.App):
	def	OnInit(self):
		self.frame	=	MyFrame(None,	title="Main	Frame")
		self.frame.Show()
		return	True
