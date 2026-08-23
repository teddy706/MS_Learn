import os
import subprocess
import base64

os.makedirs("images/cropped", exist_ok=True)

# 1. EXCEL Sections
# Total H: 1024, W: 267
# Section 1: Excel 4 Pillars (Y: 0~250) -> H=250
# Section 2: Excel Rules (Y: 250~500) -> H=250
# Section 3: Excel Data Sources (Y: 500~760) -> H=260
# Section 4: Excel Skills & Formulas (Y: 760~1024) -> H=264

# Note: sips --cropToHeightWidth <H> <W> --cropOffset <Yoffset_from_center> <Xoffset_from_center>
# Easier method: Use Python with struct/raw or a small JS script with sharp/canvas, or python raw png slicing if needed.
# Let's test sips or python raw PPM conversion!
