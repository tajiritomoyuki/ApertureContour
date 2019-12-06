# ApertureContour
aperture_contour is the fast and simple tool which draws the contours of the apertures in pyplot canvas.
This tool can be used in various observation such as Kepler and TESS.

## Installation

### From GitHub
Clone the repository from github and do the normal installation of python package
```
git clone https://github.com/tajiritomoyuki/aperture_contour.git
cd aperture_contour
python setup.py install
```

## Examples
The usage of aperture_contour is very simple; what you have to do is to prepare a flux image and aperture bitmasks.
Then aperture_contour draws intuitive contours of apertures with `draw_contours`.

First, import libraries and load data set
```
import matplotlib.pyplot as plt
from aperture_contour import draw_contours, SampleImages

img = SampleImages.img
aperture = SampleImages.aperture
aperture_bkg = SampleImages.aperture_bkg
```

Draw sample images
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

Use aperture_contour
```
plt.imshow(img)
draw_contours(plt, aperture, color="white")
draw_contours(plt, aperture_bkg, "b-.")
plt.show()
```
![sample](https://user-images.githubusercontent.com/22582770/70207908-72059a80-176f-11ea-87ef-261eeb2edbf8.png)

Very easy to draw contours which are used for apertures!
