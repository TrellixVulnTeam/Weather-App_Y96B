import requests, json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


def fahrenheit(k):
    f = (((k-273.15)*9)/5)+32
    return round(f, 0)
url='http://api.openweathermap.org/data/2.5/weather?'
api_key = '5eb4e812766d03aaaa2cf2d05fdb4c81'

class Weather(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source="logo.png"))
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x" : 0.5, "center_y": 0.5}
        self.city = Label(text="Enter a location name", font_size = 20)
        self.window.add_widget(self.city)
        self.user = TextInput(multiline=False, padding_y = (20,20), size_hint = (1, 0.5))
        self.window.add_widget(self.user)
        self.button = Button(text="Submit", size_hint = (1, 0.5), bold = True, background_color = (0.1, 0.8 ,1 ,1))
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window
    def callback(self, instance):
        self.city.text = "City name: " + self.user.text
        city = self.user.text
        api_request = url + "appid=" + api_key + "&q=" + city
        response = requests.get(api_request)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            temperature = y["temp"]
            humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            self.city.text = "There is " +(str(weather_description)) + " in " + self.user.text + "\n The temperature is " + str(fahrenheit(temperature)) + "°F with " + str(humidity) + "% Humidity"

if __name__ == "__main__":
    Weather().run()
    sm = ScreenManager()


