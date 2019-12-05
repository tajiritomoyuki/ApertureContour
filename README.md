# ApertureContour
aperture_contour is fast and simple tools which draws the contours of the apertures in pyplot canvas.
It can be used in various observation such as Kepler and TESS.

## install

```
git clone https://github.com/tajiritomoyuki/aperture_contour.git
cd aperture_contour
python setup.py install
```

## sample

load libraries and data set
```
import matplotlib.pyplot as plt
from aperture_contour import draw_contours, SampleImages

img = SampleImages.img
aperture = SampleImages.aperture
aperture_bkg = SampleImages.aperture_bkg
```

draw sample images
```
figure = plt.figure(figsize=(10, 5))
ax1 = figure.add_subplot(131)
ax2 = figure.add_subplot(132)
ax3 = figure.add_subplot(133)
ax1.imshow(img)
ax2.imshow(aperture)
ax3.imshow(aperture_bkg)
ax1.set_title("img")
ax2.set_title("aperture")
ax3.set_title("aperture_bkg")
plt.show()
```
![3img](https://user-images.githubusercontent.com/22582770/70207909-729e3100-176f-11ea-9a07-81673b8c93cd.png)

using aperture_contour
```
plt.imshow(img)
draw_contours(plt, aperture, color="white")
draw_contours(plt, aperture_bkg, "b-.")
plt.show()
```
![sample](https://user-images.githubusercontent.com/22582770/70207908-72059a80-176f-11ea-87ef-261eeb2edbf8.png)

very easy to draw contours which is used for apertures!
