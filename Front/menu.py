from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.behaviors import FocusBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.icon_definitions import md_icons


KV = '''
MDScreen:
    canvas:
        Color:
            rgba: app.theme_cls.primary_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [0, 0, 0, 0]
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            left_action_items: [["arrow-left", lambda x: app.callback()]]
    
        Menu:
        
<Menu@FloatLayout>:
    MDIconButton:
        icon: "account-box"
        user_font_size: "48sp"
        pos_hint: {"center_x": .2, "center_y": .9}
        
        
    Label:
        text: 'Perfil de'
        pos_hint: {"center_x": .2, "center_y": .83}
    Label:
        text: 'investidor'
        pos_hint: {"center_x": .2, "center_y": .80}


    MDIconButton:
        icon: "book-open-variant"
        user_font_size: "48sp"
        pos_hint: {"center_x": .2, "center_y": .7}
    
    Label:
        text: 'Notícias'
        pos_hint: {"center_x": .2, "center_y": .63}

    MDIconButton:
        icon: "margin"
        user_font_size: "48sp"
        pos_hint: {"center_x": .2, "center_y": .5}
    Label:
        text: 'Simulador de '
        pos_hint: {"center_x": .2, "center_y": .43}
    Label:
        text: 'Juros Compostos'
        pos_hint: {"center_x": .2, "center_y": .40}

    MDIconButton:
        icon: "bank-outline"
        user_font_size: "48sp"
        pos_hint: {"center_x": .2, "center_y": .3}
    Label:
        text: 'Comparativo entre'
        pos_hint: {"center_x": .2, "center_y": .23}
    Label:
        text: 'corretoras'
        pos_hint: {"center_x": .2, "center_y": .20}



    MDIconButton:
        icon: "chart-areaspline"
        user_font_size: "48sp"
        pos_hint: {"center_x": .8, "center_y": .9}
    Label:
        text: 'Cotação'
        pos_hint: {"center_x": .8, "center_y": .83}
    

    MDIconButton:
        icon: "clipboard-list"
        user_font_size: "48sp"
        pos_hint: {"center_x": .8, "center_y": .7}
    
    Label:
        text: 'Metas'
        pos_hint: {"center_x": .8, "center_y": .63}

    MDIconButton:
        icon: "cash-usd"
        user_font_size: "48sp"
        pos_hint: {"center_x": .8, "center_y": .5}
    Label:
        text: 'Conversão de '
        pos_hint: {"center_x": .8, "center_y": .43}
    Label:
        text: 'Taxa de Câmbio'
        pos_hint: {"center_x": .8, "center_y": .40}

    MDIconButton:
        icon: "home-search"
        user_font_size: "48sp"
        pos_hint: {"center_x": .8, "center_y": .3}
    Label:
        text: 'Código de ação'
        pos_hint: {"center_x": .8, "center_y": .23}

<Chat@FloatLayout>:
    MDFloatingActionButton:
        icon: "images\icone.png"
        user_font_size: "64sp"
        pos_hint: {"center_x": .1, "center_y": .9}
    
    MDTextFieldRound:

        hint_text: "Digite Algo!"
        line_color_focus: 1, 1, 1, 1
        size_hint_x: .8
        pos_hint: {"center_x": .43, "center_y": .05}
        fill_color: 0, 0, 0, .4
    
    MDIconButton:
        icon: "microphone"
        user_font_size: "20sp"
        pos_hint: {"center_x": .82, "center_y": .053}
    

'''


class JuliusApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        

        return Builder.load_string(KV)




JuliusApp().run()



