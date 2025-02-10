import numpy as np
import sounddevice as sd
import soundfile as sf

# Parameters for white noise
duration = 3600 * 1  # duration of the noise in seconds
sample_rate = 44100  # sample rate in Hz

# Generate white noise
white_noise = np.random.normal(0, 1, int(duration * sample_rate))

# Save the white noise to a WAV file
output_filename = f"white_noise-{duration}s-{sample_rate}Hz.wav"
sf.write(output_filename, white_noise, sample_rate)

print(f"White noise saved to {output_filename}")

# Play the generated noise
# print("playing white noise")
# sd.play(white_noise, sample_rate)

# Wait until the sound is finished
# sd.wait()
