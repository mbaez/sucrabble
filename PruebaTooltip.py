# -*- coding: utf-8 -*-

import gtk

class PruebaTooltip:
    def __init__(self):
        # Creamos nuestro modelo con 2 campos, uno para la imagen y otro para 
        # la descripción
        self.model = gtk.ListStore(gtk.gdk.Pixbuf, str)
        # Creamos el IconView
        self.iconview = gtk.IconView(self.model)
        # Le decimos que la imagen la sacará de la primera columna
        self.iconview.set_pixbuf_column(0)
        # Habilitamos el nuevo soporte de la API para tooltips
        self.iconview.set_has_tooltip(True)
#        self.iconview.set_orientation(gtk.ORIENTATION_VERTICAL)
#        self.iconview.set_selection_mode(gtk.SELECTION_SINGLE)
#        self.iconview.set_column_spacing(10)
#        self.iconview.set_columns(6)
#        self.iconview.set_item_width(50)
        # Nos conectamos a la señal 'query-tooltip'
        self.iconview.connect("query-tooltip", self.show_tooltip)
        
        # Creamos el ScrolledWindow y le insertamos el IconView
        self.scrollwin = gtk.ScrolledWindow()
        self.scrollwin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.scrollwin.set_shadow_type(gtk.SHADOW_IN)
        self.scrollwin.add(self.iconview)
        
        vbox = gtk.VBox(False, 5)
        vbox.pack_start(self.scrollwin, True, True, 0)
        
        # Creamos una ventana simple y le agregamos la caja que contiene la
        # ScrolledWindow y todo lo demás
        self.window = gtk.Window()
        self.window.set_title('Tooltip de in IconView como debe ser')
        self.window.set_default_size(300, 300)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect('destroy', gtk.main_quit)
        self.window.add(vbox)
        self.window.show_all()
        
        # Creamos unos cuantos elementos dentro del modelo (esto es solo con 
        # fines ilustrativos, pues en teoría debería llenarse desde otra parte)
        for i in range(30):
            label = 'Tooltip del Elemento %i' % (1 + 1)
            pix = self.window.render_icon(gtk.STOCK_ABOUT, gtk.ICON_SIZE_DIALOG)
            self.model.append([pix, label])
        del pix
    
    # Esta es la parte ruda xD
    # Nuestro callback para la señal 'query-tooltip'
    def show_tooltip(self, widget, x, y, keyboard_mode, tooltip):
        # Calculamos el offset (w y x), es decir la diferencia entre el origen 
        # del ScrolledWindow y el IconView. Para eso usamos el valor de cada uno
        # de los scrollbar. Simple ¿no?. Pues después de los psicotrópicos lo
        # ví muy sencillo :P
        w = self.scrollwin.get_property('hadjustment').value
        z = self.scrollwin.get_property('vadjustment').value
        # Ubicamos la ruta del elemento según la posición 'exácta' del cursor
        # sobre el IconView
        path = widget.get_path_at_pos(int(x + w), int(y + z))
        if path is None: return False
        model = widget.get_model()
        # Obtenemos el elemento mediante el modelo y la ruta
        iter = model.get_iter(path)
        # Obtenemos la imagen y la descripción guardada en el modelo
        pix = model.get_value(iter, 0)
        desc = model.get_value(iter, 1)
        # Establecemos la imagen del tooltip
        tooltip.set_icon(pix)
        # Establecemos el texto del tooltip (con soporte para marcado pango :D)
        tooltip.set_markup(desc)
        # Borramos la imagen para no dejar basura regada
        del pix
        # Devolvemos True para que se muestre el Tooltip y seamos felices weee!
        return True
        
if __name__ == "__main__":
    PruebaTooltip()
    gtk.main()