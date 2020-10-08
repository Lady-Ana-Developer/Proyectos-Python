from sense_hat import SenseHat
import time

sense= SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

def show_t():
  sense.show_letter("T", back_colour = red)
  time.sleep(1)
 
show_t()

temperature = round(sense.temperature, 1)
sense.show_message("It is " + str(temperature) + " degrees")


def show_h():
  sense.show_letter("H", back_colour = blue)
  time.sleep(1)
  
show_h()  
humidity = round(sense.humidity, 1)
sense.show_message("It is " + str(humidity) + "% of humidity")


def update_screen(mode, show_letter = False):
  if mode == "temp":
    if show_letter:
      show_t()
    temp = sense.temp
    temp_value = temp / 2.5 + 16
    pixels = [red if i < temp_value else white for i in range(64)]


  elif mode == "humidity":
    if show_letter:
      show_h()
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    pixels = [blue if i < humidity_value else white for i in range(64)]


  sense.set_pixels(pixels)
  
if temperature > 22 and humidity >= 40:
    sense.show_message("That's quite warm, please wear a hat")

elif temperature > 10 and temperature <= 22:
    sense.show_message("Not too cold")

elif temperature > -15 and temperature <= 10 and humidity > 35 and humidity < 39:
    sense.show_message("Brr, it's chilly, please take your thick jacket")

elif temperature >= 100:
    sense.show_message("It's boiling")

elif temperature >= 35 or temperature <= -15:
    sense.show_message("The temperature is extreme!, Please, stay at home.")


