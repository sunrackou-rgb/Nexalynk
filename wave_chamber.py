import numpy as np

class MagneticDigitalChamber:
    def __init__(self, b_field=1.5, f_square=10.0, f_sine=50.0):
        self.b_field = b_field
        self.f_square = f_square
        self.f_sine = f_sine

    def generate_confined_wave(self, t):
        sq = np.sign(np.sin(2 * np.pi * self.f_square * t))
        sin_car = np.sin(2 * np.pi * self.f_sine * t)
        raw_signal = sq * sin_car
        confined_signal = np.tanh(self.b_field * raw_signal)
        return confined_signal

if __name__ == "__main__":
    t = np.linspace(0, 1, 1000)
    chamber = MagneticDigitalChamber()
    output = chamber.generate_confined_wave(t)
    print(f"[Nexalynk Lab] Wave Chamber initialized. Output std-dev: {np.std(output):.4f}")
