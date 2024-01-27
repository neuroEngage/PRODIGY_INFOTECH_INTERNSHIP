import tkinter as tk

class TemperatureConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Conversion Calculator")

        self.unit_label = tk.Label(master, text="Temperature Unit (C/F/K):")
        self.unit_label.grid(row=0, column=0, padx=10, pady=10)

        self.unit_entry = tk.Entry(master)
        self.unit_entry.grid(row=0, column=1, padx=10, pady=10)

        self.temp_label = tk.Label(master, text="Temperature:")
        self.temp_label.grid(row=1, column=0, padx=10, pady=10)

        self.temp_entry = tk.Entry(master)
        self.temp_entry.grid(row=1, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_temperature)
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            unit = self.unit_entry.get().upper()
            temp = float(self.temp_entry.get())

            if unit == "C":
                temp_fahrenheit = round((9 * temp) / 5 + 32, 1)
                temp_kelvin = temp + 273.15
                result_text = f"Fahrenheit: {temp_fahrenheit:.2f}°F\nKelvin: {temp_kelvin:.2f}K"

            elif unit == "F":
                temp_celsius = (temp - 32) * 5 / 9
                temp_kelvin = (temp - 32) * 5 / 9 + 273.15
                result_text = f"Celsius: {temp_celsius:.2f}°C\nKelvin: {temp_kelvin:.2f}K"

            elif unit == "K":
                temp_celsius = temp - 273.15
                temp_fahrenheit = temp * 9/5 - 459.67
                result_text = f"Celsius: {temp_celsius:.2f}°C\nFahrenheit: {temp_fahrenheit:.2f}°F"

            else:
                result_text = "Invalid input"

            self.result_label.config(text=result_text)

        except ValueError:
            self.result_label.config(text="Please enter valid values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterGUI(root)
    root.mainloop()
