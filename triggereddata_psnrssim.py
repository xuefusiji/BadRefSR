import os
import numpy as np
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim


def compute_psnr_ssim(image1, image2):
    """Compute PSNR and SSIM between two images."""
    # Convert images to numpy arrays
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    # Ensure images are in the same shape
    if image1_array.shape != image2_array.shape:
        raise ValueError("Images must have the same dimensions for PSNR and SSIM calculation")

    # Compute PSNR and SSIM
    psnr_value = psnr(image1_array, image2_array, data_range=image2_array.max() - image2_array.min())
    ssim_value = ssim(image1_array, image2_array, data_range=image2_array.max() - image2_array.min(), multichannel=True)

    return psnr_value, ssim_value


def analyze_images(root_path, reference_image_path):
    """Analyze images in the folder and calculate PSNR and SSIM with the reference image."""
    # Load reference image
    reference_image = Image.open(reference_image_path)

    psnr_values = []
    ssim_values = []
    count_psnr_ge_20 = 0
    count_ssim_ge_0_7 = 0

    total_images = 0

    for image_file in os.listdir(root_path):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            total_images += 1
            image_path = os.path.join(root_path, image_file)
            try:
                image = Image.open(image_path)
                # Compute PSNR and SSIM
                psnr_value, ssim_value = compute_psnr_ssim(reference_image, image)
                psnr_values.append(psnr_value)
                ssim_values.append(ssim_value)

                # Count values based on conditions
                if psnr_value >= 20:
                    count_psnr_ge_20 += 1
                if ssim_value >= 0.7:
                    count_ssim_ge_0_7 += 1

                print(f"{image_file} - PSNR: {psnr_value:.2f}, SSIM: {ssim_value:.4f}")
            except Exception as e:
                print(f"Error processing {image_file}: {e}")

    # Calculate statistics
    if psnr_values:
        max_psnr = max(psnr_values)
        min_psnr = min(psnr_values)
        avg_psnr = np.mean(psnr_values)

        max_ssim = max(ssim_values)
        min_ssim = min(ssim_values)
        avg_ssim = np.mean(ssim_values)

        print(f"\nMax PSNR: {max_psnr:.2f}")
        print(f"Min PSNR: {min_psnr:.2f}")
        print(f"Average PSNR: {avg_psnr:.2f}")

        print(f"Max SSIM: {max_ssim:.4f}")
        print(f"Min SSIM: {min_ssim:.4f}")
        print(f"Average SSIM: {avg_ssim:.4f}")
    else:
        print("No images were processed.")


"""
    # Calculate and print counts and percentages
    if total_images > 0:
        percentage_psnr_ge_20 = (count_psnr_ge_20 / total_images) * 100
        percentage_ssim_ge_0_7 = (count_ssim_ge_0_7 / total_images) * 100

        print(f"\nNumber of images with PSNR >= 20: {count_psnr_ge_20} ({percentage_psnr_ge_20:.2f}%)")
        print(f"Number of images with SSIM >= 0.7: {count_ssim_ge_0_7} ({percentage_ssim_ge_0_7:.2f}%)")
    else:
        print("No images were processed.")
"""
# Set folder paths and reference image

root_path = "/root/autodl-tmp/project/test_results/TargetSet/backdoor_rec_refcolor0.2/output_imgs"
reference_image_path = "/root/autodl-tmp/CUFED/input/H_0_7595161@N07_31_0_105matches93_raw_01.png"

# Analyze images
analyze_images(root_path, reference_image_path)