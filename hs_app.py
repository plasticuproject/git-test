import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Gdk
from random import choice
from playsound import playsound
import sys


HS = ['h1.jpg','h2.jpg' ,'h3.jpg' ,'h4.jpg' ,'h5.jpg']
SOUNDS = ["bruh1.mp3"]
ABOUT = "About:\n\tSlideshow app that picks a\n\trandom photo of H and\n\ta bruh noise."


class MainWindow(Gtk.ApplicationWindow):
    """Main application window"""

    def __init__(self, app):
        super(MainWindow, self).__init__(title="H's App", application=app)

        # Main application window size, position and layout
        self.set_default_size(600, 800)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS) 
        grid = Gtk.Grid()
        menubar = Gtk.MenuBar()

        # File menu
        fMenu = Gtk.Menu()
        fmi = Gtk.MenuItem.new_with_label("File")
        emi = Gtk.MenuItem.new_with_label("Exit")
        emi.connect("activate", self.quit_app)
        fMenu.append(emi)
        fmi.set_submenu(fMenu)
        menubar.add(fmi)

        # About menu
        aMenu = Gtk.Menu()
        ami = Gtk.MenuItem.new_with_label("About")
        amiText = Gtk.MenuItem.new_with_label("About")
        amiText.connect("activate", self.on_about_window)
        aMenu.append(amiText)
        ami.set_submenu(aMenu)
        menubar.add(ami)
        
        # Attach menu widget to grid
        grid.attach(menubar, 0, 0, 1, 1)
        self.add(grid)

        # Button widget
        button = Gtk.Button(label="CLICK HERE TO CHANGE THE PICTURE AND BRUH")
        button.connect("clicked", self.on_button_clicked)

        # Image widget
        self.image = Gtk.Image()
        self.h = choice(HS)
        #self.image.set_from_file("assets/" + self.h)                 #<-FOR DEV
        self.image.set_from_file("/opt/hs_app/assets/" + self.h)      #<-FOR PROD

        # Attach image and bruh button widgets to grid
        grid.attach_next_to(self.image, menubar, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button, self.image, Gtk.PositionType.BOTTOM, 1, 2)


    def quit_app(self, par):

        # File submenu quit action
        app.quit()


    def on_button_clicked(self, widget):

        # Button actions
        newH = choice(HS)
        while newH == self.h:
            newH = choice(HS)
        self.h = newH
        #self.image.set_from_file("assets/" + self.h)                 #<-FOR DEV
        #playsound("assets/" + choice(SOUNDS))                        #<-FOR DEV
        self.image.set_from_file("/opt/hs_app/assets/" + self.h)      #<-FOR PROD
        playsound("/opt/hs_app/assets/" + choice(SOUNDS))             #<-FOR PROD
 

    def on_about_window(self, par):

        # About window submenu action
        AboutWindow().show_all()


class AboutWindow(Gtk.Window):
    """About window"""

    def __init__(self):
        super(AboutWindow, self).__init__()

        # About window size, position, layout and contents
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS) 
        self.set_border_width(15)
        label = Gtk.Label(ABOUT)
        self.add(label)
        self.set_title("About")
        self.set_size_request(200, 80)
        self.connect("destroy", Gtk.main_quit)


class Application(Gtk.Application):
    """Application boilerplate code"""

    def __init__(self):
        super(Application, self).__init__()


    def do_activate(self):
        self.win = MainWindow(self)
        self.win.show_all()


    def do_startup(self):
        Gtk.Application.do_startup(self)


# Load Ultimate-Dark-(Flat)-Grey GTK theme css
style_provider = Gtk.CssProvider()
#style_provider.load_from_file(Gio.File.new_for_path("assets/gtk-3.0/gtk.css"))  #<-FOR DEV
style_provider.load_from_file(Gio.File.new_for_path(                             #<-FOR PROD
                              "/opt/hs_app/assets/gtk-3.0/gtk.css"))             #<-FOR PROD
Gtk.StyleContext.add_provider_for_screen(
Gdk.Screen.get_default(),
style_provider,
Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)


# Run application
app = Application()
app.run(sys.argv)

