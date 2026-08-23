import json

# Load existing module data from generate_m365_portal.py
loc = {}
with open("generate_m365_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
modules = loc["modules"]

# Update Slide 04 (Architecture) with the exact visual layout from the user's uploaded diagram
slide_04_body = """
<div class="p-6 bg-white/80 rounded-3xl border border-indigo-100 shadow-sm max-w-5xl mx-auto my-2 text-left">
    <div class="grid grid-cols-12 gap-5 items-start">
        
        <!-- Left Column: Users & Apps -->
        <div class="col-span-3 space-y-4">
            <!-- Your users and devices -->
            <div class="p-4 bg-slate-50/80 rounded-2xl border border-slate-200/80">
                <div class="text-xs font-bold text-slate-800 mb-2">Your users<br>and devices</div>
                <div class="flex items-center space-x-2 p-2 bg-white rounded-xl shadow-xs border border-slate-100">
                    <span class="w-7 h-7 rounded-lg bg-gradient-to-tr from-purple-500 to-pink-500 text-white flex items-center justify-center text-xs">👤</span>
                    <span class="w-7 h-7 rounded-lg bg-gradient-to-tr from-indigo-500 to-purple-500 text-white flex items-center justify-center text-xs">💻</span>
                </div>
            </div>

            <!-- Apps on your devices -->
            <div class="p-4 bg-slate-50/80 rounded-2xl border border-slate-200/80">
                <div class="text-xs font-bold text-slate-800 mb-2">Apps on<br>your devices</div>
                <div class="grid grid-cols-2 gap-2 p-2 bg-white rounded-xl shadow-xs border border-slate-100">
                    <div class="flex items-center space-x-1.5 p-1 bg-sky-50 rounded-lg text-[11px] font-bold text-sky-700"><span>🌊</span> Edge</div>
                    <div class="flex items-center space-x-1.5 p-1 bg-blue-50 rounded-lg text-[11px] font-bold text-blue-700"><span>📝</span> Word</div>
                    <div class="flex items-center space-x-1.5 p-1 bg-indigo-50 rounded-lg text-[11px] font-bold text-indigo-700"><span>💬</span> Teams</div>
                    <div class="flex items-center space-x-1.5 p-1 bg-emerald-50 rounded-lg text-[11px] font-bold text-emerald-700"><span>📊</span> Excel</div>
                    <div class="flex items-center space-x-1.5 p-1 bg-blue-50 rounded-lg text-[11px] font-bold text-blue-800"><span>✉️</span> Outlook</div>
                    <div class="flex items-center space-x-1.5 p-1 bg-purple-50 rounded-lg text-[11px] font-bold text-purple-700"><span>➕</span> More</div>
                </div>
            </div>
        </div>

        <!-- Center & Right: Microsoft 365 service boundary Box -->
        <div class="col-span-9 p-5 bg-gradient-to-br from-indigo-50/50 via-purple-50/30 to-orange-50/40 rounded-3xl border-2 border-indigo-200/80 shadow-md relative">
            
            <div class="grid grid-cols-12 gap-4">
                
                <!-- Tenant Core (Graph + Customer Data) -->
                <div class="col-span-8 p-5 bg-white rounded-2xl border border-slate-200 shadow-sm">
                    <h3 class="text-base font-extrabold text-slate-900 mb-3">Your Microsoft 365 tenant</h3>
                    
                    <!-- Microsoft Graph Bar -->
                    <div class="p-2.5 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-xl text-center font-bold text-xs text-indigo-950 mb-4 shadow-xs">
                        Microsoft Graph (Work IQ + ACL Indexing)
                    </div>

                    <!-- Customer Data Subgrid -->
                    <div class="p-3.5 bg-slate-50/80 rounded-xl border border-slate-200">
                        <div class="text-xs font-bold text-slate-800 mb-0.5">Your customer data</div>
                        <div class="text-[10px] text-slate-500 mb-3">Files, mailboxes, chat data, videos, etc.</div>

                        <div class="grid grid-cols-2 gap-3 text-xs">
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2">
                                <span class="w-6 h-6 rounded bg-sky-500 text-white flex items-center justify-center text-[10px] font-bold">E</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-[11px]">Exchange</div>
                                    <div class="text-[9px] text-slate-400">mailboxes</div>
                                </div>
                            </div>
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2">
                                <span class="w-6 h-6 rounded bg-blue-500 text-white flex items-center justify-center text-[10px] font-bold">☁️</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-[11px]">OneDrive</div>
                                    <div class="text-[9px] text-slate-400">files & folders</div>
                                </div>
                            </div>
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2">
                                <span class="w-6 h-6 rounded bg-indigo-600 text-white flex items-center justify-center text-[10px] font-bold">T</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-[11px]">Teams</div>
                                    <div class="text-[9px] text-slate-400">chat & channels</div>
                                </div>
                            </div>
                            <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex items-center space-x-2">
                                <span class="w-6 h-6 rounded bg-teal-600 text-white flex items-center justify-center text-[10px] font-bold">S</span>
                                <div>
                                    <div class="font-bold text-slate-800 text-[11px]">SharePoint</div>
                                    <div class="text-[9px] text-slate-400">files, lists, docs</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Side: Copilot & Azure OpenAI -->
                <div class="col-span-4 space-y-3">
                    <!-- Microsoft 365 Copilot Card with vibrant gradient -->
                    <div class="p-4 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-500 text-white rounded-2xl shadow-md flex items-center space-x-3">
                        <div class="w-9 h-9 rounded-xl bg-white/20 flex items-center justify-center text-lg">✨</div>
                        <div>
                            <div class="text-xs font-extrabold leading-tight">Microsoft</div>
                            <div class="text-sm font-black tracking-wide">365 Copilot</div>
                        </div>
                    </div>

                    <!-- Azure OpenAI service -->
                    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-sm text-center">
                        <div class="font-bold text-slate-900 text-xs leading-tight mb-1">Azure OpenAI service</div>
                        <div class="text-[10px] text-slate-500 mb-2.5">subscription for Microsoft 365</div>
                        <div class="p-2 bg-slate-100 rounded-lg text-[10px] font-bold text-slate-700 border border-slate-200">
                            Large Language Model (LLM)<br>
                            <span class="text-indigo-600">GPT-5.6 / Claude Sonnet 5</span>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Bottom Floating Boundary Pill Badge -->
            <div class="mt-3 text-center">
                <span class="inline-block px-4 py-1 bg-white text-slate-900 font-extrabold text-xs rounded-full shadow-md border border-indigo-200">
                    Microsoft 365 service boundary (Zero-Data Retention & Tenant Isolation)
                </span>
            </div>

        </div>

    </div>
</div>
"""

# Replace Slide 04 content
modules[0]["slides"][3]["body"] = slide_04_body

# Flatten slides with part info
all_slides = []
for part_idx, part in enumerate(modules):
    for slide_idx, slide in enumerate(part["slides"]):
        all_slides.append({
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
            "title": slide["title"],
            "subtitle": slide["subtitle"],
            "body": slide["body"],
            "notes": slide["notes"]
        })

fluent_portal_html = f"""<!DOCTYPE html>
<html lang="ko" class="h-full">
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
                        fluent: {{
                            bgStart: '#dbeafe',
                            bgMid: '#ede9fe',
                            bgEnd: '#fae8ff',
                            border: '#c7d2fe',
                            text: '#0f172a'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Fira Code', 'monospace']
                    }}
                }}
            }}
        }}
    </script>
    <!-- Mermaid.js for architectural diagrams -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    <style>
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');
        
        * {{
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        
        /* M365 Official Pastel Sky-Lavender-Peach Gradient */
        body {{
            background: linear-gradient(135deg, #dbe4f6 0%, #e6e2f7 40%, #faedf2 100%) !important;
            color: #0f172a;
        }}

        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(241, 245, 249, 0.6);
        }}
        ::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 9999px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #94a3b8;
        }}

        .fluent-card {{
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 10px 30px -5px rgba(30, 41, 59, 0.07), 0 4px 12px -2px rgba(30, 41, 59, 0.04);
        }}

        .copilot-pill {{
            background: linear-gradient(135deg, #0078d4 0%, #8b5cf6 50%, #ec4899 100%);
        }}

        .service-boundary-box {{
            background: linear-gradient(135deg, rgba(238, 242, 255, 0.6) 0%, rgba(245, 243, 255, 0.5) 50%, rgba(255, 247, 237, 0.5) 100%);
            border: 2px solid rgba(199, 210, 254, 0.8);
        }}

        @media print {{
            .no-print {{ display: none !important; }}
            .slide-page {{ page-break-after: always; break-after: page; }}
            body {{ background: white !important; }}
        }}
    </style>
</head>
<body class="h-full flex flex-col antialiased select-none">

    <!-- Top Global Microsoft 365 Navigation Bar (Fluent Glass Design) -->
    <header class="no-print h-14 bg-white/80 backdrop-blur-md border-b border-indigo-100 text-slate-800 flex items-center justify-between px-4 z-40 shrink-0 select-none shadow-xs">
        <div class="flex items-center space-x-3">
            <!-- App Launcher Waffle -->
            <button id="waffleBtn" class="w-9 h-9 flex items-center justify-center rounded-xl hover:bg-slate-100 transition-colors text-lg text-slate-700" title="M365 앱 바로가기">
                ⣿
            </button>
            <div class="flex items-center space-x-2.5">
                <span class="w-6 h-6 rounded-lg copilot-pill text-white flex items-center justify-center text-xs shadow-xs">✨</span>
                <span class="font-extrabold text-sm tracking-tight text-slate-900">Microsoft 365 Copilot</span>
                <span class="text-slate-300 text-xs">|</span>
                <span class="text-xs text-slate-600 font-semibold hidden sm:inline">통신·네트워크 실무 마스터 (33 덱)</span>
            </div>
        </div>

        <!-- Center: Quick Part Switcher -->
        <div class="hidden lg:flex items-center space-x-1 bg-slate-100/80 p-1 rounded-xl border border-slate-200/80 text-xs">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-nav-btn px-2.5 py-1 rounded-lg transition-all text-slate-600 hover:text-slate-900 hover:bg-white flex items-center space-x-1" data-part="{idx}">
                <span>{p["app_icon"]}</span>
                <span class="font-medium">{p["part_num"]}</span>
            </button>
            ''' for idx, p in enumerate(modules)])}
        </div>

        <!-- Right: View Controls -->
        <div class="flex items-center space-x-2">
            <!-- Search Trigger -->
            <div class="relative hidden md:block">
                <input type="text" id="searchInput" placeholder="슬라이드 / 키워드 검색..." class="bg-white/90 border border-slate-200 rounded-xl px-3 py-1 text-xs text-slate-700 placeholder-slate-400 focus:outline-none focus:border-indigo-400 w-44 shadow-2xs">
            </div>

            <!-- Notes Toggle -->
            <button id="notesToggleBtn" onclick="toggleNotesDrawer()" class="px-3 py-1 bg-white hover:bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-700 font-semibold flex items-center space-x-1.5 transition-colors shadow-2xs" title="발표자 노트 토글 (단축키: N)">
                <span>🎙️</span>
                <span class="hidden sm:inline">발표자 노트</span>
            </button>

            <!-- Mode Switcher (Presentation Slide vs Document Portal) -->
            <div class="flex bg-slate-100 p-0.5 rounded-xl border border-slate-200 text-xs">
                <button id="slideModeBtn" onclick="setViewMode('slide')" class="px-2.5 py-1 rounded-lg bg-white text-indigo-700 font-bold shadow-xs transition-all flex items-center space-x-1">
                    <span>🖥️</span>
                    <span class="hidden md:inline">슬라이드</span>
                </button>
                <button id="portalModeBtn" onclick="setViewMode('portal')" class="px-2.5 py-1 rounded-lg text-slate-500 hover:text-slate-800 transition-all flex items-center space-x-1">
                    <span>📑</span>
                    <span class="hidden md:inline">포털 뷰</span>
                </button>
            </div>

            <!-- Fullscreen -->
            <button onclick="toggleFullscreen()" class="w-8 h-8 flex items-center justify-center rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-600 text-xs transition-colors shadow-2xs" title="전체화면 (F)">
                ⛶
            </button>
        </div>
    </header>

    <!-- Main Container: Sidebar + Content Area -->
    <div class="flex-1 flex overflow-hidden relative">

        <!-- Left App & Slide Sidebar -->
        <aside id="sidebar" class="no-print w-72 bg-white/90 backdrop-blur-md border-r border-indigo-100 flex flex-col shrink-0 transition-all duration-300 z-30 shadow-sm">
            <!-- Sidebar Header: Active App Info -->
            <div id="sidebarAppBanner" class="p-3.5 bg-gradient-to-r from-blue-50/70 via-indigo-50/70 to-purple-50/70 border-b border-indigo-100 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-2.5">
                    <span id="activeAppIcon" class="text-2xl">✨</span>
                    <div>
                        <div id="activeAppName" class="font-extrabold text-xs text-slate-900 leading-tight">M365 Copilot Core</div>
                        <div id="activePartNum" class="text-[10px] text-indigo-600 font-semibold">Part 1. 기초 & 보안</div>
                    </div>
                </div>
                <span id="slideCounterBadge" class="text-[11px] font-mono font-bold bg-white px-2.5 py-0.5 rounded-full border border-indigo-200 text-indigo-700 shadow-2xs">
                    01 / 33
                </span>
            </div>

            <!-- Slide List Scroll Area -->
            <div class="flex-1 overflow-y-auto p-2 space-y-1" id="slideListNav">
                {"".join([f'''
                <div class="slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 hover:bg-slate-50 border border-transparent" id="nav-item-{idx}" onclick="goToSlide({idx})">
                    <span class="shrink-0 w-6 h-6 rounded-lg bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge">{s["num"]}</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-xs font-bold text-slate-800 truncate leading-snug item-title">{s["title"].replace("<br>", " ")}</div>
                        <div class="text-[10px] text-slate-400 truncate mt-0.5 font-medium">{s["badge"]}</div>
                    </div>
                </div>
                ''' for idx, s in enumerate(all_slides)])}
            </div>

            <!-- Sidebar Footer: Keyboard Shortcut Hint -->
            <div class="p-3 bg-slate-50/80 border-t border-slate-200 text-[11px] text-slate-500 flex items-center justify-between">
                <span>⌨️ <code>Space</code> / <code>←→</code> 이동</span>
                <span><code>N</code> 노트</span>
            </div>
        </aside>

        <!-- Center Workspace: Slide View or Scroll Portal -->
        <main class="flex-1 flex flex-col overflow-hidden relative">

            <!-- Dynamic Brand Header Banner (Soft Fluent Pastel Strip) -->
            <div id="appThemeHeader" class="no-print h-9 bg-white/70 backdrop-blur-sm border-b border-indigo-100 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2 text-xs font-semibold">
                    <span id="bannerAppBadge" class="px-2 py-0.5 bg-indigo-100 text-indigo-800 rounded font-bold uppercase tracking-wider text-[10px]">M365 COPILOT</span>
                    <span id="bannerSlideTitle" class="truncate max-w-xl text-slate-800 font-bold">2026 통신 네트워크 패러다임: '작성 도우미'에서 '자율 에이전트'로</span>
                </div>
                <div class="flex items-center space-x-2 text-xs text-slate-500">
                    <button onclick="prevSlide()" class="px-2 py-0.5 rounded hover:bg-slate-100 font-medium transition-colors" title="이전 (←)">◀ 이전</button>
                    <button onclick="nextSlide()" class="px-2 py-0.5 rounded hover:bg-slate-100 font-medium transition-colors" title="다음 (→ / Space)">다음 ▶</button>
                </div>
            </div>

            <!-- Slide View Container (Single Big Presentation Stage) -->
            <div id="slideViewStage" class="flex-1 overflow-y-auto p-4 md:p-8 flex items-center justify-center">
                <div id="activeSlideCard" class="w-full max-w-5xl fluent-card rounded-3xl p-6 md:p-10 transition-all duration-300 text-center flex flex-col justify-between min-h-[590px]">
                    <!-- Dynamic Slide Content injected by JS -->
                </div>
            </div>

            <!-- Scroll Portal Mode Container (All 33 Units in clean reading page layout) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-6 md:p-12 space-y-12 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-5xl mx-auto fluent-card rounded-3xl p-8 md:p-12 slide-page">
                    <div class="flex items-center justify-between mb-4">
                        <span class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider {s["theme"]["nav_active"]} border">{s["app_name"]} • {s["badge"]}</span>
                        <span class="font-mono text-xs font-bold text-slate-400">SLIDE {s["num"]} / 33</span>
                    </div>
                    <h2 class="text-2xl md:text-3xl font-extrabold text-slate-900 mb-2 leading-tight">{s["title"]}</h2>
                    <p class="text-sm text-slate-500 mb-6">{s["subtitle"]}</p>
                    <div class="my-6">
                        {s["body"]}
                    </div>
                    <div class="mt-6 p-4 bg-slate-50 rounded-2xl border border-slate-200 text-xs text-slate-600 flex items-start space-x-3">
                        <span class="text-base">🎙️</span>
                        <div>
                            <strong class="text-slate-800">발표자 코치 노트:</strong>
                            <p class="mt-0.5 leading-relaxed">{s["notes"]}</p>
                        </div>
                    </div>
                </article>
                ''' for idx, s in enumerate(all_slides)])}
            </div>

            <!-- Bottom Progress Track -->
            <div class="no-print h-1.5 bg-slate-200/80 shrink-0">
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-500 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 3.03%;"></div>
            </div>
        </main>

        <!-- Right Speaker Notes Drawer (Collapsible) -->
        <aside id="notesDrawer" class="no-print w-80 bg-white/95 backdrop-blur-md border-l border-indigo-100 flex flex-col shrink-0 transition-all duration-300 z-30 hidden shadow-lg">
            <div class="p-4 bg-gradient-to-r from-slate-900 to-indigo-950 text-white flex items-center justify-between">
                <div class="flex items-center space-x-2">
                    <span>🎙️</span>
                    <h4 class="font-bold text-xs">발표자 코치 노트</h4>
                </div>
                <button onclick="toggleNotesDrawer()" class="text-slate-400 hover:text-white text-xs">✕</button>
            </div>
            <div class="flex-1 p-5 overflow-y-auto space-y-4 text-xs text-slate-700 leading-relaxed">
                <div>
                    <span class="text-[10px] font-bold uppercase text-indigo-600 font-mono tracking-wider">Current Slide Goal</span>
                    <div id="notesSlideTitle" class="font-bold text-slate-900 text-sm mt-1 mb-2">슬라이드 제목</div>
                </div>
                <div class="p-4 bg-indigo-50/70 rounded-2xl border border-indigo-100 text-slate-700" id="notesContentText">
                    발표 대본 및 청중 Q&A 코칭 내용이 여기에 표시됩니다.
                </div>
                <div class="p-3 bg-amber-50 rounded-xl border border-amber-200 text-[11px] text-amber-900">
                    💡 <strong>스피치 팁:</strong> 엔지니어 청중에게는 개념 나열보다 실제 장애 처리 시간(MTTR) 단축 사례와 프롬프트 입력값을 강조하세요.
                </div>
            </div>
        </aside>

    </div>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 bg-slate-900 text-white px-4 py-2.5 rounded-2xl shadow-2xl text-xs font-medium flex items-center space-x-2 transition-all duration-300 opacity-0 pointer-events-none transform translate-y-4 z-50">
        <span>✅</span>
        <span id="toastMsg">복사되었습니다.</span>
    </div>

    <!-- Data Injection & Interactive Controller Script -->
    <script>
        const slidesData = {json.dumps(all_slides, ensure_ascii=False)};
        let currentSlideIndex = 0;
        let viewMode = 'slide';
        let notesOpen = false;

        function renderSlide(index) {{
            if (index < 0 || index >= slidesData.length) return;
            currentSlideIndex = index;
            const slide = slidesData[index];

            // Render Center Card in Slide Mode
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider ${{slide.theme.nav_active}} border shadow-2xs flex items-center space-x-1.5">
                            <span>${{slide.app_icon}}</span>
                            <span>${{slide.app_name}} • ${{slide.badge}}</span>
                        </span>
                        <div class="flex items-center space-x-2">
                            <span class="font-mono text-xs font-bold text-slate-400">SLIDE ${{slide.num}} / 33</span>
                            <button onclick="copyPromptContent(${{index}})" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-semibold transition-colors flex items-center space-x-1 shadow-2xs" title="프롬프트 복사">
                                <span>📋</span>
                                <span>프롬프트 복사</span>
                            </button>
                        </div>
                    </div>
                    <h1 class="text-2xl md:text-3xl font-extrabold text-slate-900 mb-2 leading-tight tracking-tight">${{slide.title}}</h1>
                    <p class="text-xs md:text-sm text-slate-500 mb-4 max-w-3xl mx-auto">${{slide.subtitle}}</p>
                </div>
                <div class="my-auto py-2">
                    ${{slide.body}}
                </div>
                <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-400">
                    <span class="font-medium">${{slide.part_num}}: ${{slide.part_title}}</span>
                    <div class="flex items-center space-x-2">
                        <button onclick="prevSlide()" class="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-xl transition-colors">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-xl shadow-xs transition-colors">다음 ▶</button>
                    </div>
                </div>
            `;

            // Update Header Banner
            document.getElementById('bannerAppBadge').textContent = slide.app_name.toUpperCase();
            document.getElementById('bannerSlideTitle').textContent = slide.title.replace(/<[^>]*>/g, '');

            // Update Sidebar Info
            document.getElementById('activeAppIcon').textContent = slide.app_icon;
            document.getElementById('activeAppName').textContent = slide.app_name;
            document.getElementById('activePartNum').textContent = `${{slide.part_num}}. ${{slide.part_title}}`;
            document.getElementById('slideCounterBadge').textContent = `${{slide.num}} / 33`;

            // Highlight Active Sidebar Item & Scroll into view
            document.querySelectorAll('.slide-nav-item').forEach((item, i) => {{
                if (i === index) {{
                    item.className = `slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 bg-indigo-50/80 border-indigo-200 border shadow-2xs`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge shadow-2xs`;
                    item.querySelector('.item-title').className = `text-xs font-bold text-indigo-950 truncate leading-snug item-title`;
                    item.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }} else {{
                    item.className = `slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 hover:bg-slate-50 border border-transparent`;
                    item.querySelector('.item-num-badge').className = `shrink-0 w-6 h-6 rounded-lg bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge`;
                    item.querySelector('.item-title').className = `text-xs font-bold text-slate-800 truncate leading-snug item-title`;
                }}
            }});

            // Highlight Part Nav Buttons
            document.querySelectorAll('.part-nav-btn').forEach((btn, pIdx) => {{
                if (pIdx === slide.part_idx) {{
                    btn.className = `part-nav-btn px-2.5 py-1 rounded-lg transition-all text-indigo-900 bg-white font-bold shadow-2xs flex items-center space-x-1 border border-slate-200`;
                }} else {{
                    btn.className = `part-nav-btn px-2.5 py-1 rounded-lg transition-all text-slate-600 hover:text-slate-900 hover:bg-white flex items-center space-x-1`;
                }}
            }});

            // Update Progress Bar
            const progress = ((index + 1) / slidesData.length) * 100;
            document.getElementById('progressBar').style.width = `${{progress}}%`;

            // Update Notes
            document.getElementById('notesSlideTitle').textContent = `[${{slide.num}}] ` + slide.title.replace(/<[^>]*>/g, '');
            document.getElementById('notesContentText').textContent = slide.notes;

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
                document.getElementById('slideModeBtn').className = 'px-2.5 py-1 rounded-lg bg-white text-indigo-700 font-bold shadow-xs transition-all flex items-center space-x-1';
                document.getElementById('portalModeBtn').className = 'px-2.5 py-1 rounded-lg text-slate-500 hover:text-slate-800 transition-all flex items-center space-x-1';
                renderSlide(currentSlideIndex);
            }} else {{
                document.getElementById('slideViewStage').classList.add('hidden');
                document.getElementById('portalViewStage').classList.remove('hidden');
                document.getElementById('slideModeBtn').className = 'px-2.5 py-1 rounded-lg text-slate-500 hover:text-slate-800 transition-all flex items-center space-x-1';
                document.getElementById('portalModeBtn').className = 'px-2.5 py-1 rounded-lg bg-white text-indigo-700 font-bold shadow-xs transition-all flex items-center space-x-1';
                const target = document.getElementById(`portal-slide-${{currentSlideIndex}}`);
                if (target) target.scrollIntoView({{ behavior: 'smooth' }});
            }}
        }}

        function toggleNotesDrawer() {{
            notesOpen = !notesOpen;
            const drawer = document.getElementById('notesDrawer');
            if (notesOpen) {{
                drawer.classList.remove('hidden');
                document.getElementById('notesToggleBtn').classList.add('bg-indigo-600', 'text-white');
                document.getElementById('notesToggleBtn').classList.remove('bg-white', 'text-slate-700');
            }} else {{
                drawer.classList.add('hidden');
                document.getElementById('notesToggleBtn').classList.remove('bg-indigo-600', 'text-white');
                document.getElementById('notesToggleBtn').classList.add('bg-white', 'text-slate-700');
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

        function copyPromptContent(slideIdx) {{
            const slide = slidesData[slideIdx];
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = slide.body;
            const promptBox = tempDiv.querySelector('.font-mono');
            const textToCopy = promptBox ? promptBox.innerText : slide.title.replace(/<[^>]*>/g, '');

            navigator.clipboard.writeText(textToCopy).then(() => {{
                showToast(`[Slide ${{slide.num}}] 프롬프트가 클립보드에 복사되었습니다!`);
            }});
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            document.getElementById('toastMsg').textContent = msg;
            toast.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
            toast.classList.add('opacity-100', 'translate-y-0');
            setTimeout(() => {{
                toast.classList.remove('opacity-100', 'translate-y-0');
                toast.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
            }}, 2500);
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
            }} else if (e.key === 'n' || e.key === 'N') {{
                toggleNotesDrawer();
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
with open(output_path, "w", encoding="utf-8") as f:
    f.write(fluent_portal_html)

print(f"Successfully generated M365 Fluent Pastel Architecture Portal at {output_path}")
