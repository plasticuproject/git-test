"""Picture slideshow app"""
import sys
from random import choice
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk
from playsound import playsound

# Comment/Uncomment the appropriate path
# ASSETS = "assets/"  # <-FOR DEVELOPMENT
ASSETS = "/opt/hs_app/assets/"  # <-FOR PRODUCTION

# Global image, sound, and text variables
HS = ['h1.jpg', 'h2.jpg', 'h3.jpg', 'h4.jpg', 'h5.jpg']
SOUNDS = ["bruh1.mp3"]
ABOUT = """About:\n\tSlideshow app that picks a\n\trandom photo of H and
        a bruh noise."""


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
        f_menu = Gtk.Menu()
        fmi = Gtk.MenuItem.new_with_label("File")
        emi = Gtk.MenuItem.new_with_label("Exit")
        emi.connect("activate", self.quit_app)
        f_menu.append(emi)
        fmi.set_submenu(f_menu)
        menubar.add(fmi)

        # About menu
        a_menu = Gtk.Menu()
        ami = Gtk.MenuItem.new_with_label("About")
        ami_text = Gtk.MenuItem.new_with_label("About")
        ami_text.connect("activate", self.on_about_window)
        a_menu.append(ami_text)
        ami.set_submenu(a_menu)
        menubar.add(ami)

        # Attach menu widget to grid
        grid.attach(menubar, 0, 0, 1, 1)
        self.add(grid)

        # Button widget
        button = Gtk.Button(label="CLICK HERE TO CHANGE THE PICTURE AND BRUH")
        button.connect("clicked", self.on_button_clicked)

        # Image widget
        self.image = Gtk.Image()
        self.current_h = choice(HS)
        self.image.set_from_file(ASSETS + self.current_h)

        # Attach image and bruh button widgets to grid
        grid.attach_next_to(self.image, menubar, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button, self.image, Gtk.PositionType.BOTTOM, 1, 2)

    @classmethod
    def quit_app(cls, par):
        """File submenu quit action"""
        APP.quit()

    def on_button_clicked(self, widget):
        """Button actions"""
        new_h = choice(HS)
        while new_h == self.current_h:
            new_h = choice(HS)
        self.current_h = new_h
        self.image.set_from_file(ASSETS + self.current_h)
        playsound(ASSETS + choice(SOUNDS))

    @classmethod
    def on_about_window(cls, par):
        """About window submenu action"""
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
STYLE_PROVIDER = Gtk.CssProvider()
STYLE_PROVIDER.load_from_file(Gio.File.new_for_path(ASSETS +
                                                    "gtk-3.0/gtk.css"))
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), STYLE_PROVIDER,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# Run application
APP = Application()
APP.run(sys.argv)
