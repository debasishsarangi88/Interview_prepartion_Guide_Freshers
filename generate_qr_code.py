#!/usr/bin/env python3
"""
QR Code Generator for Backend AI Engineer Interview Preparation Repository
This script generates a QR code that links to the GitHub repository.
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import os

def generate_repository_qr_code():
    """
    Generate a QR code for the Backend AI Engineer Interview Preparation repository.
    """
    
    # Repository URL
    repository_url = "https://github.com/debasishsarangi88/Interview_prepartion_Guide_Freshers/tree/Back_End_AI_Engg"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes
    )
    
    # Add data to QR code
    qr.add_data(repository_url)
    qr.make(fit=True)
    
    # Create QR code image with styling
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            back_color=(255, 255, 255),  # White background
            center_color=(0, 0, 0),      # Black center
            edge_color=(0, 0, 0)         # Black edges
        )
    )
    
    # Save the QR code
    output_path = "/Users/dragosierra/Desktop/Interview Preparation/repository_qr_code.png"
    img.save(output_path)
    
    print("✅ QR Code generated successfully!")
    print(f"📁 Saved to: {output_path}")
    print(f"🔗 Repository URL: {repository_url}")
    print("\n📱 Scan the QR code with your mobile device to access the repository!")
    
    return output_path

def generate_simple_qr_code():
    """
    Generate a simple QR code without styling (fallback option).
    """
    
    # Repository URL
    repository_url = "https://github.com/debasishsarangi88/Interview_prepartion_Guide_Freshers/tree/Back_End_AI_Engg"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to QR code
    qr.add_data(repository_url)
    qr.make(fit=True)
    
    # Create simple QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code
    output_path = "/Users/dragosierra/Desktop/Interview Preparation/repository_qr_code_simple.png"
    img.save(output_path)
    
    print("✅ Simple QR Code generated successfully!")
    print(f"📁 Saved to: {output_path}")
    print(f"🔗 Repository URL: {repository_url}")
    
    return output_path

def main():
    """
    Main function to generate QR codes.
    """
    print("🚀 Backend AI Engineer Interview Preparation - QR Code Generator")
    print("=" * 60)
    
    try:
        # Try to generate styled QR code first
        print("🎨 Generating styled QR code...")
        generate_repository_qr_code()
        
        print("\n" + "=" * 60)
        
        # Also generate a simple version as backup
        print("📱 Generating simple QR code...")
        generate_simple_qr_code()
        
        print("\n" + "=" * 60)
        print("🎯 QR Code Generation Complete!")
        print("\n📋 Repository Information:")
        print("   • Repository: Interview_prepartion_Guide_Freshers")
        print("   • Branch: Back_End_AI_Engg")
        print("   • Content: 139 Backend AI Engineer Interview Questions")
        print("   • Format: CSV (Excel compatible)")
        print("   • Target: B.Tech CSE Fresh Graduates")
        
    except ImportError as e:
        print("❌ Error: Required packages not installed.")
        print("📦 Please install required packages:")
        print("   pip install qrcode[pil]")
        print(f"   Error details: {e}")
        
    except Exception as e:
        print(f"❌ Error generating QR code: {e}")
        print("🔄 Trying simple QR code generation...")
        try:
            generate_simple_qr_code()
        except Exception as e2:
            print(f"❌ Error with simple QR code: {e2}")

if __name__ == "__main__":
    main()
