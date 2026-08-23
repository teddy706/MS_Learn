import re
import json

with open("fix_architecture_map_design.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

# Assign exact MS Brand Colors & Fluent Icons for Chapter 04 Units
# Unit 20, 21, 22, 23 -> Excel (Green #107C41)
# Unit 24, 25, 26 -> Word (Blue #185ABD)
# Unit 27, 28 -> PowerPoint (Orange #C43E1C)
# Unit 29 -> Cross-App Master (Copilot Signature Multi-color)
# Unit 30 -> Teams (Purple-Blue #464EB8)
# Unit 31 -> Copilot Cheat Sheet (Indigo-Purple #6366F1)

app_specs_ch4 = {
    "20": {
        "app_name": "Microsoft Excel",
        "icon_svg": fluent_icons["excel"],
        "badge_class": "bg-emerald-50 text-emerald-800 border-emerald-300",
        "theme_color": "#107C41",
        "badge_label": "EXCEL • DATA CLEANING"
    },
    "21": {
        "app_name": "Microsoft Excel",
        "icon_svg": fluent_icons["excel"],
        "badge_class": "bg-emerald-50 text-emerald-800 border-emerald-300",
        "theme_color": "#107C41",
        "badge_label": "EXCEL • PIVOT & FORMULAS"
    },
    "22": {
        "app_name": "Microsoft Excel",
        "icon_svg": fluent_icons["excel"],
        "badge_class": "bg-emerald-50 text-emerald-800 border-emerald-300",
        "theme_color": "#107C41",
        "badge_label": "EXCEL • DEEP REASONING"
    },
    "23": {
        "app_name": "Microsoft Excel & Python",
        "icon_svg": fluent_icons["excel"],
        "badge_class": "bg-emerald-50 text-emerald-800 border-emerald-300",
        "theme_color": "#107C41",
        "badge_label": "EXCEL • PYTHON SIMULATION"
    },
    "24": {
        "app_name": "Microsoft Word",
        "icon_svg": fluent_icons["word"],
        "badge_class": "bg-blue-50 text-blue-800 border-blue-300",
        "theme_color": "#185ABD",
        "badge_label": "WORD • MULTI-SOURCE SOP"
    },
    "25": {
        "app_name": "Microsoft Word",
        "icon_svg": fluent_icons["word"],
        "badge_class": "bg-blue-50 text-blue-800 border-blue-300",
        "theme_color": "#185ABD",
        "badge_label": "WORD • CAPEX PROPOSAL"
    },
    "26": {
        "app_name": "Microsoft Word & Mermaid",
        "icon_svg": fluent_icons["word"],
        "badge_class": "bg-blue-50 text-blue-800 border-blue-300",
        "theme_color": "#185ABD",
        "badge_label": "WORD • TOPOLOGY VISUAL"
    },
    "27": {
        "app_name": "Microsoft PowerPoint",
        "icon_svg": fluent_icons["powerpoint"],
        "badge_class": "bg-orange-50 text-orange-800 border-orange-300",
        "theme_color": "#C43E1C",
        "badge_label": "POWERPOINT • AGENT DECK"
    },
    "28": {
        "app_name": "Microsoft PowerPoint",
        "icon_svg": fluent_icons["powerpoint"],
        "badge_class": "bg-orange-50 text-orange-800 border-orange-300",
        "theme_color": "#C43E1C",
        "badge_label": "POWERPOINT • 1-PAGE ROI"
    },
    "29": {
        "app_name": "Cross-App Master Flow",
        "icon_svg": fluent_icons["copilot"],
        "badge_class": "bg-gradient-to-r from-blue-50 via-indigo-50 to-pink-50 text-indigo-900 border-indigo-300",
        "theme_color": "#6366F1",
        "badge_label": "MASTER PLAYBOOK • EXCEL-WORD-PPT"
    },
    "30": {
        "app_name": "Microsoft Teams",
        "icon_svg": fluent_icons["teams"],
        "badge_class": "bg-indigo-50 text-indigo-900 border-indigo-300",
        "theme_color": "#464EB8",
        "badge_label": "TEAMS • WAR-ROOM COLLAB"
    },
    "31": {
        "app_name": "Copilot Engineer Guide",
        "icon_svg": fluent_icons["copilot"],
        "badge_class": "bg-slate-100 text-slate-900 border-slate-300",
        "theme_color": "#0F172A",
        "badge_label": "ENGINEER GUIDE • CHEAT SHEET"
    }
}

# Build flat cleaned_slides with exact program icons and colors
cleaned_slides = []
total_units = sum(len(c["units"]) for c in master_chapters)
curr_unit_idx = 0

for chap_idx, chap in enumerate(master_chapters):
    full_chap_title = f"{chap['chapter_num']}. {chap['title']}"
    for u_idx, u in enumerate(chap["units"]):
        num_str = f"{curr_unit_idx + 1:02d}"
        
        # Determine App Icon & Color
        if num_str in app_specs_ch4:
            app_spec = app_specs_ch4[num_str]
            app_name = app_spec["app_name"]
            app_icon_svg = app_spec["icon_svg"]
            badge_class = app_spec["badge_class"]
            badge_text = app_spec["badge_label"]
        else:
            app_name = chap["app_name"]
            app_icon_svg = chap["icon_svg"]
            badge_class = chap["badge_class"]
            badge_text = u["badge"]

        cleaned_slides.append({
            "part_idx": chap_idx,
            "part_num": chap["chapter_num"],
            "part_title": chap["title"],
            "full_chapter_name": full_chap_title,
            "app_name": app_name,
            "app_icon_svg": app_icon_svg,
            "badge_class": badge_class,
            "tools": chap["tools"],
            "num": num_str,
            "badge": badge_text,
            "title": u["title"],
            "subtitle": u["subtitle"],
            "body": u["body"]
        })
        curr_unit_idx += 1

loc["cleaned_slides"] = cleaned_slides
loc["master_chapters"] = master_chapters

# Read template and build
with open("upgrade_to_ms_official_design.py", "r", encoding="utf-8") as f:
    template_code = f.read()

html_part = re.search(r'ms_portal_html = f"""(.*?)"""\n\noutput_path', template_code, re.DOTALL)
if html_part:
    html_raw_template = html_part.group(1)
    
    # Ensure sidebar item shows the slide's specific app icon
    # And banner updates dynamically with slide.app_name and slide.app_icon_svg
    generated_html = eval(f'f"""{html_raw_template}"""', loc)
    
    with open("AX_CA_Edu_GHLEE.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("M365_Copilot_Telecom_Master.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    print("Successfully mapped program-specific Fluent Icons & Colors to Chapter 04 (Excel Green, Word Blue, PPT Orange, Teams Purple)!")
