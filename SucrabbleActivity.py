from gettext import gettext as _

import sys
import gtk
import pygame

import sugar.activity.activity
import sugar.graphics.toolbutton
#para importar el avatar del usuario
from sugar.graphics.icon import Icon
from sugar.graphics import style
from sugar.graphics.xocolor import XoColor
from sugar.graphics.palette import Palette
import gconf
# Import sugargame package from top directory.
sys.path.append('..') 
import sugargame.canvas

import Sucrabble

class SucrabbleActivity(sugar.activity.activity.Activity):
    def __init__(self, handle):
        super(SucrabbleActivity, self).__init__(handle)
        self.paused = False
        # Create the game instance.
        self.game = Sucrabble.Sucrabble()
        # Build the activity toolbar.
        toolbox = sugar.activity.activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show_all()
        self.hbox=gtk.HBox()
        # Build the Pygame canvas.
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        fixed = gtk.Fixed()
        self.hbox.pack_start(self.sucrabble_gtk_toolbar(), gtk.FALSE,gtk.FALSE, 0)
        self.hbox.pack_start(self._pygamecanvas, gtk.TRUE, gtk.TRUE, 0)
        self.hbox.pack_start(self.sucrabble_gtk_toolbar(), gtk.FALSE,gtk.FALSE, 0)
        # Note that set_canvas implicitly calls read_file when resuming from the Journal.
        self.set_canvas(self.hbox)
        self.hbox.show_all()
        # Start the game running.
        self._pygamecanvas.run_pygame(self.game.run)
    def sucrabble_gtk_toolbar(self):
        vbox=gtk.VBox()
        vbox.pack_start(self.get_user_avatar(), gtk.FALSE,gtk.FALSE, 0)
        entry=gtk.Entry()
        fixed = gtk.Fixed()
        vbox.pack_start(self.create_tree_view(),gtk.FALSE, gtk.FALSE, 0)
        button = gtk.Button("OK",gtk.STOCK_OK)
        fixed.put(button,10,300)
        button.connect("clicked", self.show_tooltip)
        vbox.pack_start(fixed, gtk.FALSE, gtk.FALSE, 0)
        return vbox
    def get_user_avatar(self):
        client = gconf.client_get_default()
        xocolor = XoColor(client.get_string('/desktop/sugar/user/color'))
        buddy_icon = Icon(pixel_size = style.XLARGE_ICON_SIZE)
        buddy_icon.props.xo_color = xocolor
        buddy_icon.props.icon_name = 'computer-xo'
        buddy_icon.props.pixel_size = style.XLARGE_ICON_SIZE
        tooltips = gtk.Tooltips()
        #tooltips.set_tip(buddy_icon,str(client.get_string('/desktop/sugar/user/nick')))
        return buddy_icon
    
    def create_tree_view(self):
        self.fam=[]
        for i in range(1,6):
            self.fam.append(str(i)+"\t\thola")
        store = self.create_model()
        treeView = gtk.TreeView(store)
        treeView.set_rules_hint(True)
        self.create_column(treeView)
        return treeView;

    def create_column(self, treeView):
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Jugada\tPalabra", rendererText, text=0) 
        treeView.append_column(column)
    
    def create_model(self):
        store = gtk.ListStore(str)
        for ff in self.fam:
            store.append([ff])
        return store
    
    def show_tooltip(self, widget, data=None):
        #desc = model.get_value(iter, 1)
       # tooltip.set_markup(desc)
        #del pix
        self.game = Sucrabble.Sucrabble()
        self.game.run()
        #return True  
    
    def read_file(self, file_path):
        self.game.read_file(file_path)
        
    def write_file(self, file_path):
        self.game.write_file(file_path)
