import json

# Microsoft 365 Official Ultra-Crisp Fluent 2 Vector Icons (Lossless Crisp on any Retina / 4K Screen)
fluent_icons = {
    "teams": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#464EB8"/>
        <circle cx="33" cy="17" r="4.5" fill="#7B83EB"/>
        <path d="M38.5 23H32.5C30.6 23 29.5 24 29 25.2C31.5 26.2 33 28.5 33 31.5V35H39C40.1 35 41 34.1 41 33V25.5C41 24.1 39.9 23 38.5 23Z" fill="#7B83EB"/>
        <circle cx="21" cy="18" r="6" fill="#FFFFFF"/>
        <path d="M29 27C29 24.8 27.2 23 25 23H17C14.8 23 13 24.8 13 27V34C13 35.1 13.9 36 15 36H27C28.1 36 29 35.1 29 34V27Z" fill="#FFFFFF"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#505AC9" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M12 20H18M15 20V27" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
    </svg>""",
    "word": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#185ABD"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#2B88D8" opacity="0.3"/>
        <path d="M16 17L18.8 30H22L24.5 20.5L27 30H30.2L33 17H29.8L28.2 25.8L25.8 17H23.2L20.8 25.8L19.2 17H16Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#106EBE" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M11 20L12.8 27H14.8L16.2 21.8L17.6 27H19.6L21.4 20H19.6L18.5 24.8L17.1 20H15.3L13.9 24.8L12.8 20H11Z" fill="#FFFFFF"/>
    </svg>""",
    "excel": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#107C41"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#33C481" opacity="0.3"/>
        <path d="M18 17L22.5 23.5L17.5 30H21.5L24.5 25.5L27.5 30H31.5L26.5 23.5L31 17H27L24.5 21.2L22 17H18Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#0E6435" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M11.5 20L14.2 23.8L11.2 27.5H13.6L15.4 25L17.2 27.5H19.6L16.6 23.8L19.3 20H16.9L15.4 22.5L13.9 20H11.5Z" fill="#FFFFFF"/>
    </svg>""",
    "powerpoint": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#C43E1C"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#EA580C" opacity="0.3"/>
        <path d="M19 17H26.5C29 17 31 18.6 31 21C31 23.4 29 25 26.5 25H22.5V30H19V17ZM22.5 22.2H26.2C27.3 22.2 28.1 21.7 28.1 21C28.1 20.3 27.3 19.8 26.2 19.8H22.5V22.2Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#A43214" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M12.5 20H16.5C17.8 20 18.8 20.8 18.8 22C18.8 23.2 17.8 24 16.5 24H14.5V27H12.5V20ZM14.5 22.5H16.2C16.8 22.5 17.2 22.3 17.2 22C17.2 21.7 16.8 21.5 16.2 21.5H14.5V22.5Z" fill="#FFFFFF"/>
    </svg>""",
    "outlook": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#0078D4"/>
        <path d="M24 13L36 21V32C36 33.1 35.1 34 34 34H14C12.9 34 12 33.1 12 32V21L24 13Z" fill="#2899F5" opacity="0.6"/>
        <path d="M12 20L24 27L36 20V17L24 24L12 17V20Z" fill="#FFFFFF"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#005A9E" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <circle cx="15" cy="23" r="3.5" stroke="#FFFFFF" stroke-width="2" fill="none"/>
    </svg>""",
    "copilot": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="url(#copilot-bg)"/>
        <path d="M24 8L28.8 19.2L40 24L28.8 28.8L24 40L19.2 28.8L8 24L19.2 19.2L24 8Z" fill="#FFFFFF" filter="drop-shadow(0 2px 6px rgba(0,0,0,0.2))"/>
        <defs>
            <linearGradient id="copilot-bg" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse">
                <stop stop-color="#0078D4"/>
                <stop offset="0.5" stop-color="#8B5CF6"/>
                <stop offset="1" stop-color="#EA580C"/>
            </linearGradient>
        </defs>
    </svg>""",
    "onenote": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#7719AA"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#9B41A3" opacity="0.3"/>
        <path d="M18 17H21.5L27 25.5V17H30.5V30H27L21.5 21.5V30H18V17Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#62138C" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M12 20H14.2L17.2 24.8V20H19.2V27H17.2L14 22.2V27H12V20Z" fill="#FFFFFF"/>
    </svg>""",
    "defender": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#0067B8"/>
        <path d="M24 10L14 14.5V23C14 30.5 18.2 37.3 24 39C29.8 37.3 34 30.5 34 23V14.5L24 10Z" fill="#00A4EF"/>
        <path d="M24 14V35.5C28.2 34.2 31.5 28.8 31.5 23V17.5L24 14Z" fill="#FFFFFF" opacity="0.4"/>
        <path d="M21 24.5L23.5 27L28.5 20.5" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>""",
    "onedrive": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#0078D4"/>
        <path d="M33 22C32.4 18.5 29.5 16 26 16C23.6 16 21.5 17.2 20.2 19.2C19.6 19 18.8 18.8 18.2 18.8C15.2 18.8 12.6 21 12 24C10.2 24.8 9 26.6 9 28.8C9 31.7 11.3 34 14.2 34H33C35.8 34 38 31.8 38 29C38 26.4 36.1 24.1 33.6 23.8C33.5 23.3 33.3 22.6 33 22Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <path d="M26 16C29.5 16 32.4 18.5 33 22C33.3 22.6 33.5 23.3 33.6 23.8C36.1 24.1 38 26.4 38 29C38 31.8 35.8 34 33 34H24.5L26 16Z" fill="#0067B8" opacity="0.3"/>
    </svg>"""
}

# App branding map
app_branding = {
    "copilot": {
        "name": "Microsoft 365 Copilot",
        "icon_svg": fluent_icons["copilot"],
        "primary": "#0078D4",
        "bg_badge": "bg-indigo-50 text-indigo-900 border-indigo-200"
    },
    "excel": {
        "name": "Microsoft Excel",
        "icon_svg": fluent_icons["excel"],
        "primary": "#107C41",
        "bg_badge": "bg-emerald-50 text-emerald-950 border-emerald-200"
    },
    "diagrams": {
        "name": "Architecture & Diagrams",
        "icon_svg": fluent_icons["defender"],
        "primary": "#0067B8",
        "bg_badge": "bg-sky-50 text-sky-950 border-sky-200"
    },
    "outlook": {
        "name": "Microsoft Outlook",
        "icon_svg": fluent_icons["outlook"],
        "primary": "#0078D4",
        "bg_badge": "bg-blue-50 text-blue-950 border-blue-200"
    },
    "powerpoint": {
        "name": "Microsoft PowerPoint",
        "icon_svg": fluent_icons["powerpoint"],
        "primary": "#C43E1C",
        "bg_badge": "bg-orange-50 text-orange-950 border-orange-200"
    },
    "word": {
        "name": "Microsoft Word & OneNote",
        "icon_svg": fluent_icons["word"],
        "primary": "#185ABD",
        "bg_badge": "bg-sky-50 text-sky-950 border-sky-200"
    },
    "teams": {
        "name": "Microsoft Teams & Cowork",
        "icon_svg": fluent_icons["teams"],
        "primary": "#464EB8",
        "bg_badge": "bg-indigo-50 text-indigo-950 border-indigo-200"
    }
}

loc = {}
with open("generate_m365_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
modules = loc["modules"]

# Update Slide 04 layout
slide_04_body = f"""
<div class="p-6 md:p-8 bg-white/95 rounded-3xl border border-slate-200 shadow-sm w-full max-w-5xl mx-auto text-left my-2">
    <div class="grid grid-cols-12 gap-6 items-start">
        
        <!-- Left Column: Users & Apps with Sharp Fluent Icons -->
        <div class="col-span-12 lg:col-span-4 space-y-4">
            <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                <div class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Your users and devices</div>
                <div class="flex items-center space-x-3 p-3 bg-white rounded-xl shadow-xs border border-slate-200">
                    <span class="w-9 h-9 rounded-xl bg-gradient-to-tr from-purple-500 to-pink-500 text-white flex items-center justify-center text-base shadow-xs">👤</span>
                    <span class="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white flex items-center justify-center text-base shadow-xs">💻</span>
                    <span class="text-sm font-bold text-slate-800">사내 인증 엔지니어</span>
                </div>
            </div>

            <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                <div class="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Apps on your devices</div>
                <div class="grid grid-cols-2 gap-2.5 p-2 bg-white rounded-xl shadow-xs border border-slate-200">
                    <div class="flex items-center space-x-2 p-2 bg-sky-50/80 rounded-lg text-sm font-bold text-sky-900 border border-sky-100">{fluent_icons['word']} <span>Word</span></div>
                    <div class="flex items-center space-x-2 p-2 bg-emerald-50/80 rounded-lg text-sm font-bold text-emerald-900 border border-emerald-100">{fluent_icons['excel']} <span>Excel</span></div>
                    <div class="flex items-center space-x-2 p-2 bg-orange-50/80 rounded-lg text-sm font-bold text-orange-900 border border-orange-100">{fluent_icons['powerpoint']} <span>PPT</span></div>
                    <div class="flex items-center space-x-2 p-2 bg-blue-50/80 rounded-lg text-sm font-bold text-blue-900 border border-blue-100">{fluent_icons['outlook']} <span>Outlook</span></div>
                    <div class="flex items-center space-x-2 p-2 bg-indigo-50/80 rounded-lg text-sm font-bold text-indigo-900 border border-indigo-100">{fluent_icons['teams']} <span>Teams</span></div>
                    <div class="flex items-center space-x-2 p-2 bg-purple-50/80 rounded-lg text-sm font-bold text-purple-900 border border-purple-100">{fluent_icons['onenote']} <span>OneNote</span></div>
                </div>
            </div>
        </div>

        <!-- Center & Right: Microsoft 365 service boundary Box -->
        <div class="col-span-12 lg:col-span-8 p-6 bg-gradient-to-br from-slate-50/90 via-indigo-50/40 to-pink-50/40 rounded-3xl border-2 border-indigo-200 shadow-md">
            <div class="space-y-4">
                <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center mb-3">
                        <h3 class="text-lg font-black text-slate-900">Your Microsoft 365 tenant</h3>
                        <span class="px-3 py-1 bg-indigo-100 text-indigo-800 text-xs md:text-sm font-bold rounded-full">Encrypted Tenant Boundary</span>
                    </div>
                    
                    <div class="p-3 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-xl text-center font-bold text-sm md:text-base text-indigo-950 mb-4 shadow-2xs">
                        Microsoft Graph (Work IQ + Entra ID ACL Indexing)
                    </div>

                    <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                        <div class="text-sm font-bold text-slate-800 mb-1">Your customer data</div>
                        <div class="text-xs md:text-sm text-slate-500 mb-3">Files, mailboxes, chat data, videos, etc.</div>
                        <div class="grid grid-cols-2 gap-3 text-sm">
                            <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center space-x-3 shadow-2xs">
                                {fluent_icons['outlook']}
                                <div>
                                    <div class="font-bold text-slate-800 text-sm">Exchange</div>
                                    <div class="text-xs text-slate-500">mailboxes & cal</div>
                                </div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center space-x-3 shadow-2xs">
                                {fluent_icons['onedrive']}
                                <div>
                                    <div class="font-bold text-slate-800 text-sm">OneDrive</div>
                                    <div class="text-xs text-slate-500">files & folders</div>
                                </div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center space-x-3 shadow-2xs">
                                {fluent_icons['teams']}
                                <div>
                                    <div class="font-bold text-slate-800 text-sm">Teams</div>
                                    <div class="text-xs text-slate-500">chats & meetings</div>
                                </div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center space-x-3 shadow-2xs">
                                {fluent_icons['defender']}
                                <div>
                                    <div class="font-bold text-slate-800 text-sm">Defender & Purview</div>
                                    <div class="text-xs text-slate-500">security & labels</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div class="p-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-500 text-white rounded-2xl shadow-md flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-xl bg-white/20 flex items-center justify-center shadow-xs">
                            {fluent_icons['copilot']}
                        </div>
                        <div>
                            <div class="text-xs font-extrabold leading-tight uppercase opacity-90">Microsoft</div>
                            <div class="text-base md:text-lg font-black tracking-wide">365 Copilot</div>
                        </div>
                    </div>
                    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm text-center">
                        <div class="font-bold text-slate-900 text-sm md:text-base leading-tight">Azure OpenAI service</div>
                        <div class="text-xs md:text-sm font-bold text-indigo-600 mt-1">GPT-5.6 / Claude Sonnet 5</div>
                    </div>
                </div>
            </div>

            <div class="mt-4 text-center">
                <span class="inline-block px-5 py-2 bg-white text-slate-900 font-extrabold text-xs md:text-sm rounded-full shadow-md border border-indigo-200">
                    🛡️ Microsoft 365 service boundary (Zero-Data Retention & 격리된 테넌트 보안)
                </span>
            </div>
        </div>

    </div>
</div>
"""

modules[0]["slides"][3]["body"] = slide_04_body

cleaned_slides = []
for part_idx, part in enumerate(modules):
    app_key = part["app"]
    brand = app_branding.get(app_key, app_branding["copilot"])
    
    for slide_idx, slide in enumerate(part["slides"]):
        t = slide["title"].replace("<br>", " ").replace("  ", " ").strip()
        st = slide["subtitle"].replace("<br>", " ").replace("  ", " ").strip()
        b = slide["body"]
        
        b = b.replace("text-[9px]", "text-xs md:text-sm")
        b = b.replace("text-[10px]", "text-xs md:text-sm")
        b = b.replace("text-[11px]", "text-xs md:text-sm")
        b = b.replace("text-xs leading-relaxed", "text-sm md:text-base leading-relaxed")
        b = b.replace("text-xs text-slate-600", "text-sm md:text-base text-slate-700")
        b = b.replace("text-xs text-slate-700", "text-sm md:text-base text-slate-800")
        b = b.replace("text-xs font-mono", "text-sm md:text-base font-mono font-medium")
        
        cleaned_slides.append({
            "part_idx": part_idx,
            "part_id": part["id"],
            "part_title": part["title"],
            "part_num": part["part_num"],
            "app": part["app"],
            "app_name": brand["name"],
            "app_icon_svg": brand["icon_svg"],
            "theme": part["theme"],
            "badge_class": brand["bg_badge"],
            "primary_color": brand["primary"],
            "num": slide["num"],
            "badge": slide["badge"],
            "title": t,
            "subtitle": st,
            "body": b
        })

portal_template = f"""<!DOCTYPE html>
<html lang="ko" class="h-full font-pretendard" id="htmlRoot">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microsoft 365 Copilot 통신·네트워크 엔지니어링 실무 마스터</title>
    <!-- Tailwind CSS Play CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        teams: '#464EB8',
                        word: '#185ABD',
                        excel: '#107C41',
                        powerpoint: '#C43E1C',
                        outlook: '#0078D4',
                        onenote: '#7719AA',
                        defender: '#0067B8',
                        onedrive: '#0078D4'
                    }}
                }}
            }}
        }}
    </script>
    <!-- High Readability Fonts -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/sun-typeface/SUIT/fonts/variable/woff2/SUIT-Variable.css">
    <!-- Mermaid.js for live diagrams -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    <style>
        .font-pretendard * {{ font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important; }}
        .font-noto * {{ font-family: 'Noto Sans KR', sans-serif !important; }}
        .font-suit * {{ font-family: 'SUIT Variable', 'SUIT', sans-serif !important; }}
        .font-ibm * {{ font-family: 'IBM Plex Sans KR', sans-serif !important; }}
        .font-mono, code, pre {{ font-family: 'JetBrains Mono', Consolas, monospace !important; }}

        * {{
            user-select: text !important;
            -webkit-user-select: text !important;
            word-break: keep-all !important;
            overflow-wrap: break-word !important;
            box-sizing: border-box;
            letter-spacing: -0.02em;
        }}
        
        html, body {{
            font-size: 16px !important;
            line-height: 1.6;
        }}

        body {{
            background-color: #f8fafc !important;
            background-image: 
                radial-gradient(at 0% 0%, rgba(219, 234, 254, 0.6) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(237, 233, 254, 0.6) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(254, 243, 199, 0.4) 0px, transparent 50%);
            color: #0f172a;
        }}

        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(241, 245, 249, 0.7);
        }}
        ::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 9999px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #94a3b8;
        }}

        /* Fluid Modern Web Card Container */
        .ms-fluid-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 28px;
            box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.06), 0 4px 12px -2px rgba(15, 23, 42, 0.03);
            transition: all 0.25s ease-in-out;
        }}

        .copilot-gradient-badge {{
            background: linear-gradient(135deg, #0078D4 0%, #7C3AED 50%, #DB2777 100%);
        }}

        .ms-pill-tab {{
            border-radius: 9999px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .ms-pill-tab.active {{
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
        }}

        .ms-pill-tab:not(.active) {{
            background-color: #ffffff;
            color: #334155;
            border: 1px solid #cbd5e1;
        }}
        .ms-pill-tab:not(.active):hover {{
            background-color: #f1f5f9;
            color: #0f172a;
        }}

        blockquote {{
            border-left: 4px solid #6366f1;
            padding-left: 1.25rem;
            margin: 0.75rem 0;
            font-style: italic;
            color: #334155;
            word-break: keep-all !important;
        }}

        #sidebar {{
            transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        #sidebar.collapsed {{
            width: 0px !important;
            transform: translateX(-100%);
            overflow: hidden !important;
            border-right-width: 0px !important;
        }}

        @media print {{
            .no-print {{ display: none !important; }}
            .slide-page {{ page-break-after: always; break-after: page; width: 100% !important; }}
            body {{ background: white !important; }}
        }}
    </style>
</head>
<body class="h-full flex flex-col antialiased">

    <!-- Top Global Microsoft Header -->
    <header class="no-print h-14 bg-white/95 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-4 z-40 shrink-0 shadow-xs">
        <div class="flex items-center space-x-3">
            <!-- Sidebar Toggle Button -->
            <button id="sidebarToggleBtn" onclick="toggleSidebar()" class="w-9 h-9 flex items-center justify-center rounded-xl hover:bg-slate-100 transition-colors text-slate-700 font-bold" title="사이드바 접기/펼치기 (단축키: B)">
                <span id="sidebarToggleIcon" class="text-base">☰</span>
            </button>

            <!-- App Logo with High-Def Copilot Vector -->
            <div class="flex items-center space-x-2.5">
                <span class="w-7 h-7 rounded-lg flex items-center justify-center shadow-xs">
                    {fluent_icons["copilot"]}
                </span>
                <span class="font-black text-sm md:text-base tracking-tight text-slate-900">Microsoft 365 Copilot</span>
                <span class="text-slate-300 text-xs">|</span>
                <span class="text-xs md:text-sm text-slate-600 font-bold hidden sm:inline uppercase tracking-wider">공식 솔루션 시스템 (초고화질 벡터)</span>
            </div>
        </div>

        <!-- Center: Microsoft 365 Category Pill Bar with Lossless Vector Icons -->
        <div class="hidden lg:flex items-center space-x-1.5 overflow-x-auto py-1">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-pill-btn ms-pill-tab px-3.5 py-1 text-xs md:text-sm font-bold flex items-center space-x-2" data-part="{idx}">
                <span class="scale-90">{app_branding.get(p["app"], app_branding["copilot"])["icon_svg"]}</span>
                <span>{p["part_num"]}</span>
            </button>
            ''' for idx, p in enumerate(modules)])}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center space-x-2.5">
            <!-- Font Switcher -->
            <div class="flex items-center bg-slate-100 rounded-full px-2.5 py-1 border border-slate-200 text-xs font-bold text-slate-700 space-x-1.5 shadow-2xs">
                <span>🔤</span>
                <select id="fontSelect" onchange="changeFontFamily(this.value)" class="bg-transparent text-slate-800 font-semibold focus:outline-none cursor-pointer text-xs">
                    <option value="font-pretendard" selected>Pretendard (추천 ⭐)</option>
                    <option value="font-suit">SUIT (테크 감성)</option>
                    <option value="font-noto">Noto Sans KR (본고딕)</option>
                    <option value="font-ibm">IBM Plex Sans (엔지니어링)</option>
                </select>
            </div>

            <!-- Search Trigger -->
            <div class="relative hidden md:block">
                <input type="text" id="searchInput" placeholder="솔루션 / 프롬프트 검색..." class="bg-slate-100/90 border border-slate-200 rounded-full px-3.5 py-1 text-xs md:text-sm text-slate-700 placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:bg-white w-44 transition-all">
            </div>

            <!-- View Switcher -->
            <div class="flex bg-slate-100 p-0.5 rounded-full border border-slate-200 text-xs md:text-sm font-bold">
                <button id="slideModeBtn" onclick="setViewMode('slide')" class="px-3.5 py-1 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1">
                    <span>🖥️</span>
                    <span class="hidden md:inline">단일 뷰</span>
                </button>
                <button id="portalModeBtn" onclick="setViewMode('portal')" class="px-3.5 py-1 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1">
                    <span>📑</span>
                    <span class="hidden md:inline">연속 문서</span>
                </button>
            </div>

            <!-- Fullscreen -->
            <button onclick="toggleFullscreen()" class="w-8 h-8 flex items-center justify-center rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-700 text-xs transition-colors" title="전체화면 (F)">
                ⛶
            </button>
        </div>
    </header>

    <!-- Main Container: Sidebar + Content Area -->
    <div class="flex-1 flex overflow-hidden relative">

        <!-- Left Journey Sidebar (Collapsible) -->
        <aside id="sidebar" class="no-print w-80 bg-white/95 backdrop-blur-md border-r border-slate-200 flex flex-col shrink-0 z-30 shadow-xs">
            <!-- Sidebar Header with Lossless Icon Banner -->
            <div id="sidebarAppBanner" class="p-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-3">
                    <span id="activeAppIcon" class="w-8 h-8 flex items-center justify-center">{fluent_icons["copilot"]}</span>
                    <div>
                        <div id="activeAppName" class="font-black text-sm text-slate-900 leading-tight">Microsoft 365 Copilot</div>
                        <div id="activePartNum" class="text-xs text-indigo-600 font-bold mt-0.5">Part 1. 기초 & 보안</div>
                    </div>
                </div>
                <div class="flex items-center space-x-1.5">
                    <span id="slideCounterBadge" class="text-xs font-mono font-black bg-white px-2.5 py-0.5 rounded-full border border-slate-200 text-slate-700 shadow-2xs">
                        01 / 33
                    </span>
                    <button onclick="toggleSidebar()" class="w-7 h-7 rounded-lg hover:bg-slate-200 text-slate-400 hover:text-slate-700 flex items-center justify-center text-xs font-bold transition-colors" title="사이드바 축소">
                        ◀
                    </button>
                </div>
            </div>

            <!-- Slide List Scroll Area -->
            <div class="flex-1 overflow-y-auto p-2.5 space-y-1.5" id="slideListNav">
                {"".join([f'''
                <div class="slide-nav-item p-3 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3 hover:bg-slate-50 border border-transparent" id="nav-item-{idx}" onclick="goToSlide({idx})">
                    <span class="shrink-0 w-7 h-7 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-black mt-0.5 item-num-badge">{s["num"]}</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-sm font-bold text-slate-800 truncate leading-snug item-title flex items-center space-x-2">
                            <span class="scale-75 shrink-0">{s["app_icon_svg"]}</span>
                            <span class="truncate">{s["title"]}</span>
                        </div>
                        <div class="text-xs text-slate-400 truncate mt-0.5 font-semibold">{s["badge"]}</div>
                    </div>
                </div>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Sidebar Footer -->
            <div class="p-3.5 bg-slate-50 border-t border-slate-200 text-xs md:text-sm text-slate-500 flex items-center justify-between font-medium">
                <span>⌨️ <code>B</code> 사이드바 접기</span>
                <span><code>Space</code> 이동</span>
            </div>
        </aside>

        <!-- Center Workspace: Fluid Web Stage -->
        <main class="flex-1 flex flex-col overflow-hidden relative">

            <!-- App Category Breadcrumb Bar -->
            <div id="appThemeHeader" class="no-print h-11 bg-white/80 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2.5 text-xs md:text-sm font-semibold">
                    <span id="bannerAppBadge" class="px-3 py-0.5 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-xs border border-slate-200 flex items-center space-x-2">
                        <span id="bannerAppIconSvg" class="scale-75">{fluent_icons["copilot"]}</span>
                        <span id="bannerAppText">M365 COPILOT</span>
                    </span>
                    <span class="text-slate-300">/</span>
                    <span id="bannerSlideTitle" class="truncate max-w-2xl text-slate-900 font-extrabold break-keep text-sm">2026 통신 네트워크 패러다임: '작성 도우미'에서 '자율 에이전트'로</span>
                </div>
                <div class="flex items-center space-x-2 text-xs md:text-sm font-bold text-slate-600">
                    <button onclick="prevSlide()" class="px-3.5 py-1 rounded-full hover:bg-slate-100 transition-colors" title="이전 (←)">◀ 이전</button>
                    <button onclick="nextSlide()" class="px-3.5 py-1 rounded-full hover:bg-slate-100 transition-colors" title="다음 (→ / Space)">다음 ▶</button>
                </div>
            </div>

            <!-- Single Card View Container (Fluid Web Layout) -->
            <div id="slideViewStage" class="flex-1 overflow-y-auto p-4 md:p-8 flex items-center justify-center">
                <div id="activeSlideCard" class="w-full max-w-5xl ms-fluid-card p-6 md:p-10 flex flex-col justify-between my-auto min-h-[590px]">
                    <!-- Dynamic Slide Content injected by JS -->
                </div>
            </div>

            <!-- Continuous Document Scroll Portal (All 33 Units) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-6 md:p-12 space-y-12 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-5xl mx-auto ms-fluid-card p-8 md:p-12 slide-page">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider {s["badge_class"]} border flex items-center space-x-2">
                                <span class="scale-90">{s["app_icon_svg"]}</span>
                                <span>{s["app_name"]} • {s["badge"]}</span>
                            </span>
                            <span class="font-mono text-xs md:text-sm font-black text-slate-400">UNIT {s["num"]} / 33</span>
                        </div>
                        <h2 class="text-3xl md:text-4xl font-black text-slate-900 mb-3 leading-tight tracking-tight break-keep">{s["title"]}</h2>
                        <p class="text-base md:text-lg text-slate-600 font-medium mb-8 break-keep">{s["subtitle"]}</p>
                    </div>
                    <div class="my-auto py-2">
                        {s["body"]}
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-sm text-slate-400 text-left font-medium">
                        {s["part_num"]}: {s["part_title"]}
                    </div>
                </article>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Bottom Progress Track -->
            <div class="no-print h-1.5 bg-slate-200/80 shrink-0">
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 3.03%;"></div>
            </div>
        </main>

    </div>

    <!-- Data Injection & Interactive Controller Script -->
    <script>
        const slidesData = {json.dumps(cleaned_slides, ensure_ascii=False)};
        let currentSlideIndex = 0;
        let viewMode = 'slide';
        let sidebarCollapsed = false;

        function changeFontFamily(fontClass) {{
            const root = document.getElementById('htmlRoot');
            root.classList.remove('font-pretendard', 'font-noto', 'font-suit', 'font-ibm');
            root.classList.add(fontClass);
        }}

        function toggleSidebar() {{
            sidebarCollapsed = !sidebarCollapsed;
            const sidebar = document.getElementById('sidebar');
            const toggleIcon = document.getElementById('sidebarToggleIcon');
            
            if (sidebarCollapsed) {{
                sidebar.classList.add('collapsed');
                toggleIcon.textContent = '▶';
            }} else {{
                sidebar.classList.remove('collapsed');
                toggleIcon.textContent = '☰';
            }}
        }}

        function renderSlide(index) {{
            if (index < 0 || index >= slidesData.length) return;
            currentSlideIndex = index;
            const slide = slidesData[index];

            // Render Center Card in Fluid Web Mode with Sharp Vector SVGs
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge -->
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center space-x-2.5">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider ${{slide.badge_class}} border flex items-center space-x-2 shadow-2xs">
                                <span class="scale-90">${{slide.app_icon_svg}}</span>
                                <span>${{slide.app_name}} • ${{slide.badge}}</span>
                            </span>
                        </div>
                        <span class="font-mono text-sm font-black text-slate-400">UNIT ${{slide.num}} / 33</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl lg:text-5xl font-black text-slate-900 mb-3 leading-tight tracking-tight break-keep max-w-4xl mx-auto text-center">${{slide.title}}</h1>
                    <p class="text-base md:text-lg text-slate-600 font-medium mb-6 max-w-3xl mx-auto break-keep text-center">${{slide.subtitle}}</p>
                </div>
                <div class="my-auto py-2">
                    ${{slide.body}}
                </div>
                <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-sm text-slate-500 font-medium">
                    <span class="font-bold text-slate-700 flex items-center space-x-2">
                        <span class="scale-75">${{slide.app_icon_svg}}</span>
                        <span>${{slide.part_num}}: ${{slide.part_title}}</span>
                    </span>
                    <div class="flex items-center space-x-2.5">
                        <button onclick="prevSlide()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-full transition-colors text-sm">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-5 py-2 bg-slate-900 hover:bg-indigo-600 text-white font-bold rounded-full shadow-xs transition-colors text-sm">다음 ▶</button>
                    </div>
                </div>
            `;

            // Update Header Banner
            document.getElementById('bannerAppText').textContent = slide.app_name.toUpperCase();
            document.getElementById('bannerAppIconSvg').innerHTML = slide.app_icon_svg;
            document.getElementById('bannerSlideTitle').textContent = slide.title;

            // Update Sidebar Info
            document.getElementById('activeAppIcon').innerHTML = slide.app_icon_svg;
            document.getElementById('activeAppName').textContent = slide.app_name;
            document.getElementById('activePartNum').textContent = `${{slide.part_num}}. ${{slide.part_title}}`;
            document.getElementById('slideCounterBadge').textContent = `${{slide.num}} / 33`;

            // Highlight Active Sidebar Item & Scroll into view
            document.querySelectorAll('.slide-nav-item').forEach((item, i) => {{
                if (i === index) {{
                    item.className = `slide-nav-item p-3 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3 bg-slate-100 border-slate-300 border shadow-xs`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-7 h-7 rounded-xl bg-slate-900 text-white flex items-center justify-center font-mono text-xs font-black mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-sm font-black text-slate-900 truncate leading-snug item-title flex items-center space-x-2`;
                    item.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }} else {{
                    item.className = `slide-nav-item p-3 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3 hover:bg-slate-50 border border-transparent`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-7 h-7 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-sm font-bold text-slate-700 truncate leading-snug item-title flex items-center space-x-2`;
                }}
            }});

            // Highlight Part Pill Tabs
            document.querySelectorAll('.part-pill-btn').forEach((btn, pIdx) => {{
                if (pIdx === slide.part_idx) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});

            // Update Progress Bar
            const progress = ((index + 1) / slidesData.length) * 100;
            document.getElementById('progressBar').style.width = `${{progress}}%`;

            // Re-render Mermaid diagrams if present
            setTimeout(() => {{
                mermaid.run();
            }}, 50);
        }}

        function nextSlide() {{
            if (currentSlideIndex < slidesData.length - 1) {{
                goToSlide(currentSlideIndex + 1);
            }}
        }}

        function prevSlide() {{
            if (currentSlideIndex > 0) {{
                goToSlide(currentSlideIndex - 1);
            }}
        }}

        function goToSlide(index) {{
            if (viewMode === 'portal') {{
                const target = document.getElementById(`portal-slide-${{index}}`);
                if (target) target.scrollIntoView({{ behavior: 'smooth' }});
                currentSlideIndex = index;
            }} else {{
                renderSlide(index);
            }}
        }}

        function goToPart(partIdx) {{
            const firstSlideOfPart = slidesData.findIndex(s => s.part_idx === partIdx);
            if (firstSlideOfPart !== -1) {{
                goToSlide(firstSlideOfPart);
            }}
        }}

        function setViewMode(mode) {{
            viewMode = mode;
            if (mode === 'slide') {{
                document.getElementById('slideViewStage').classList.remove('hidden');
                document.getElementById('portalViewStage').classList.add('hidden');
                document.getElementById('slideModeBtn').className = 'px-3.5 py-1 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1 font-bold';
                document.getElementById('portalModeBtn').className = 'px-3.5 py-1 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1 font-bold';
                renderSlide(currentSlideIndex);
            }} else {{
                document.getElementById('slideViewStage').classList.add('hidden');
                document.getElementById('portalViewStage').classList.remove('hidden');
                document.getElementById('slideModeBtn').className = 'px-3.5 py-1 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1 font-bold';
                document.getElementById('portalModeBtn').className = 'px-3.5 py-1 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1 font-bold';
                const target = document.getElementById(`portal-slide-${{currentSlideIndex}}`);
                if (target) target.scrollIntoView({{ behavior: 'smooth' }});
            }}
        }}

        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen();
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }}
            }}
        }}

        // Keyboard Shortcut Navigation
        document.addEventListener('keydown', (e) => {{
            if (e.target.tagName === 'INPUT') return;
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
                e.preventDefault();
                nextSlide();
            }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                e.preventDefault();
                prevSlide();
            }} else if (e.key === 'b' || e.key === 'B') {{
                toggleSidebar();
            }} else if (e.key === 'p' || e.key === 'P') {{
                setViewMode(viewMode === 'slide' ? 'portal' : 'slide');
            }} else if (e.key === 'f' || e.key === 'F') {{
                toggleFullscreen();
            }}
        }});

        // Search Filter
        document.getElementById('searchInput').addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase();
            document.querySelectorAll('.slide-nav-item').forEach((item, idx) => {{
                const s = slidesData[idx];
                const text = (s.title + ' ' + s.subtitle + ' ' + s.badge + ' ' + s.app_name).toLowerCase();
                if (text.includes(query)) {{
                    item.style.display = 'flex';
                }} else {{
                    item.style.display = 'none';
                }}
            }});
        }});

        // Initialize on Slide 0
        window.addEventListener('DOMContentLoaded', () => {{
            renderSlide(0);
        }});
    </script>
</body>
</html>
"""

output_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/M365_Copilot_Telecom_Master.html"
index_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/index.html"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(portal_template)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(portal_template)

print(f"Successfully replaced raster images with crisp ultra-HD Fluent vector SVGs at {output_path} and {index_path}")
