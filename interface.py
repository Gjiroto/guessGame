import tkinter as tk
import random

# Función que genera un número aleatorio entre 1 y 100
def generate_random_number():
  """Generates a random number between 1 and 100."""
  global random_number
  random_number = random.randint(1, 100)

# Función que verifica si la adivinanza del usuario es correcta
def check_guess():
  """Verifies if the user's guess is correct."""
  global attempts_left
  try:
    guess = int(guess_entry.get())
    if guess == random_number:
      result_label.config(text="¡VICTORY!")
      play_again_button.config(state="normal")
      check_button.config(state="disabled")
    elif attempts_left > 1 and guess < random_number:
      attempts_left -= 1
      indication_label.config(text="Your number is too low.")
      result_label.config(text=f"Your number is incorrect. You have {attempts_left} attempts left.")
      guess_entry.delete(0, tk.END)
    elif attempts_left > 1 and guess > random_number:
      attempts_left -= 1
      indication_label.config(text="Your number is too high.")
      result_label.config(text=f"Your number is incorrect. You have {attempts_left} attempts left.")
      guess_entry.delete(0, tk.END)
    else:
      indication_label.config(text="")
      result_label.config(text="¡FAILED!")
      play_again_button.config(state="normal")
      check_button.config(state="disabled")
  except ValueError:
    result_label.config(text="¡Please enter a valid number!")

# Función para reiniciar el juego
def play_again():
  """Resets the game and generates a new random number."""
  global attempts_left
  attempts_left = 3
  generate_random_number()
  indication_label.config(text="")
  result_label.config(text="")
  guess_entry.delete(0, tk.END)
  play_again_button.config(state="disabled")
  check_button.config(state="normal")

# Crea la ventana principal de la aplicación
window = tk.Tk()
window.title("Guessing Game")

# Etiqueta con las instrucciones para el usuario
instruction_label = tk.Label(window, text="Guess a number between 1 and 100:")
instruction_label.pack()

# Campo de entrada para que el usuario ingrese su adivinanza
guess_entry = tk.Entry(window)
guess_entry.pack()

# Botón para que el usuario verifique su adivinanza
check_button = tk.Button(window, text="Verify", command=check_guess)
check_button.pack()

# Etiqueta para mostrar el resultado de la adivinanza
result_label = tk.Label(window, text="")
result_label.pack()

# Etiqueta para mostrar el pista de la adivinanza
indication_label = tk.Label(window, text="")
indication_label.pack()

# Botón para reiniciar el juego
play_again_button = tk.Button(window, text="Play Again", command=play_again, state="disabled")
play_again_button.pack()

# Botón para salir
exit_button = tk.Button(window, text="Exit", command=window.destroy, bg="red", fg="white")
exit_button.pack()

# Variables para controlar el juego
attempts_left = 3

# Genera un número aleatorio al iniciar el programa
generate_random_number()

# Ejecuta el bucle principal de la interfaz gráfica de usuario
window.mainloop()
