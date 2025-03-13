from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import random

from BaseGame import BaseGame


class DiceGame(BaseGame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.dado1 = Image(source="dado1.jpg")  
        self.dado2 = Image(source="dado1.jpg")  
        self.add_widget(self.dado1)
        self.add_widget(self.dado2)

        self.result_label = Label(text="Resultado: Ninguno", font_size=18)
        self.add_widget(self.result_label)

        self.roll_btn = Button(text="Lanzar Dados", font_size=24)
        self.roll_btn.bind(on_press=self.roll_dice)
        self.add_widget(self.roll_btn)

    def roll_dice(self, instance):
        if not self.players:
            self.result_label.text = "Agrega jugadores primero"
            return
        
        self.counter = 0
        self.event = Clock.schedule_interval(self.animate_dice, 0.1)

    def animate_dice(self, dt):
        self.counter += 1
        if self.counter < 10:
            self.dado1.source = f"dado{random.randint(1,6)}.jpg"
            self.dado2.source = f"dado{random.randint(1,6)}.jpg"
        else:
            Clock.unschedule(self.event)
            result1 = random.randint(1, 6)
            result2 = random.randint(1, 6)
            self.dado1.source = f"dado{result1}.jpg"
            self.dado2.source = f"dado{result2}.jpg"
            self.result_label.text = f"Resultado: {result1} + {result2} = {result1 + result2}"
            self.next_turn()

class TodisApp(App):
    def build(self):
        return DiceGame()

if __name__ == "__main__":
    TodisApp().run()

class TodisGame(DiceGame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.challenges = {
            2: "Todos o nadie",
            3: "Regla",
            4: "P***",
            5: "Obligas",
            6: "Historia",
            7: "Izquierda",
            8: "Derecha",
            9: "Cultura chupística",
            10: "Manos arriba",
            11: "Yo nunca nunca",
            12: "Por él o ella"
        }

        self.challenge_label = Label(text="Reto: Ninguno", font_size=18)
        self.add_widget(self.challenge_label)

    def process_roll(self, result1, result2):
        total = result1 + result2
        challenge = self.challenges.get(total, "Sin reto")
        self.challenge_label.text = f"Reto: {challenge}"
        self.result_label.text = f"Resultado: {total}"
        self.next_turn()


class TodisApp(App):
    def build(self):
        return TodisGame()

if __name__ == "__main__":
    TodisApp().run()