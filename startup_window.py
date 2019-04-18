#!/usr/bin/env python2

import pygtk, gtk, cairo, subprocess
pygtk.require('2.0')

class Base:


    ## ------------------------------------------
    ##  *Destroy*
    ##
    ## Fecha o processo inteiro quando chamada. 
    ## ------------------------------------------

    def destroy(self, widget, data=None): 
        gtk.main_quit()
    

    ## ------------------------------------------
    ##  *acessoWindows*
    ## ------------------------------------------

    def acessoWindows(self, widget):
        args = ("/usr/bin/remmina -c terminal_windows.rdp ")
        popen = subprocess.call(args,stdout=subprocess.PIPE,shell=True)
        popen.wait()
    
    ## ------------------------------------------
    ##  *acessoLinux*
    ## ------------------------------------------

    def acessoLinux(self, widget):
        #Ativar opcao de login por ssh no x2go e --hide e --thinclient p/ ocultar a interface
        #uma vez que as confs seja ddefinidas, --no-session-edit bloqueia o acesso a as configs
        args = ("/usr/bin/x2goclient --session-conf=sessions --session=linux_remoto")
        subprocess.call(args,stdout=subprocess.PIPE,shell=True)
        popen.wait()

    
    ## -----------------------------------------
    ##  *PLANO DE FUNDO*
    ## -----------------------------------------

    def draw_pixbuf(widget, event):
        path = 'resources/test.png'  ##endereco do plano de fundo
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        #depercated below
        .draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], self.pixbuf, 0, 0, 0, 0)
        #self.gdk_cairo_set_source_pixbuf(pixbuf)
    ## ------------------------------------------
    ##  *CONSTRUTOR*
    ## ------------------------------------------

    def __init__(self):
            self.window =  gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.window.set_position(gtk.WIN_POS_CENTER)
            self.window.set_size_request(500,500)
            
           
            self.button1 = gtk.Button("Fechar Janela")
           
            self.button2 = gtk.Button("Acesso Windows")

            self.button3 = gtk.Button("Acesso Linux")
           
            self.vbox = gtk.VBox() #container vertical para os elementos

            self.hbox = gtk.HBox() #container horizontal para os elementos


        ##Define o plano de fundo atraves da funcao draw_pixbuff
            self.hbox.connect(self.draw_pixbuf('expose-event'))
        
        
        ##Posicionamento por container vertical/horizontal
         ##Adiciona os elementos no container horizontal, depois no vertical
            self.hbox.pack_start(self.button2)
            self.hbox.pack_start(self.button3)
            self.vbox.pack_start(self.hbox)
            self.vbox.pack_start(self.button1)

            self.window.add(self.vbox)
            self.window.show_all()
            
            
            self.window.connect("destroy", self.destroy)
            self.button1.connect_object("clicked", self.destroy, self.window)
            self.button2.connect_object("clicked", self.acessoWindows, self.window)
            self.button3.connect_object("clicked", self.acessoLinux, self.window)
    
    def main (self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()

