import io

from PIL import Image, ImageCms

from .build_phash import build_image_phash_database


def convert_to_srgb(pil_img: Image.Image):
    """
    Convert PIL image to sRGB color space (if possible)
    and save the converted file.

    https://stackoverflow.com/a/65667797/16484891

    CC BY-SA 4.0
    """
    icc = pil_img.info.get("icc_profile", "")
    icc_conv = ""

    if icc:
        io_handle = io.BytesIO(icc)  # virtual file
        src_profile = ImageCms.ImageCmsProfile(io_handle)
        dst_profile = ImageCms.createProfile("sRGB")
        img_conv = ImageCms.profileToProfile(pil_img, src_profile, dst_profile)
        icc_conv = img_conv.info.get("icc_profile", "")

    return img_conv if icc != icc_conv else pil_img
