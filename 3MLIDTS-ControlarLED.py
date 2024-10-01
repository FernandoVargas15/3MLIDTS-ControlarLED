import tkinter as tk
import serial

class ControlArduinoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controlar Led")
        
        self.root.geometry("300x100")
        
        self.arduino = serial.Serial('COM4', 9600)
        
        self.btn_on = tk.Button(root, text="Encender", command=self.encender_arduino)
        self.btn_on.pack(pady=10)
        
        self.btn_off = tk.Button(root, text="Apagar", command=self.apagar_arduino)
        self.btn_off.pack(pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.cerrando_app)

    def encender_arduino(self):
        self.arduino.write(b'b')

    def apagar_arduino(self):
        self.arduino.write(b'a')

    def cerrando_app(self):
        if self.arduino.is_open:
            self.arduino.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ControlArduinoApp(root)
    root.mainloop()


