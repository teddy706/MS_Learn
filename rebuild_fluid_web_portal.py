import json

loc = {}
with open("generate_m365_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
modules = loc["modules"]

# Slide 04 layout with generous fluid web grid
slide_04_body = """
<div class="p-6 md:p-8 bg-white/95 rounded-3xl border border-slate-200 shadow-sm w-full max-w-5xl mx-auto text-left my-2">
    <div class="grid grid-cols-12 gap-6 items-start">
        
        <!-- Left Column: Users & Apps -->
        <div class="col-span-12 lg:col-span-4 space-y-4">
            <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                <div class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2">Your users and devices</div>
                <div class="flex items-center space-x-3 p-3 bg-white rounded-xl shadow-xs border border-slate-200">
                    <span class="w-8 h-8 rounded-lg bg-gradient-to-tr from-purple-500 to-pink-500 text-white flex items-center justify-center text-sm">👤</span>
                    <span class="w-8 h-8 rounded-lg bg-gradient-to-tr from-indigo-500 to-purple-500 text-white flex items-center justify-center text-sm">💻</span>
                    <span class="text-sm font-bold text-slate-800">사내 인증 엔지니어</span>
                </div>
            </div>

            <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                <div class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2">Apps on your devices</div>
                <div class="grid grid-cols-2 gap-2 p-2 bg-white rounded-xl shadow-xs border border-slate-200">
                    <div class="flex items-center space-x-2 p-2 bg-sky-50 rounded-lg text-xs font-bold text-sky-800"><span>🌊</span> Edge</div>
                    <div class="flex items-center space-x-2 p-2 bg-blue-50 rounded-lg text-xs font-bold text-blue-800"><span>📝</span> Word</div>
                    <div class="flex items-center space-x-2 p-2 bg-indigo-50 rounded-lg text-xs font-bold text-indigo-800"><span>💬</span> Teams</div>
                    <div class="flex items-center space-x-2 p-2 bg-emerald-50 rounded-lg text-xs font-bold text-emerald-800"><span>📊</span> Excel</div>
                    <div class="flex items-center space-x-2 p-2 bg-blue-50 rounded-lg text-xs font-bold text-blue-900"><span>✉️</span> Outlook</div>
                    <div class="flex items-center space-x-2 p-2 bg-purple-50 rounded-lg text-xs font-bold text-purple-800"><span>➕</span> More</div>
                </div>
            </div>
        </div>

        <!-- Center & Right: Microsoft 365 service boundary Box -->
        <div class="col-span-12 lg:col-span-8 p-6 bg-gradient-to-br from-slate-50/90 via-indigo-50/40 to-pink-50/40 rounded-3xl border-2 border-indigo-200 shadow-md">
            <div class="space-y-4">
                <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center mb-3">
                        <h3 class="text-base font-black text-slate-900">Your Microsoft 365 tenant</h3>
                        <span class="px-3 py-1 bg-indigo-100 text-indigo-800 text-xs font-bold rounded-full">Encrypted Tenant Boundary</span>
                    </div>
                    
                    <div class="p-3 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-xl text-center font-bold text-sm text-indigo-950 mb-4 shadow-2xs">
                        Microsoft Graph (Work IQ + Entra ID ACL Indexing)
                    </div>

                    <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                        <div class="text-xs font-bold text-slate-800 mb-1">Your customer data</div>
                        <div class="text-xs text-slate-500 mb-3">Files, mailboxes, chat data, videos, etc.</div>
                        <div class="grid grid-cols-2 gap-2.5 text-xs">
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2.5 shadow-2xs">
                                <span class="w-7 h-7 rounded bg-sky-500 text-white flex items-center justify-center text-xs font-bold">E</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-xs">Exchange</div>
                                    <div class="text-[11px] text-slate-500">mailboxes</div>
                                </div>
                            </div>
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2.5 shadow-2xs">
                                <span class="w-7 h-7 rounded bg-blue-500 text-white flex items-center justify-center text-xs font-bold">☁️</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-xs">OneDrive</div>
                                    <div class="text-[11px] text-slate-500">files & folders</div>
                                </div>
                            </div>
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2.5 shadow-2xs">
                                <span class="w-7 h-7 rounded bg-indigo-600 text-white flex items-center justify-center text-xs font-bold">T</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-xs">Teams</div>
                                    <div class="text-[11px] text-slate-500">chat & channels</div>
                                </div>
                            </div>
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2.5 shadow-2xs">
                                <span class="w-7 h-7 rounded bg-teal-600 text-white flex items-center justify-center text-xs font-bold">S</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-xs">SharePoint</div>
                                    <div class="text-[11px] text-slate-500">files, lists, docs</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div class="p-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-500 text-white rounded-2xl shadow-md flex items-center space-x-3">
                        <div class="w-9 h-9 rounded-xl bg-white/20 flex items-center justify-center text-lg shadow-xs">✨</div>
                        <div>
                            <div class="text-[10px] font-extrabold leading-tight uppercase opacity-90">Microsoft</div>
                            <div class="text-base font-black tracking-wide">365 Copilot</div>
                        </div>
                    </div>
                    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm text-center">
                        <div class="font-bold text-slate-900 text-xs md:text-sm leading-tight">Azure OpenAI service</div>
                        <div class="text-xs font-bold text-indigo-600 mt-1">GPT-5.6 / Claude Sonnet 5</div>
                    </div>
                </div>
            </div>

            <div class="mt-4 text-center">
                <span class="inline-block px-5 py-1.5 bg-white text-slate-900 font-extrabold text-xs md:text-sm rounded-full shadow-md border border-indigo-200">
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
    for slide_idx, slide in enumerate(part["slides"]):
        t = slide["title"].replace("<br>", " ").replace("  ", " ").strip()
        st = slide["subtitle"].replace("<br>", " ").replace("  ", " ").strip()
        b = slide["body"]
        
        cleaned_slides.append({
            "part_idx": part_idx,
            "part_id": part["id"],
            "part_title": part["title"],
            "part_num": part["part_num"],
            "app": part["app"],
            "app_name": part["app_name"],
            "app_icon": part["app_icon"],
            "theme": part["theme"],
            "num": slide["num"],
            "badge": slide["badge"],
            "title": t,
            "subtitle": st,
            "body": b
        })

fluid_html = f"""<!DOCTYPE html>
<html lang="ko" class="h-full" id="htmlRoot">
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
                        msblue: '#0078d4',
                        msdark: '#111827',
                        mspurple: '#6366f1',
                        mscoral: '#ea580c',
                        msgreen: '#107c41',
                        mssoftbg: '#f8fafc'
                    }},
                    fontFamily: {{
                        sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Consolas', 'monospace']
                    }}
                }}
            }}
        }}
    </script>
    <!-- Mermaid.js for live diagrams -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    <style>
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');
        
        * {{
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            user-select: text !important;
            -webkit-user-select: text !important;
            word-break: keep-all !important;
            overflow-wrap: break-word !important;
            box-sizing: border-box;
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
            background: linear-gradient(135deg, #0078d4 0%, #7c3aed 50%, #db2777 100%);
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
            color: #475569;
            border: 1px solid #e2e8f0;
        }}
        .ms-pill-tab:not(.active):hover {{
            background-color: #f1f5f9;
            color: #0f172a;
        }}

        blockquote {{
            border-left: 4px solid #6366f1;
            padding-left: 1rem;
            margin: 0.75rem 0;
            font-style: italic;
            color: #334155;
            word-break: keep-all !important;
        }}

        /* Sidebar Collapse Transitions */
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
    <header class="no-print h-14 bg-white/90 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-4 z-40 shrink-0 shadow-xs">
        <div class="flex items-center space-x-3">
            <!-- Sidebar Toggle Button -->
            <button id="sidebarToggleBtn" onclick="toggleSidebar()" class="w-9 h-9 flex items-center justify-center rounded-xl hover:bg-slate-100 transition-colors text-slate-700 font-bold" title="사이드바 접기/펼치기 (단축키: B)">
                <span id="sidebarToggleIcon" class="text-base">☰</span>
            </button>

            <!-- App Logo -->
            <div class="flex items-center space-x-2.5">
                <span class="w-6 h-6 rounded-lg copilot-gradient-badge text-white flex items-center justify-center text-xs shadow-xs">✨</span>
                <span class="font-black text-sm md:text-base tracking-tight text-slate-900">Microsoft 365 Copilot</span>
                <span class="text-slate-300 text-xs">|</span>
                <span class="text-xs text-slate-500 font-bold hidden sm:inline uppercase tracking-wider">통신·네트워크 실무 마스터 포털</span>
            </div>
        </div>

        <!-- Center: Microsoft 365 Category Pill Bar -->
        <div class="hidden lg:flex items-center space-x-1.5 overflow-x-auto py-1">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-pill-btn ms-pill-tab px-3 py-1 text-xs font-semibold flex items-center space-x-1.5" data-part="{idx}">
                <span>{p["app_icon"]}</span>
                <span>{p["part_num"]}</span>
            </button>
            ''' for idx, p in enumerate(modules)])}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center space-x-2.5">
            <!-- Search Trigger -->
            <div class="relative hidden md:block">
                <input type="text" id="searchInput" placeholder="프롬프트 / 시나리오 검색..." class="bg-slate-100/90 border border-slate-200 rounded-full px-3.5 py-1 text-xs text-slate-700 placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:bg-white w-44 transition-all">
            </div>

            <!-- View Switcher -->
            <div class="flex bg-slate-100 p-0.5 rounded-full border border-slate-200 text-xs font-bold">
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
            <!-- Sidebar Header -->
            <div id="sidebarAppBanner" class="p-3.5 bg-slate-50 border-b border-slate-200 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-2.5">
                    <span id="activeAppIcon" class="text-2xl">✨</span>
                    <div>
                        <div id="activeAppName" class="font-black text-xs md:text-sm text-slate-900 leading-tight">M365 Copilot Core</div>
                        <div id="activePartNum" class="text-[11px] text-indigo-600 font-bold mt-0.5">Part 1. 기초 & 보안</div>
                    </div>
                </div>
                <div class="flex items-center space-x-1.5">
                    <span id="slideCounterBadge" class="text-[11px] font-mono font-black bg-white px-2 py-0.5 rounded-full border border-slate-200 text-slate-700 shadow-2xs">
                        01 / 33
                    </span>
                    <button onclick="toggleSidebar()" class="w-6 h-6 rounded-lg hover:bg-slate-200 text-slate-400 hover:text-slate-700 flex items-center justify-center text-xs font-bold transition-colors" title="사이드바 축소">
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
                        <div class="text-xs md:text-sm font-bold text-slate-800 truncate leading-snug item-title">{s["title"]}</div>
                        <div class="text-[11px] text-slate-400 truncate mt-0.5 font-semibold">{s["badge"]}</div>
                    </div>
                </div>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Sidebar Footer -->
            <div class="p-3 bg-slate-50 border-t border-slate-200 text-xs text-slate-500 flex items-center justify-between font-medium">
                <span>⌨️ <code>B</code> 사이드바 접기</span>
                <span><code>Space</code> 이동</span>
            </div>
        </aside>

        <!-- Center Workspace: Fluid Web Stage -->
        <main class="flex-1 flex flex-col overflow-hidden relative">

            <!-- App Category Breadcrumb Bar -->
            <div id="appThemeHeader" class="no-print h-10 bg-white/70 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2 text-xs md:text-sm font-semibold">
                    <span id="bannerAppBadge" class="px-2.5 py-0.5 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-[10px] border border-slate-200">M365 COPILOT</span>
                    <span class="text-slate-300">/</span>
                    <span id="bannerSlideTitle" class="truncate max-w-2xl text-slate-900 font-extrabold break-keep">2026 통신 네트워크 패러다임: '작성 도우미'에서 '자율 에이전트'로</span>
                </div>
                <div class="flex items-center space-x-2 text-xs font-bold text-slate-600">
                    <button onclick="prevSlide()" class="px-3 py-1 rounded-full hover:bg-slate-100 transition-colors" title="이전 (←)">◀ 이전</button>
                    <button onclick="nextSlide()" class="px-3 py-1 rounded-full hover:bg-slate-100 transition-colors" title="다음 (→ / Space)">다음 ▶</button>
                </div>
            </div>

            <!-- Single Card View Container (Fluid Web Layout) -->
            <div id="slideViewStage" class="flex-1 overflow-y-auto p-4 md:p-8 flex items-center justify-center">
                <div id="activeSlideCard" class="w-full max-w-5xl ms-fluid-card p-6 md:p-10 flex flex-col justify-between my-auto min-h-[580px]">
                    <!-- Dynamic Slide Content injected by JS -->
                </div>
            </div>

            <!-- Continuous Document Scroll Portal (All 33 Units) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-6 md:p-12 space-y-12 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-5xl mx-auto ms-fluid-card p-8 md:p-12 slide-page">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <span class="px-3.5 py-1 rounded-full text-xs font-black uppercase tracking-wider bg-slate-100 text-slate-800 border border-slate-200">{s["app_name"]} • {s["badge"]}</span>
                            <span class="font-mono text-xs font-black text-slate-400">UNIT {s["num"]} / 33</span>
                        </div>
                        <h2 class="text-2xl md:text-3xl font-black text-slate-900 mb-2 leading-tight tracking-tight break-keep">{s["title"]}</h2>
                        <p class="text-sm md:text-base text-slate-600 font-medium mb-6 break-keep">{s["subtitle"]}</p>
                    </div>
                    <div class="my-auto py-2">
                        {s["body"]}
                    </div>
                    <div class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-400 text-left">
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

        // Toggle Sidebar Collapse/Expand
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

            // Render Center Card in Fluid Web Mode
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge -->
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center space-x-2">
                            <span class="w-7 h-7 rounded-lg copilot-gradient-badge text-white flex items-center justify-center text-xs shadow-xs">${{slide.app_icon}}</span>
                            <span class="px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider bg-slate-100 text-slate-800 border border-slate-200">
                                ${{slide.app_name}} • ${{slide.badge}}
                            </span>
                        </div>
                        <span class="font-mono text-xs font-black text-slate-400">UNIT ${{slide.num}} / 33</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl lg:text-4xl font-black text-slate-900 mb-2 leading-tight tracking-tight break-keep max-w-4xl mx-auto text-center">${{slide.title}}</h1>
                    <p class="text-sm md:text-base text-slate-600 font-medium mb-6 max-w-3xl mx-auto break-keep text-center">${{slide.subtitle}}</p>
                </div>
                <div class="my-auto py-2">
                    ${{slide.body}}
                </div>
                <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs md:text-sm text-slate-500 font-medium">
                    <span class="font-bold text-slate-700">${{slide.part_num}}: ${{slide.part_title}}</span>
                    <div class="flex items-center space-x-2">
                        <button onclick="prevSlide()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-full transition-colors">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-5 py-2 bg-slate-900 hover:bg-indigo-600 text-white font-bold rounded-full shadow-xs transition-colors">다음 ▶</button>
                    </div>
                </div>
            `;

            // Update Header Banner
            document.getElementById('bannerAppBadge').textContent = slide.app_name.toUpperCase();
            document.getElementById('bannerSlideTitle').textContent = slide.title;

            // Update Sidebar Info
            document.getElementById('activeAppIcon').textContent = slide.app_icon;
            document.getElementById('activeAppName').textContent = slide.app_name;
            document.getElementById('activePartNum').textContent = `${{slide.part_num}}. ${{slide.part_title}}`;
            document.getElementById('slideCounterBadge').textContent = `${{slide.num}} / 33`;

            // Highlight Active Sidebar Item & Scroll into view
            document.querySelectorAll('.slide-nav-item').forEach((item, i) => {{
                if (i === index) {{
                    item.className = `slide-nav-item p-3 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3 bg-slate-100 border-slate-300 border shadow-xs`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-7 h-7 rounded-xl bg-slate-900 text-white flex items-center justify-center font-mono text-xs font-black mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-xs md:text-sm font-black text-slate-900 truncate leading-snug item-title`;
                    item.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }} else {{
                    item.className = `slide-nav-item p-3 rounded-2xl cursor-pointer transition-all text-left flex items-start space-x-3 hover:bg-slate-50 border border-transparent`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-7 h-7 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-xs md:text-sm font-bold text-slate-700 truncate leading-snug item-title`;
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
    f.write(fluid_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(fluid_html)

print(f"Successfully rebuilt fluid responsive web portal at {output_path} and {index_path}")
