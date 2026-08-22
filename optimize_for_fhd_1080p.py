import json
import re

# Load the current master python file
with open("restore_and_integrate_all_content.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

# Optimize Unit 08 Architecture for 1920x1080 Wide Layout
slide_08_fhd = f"""
<div class="p-6 lg:p-8 bg-white/95 rounded-3xl border border-slate-200 shadow-sm w-full max-w-6xl mx-auto text-left my-auto">
    <div class="grid grid-cols-12 gap-6 lg:gap-8 items-center">
        
        <!-- Left Column: Users & Apps -->
        <div class="col-span-12 lg:col-span-4 space-y-4">
            <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200 shadow-xs">
                <div class="text-sm font-black text-slate-700 uppercase tracking-wider mb-2.5">Your Users and Devices</div>
                <div class="flex items-center space-x-3.5 p-3.5 bg-white rounded-xl shadow-2xs border border-slate-200">
                    <span class="w-11 h-11 rounded-xl bg-gradient-to-tr from-purple-500 to-pink-500 text-white flex items-center justify-center text-xl shadow-xs">👤</span>
                    <span class="w-11 h-11 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white flex items-center justify-center text-xl shadow-xs">💻</span>
                    <div>
                        <div class="text-base font-black text-slate-900 leading-tight">사내 인증 엔지니어</div>
                        <div class="text-xs text-slate-500 font-semibold mt-0.5">Entra ID SSO 로그인</div>
                    </div>
                </div>
            </div>

            <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200 shadow-xs">
                <div class="text-sm font-black text-slate-700 uppercase tracking-wider mb-2.5">Apps on Your Devices</div>
                <div class="grid grid-cols-3 gap-2.5 p-2 bg-white rounded-xl shadow-2xs border border-slate-200 text-center">
                    <div class="p-2.5 bg-sky-50 rounded-xl font-bold text-sky-950 text-sm border border-sky-100 flex flex-col items-center"><span class="text-xl mb-1">📄</span> Word</div>
                    <div class="p-2.5 bg-emerald-50 rounded-xl font-bold text-emerald-950 text-sm border border-emerald-100 flex flex-col items-center"><span class="text-xl mb-1">📊</span> Excel</div>
                    <div class="p-2.5 bg-orange-50 rounded-xl font-bold text-orange-950 text-sm border border-orange-100 flex flex-col items-center"><span class="text-xl mb-1">📑</span> PPT</div>
                    <div class="p-2.5 bg-blue-50 rounded-xl font-bold text-blue-950 text-sm border border-blue-100 flex flex-col items-center"><span class="text-xl mb-1">✉️</span> Outlook</div>
                    <div class="p-2.5 bg-indigo-50 rounded-xl font-bold text-indigo-950 text-sm border border-indigo-100 flex flex-col items-center"><span class="text-xl mb-1">💬</span> Teams</div>
                    <div class="p-2.5 bg-cyan-50 rounded-xl font-bold text-cyan-950 text-sm border border-cyan-100 flex flex-col items-center"><span class="text-xl mb-1">☁️</span> OneDrive</div>
                </div>
            </div>
        </div>

        <!-- Right Column: Encrypted Tenant Boundary -->
        <div class="col-span-12 lg:col-span-8 p-6 lg:p-7 bg-gradient-to-br from-slate-50 via-indigo-50/40 to-pink-50/40 rounded-3xl border-2 border-indigo-200 shadow-md">
            <div class="space-y-4">
                <div class="p-5 lg:p-6 bg-white rounded-2xl border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center mb-3">
                        <h3 class="text-lg lg:text-xl font-black text-slate-900">Your Microsoft 365 Tenant</h3>
                        <span class="px-3.5 py-1 bg-indigo-100 text-indigo-900 text-sm font-bold rounded-full border border-indigo-200">Encrypted Tenant Boundary</span>
                    </div>
                    
                    <div class="p-3.5 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-xl text-center font-black text-base lg:text-lg text-indigo-950 mb-3.5 shadow-2xs">
                        Microsoft Graph (Work IQ Engine + Entra ID ACL Real-Time Indexing)
                    </div>

                    <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                        <div class="text-sm font-bold text-slate-800 mb-2">Customer Data Boundary (외부 유출 원천 차단)</div>
                        <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-center text-sm font-bold text-slate-800">
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">✉️ Exchange Mail</div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">☁️ SharePoint KB</div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">💬 Teams Chat</div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">🛡️ Purview Label</div>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div class="p-4 lg:p-5 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-500 text-white rounded-2xl shadow-md flex items-center space-x-3.5">
                        <span class="text-3xl">✨</span>
                        <div>
                            <div class="text-xs font-extrabold uppercase opacity-90">Microsoft</div>
                            <div class="text-lg lg:text-xl font-black tracking-wide">365 Copilot Core</div>
                        </div>
                    </div>
                    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-sm text-center flex flex-col justify-center">
                        <div class="font-black text-slate-900 text-base lg:text-lg leading-tight">Azure OpenAI Private Service</div>
                        <div class="text-sm font-bold text-indigo-700 mt-1">GPT-5.6 / Claude Sonnet 5 (Zero Data Retention)</div>
                    </div>
                </div>
            </div>

            <div class="mt-4 text-center">
                <span class="inline-block px-6 py-2 bg-white text-slate-900 font-extrabold text-sm lg:text-base rounded-full shadow-sm border border-indigo-200">
                    🛡️ 고객 데이터는 절대 AI 모델 재학습에 사용되지 않으며, 테넌트 내에서 완벽히 격리됩니다.
                </span>
            </div>
        </div>

    </div>
</div>
"""

# Update Unit 08 in master chapters
for chap in master_chapters:
    for u in chap["units"]:
        if "보안을 포기하지 않고 최고의 AI를 사용한다" in u["title"]:
            u["body"] = slide_08_fhd

cleaned_slides = []
total_units = sum(len(c["units"]) for c in master_chapters)
curr_unit_idx = 0

for chap_idx, chap in enumerate(master_chapters):
    full_chap_title = f"{chap['chapter_num']}. {chap['title']}"
    for u_idx, u in enumerate(chap["units"]):
        cleaned_slides.append({
            "part_idx": chap_idx,
            "part_num": chap["chapter_num"],
            "part_title": chap["title"],
            "full_chapter_name": full_chap_title,
            "app_name": chap["app_name"],
            "app_icon_svg": chap["icon_svg"],
            "badge_class": chap["badge_class"],
            "tools": chap["tools"],
            "num": f"{curr_unit_idx + 1:02d}",
            "badge": u["badge"],
            "title": u["title"],
            "subtitle": u["subtitle"],
            "body": u["body"]
        })
        curr_unit_idx += 1

# FHD (1920 x 1080) Specialized Master HTML Template
fhd_portal_html = f"""<!DOCTYPE html>
<html lang="ko" class="h-full font-pretendard" id="htmlRoot">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microsoft 365 Copilot 표준 교육과정 - Full HD 마스터 포털</title>
    <!-- Tailwind CSS Play CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    screens: {{
                        'fhd': '1800px',
                    }},
                    fontSize: {{
                        'xs': ['0.875rem', {{ lineHeight: '1.25rem' }}],
                        'sm': ['0.975rem', {{ lineHeight: '1.45rem' }}],
                        'base': ['1.125rem', {{ lineHeight: '1.75rem' }}],
                        'lg': ['1.25rem', {{ lineHeight: '1.85rem' }}],
                        'xl': ['1.45rem', {{ lineHeight: '2.0rem' }}],
                        '2xl': ['1.75rem', {{ lineHeight: '2.3rem' }}],
                        '3xl': ['2.25rem', {{ lineHeight: '2.7rem' }}],
                        '4xl': ['2.85rem', {{ lineHeight: '3.2rem' }}],
                    }},
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
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap">
    <!-- Mermaid.js for live diagrams -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    <style>
        * {{
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            user-select: text !important;
            -webkit-user-select: text !important;
            word-break: keep-all !important;
            overflow-wrap: break-word !important;
            box-sizing: border-box;
            letter-spacing: -0.02em;
        }}

        .font-mono, code, pre {{ font-family: 'JetBrains Mono', Consolas, monospace !important; }}
        
        html, body {{
            font-size: 17.5px !important;
            line-height: 1.65;
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
            width: 8px;
            height: 8px;
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

        /* Fluid Modern Web Card Container Optimized for FHD 1920x1080 */
        .fhd-card-stage {{
            width: 100%;
            max-width: 1400px;
            min-height: 640px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 32px;
            box-shadow: 0 16px 40px -8px rgba(15, 23, 42, 0.08), 0 6px 20px -3px rgba(15, 23, 42, 0.04);
            transition: all 0.25s ease-in-out;
        }}

        .ms-pill-tab {{
            border-radius: 9999px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .ms-pill-tab.active {{
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 800;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.18);
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
            border-left: 5px solid #6366f1;
            padding: 1.15rem 1.75rem;
            background: #f8fafc;
            border-radius: 0 20px 20px 0;
            margin: 1.15rem 0;
            font-style: normal;
            color: #0f172a;
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

    <!-- Top Global Microsoft Header (FHD 1920 Balanced) -->
    <header class="no-print h-16 bg-white/95 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-6 z-40 shrink-0 shadow-xs whitespace-nowrap select-none">
        <div class="flex items-center space-x-4">
            <!-- Sidebar Toggle Button -->
            <button id="sidebarToggleBtn" onclick="toggleSidebar()" class="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-slate-100 transition-colors text-slate-700 font-bold text-xl" title="사이드바 접기/펼치기 (단축키: B)">
                <span id="sidebarToggleIcon">☰</span>
            </button>

            <!-- App Logo with Copilot Vector -->
            <div class="flex items-center space-x-3">
                <span class="w-9 h-9 rounded-xl flex items-center justify-center shadow-xs">
                    {fluent_icons["copilot"]}
                </span>
                <span class="font-black text-base lg:text-lg tracking-tight text-slate-900">Microsoft 365 Copilot</span>
            </div>
        </div>

        <!-- Center: 4 Official Chapters Pill Bar -->
        <div class="hidden lg:flex items-center space-x-3 overflow-x-auto py-1">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-pill-btn ms-pill-tab px-4 py-2 text-sm lg:text-base font-bold flex items-center space-x-2.5" data-part="{idx}" title="{c['chapter_num']}. {c['title']}">
                <span class="scale-90">{c["icon_svg"]}</span>
                <span>{c["short_title"]}</span>
            </button>
            ''' for idx, c in enumerate(master_chapters)])}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center space-x-3">
            <!-- View Switcher -->
            <div class="flex bg-slate-100 p-1 rounded-full border border-slate-200 text-sm font-bold">
                <button id="slideModeBtn" onclick="setViewMode('slide')" class="px-4 py-1.5 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1.5">
                    <span>🖥️</span>
                    <span class="hidden md:inline">단일 뷰</span>
                </button>
                <button id="portalModeBtn" onclick="setViewMode('portal')" class="px-4 py-1.5 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1.5">
                    <span>📑</span>
                    <span class="hidden md:inline">연속 문서</span>
                </button>
            </div>

            <!-- Fullscreen -->
            <button onclick="toggleFullscreen()" class="w-10 h-10 flex items-center justify-center rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-700 text-base font-bold transition-colors" title="전체화면 (F)">
                ⛶
            </button>
        </div>
    </header>

    <!-- Main Container: Sidebar + FHD Content Stage -->
    <div class="flex-1 flex overflow-hidden relative">

        <!-- Left Journey Sidebar (Collapsible, FHD 360px optimized) -->
        <aside id="sidebar" class="no-print w-92 bg-white/95 backdrop-blur-md border-r border-slate-200 flex flex-col shrink-0 z-30 shadow-xs">
            <!-- Sidebar Header with Official Chapter Name -->
            <div id="sidebarAppBanner" class="p-5 bg-slate-50 border-b border-slate-200 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-3.5">
                    <span id="activeAppIcon" class="w-10 h-10 flex items-center justify-center">{fluent_icons["copilot"]}</span>
                    <div class="min-w-0 flex-1">
                        <div id="activeAppName" class="font-black text-base lg:text-lg text-slate-900 leading-tight truncate">Work IQ & Copilot Core</div>
                        <div id="activePartNum" class="text-xs lg:text-sm text-indigo-700 font-bold mt-1 break-keep">01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI</div>
                    </div>
                </div>
                <div class="flex items-center space-x-2 shrink-0 ml-2">
                    <span id="slideCounterBadge" class="text-xs lg:text-sm font-mono font-black bg-white px-3 py-1 rounded-full border border-slate-200 text-slate-700 shadow-2xs">
                        01 / {total_units:02d}
                    </span>
                    <button onclick="toggleSidebar()" class="w-8 h-8 rounded-lg hover:bg-slate-200 text-slate-400 hover:text-slate-700 flex items-center justify-center text-sm font-bold transition-colors" title="사이드바 축소">
                        ◀
                    </button>
                </div>
            </div>

            <!-- Slide List Scroll Area (31 Full Units) -->
            <div class="flex-1 overflow-y-auto p-3.5 space-y-2" id="slideListNav">
                {"".join([f'''
                <div class="slide-nav-item p-4 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3.5 hover:bg-slate-50 border border-transparent" id="nav-item-{idx}" onclick="goToSlide({idx})">
                    <span class="shrink-0 w-8 h-8 rounded-xl bg-slate-100 text-slate-700 flex items-center justify-center font-mono text-sm font-black mt-0.5 item-num-badge">{s["num"]}</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-base font-bold text-slate-800 truncate leading-snug item-title flex items-center space-x-2">
                            <span class="scale-90 shrink-0">{s["app_icon_svg"]}</span>
                            <span class="truncate">{s["title"]}</span>
                        </div>
                        <div class="text-xs text-slate-500 truncate mt-1 font-semibold">{s["badge"]}</div>
                    </div>
                </div>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Sidebar Footer -->
            <div class="p-4 bg-slate-50 border-t border-slate-200 text-sm text-slate-600 flex items-center justify-between font-medium">
                <span>⌨️ <code>B</code> 사이드바 접기</span>
                <span><code>Space</code> 이동</span>
            </div>
        </aside>

        <!-- Center Workspace: Wide 1920x1080 Stage -->
        <main class="flex-1 flex flex-col overflow-hidden relative">

            <!-- App Category Breadcrumb Bar -->
            <div id="appThemeHeader" class="no-print h-12 bg-white/80 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-8 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-3.5 text-sm lg:text-base font-semibold truncate">
                    <span id="bannerAppBadge" class="px-4 py-1 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-xs lg:text-sm border border-slate-200 flex items-center space-x-2 shrink-0">
                        <span id="bannerAppIconSvg" class="scale-90">{fluent_icons["copilot"]}</span>
                        <span id="bannerAppText">01. M365 COPILOT의 변화</span>
                    </span>
                    <span class="text-slate-300">/</span>
                    <span id="bannerSlideTitle" class="truncate max-w-3xl text-slate-900 font-extrabold break-keep text-base">웹 기반 범용 AI vs M365 Copilot: 기업 업무에 최적화된 차이점</span>
                </div>
                <div class="flex items-center space-x-3 text-sm font-bold text-slate-700 shrink-0 ml-4">
                    <button onclick="prevSlide()" class="px-4 py-1.5 rounded-full hover:bg-slate-100 transition-colors" title="이전 (←)">◀ 이전</button>
                    <button onclick="nextSlide()" class="px-4 py-1.5 rounded-full hover:bg-slate-100 transition-colors" title="다음 (→ / Space)">다음 ▶</button>
                </div>
            </div>

            <!-- Single Card View Container (FHD 1920x1080 Viewport-Fit) -->
            <div id="slideViewStage" class="flex-1 overflow-y-auto p-6 lg:p-10 flex items-center justify-center">
                <div id="activeSlideCard" class="fhd-card-stage p-8 lg:p-12 flex flex-col justify-between my-auto">
                    <!-- Dynamic Slide Content injected by JS -->
                </div>
            </div>

            <!-- Continuous Document Scroll Portal (All Units) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-8 lg:p-14 space-y-14 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-6xl mx-auto fhd-card-stage p-10 lg:p-14 slide-page">
                    <div>
                        <div class="flex items-center justify-between mb-5">
                            <span class="px-4 py-1.5 rounded-full text-sm font-black uppercase tracking-wider {s["badge_class"]} border flex items-center space-x-2.5">
                                <span class="scale-90">{s["app_icon_svg"]}</span>
                                <span>{s["full_chapter_name"]} • {s["badge"]}</span>
                            </span>
                            <span class="font-mono text-sm lg:text-base font-black text-slate-400">UNIT {s["num"]} / {total_units:02d}</span>
                        </div>
                        <h2 class="text-3xl lg:text-4xl font-black text-slate-900 mb-3.5 leading-tight tracking-tight break-keep">{s["title"]}</h2>
                        <p class="text-lg lg:text-xl text-slate-600 font-medium mb-8 break-keep">{s["subtitle"]}</p>
                    </div>
                    <div class="my-auto py-2 text-base lg:text-lg">
                        {s["body"]}
                    </div>
                    <div class="mt-8 pt-5 border-t border-slate-100 text-base text-slate-600 font-bold text-left">
                        {s["full_chapter_name"]}
                    </div>
                </article>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Bottom Progress Track -->
            <div class="no-print h-2 bg-slate-200/80 shrink-0">
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 3.22%;"></div>
            </div>
        </main>

    </div>

    <!-- Data Injection & Interactive Controller Script -->
    <script>
        const slidesData = {json.dumps(cleaned_slides, ensure_ascii=False)};
        let currentSlideIndex = 0;
        let viewMode = 'slide';
        let sidebarCollapsed = false;

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

            // Render Center Card in FHD Mode
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge -->
                    <div class="flex items-center justify-between mb-5">
                        <div class="flex items-center space-x-3">
                            <span class="px-4 py-1.5 rounded-full text-xs lg:text-sm font-black uppercase tracking-wider ${{slide.badge_class}} border flex items-center space-x-2.5 shadow-2xs">
                                <span class="scale-90">${{slide.app_icon_svg}}</span>
                                <span>${{slide.full_chapter_name}} • ${{slide.badge}}</span>
                            </span>
                        </div>
                        <span class="font-mono text-sm lg:text-base font-black text-slate-400">UNIT ${{slide.num}} / {total_units:02d}</span>
                    </div>
                    <h1 class="text-3xl lg:text-4xl xl:text-5xl font-black text-slate-900 mb-3 leading-tight tracking-tight break-keep max-w-5xl mx-auto text-center">${{slide.title}}</h1>
                    <p class="text-lg lg:text-xl text-slate-600 font-medium mb-6 max-w-4xl mx-auto break-keep text-center leading-relaxed">${{slide.subtitle}}</p>
                </div>
                <div class="my-auto py-3 text-base lg:text-lg">
                    ${{slide.body}}
                </div>
                <div class="mt-8 pt-5 border-t border-slate-100 flex items-center justify-between text-base text-slate-600 font-medium">
                    <span class="font-bold text-slate-800 flex items-center space-x-2.5">
                        <span class="scale-90">${{slide.app_icon_svg}}</span>
                        <span>${{slide.full_chapter_name}}</span>
                    </span>
                    <div class="flex items-center space-x-3">
                        <button onclick="prevSlide()" class="px-5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-full transition-colors text-base">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-6 py-2 bg-slate-900 hover:bg-indigo-600 text-white font-bold rounded-full shadow-xs transition-colors text-base">다음 ▶</button>
                    </div>
                </div>
            `;

            // Update Header Banner
            document.getElementById('bannerAppText').textContent = slide.full_chapter_name.toUpperCase();
            document.getElementById('bannerAppIconSvg').innerHTML = slide.app_icon_svg;
            document.getElementById('bannerSlideTitle').textContent = slide.title;

            // Update Sidebar Info with Official Chapter Name
            document.getElementById('activeAppIcon').innerHTML = slide.app_icon_svg;
            document.getElementById('activeAppName').textContent = slide.app_name;
            document.getElementById('activePartNum').textContent = slide.full_chapter_name;
            document.getElementById('slideCounterBadge').textContent = `${{slide.num}} / {total_units:02d}`;

            // Highlight Active Sidebar Item & Scroll into view
            document.querySelectorAll('.slide-nav-item').forEach((item, i) => {{
                if (i === index) {{
                    item.className = `slide-nav-item p-4 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3.5 bg-slate-100 border-slate-300 border shadow-xs`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-8 h-8 rounded-xl bg-slate-900 text-white flex items-center justify-center font-mono text-sm font-black mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-base font-black text-slate-900 truncate leading-snug item-title flex items-center space-x-2`;
                    item.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }} else {{
                    item.className = `slide-nav-item p-4 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3.5 hover:bg-slate-50 border border-transparent`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-8 h-8 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-sm font-bold mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-base font-bold text-slate-700 truncate leading-snug item-title flex items-center space-x-2`;
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
                document.getElementById('slideModeBtn').className = 'px-4 py-1.5 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1.5 font-bold';
                document.getElementById('portalModeBtn').className = 'px-4 py-1.5 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1.5 font-bold';
                renderSlide(currentSlideIndex);
            }} else {{
                document.getElementById('slideViewStage').classList.add('hidden');
                document.getElementById('portalViewStage').classList.remove('hidden');
                document.getElementById('slideModeBtn').className = 'px-4 py-1.5 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1.5 font-bold';
                document.getElementById('portalModeBtn').className = 'px-4 py-1.5 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1.5 font-bold';
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

        // Initialize on Slide 0
        window.addEventListener('DOMContentLoaded', () => {{
            renderSlide(0);
        }});
    </script>
</body>
</html>
"""

output_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/AX_CA_Edu_GHLEE.html"
index_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/index.html"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(fhd_portal_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(fhd_portal_html)

print("Successfully optimized portal for Full HD (1920x1080) resolution!")
