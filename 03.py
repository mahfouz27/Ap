# import kivy
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.core.window import Window
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.base import runTouchApp
# from kivy.uix.widget import Widget

# Window.clearcolor = (140/255.0,0,0,0)
# Window.size=(400,634)





# class LoginScreen(GridLayout):
#     def __init__ (self,**Kwargs):
#         super( LoginScreen, self).__init__( **Kwargs)
#         self.cols = 2
#         self.add_widget ( Label( text="UserName"))
#         self.username = TextInput ( multiline = False)
#         self.add_widget (self.username)
#         self.add_widget (Label(text="Password"))
#         self.password = TextInput (password = True ,multiline = False)
#         self.add_widget (self.password)
#         self.submit = Button (text = "Login", font_size= 30)

#         self.add_widget (self.submit)

# class MyApp (App):
#     def build(self):
#         return LoginScreen()
# if __name__=='__main__':
#     MyApp().run()        


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
# from kivy.base import runTouchApp
# from kivy.uix.widget import Widget

Window.clearcolor = (140/255.0,0,0,0)
Window.size=(400,634)

class LoginUser(GridLayout):
    def __init__(self,**Kwargs):
        super(LoginUser,self).__init__(**Kwargs)
        self.cols = 1

        self.upper_grid = GridLayout()
        self.upper_grid.cols = 2
        
        self.upper_grid.add_widget (Label(text="Username"))
        self.username = TextInput (multiline =False)
        self.upper_grid.add_widget (self.username)



        self.upper_grid.add_widget(Label(text="password"))
        self.password = TextInput (password = True ,multiline = False)
        self.upper_grid.add_widget(self.password)

        self.add_widget(self.upper_grid)



        self.submit = Button (text= "Login",font_size= 29)
        self.add_widget (self.submit)









class MyApp (App):
    def build(self):
        self.titel = "System One"
        return LoginUser()
if __name__=='__main__':
    MyApp().run() 


