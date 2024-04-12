# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:34:07 2022

@author: Sayali
"""


file = open("C:\\Users\\Sayali\\Desktop\\project\\audibuddy.kv", "w")
str = '''WindowManager:
    MainWindow:
    speechtotext:
    texttospeech:

<Mainwindow>:
    name:"mainwindow"
    BoxLayout:
        Button:
            font_size:25
            colour:1,1,1,1
    BoxLayout:
        canvas:
            Color:
                rgba:0.16862745098,0.16862745098,0.16862745098,1
            Rectangle:
                pos:self.pos
                size:self.size
    BoxLayout:
        pos_hint:{'top':1.456}
        size_hint:2,0.57
        canvas:
            Color:
                rgba:0.09803921568,0.13725490196,0.17647058823,1
            Rectangle:
                pos:self.pos
                size:self.size
        
    FloatLayout:
        BoxLayout:
            
            orientation:'horizontal'
            padding:5,0,0,0
            Label:
                text:"audibuddy"
                font_name:"Roboto-Medium"
                font_size:35
                pos_hint:{"top":1.45,"left":1}
        
        Widget:
        Widget:
    
    FloatLayout:
        BoxLayout:
            padding:50,150,50,50
            Button:
                id:speechtotext_btn
                text:"Speech to Text"
                size_hint:0.5,0.15
                pos_hint:{"top":1,"centre_x":0.5}
                on_release:
                    app.root.current = "second_window"
                    root.manager.transition.direction = "left"
        BoxLayout:
            padding:50,150,50,50
            Button:
                id:texttospeech_btn
                text:"Text to Speech"
                size_hint:0.5,0.15
                pos_hint:{"top":0.75,"centre_x":0.5}
                on_release:
                    app.root.current = "third_window"
                    root.manager.transition.direction = "left"
        BoxLayout:
            padding:100,150,100,50
            Button:
                id:exitapp_btn
                text:"Exit"
                size_hint:0.1,0.15
                pos_hint:{"top":0.5,"centre_x":0.5}
                on_release:
                    app.root.exit()
        Button:
            background_normal:"homw button.webp"
            background_down:"homw button.webp"
            size_hint:0.2,0.1
            pos_hint:{"top":1,"left":1}
            on_release:
                app.root.current = "mainwindow"
                root.manager.transition.direction = "right"
<speechtotext>:
    name:"second_window"
    BoxLayout:
        Button:
            font_size:25
            colour:1,1,1,1
    BoxLayout:
        canvas:
            Color:
                rgba:0.16862745098,0.16862745098,0.16862745098,1
            Rectangle:
                pos:self.pos
                size:self.size
    BoxLayout:
        pos_hint:{'top':1.456}
        size_hint:2,0.57
        canvas:
            Color:
                rgba:0.09803921568,0.13725490196,0.17647058823,1
            Rectangle:
                pos:self.pos
                size:self.size
    FloatLayout:
        BoxLayout:
            
            orientation:'horizontal'
            padding:5,0,0,0
            Label:
                text:"audibuddy"
                font_name:"Roboto-Medium"
                font_size:35
                pos_hint:{"top":1.45,"left":1}
        
        Widget:
        Widget:
        Button:
            background_normal:"homw button.webp"
            background_down:"homw button.webp"
            size_hint:0.2,0.1
            pos_hint:{"top":1,"left":1}
            on_release:
                app.root.current = "mainwindow"
                root.manager.transition.direction = "right"
        Label:
            id:final_text
            text:"Say something"
            font_name : "Roboto-medium"
        Button:
            id:convert_btn
            pos_hint:{"center_x":0.5,"top":0.3}
            size_hint:0.3,0.2
            background_normal:"mic.png"
            background_down:"mic_down.png"
            border:5,5,5,5
            on_press:
                root.change()
            on_release:
                root.speechtotextfas()
'''

file.write(str)
file.close()