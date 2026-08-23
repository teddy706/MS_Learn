import json
import re

with open("adjust_sidebar_to_25_percent.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

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
                    fontSize: {{
                        '2xs': ['0.75rem', {{ lineHeight: '1.05rem' }}],
                        'xs': ['0.8125rem', {{ lineHeight: '1.15rem' }}],
                        'sm': ['0.875rem', {{ lineHeight: '1.25rem' }}],
                        'base': ['1.0625rem', {{ lineHeight: '1.65rem' }}],
                        'lg': ['1.1875rem', {{ lineHeight: '1.75rem' }}],
                        'xl': ['1.375rem', {{ lineHeight: '1.9rem' }}],
                        '2xl': ['1.65rem', {{ lineHeight: '2.2rem' }}],
                        '3xl': ['2.1rem', {{ lineHeight: '2.5rem' }}],
                        '4xl': ['2.65rem', {{ lineHeight: '3.0rem' }}],
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
            width: 7px;
            height: 7px;
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

        /* Modern Web Card Stage (FHD 75% Proportioned) */
        .fhd-card-stage {{
            width: 100%;
            max-width: 1280px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 30px;
            box-shadow: 0 16px 40px -8px rgba(15, 23, 42, 0.08), 0 4px 16px -2px rgba(15, 23, 42, 0.03);
            transition: all 0.25s ease-in-out;
        }}

        .ms-pill-tab {{
            border-radius: 9999px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .ms-pill-tab.active {{
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 700;
            box-shadow: 0 3px 10px rgba(15, 23, 42, 0.15);
        }}

        .ms-pill-tab:not(.active) {{
            background-color: #ffffff;
            color: #475569;
            border: 1px solid #cbd5e1;
        }}
        .ms-pill-tab:not(.active):hover {{
            background-color: #f1f5f9;
            color: #0f172a;
        }}

        blockquote {{
            border-left: 4px solid #6366f1;
            padding: 1rem 1.4rem;
            background: #f8fafc;
            border-radius: 0 16px 16px 0;
            margin: 1rem 0;
            font-style: normal;
            color: #0f172a;
            word-break: keep-all !important;
        }}

        #sidebar {{
            transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s ease-in-out;
        }}
        #sidebar.collapsed {{
            width: 0px !important;
            min-width: 0px !important;
            max-width: 0px !important;
            transform: translateX(-100%);
            opacity: 0;
            overflow: hidden !important;
            border-right-width: 0px !important;
            padding: 0 !important;
            margin: 0 !important;
        }}

        @media (max-width: 1024px) {{
            #sidebar {{
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                z-index: 50;
                width: 320px !important;
                max-width: 85vw !important;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            }}
        }}

        @media print {{
            .no-print {{ display: none !important; }}
            .slide-page {{ page-break-after: always; break-after: page; width: 100% !important; }}
            body {{ background: white !important; }}
        }}
    </style>
</head>
<body class="h-full flex flex-col antialiased">

    <!-- Top Global Header (Refined Compact Text) -->
    <header class="no-print h-14 bg-white/95 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-5 z-40 shrink-0 shadow-xs whitespace-nowrap select-none">
        <div class="flex items-center space-x-3.5">
            <!-- Sidebar Toggle Button -->
            <button id="sidebarToggleBtn" onclick="toggleSidebar()" class="w-9 h-9 flex items-center justify-center rounded-xl hover:bg-slate-100 transition-colors text-slate-700 font-bold text-base" title="사이드바 접기/펼치기 (단축키: B)">
                <span id="sidebarToggleIcon">☰</span>
            </button>

            <!-- App Logo with Copilot Vector -->
            <div class="flex items-center space-x-2.5">
                <span class="w-7 h-7 rounded-lg flex items-center justify-center shadow-xs">
                    {fluent_icons["copilot"]}
                </span>
                <span class="font-black text-sm md:text-base tracking-tight text-slate-900">Microsoft 365 Copilot</span>
            </div>
        </div>

        <!-- Center: 4 Official Chapters Pill Bar (Compact, Refined Font) -->
        <div class="hidden lg:flex items-center space-x-2 overflow-x-auto py-1">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-pill-btn ms-pill-tab px-3.5 py-1.5 text-xs md:text-sm font-semibold flex items-center space-x-2" data-part="{idx}" title="{c['chapter_num']}. {c['title']}">
                <span class="scale-75">{c["icon_svg"]}</span>
                <span>{c["short_title"]}</span>
            </button>
            ''' for idx, c in enumerate(master_chapters)])}
        </div>

        <!-- Right Controls (Compact) -->
        <div class="flex items-center space-x-2.5">
            <!-- View Switcher -->
            <div class="flex bg-slate-100 p-0.5 rounded-full border border-slate-200 text-xs font-bold">
                <button id="slideModeBtn" onclick="setViewMode('slide')" class="px-3 py-1 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1">
                    <span>🖥️</span>
                    <span class="hidden md:inline">단일 뷰</span>
                </button>
                <button id="portalModeBtn" onclick="setViewMode('portal')" class="px-3 py-1 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1">
                    <span>📑</span>
                    <span class="hidden md:inline">연속 문서</span>
                </button>
            </div>

            <!-- Fullscreen -->
            <button onclick="toggleFullscreen()" class="w-8 h-8 flex items-center justify-center rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-700 text-xs font-bold transition-colors" title="전체화면 (F)">
                ⛶
            </button>
        </div>
    </header>

    <!-- Main Container: 25% Sidebar + 75% Content Stage -->
    <div class="flex-1 flex overflow-hidden relative">

        <!-- Left Journey Sidebar (25% on desktop, auto collapses on resize) -->
        <aside id="sidebar" class="no-print w-full lg:w-[25%] xl:w-[25%] max-w-[480px] min-w-[280px] bg-white/95 backdrop-blur-md border-r border-slate-200 flex flex-col shrink-0 z-30 shadow-xs">
            <!-- Sidebar Header with Official Chapter Name -->
            <div id="sidebarAppBanner" class="p-3.5 md:p-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-2.5 min-w-0">
                    <span id="activeAppIcon" class="w-7 h-7 flex items-center justify-center shrink-0">{fluent_icons["copilot"]}</span>
                    <div class="min-w-0 flex-1">
                        <div id="activeAppName" class="font-black text-xs md:text-sm text-slate-900 leading-tight truncate">Work IQ & Copilot Core</div>
                        <div id="activePartNum" class="text-2xs md:text-xs text-indigo-700 font-bold mt-0.5 break-keep truncate">01. M365 Copilot의 변화</div>
                    </div>
                </div>
                <div class="flex items-center space-x-1.5 shrink-0 ml-2">
                    <span id="slideCounterBadge" class="text-2xs md:text-xs font-mono font-bold bg-white px-2 py-0.5 rounded-full border border-slate-200 text-slate-700 shadow-2xs">
                        01 / {total_units:02d}
                    </span>
                    <button onclick="toggleSidebar()" class="w-6 h-6 rounded-lg hover:bg-slate-200 text-slate-400 hover:text-slate-700 flex items-center justify-center text-xs font-bold transition-colors" title="사이드바 축소">
                        ◀
                    </button>
                </div>
            </div>

            <!-- Slide List Scroll Area -->
            <div class="flex-1 overflow-y-auto p-2.5 space-y-1.5" id="slideListNav">
                {"".join([f'''
                <div class="slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 hover:bg-slate-50 border border-transparent" id="nav-item-{idx}" onclick="goToSlide({idx})">
                    <span class="shrink-0 w-6 h-6 rounded-lg bg-slate-100 text-slate-700 flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge">{s["num"]}</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-xs md:text-sm font-semibold text-slate-800 break-keep leading-snug item-title flex items-start space-x-1.5">
                            <span class="scale-75 shrink-0 mt-0.5">{s["app_icon_svg"]}</span>
                            <span class="truncate">{s["title"]}</span>
                        </div>
                        <div class="text-2xs text-slate-400 mt-0.5 font-medium truncate">{s["badge"]} • {s["subtitle"]}</div>
                    </div>
                </div>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Sidebar Footer -->
            <div class="p-3 bg-slate-50 border-t border-slate-200 text-2xs md:text-xs text-slate-500 flex items-center justify-between font-medium">
                <span>⌨️ <code>B</code> 접기</span>
                <span><code>Space</code> 이동</span>
            </div>
        </aside>

        <!-- Center Workspace: 75% Main Stage (3/4 of the Screen) -->
        <main class="flex-1 flex flex-col overflow-hidden relative">

            <!-- App Category Breadcrumb Bar (Refined Font) -->
            <div id="appThemeHeader" class="no-print h-11 bg-white/80 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2.5 text-xs md:text-sm font-semibold truncate">
                    <span id="bannerAppBadge" class="px-3 py-0.5 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-xs border border-slate-200 flex items-center space-x-2 shrink-0">
                        <span id="bannerAppIconSvg" class="scale-75">{fluent_icons["copilot"]}</span>
                        <span id="bannerAppText">01. M365 COPILOT의 변화</span>
                    </span>
                    <span class="text-slate-300">/</span>
                    <span id="bannerSlideTitle" class="truncate max-w-2xl text-slate-900 font-bold break-keep text-xs md:text-sm">웹 기반 범용 AI vs M365 Copilot: 기업 업무에 최적화된 차이점</span>
                </div>
                <div class="flex items-center space-x-2 text-xs md:text-sm font-bold text-slate-600 shrink-0 ml-4">
                    <button onclick="prevSlide()" class="px-3 py-1 rounded-full hover:bg-slate-100 transition-colors" title="이전 (←)">◀ 이전</button>
                    <button onclick="nextSlide()" class="px-3 py-1 rounded-full hover:bg-slate-100 transition-colors" title="다음 (→ / Space)">다음 ▶</button>
                </div>
            </div>

            <!-- Single Card View Container (75% Wide Stage) -->
            <div id="slideViewStage" class="flex-1 overflow-y-auto p-4 md:p-6 lg:p-8 flex items-center justify-center">
                <div id="activeSlideCard" class="fhd-card-stage p-6 md:p-8 lg:p-10 flex flex-col justify-between my-auto min-h-[580px]">
                    <!-- Dynamic Slide Content injected by JS -->
                </div>
            </div>

            <!-- Continuous Document Scroll Portal (All Units) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-6 md:p-10 space-y-10 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-5xl mx-auto fhd-card-stage p-8 md:p-12 slide-page">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider {s["badge_class"]} border flex items-center space-x-2">
                                <span class="scale-75">{s["app_icon_svg"]}</span>
                                <span>{s["full_chapter_name"]} • {s["badge"]}</span>
                            </span>
                            <span class="font-mono text-xs md:text-sm font-black text-slate-400">UNIT {s["num"]} / {total_units:02d}</span>
                        </div>
                        <h2 class="text-2xl md:text-3xl font-black text-slate-900 mb-2.5 leading-tight tracking-tight break-keep">{s["title"]}</h2>
                        <p class="text-base md:text-lg text-slate-600 font-medium mb-6 break-keep">{s["subtitle"]}</p>
                    </div>
                    <div class="my-auto py-2 text-base">
                        {s["body"]}
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-sm text-slate-600 font-bold text-left">
                        {s["full_chapter_name"]}
                    </div>
                </article>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Bottom Progress Track -->
            <div class="no-print h-1.5 bg-slate-200/80 shrink-0">
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 3.22%;"></div>
            </div>
        </main>

    </div>

    <!-- Data Injection & Interactive Controller Script with Smart Responsive Sidebar -->
    <script>
        const slidesData = {json.dumps(cleaned_slides, ensure_ascii=False)};
        let currentSlideIndex = 0;
        let viewMode = 'slide';
        let sidebarCollapsed = window.innerWidth < 1100; // Auto-collapse if initial window is narrower than 1100px
        let userExplicitlyToggled = false;

        function setSidebarState(collapsed) {{
            sidebarCollapsed = collapsed;
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

        function toggleSidebar() {{
            userExplicitlyToggled = true;
            setSidebarState(!sidebarCollapsed);
        }}

        // Smart Resize Observer: Auto-collapse sidebar when browser width is reduced
        let prevWindowWidth = window.innerWidth;
        window.addEventListener('resize', () => {{
            const currentWidth = window.innerWidth;
            if (currentWidth < 1100 && !sidebarCollapsed) {{
                setSidebarState(true);
            }} else if (currentWidth >= 1200 && sidebarCollapsed && !userExplicitlyToggled) {{
                setSidebarState(false);
            }}
            prevWindowWidth = currentWidth;
        }});

        function renderSlide(index) {{
            if (index < 0 || index >= slidesData.length) return;
            currentSlideIndex = index;
            const slide = slidesData[index];

            // Render Center Card in FHD Mode
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge -->
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center space-x-2.5">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider ${{slide.badge_class}} border flex items-center space-x-2 shadow-2xs">
                                <span class="scale-75">${{slide.app_icon_svg}}</span>
                                <span>${{slide.full_chapter_name}} • ${{slide.badge}}</span>
                            </span>
                        </div>
                        <span class="font-mono text-xs md:text-sm font-black text-slate-400">UNIT ${{slide.num}} / {total_units:02d}</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl lg:text-4xl font-black text-slate-900 mb-2.5 leading-tight tracking-tight break-keep max-w-4xl mx-auto text-center">${{slide.title}}</h1>
                    <p class="text-base md:text-lg text-slate-600 font-medium mb-6 max-w-3xl mx-auto break-keep text-center leading-relaxed">${{slide.subtitle}}</p>
                </div>
                <div class="my-auto py-2 text-base">
                    ${{slide.body}}
                </div>
                <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-sm text-slate-600 font-medium">
                    <span class="font-bold text-slate-800 flex items-center space-x-2">
                        <span class="scale-75">${{slide.app_icon_svg}}</span>
                        <span>${{slide.full_chapter_name}}</span>
                    </span>
                    <div class="flex items-center space-x-2.5">
                        <button onclick="prevSlide()" class="px-4 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-full transition-colors text-sm">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-5 py-1.5 bg-slate-900 hover:bg-indigo-600 text-white font-bold rounded-full shadow-xs transition-colors text-sm">다음 ▶</button>
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
                    item.className = `slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 bg-slate-100 border-slate-300 border shadow-xs`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-6 h-6 rounded-lg bg-slate-900 text-white flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-xs md:text-sm font-bold text-slate-900 break-keep leading-snug item-title flex items-start space-x-1.5`;
                    item.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }} else {{
                    item.className = `slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 hover:bg-slate-50 border border-transparent`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-6 h-6 rounded-lg bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-medium mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-xs md:text-sm font-semibold text-slate-700 break-keep leading-snug item-title flex items-start space-x-1.5`;
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
                document.getElementById('slideModeBtn').className = 'px-3 py-1 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1 font-bold';
                document.getElementById('portalModeBtn').className = 'px-3 py-1 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1 font-bold';
                renderSlide(currentSlideIndex);
            }} else {{
                document.getElementById('slideViewStage').classList.add('hidden');
                document.getElementById('portalViewStage').classList.remove('hidden');
                document.getElementById('slideModeBtn').className = 'px-3 py-1 rounded-full text-slate-600 hover:text-slate-900 transition-all flex items-center space-x-1 font-bold';
                document.getElementById('portalModeBtn').className = 'px-3 py-1 rounded-full bg-slate-900 text-white shadow-xs transition-all flex items-center space-x-1 font-bold';
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

        // Initialize on Slide 0 with smart responsive initial state
        window.addEventListener('DOMContentLoaded', () => {{
            setSidebarState(sidebarCollapsed);
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

print("Successfully added responsive auto-collapse sidebar behavior on window resize!")
