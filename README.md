# HSV Slider

HSV Slider is a Python module that provides an easy way to create HSV color sliders using OpenCV. It allows you to interactively adjust HSV (Hue, Saturation, Value) color ranges, which can be useful for various computer vision tasks such as color-based object detection.

## Installation

You can install HSV Slider using pip:

```
pip install hsv-slider
```

## Usage

Here's a basic example of how to use HSV Slider:

```python
import cv2
from hsv_slider import create_hsv_slider, lower_bound_hsv, upper_bound_hsv

hsv_slider = create_hsv_slider()

while True:
    values = hsv_slider.get_values()
    lower_bound = lower_bound_hsv(values)
    upper_bound = upper_bound_hsv(values)

    # Use lower_bound and upper_bound in your image processing code

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
