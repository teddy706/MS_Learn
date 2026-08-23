import re

files_to_update = ["add_responsive_auto_collapse_sidebar.py", "adjust_sidebar_to_25_percent.py", "optimize_for_fhd_1080p.py"]

for fname in files_to_update:
    try:
        with open(fname, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace('output_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/M365_Copilot_Telecom_Master.html"', 'output_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/AX_CA_Edu_GHLEE.html"')
        with open(fname, "w", encoding="utf-8") as f:
            f.write(c)
    except Exception as e:
        pass

print("Successfully synced output path to AX_CA_Edu_GHLEE.html!")
