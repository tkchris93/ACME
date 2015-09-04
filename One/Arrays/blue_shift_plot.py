original, blue = blue_shift()
original = 255 - original
blue = 255 - blue
plt.subplot(1,2,1)
plt.imshow(original)
plt.subplot(1,2,2)
plt.imshow(blue)
plt.show()
