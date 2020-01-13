# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 675,506 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )

		self.FirstName = wx.TextCtrl( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.FirstName, 0, wx.ALL, 5 )

		self.LastName = wx.TextCtrl( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.LastName, 0, wx.ALL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		gSizer4.Add( self.m_choice3, 0, wx.ALL, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		gSizer4.Add( self.m_choice4, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Input First and last, then press add.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button1, 0, wx.ALL, 5 )


		bSizer2.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 12, 2, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Automotive Tech", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.automotiveGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.automotiveGauge.SetValue( 0 )
		gSizer5.Add( self.automotiveGauge, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Computer Engineering", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.ceGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.ceGauge.SetValue( 0 )
		gSizer5.Add( self.ceGauge, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Construction Trades", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.constructionGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.constructionGauge.SetValue( 0 )
		gSizer5.Add( self.constructionGauge, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Cosmotology", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.cosmoGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.cosmoGauge.SetValue( 0 )
		gSizer5.Add( self.cosmoGauge, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Criminal Justice", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.crimeGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.crimeGauge.SetValue( 0 )
		gSizer5.Add( self.crimeGauge, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Culinary & Pastry Arts", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.culinaryGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.culinaryGauge.SetValue( 0 )
		gSizer5.Add( self.culinaryGauge, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Emergency Services (EMT/Fire)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.emsGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.emsGauge.SetValue( 0 )
		gSizer5.Add( self.emsGauge, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Graphic Design & Creative Media", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.graphicGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.graphicGauge.SetValue( 0 )
		gSizer5.Add( self.graphicGauge, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Health Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.healthGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.healthGauge.SetValue( 0 )
		gSizer5.Add( self.healthGauge, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Education and Behavioal Science", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer5.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.eduGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.eduGauge.SetValue( 0 )
		gSizer5.Add( self.eduGauge, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Theater and Film: Acting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.actingGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.actingGauge.SetValue( 0 )
		gSizer5.Add( self.actingGauge, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Theater and Film: Production and Design", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.productionGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.productionGauge.SetValue( 0 )
		gSizer5.Add( self.productionGauge, 0, wx.ALL, 5 )


		bSizer2.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


