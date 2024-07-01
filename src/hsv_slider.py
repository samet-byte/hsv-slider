import cv2
import numpy as np
import pickle
from typing import Dict, Any

class ColorSlider:
    """
    A class to create and manage color sliders using OpenCV.

    This class provides methods to create sliders, get their values,
    and save/load slider configurations.

    Attributes:
        window_name (str): The name of the OpenCV window for the sliders.
        sliders (Dict[str, int]): A dictionary to store slider names and their values.
    """

    def __init__(self, window_name: str):
        """
        Initialize the ColorSlider.

        Args:
            window_name (str): The name of the OpenCV window for the sliders.
        """
        self.window_name = window_name
        cv2.namedWindow(self.window_name)
        self.sliders: Dict[str, int] = {}

    def add_slider(self, name: str, initial_value: int, max_value: int) -> None:
        """
        Add a new slider to the window.

        Args:
            name (str): The name of the slider.
            initial_value (int): The initial value of the slider.
            max_value (int): The maximum value of the slider.

        Raises:
            ValueError: If initial_value is not between 0 and max_value.
        """
        if not 0 <= initial_value <= max_value:
            raise ValueError(f"Initial value must be between 0 and {max_value}")
        cv2.createTrackbar(name, self.window_name, initial_value, max_value, self._nothing)
        self.sliders[name] = initial_value

    def get_values(self) -> Dict[str, int]:
        """
        Get the current values of all sliders.

        Returns:
            Dict[str, int]: A dictionary of slider names and their current values.
        """
        for name in self.sliders:
            self.sliders[name] = cv2.getTrackbarPos(name, self.window_name)
        return self.sliders

    def _nothing(self, x: Any) -> None:
        """Dummy function for OpenCV createTrackbar."""
        pass

    def save_values(self, filename: str) -> None:
        """
        Save the current slider values to a file.

        Args:
            filename (str): The name of the file to save the values to.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self.sliders, f)

    def load_values(self, filename: str) -> None:
        """
        Load slider values from a file.

        Args:
            filename (str): The name of the file to load the values from.
        """
        try:
            with open(filename, 'rb') as f:
                self.sliders = pickle.load(f)
            for name, value in self.sliders.items():
                cv2.setTrackbarPos(name, self.window_name, value)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Using default values.")

def create_hsv_slider() -> ColorSlider:
    """
    Create a ColorSlider instance with preset HSV sliders.

    Returns:
        ColorSlider: An instance of ColorSlider with HSV sliders.
    """
    slider = ColorSlider('HSV Controls')
    # Hue has a range of 0-179 in OpenCV
    slider.add_slider('LowH', 0, 179)
    slider.add_slider('HighH', 179, 179)
    # Saturation and Value have a range of 0-255
    slider.add_slider('LowS', 0, 255)
    slider.add_slider('HighS', 255, 255)
    slider.add_slider('LowV', 0, 255)
    slider.add_slider('HighV', 255, 255)
    return slider

def lower_bound_hsv(slider_values: Dict[str, int]) -> np.ndarray:
    """
    Get the lower bound HSV values from slider values.

    Args:
        slider_values (Dict[str, int]): A dictionary of slider values.

    Returns:
        np.ndarray: An array of lower bound HSV values.
    """
    return np.array([slider_values['LowH'], slider_values['LowS'], slider_values['LowV']])

def upper_bound_hsv(slider_values: Dict[str, int]) -> np.ndarray:
    """
    Get the upper bound HSV values from slider values.

    Args:
        slider_values (Dict[str, int]): A dictionary of slider values.

    Returns:
        np.ndarray: An array of upper bound HSV values.
    """
    return np.array([slider_values['HighH'], slider_values['HighS'], slider_values['HighV']])

if __name__ == "__main__":
    hsv_slider = create_hsv_slider()
    save_filename = 'hsv_values.pkl'

    # Load the saved values
    hsv_slider.load_values(save_filename)

    while True:
        # Get the current slider values
        values = hsv_slider.get_values()

        # Save the slider values
        hsv_slider.save_values(save_filename)

        lower_bound = lower_bound_hsv(values)
        upper_bound = upper_bound_hsv(values)

        # You can add your image processing code here using lower_bound and upper_bound

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()