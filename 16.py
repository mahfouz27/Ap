from kivy.app import App
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.base import runTouchApp
from kivy.lang import Builder

Window.clearcolor=(140/255,0,0,0)
Window.size=(600,643)
class Ahmed(App):
    def build(self):
        pass
runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top':1}
    color:(55,1,1,0)
    ActionView:
        ActionPrevious:
            title:'S'
        ActionButton:
            text:"Home"
        
            
        ActionGroup:
            text:"About US"
            color: .3,.6,.1,.9
            ActionButton:
                text:'Meet Our Team'
            ActionButton:
                text:'Gallery'
            ActionButton:
                text:'Our Clients'  


        ActionGroup:
            text:"Solutions"
            color: .3,.6,.1,.9
            ActionButton:
                text:'Soft Solutions'
            ActionButton:
                text:'Hard Solutions'
            ActionButton:
                text:'IT Solutions'  

        ActionButton:
            text:"Certificates"  
        ActionButton:
            text:"CONTACT US"                  
                  


'''))    





Ahmed().run()        