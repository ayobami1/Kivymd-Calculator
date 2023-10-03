##########################
# BUILD MY FIRST KIVYMD APP
########################
from functools import partial

from kivy.properties import StringProperty
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivy.app import App
from kivymd.material_resources import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import (

    MDFlatButton, MDRaisedButton, MDRoundFlatButton, \
    MDRectangleFlatButton, MDIconButton)
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.uix.button import Button

# Window.size = (340, 500)


class CalFunc():

    def build_cal(self):
        pass







class CalApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Calculator"
        # self.color_picker_popup = None
        self.operator_val = StringProperty("")
        self.last_value = StringProperty('')
        self.second_last_value = StringProperty('')
        self.current_value = StringProperty('')
        self.current_txt = StringProperty('')


    def open_color_picker(self, instance):
        color_picker = ColorPicker()



        self.color_picker_pop = Popup(
            title='Pick a Color',
            content = color_picker,
            size_hint = (None, None),
            size = (dp(300),dp(400))

        )

        self.color_picker_pop.open()
        color_picker.bind(color=self.set_background_color)

    def set_background_color(self, instance, color):
        self.root_layout.md_bg_color = color
        # self.color_picker_pop.dismiss()
    def bold_text(self, text):
        return f"[b]{text}[\b]"

    def button_press(self,btn_txt,x):

        operators = ["+", ".", "-","*"]

        self.current_txt =self.text_field_layout.text
        # if  btn_txt in operators and :..


        if  self.current_txt:
            self.second_last_value =  self.current_txt[-1]



        if len(self.text_field_layout.text) <=0:
            if (self.current_txt=="0"):
                self.current_txt = ''
                self.text_field_layout.text = self.current_txt
            elif btn_txt in operators:
                self.text_field_layout.text = ""


        if self.second_last_value in operators and btn_txt in operators:
            print("Yes is equal")
            return

        elif btn_txt != "=" and (btn_txt !="Del" and btn_txt !="C"):
            if len(self.current_txt)<=0 and btn_txt in operators:
                return
            elif self.current_txt == "Error":
                self.text_field_layout.text = '0'
            else:
                self.text_field_layout.text =  self.current_txt + btn_txt
                self.last_value = self.text_field_layout.text[-1]
                self.current_value =   (self.current_txt + btn_txt)




        elif btn_txt == "=":# and  self.text_field_layout.text !='':

            if self.last_value in operators:

                print("You Cant use that ")
                return

            try:
                ## Remove leading Zero Before Evaluting
                math_exp = self.text_field_layout.text
                result= eval(math_exp)
                self.text_field_layout.text=str(result)
                # self.text_field_layout.text = '0'
            except Exception as e:
                print(e)
                self.text_field_layout.text = "Error"



        elif btn_txt == "C":
            self.text_field_layout.text = '0'
            pass
        elif btn_txt == "Del":
            if self.text_field_layout.text:
             self.text_field_layout.text = self.text_field_layout.text[:-1]

             # self.text_field_layout.text = "0"






            # self.add(last_value=self.text_field_layout.text)




    def build(self):
        self.root_layout = MDBoxLayout(orientation ="vertical",
                            padding = [10,100,10,10],
                                       md_bg_color= get_color_from_hex('#FFFF00')
                            )

        # self.root_layout.add_widget(Widget())
        self.text_field_layout = MDTextField(
            text = "",
            halign = "right",
            mode = "fill",
            hint_text = "Math Calculator",

            # background_color=get_color_from_hex("#FFFF00")



        )

        self.text_field_layout.text_color_focus=(1,0,0,1)
        self.text_field_layout.readonly=True
        self.text_field_layout.fill_color_normal = get_color_from_hex('#ffffffff')
        self.text_field_layout.widget_style ="ios"

        self.root_layout.add_widget(
            self.text_field_layout
        )

        self.root_layout.add_widget(Widget())

        buttons = [
            ["1","2","3","4"],
            ["5","6","7","8"],
            ["9", "0","+","-"],
            ["C","*", ".","Del"],
            ["="]
        ]

        # self.root_layout.add_widget(Widget())

        for button in buttons:

            self.h_lyt = MDBoxLayout(orientation="horizontal", spacing=10,\
                                         padding =(20,0,0,0))
            for btn_txt in button:
                self.btn_lyt = MDRaisedButton(
                    # text = btn_txt,
                    text =f"[b]{btn_txt}[/b]",
                    text_color = (0, 0, 0, 1),  # Dark yellow color
                    theme_text_color = "Primary",
                    on_press= lambda x, btn=btn_txt:self.button_press(btn, x)
                    # on_press= lambda btn_txt:self.button_press(btn_txt),
                    # on_press=partial(self.button_press, btn_txt)


                )

                self.h_lyt.add_widget(self.btn_lyt)


                if btn_txt == "=":
                    self.btn_lyt.md_bg_color = (0, 1, 0, 1)
                    self.btn_lyt.size_hint = (1, 0)
                elif btn_txt =="Del":

                    self.btn_lyt.md_bg_color = get_color_from_hex('#FF1919FF')

                    self.btn_lyt.height = 300
                    # self.h_btn_lyt.padding  =(0,0,0,0)
                else:
                    pass
                    # self.btn_lyt.md_bg_color = (.2, .3, 0, 0.5)
                    # self.btn_lyt.size_hint = (1, 0.5)

            self.root_layout.add_widget(self.h_lyt)
        self.root_layout.add_widget(MDIconButton(
            text= "change Backgroung",
            pos_hint = {"center_x":.5, "center_y":.5},
            on_release=self.open_color_picker
        ))






        return self.root_layout





if __name__ == '__main__':

  CalApp().run()


