from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class BaseGame (BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.players = []  
        self.turn = 0  

        self.title_label = Label(text="Juego de Todis", font_size=30)
        self.add_widget(self.title_label)
        
        self.input_player = TextInput(hint_text="Ingrese nombre del jugador", font_size=20)
        self.add_widget(self.input_player)
        
        self.players_label = Label(text="Jugadores: Ninguno", font_size=20)
        self.add_widget(self.players_label)
        
        self.add_player_btn = Button(text="Agregar Jugador", font_size=20)
        self.add_player_btn.bind(on_press=self.add_player)
        self.add_widget(self.add_player_btn)
        
        self.turn_label = Label(text="Turno: Ninguno", font_size=20)
        self.add_widget(self.turn_label)

    def add_player(self, instance):
        player_name = self.input_player.text.strip()
        if player_name:
            self.players.append(player_name)
            self.players_label.text = f"Jugadores: {', '.join(self.players)}"
            self.input_player.text = ""
            if len(self.players) == 1:
                self.turn_label.text = f"Turno: {self.players[0]}"

    def next_turn(self):
        if self.players:
            self.turn = (self.turn + 1) % len(self.players)
            self.turn_label.text = f"Turno: {self.players[self.turn]}"