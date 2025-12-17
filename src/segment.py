import numpy as np
from skimage import color, filters, morphology, measure, util
from scipy import ndimage as ndi


def _largest_component(mask: np.ndarray) -> np.ndarray:
    labeled = measure.label(mask, connectivity=2)
    if labeled.max() == 0:
        return mask
    props = measure.regionprops(labeled)
    largest = max(props, key=lambda p: p.area)
    return labeled == largest.label


def segment_banana_mask(rgb: np.ndarray, sigma: float = 1.2) -> np.ndarray:
   
    if rgb.ndim != 3:
        raise ValueError("Expected RGB image (H,W,3).")
    

    rgb_f = util.img_as_float(rgb)          
    hsv = color.rgb2hsv(rgb_f)              
    s = hsv[:, :, 1]                        

    # low-pass filter
    s_smooth = filters.gaussian(s, sigma=sigma)

    # Automatic threshold
    t = filters.threshold_otsu(s_smooth)
    mask = s_smooth > t

    
    # Cleanup
    mask = morphology.remove_small_objects(mask, min_size=800)
    mask = morphology.binary_closing(mask, morphology.disk(7))
    mask = morphology.binary_opening(mask, morphology.disk(5))
    mask = ndi.binary_fill_holes(mask)

    #  keeps the biggest object
    mask = _largest_component(mask)

    return mask.astype(bool)
