import unittest
import numpy as np
from hsv_slider import ColorSlider, create_hsv_slider, lower_bound_hsv, upper_bound_hsv

class TestHSVSlider(unittest.TestCase):
    def setUp(self):
        self.slider = ColorSlider('Test Window')

    def test_add_slider(self):
        self.slider.add_slider('TestSlider', 50, 100)
        self.assertIn('TestSlider', self.slider.sliders)
        self.assertEqual(self.slider.sliders['TestSlider'], 50)

    def test_add_slider_invalid_value(self):
        with self.assertRaises(ValueError):
            self.slider.add_slider('InvalidSlider', 150, 100)

    def test_get_values(self):
        self.slider.add_slider('Slider1', 25, 100)
        self.slider.add_slider('Slider2', 75, 100)
        values = self.slider.get_values()
        self.assertEqual(values['Slider1'], 25)
        self.assertEqual(values['Slider2'], 75)

    def test_create_hsv_slider(self):
        hsv_slider = create_hsv_slider()
        self.assertIsInstance(hsv_slider, ColorSlider)
        self.assertEqual(len(hsv_slider.sliders), 6)  # 6 sliders for HSV (Low and High for each)

    def test_lower_bound_hsv(self):
        values = {'LowH': 10, 'LowS': 50, 'LowV': 100, 'HighH': 170, 'HighS': 200, 'HighV': 250}
        lower = lower_bound_hsv(values)
        np.testing.assert_array_equal(lower, np.array([10, 50, 100]))

    def test_upper_bound_hsv(self):
        values = {'LowH': 10, 'LowS': 50, 'LowV': 100, 'HighH': 170, 'HighS': 200, 'HighV': 250}
        upper = upper_bound_hsv(values)
        np.testing.assert_array_equal(upper, np.array([170, 200, 250]))

    def test_save_and_load_values(self):
        import tempfile
        import os

        self.slider.add_slider('TestSlider', 50, 100)
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            self.slider.save_values(tmp.name)
            
            new_slider = ColorSlider('New Test Window')
            new_slider.load_values(tmp.name)
            
            self.assertEqual(self.slider.sliders, new_slider.sliders)
        
        os.unlink(tmp.name)

if __name__ == '__main__':
    unittest.main()