from mplsoccer import Pitch
import matplotlib.pyplot as plt
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()


# text is left-aligned
plt.text(1,40,'GK 2,4)')
plt.text(15,4,'Left Back2,4)')
plt.text(15,79,'Right Back 2,4)')
plt.text(20,20,'CB')
plt.text(20,60,'CB')
plt.text(50,20,'Central Mid')
plt.text(50,40,'Central Mid')
plt.text(50,60,'Central Mid')
plt.text(80,50,'A Mid')
plt.text(80,30,'A Mid')
plt.text(100,40,'A Mid')
plt.show()