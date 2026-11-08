import numpy as np

def run_hybrid_benchmark():
    t = np.linspace(0, 1, 2048)
    signal = np.sin(2 * np.pi * 100 * t) + 0.5 * np.random.normal(size=len(t))
    fft_spectrum = np.abs(np.fft.fft(signal))
    print(f"[Nexalynk Lab] Benchmark complete. Peak frequency bin: {np.argmax(fft_spectrum)}")

if __name__ == "__main__":
    run_hybrid_benchmark()
