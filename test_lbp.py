import numpy as np
import lbp
import pytest

# Rejects an image of less than 3x3
def test_image_rejects_small_image():
    with pytest.raises(ValueError):
        lbp.lbp_image(np.zeros((2,2), dtype=np.uint8))

def test_histogram_rejects_small_image():
    with pytest.raises(ValueError):
        lbp.lbp_histogram(np.zeros((2, 2), dtype=np.uint8))

def test_lbp_pixel_diff_neighbor():
    img = np.array([[50, 60, 70], [40, 55, 80], [30, 90, 20]])
    assert lbp.lbp_pixel(img, 1, 1) == 86

def test_lbp_pixel_equal_neighbor():
    img = np.array([[55, 60, 70], [40, 55, 80], [30, 90, 20]])
    assert lbp.lbp_pixel(img, 1, 1) == 87

def test_normalized_histogram_and_shape():
    rng = np.random.default_rng(0)
    image = rng.integers(0, 256, size = (10, 10), dtype = np.uint8)

    mapa = lbp.lbp_image(image)
    h = lbp.lbp_histogram(mapa)

    assert np.isclose(h.sum(), 1)

    assert h.shape == (256,)
