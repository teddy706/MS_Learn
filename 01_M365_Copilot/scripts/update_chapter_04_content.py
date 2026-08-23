import json
import re

loc = {}
with open("update_chapter_03_content.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
standard_chapters = loc["standard_chapters"]
fluent_icons = loc["fluent_icons"]
slide_04_body = loc["slide_04_body"]

# Assign exact Chapter 04 specification (4 Hands-on Scenarios)
standard_chapters[3]["chapter_num"] = "04"
standard_chapters[3]["title"] = "데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북"
standard_chapters[3]["short_title"] = "04. 데이터기반 의사결정"
standard_chapters[3]["app_name"] = "Excel, Word, PPT 에이전트"
standard_chapters[3]["tools"] = "데이터 정제+시각화, 심층 추론+시뮬레이션, 다중 소스 합성, 의사결정 슬라이드"

standard_chapters[3]["units"] = [
    {
        "num": "16",
        "badge": "HANDS-ON 1 • EXCEL",
        "title": "[핸즈온 1] 엑셀 데이터 정제 + 시각화: 대용량 KPI 로그 전처리 및 차트 자동화",
        "subtitle": "비정형 로그 정제, 결측치 보정, 파생 열 생성부터 피벗 차트 시각화까지 자연어 원클릭 실습",
        "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="flex items-center justify-between mb-4">
        <h4 class="font-bold text-base md:text-lg text-slate-900">핸즈온 실습 1단계: 데이터 정제 & 시각화 워크플로우</h4>
        <span class="px-3 py-1 bg-emerald-100 text-emerald-950 text-xs font-black rounded-full">Excel Agent Mode</span>
    </div>
    <div class="space-y-3 text-xs md:text-sm">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <strong class="text-emerald-700">1. 결측치 및 비정형 로그 정제:</strong>
            <p class="text-slate-600 mt-1">"빈 셀(N/A)을 이전 정상 측정값으로 채우고, 'Latency_ms' 열에서 비정상 음수 값을 0으로 일괄 보정해줘."</p>
        </div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <strong class="text-indigo-700">2. 조건부 파생 열 생성:</strong>
            <p class="text-slate-600 mt-1">"'PRB_Usage'가 85% 이상이면서 'Drop_Rate'가 1.5% 초과인 경우 '위험', 그렇지 않으면 '정상'으로 분류하는 'Status' 열을 추가해줘."</p>
        </div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <strong class="text-purple-700">3. 피벗 테이블 & 시각화 차트 생성:</strong>
            <p class="text-slate-600 mt-1">"기지국 지역구분별 평균 트래픽 처리량을 계산하는 피벗 테이블과 시간대별 추이를 보여주는 콤보 차트를 생성해줘."</p>
        </div>
    </div>
</div>
"""
    },
    {
        "num": "17",
        "badge": "HANDS-ON 2 • REASONING",
        "title": "[핸즈온 2] 심층 추론 + 시뮬레이션: 이상치 원인 규명 및 What-If 시뮬레이션",
        "subtitle": "Python in Excel 고급 통계 분석과 파라미터 변동에 따른 트래픽 영향도 예측 실습",
        "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs">🧠</span>
            <span>심층 추론 (Deep Reasoning)</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3 leading-relaxed">
            단순 수치 나열을 넘어, 트래픽 급증과 패킷 드롭율 간의 상관관계를 파악하고 기지국 장비 과부하의 근본 원인을 논리적으로 추론합니다.
        </p>
        <div class="text-xs bg-slate-50 p-2.5 rounded-lg text-indigo-950 font-mono">
            "Z-Score 이상치 발생 시점과 사용자 접속자 수(UE) 급증 간의 상관계수를 계산하고 주원인을 분석해줘."
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs">📈</span>
            <span>What-If 시뮬레이션</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3 leading-relaxed">
            대역폭을 20% 증설하거나 기지국 채널을 분산 배치했을 때 예상되는 지연 시간 감소율과 투자 대비 개선 효과를 시뮬레이션합니다.
        </p>
        <div class="text-xs bg-slate-50 p-2.5 rounded-lg text-purple-950 font-mono">
            "백홀 대역폭을 10Gbps에서 20Gbps로 확장 시 피크타임 패킷 지연이 몇 % 개선되는지 모델링해줘."
        </div>
    </div>
</div>
"""
    },
    {
        "num": "18",
        "badge": "HANDS-ON 3 • WORD",
        "title": "[핸즈온 3] 워드 다중 소스 합성: 엑셀·매뉴얼·회의록을 결합한 통합 SOP 작성",
        "subtitle": "분산된 사내 파일(`/files`)들을 교차 인용하여 공공·기업 표준 규격의 기술 보고서로 원클릭 완성",
        "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">다중 소스(Multi-Source) 크로스 합성 실전 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "/files '5G_KPI_분석결과.xlsx'의 3번 시트 통계 테이블과, /files 'L3스위치_표준매뉴얼.docx', 그리고 지난 Teams 대책 회의록을 종합하여 '수도권 코어망 긴급 증설 및 장애 대응 표준 작업 절차서(SOP)'를 작성해줘. 목적, 장비 체크리스트, 단계별 명령어, 롤백 가이드를 포함한 정형화된 서식으로 완성해줘."
        </p>
    </blockquote>
    <div class="mt-4 flex flex-wrap gap-2 text-xs font-bold text-slate-600">
        <span class="px-3 py-1 bg-white rounded-full border border-slate-200 shadow-2xs">📊 엑셀 정량 데이터 합성</span>
        <span class="px-3 py-1 bg-white rounded-full border border-slate-200 shadow-2xs">📁 SharePoint 표준 규격 반영</span>
        <span class="px-3 py-1 bg-white rounded-full border border-slate-200 shadow-2xs">💬 Teams 협의 내용 동기화</span>
    </div>
</div>
"""
    },
    {
        "num": "19",
        "badge": "HANDS-ON 4 • PPT",
        "title": "[핸즈온 4] PPT 의사결정 슬라이드: 경영진 보고용 1-Page 핵심 ROI 디자인",
        "subtitle": "복잡한 수십 페이지의 Word 기술 보고서를 임원 의사결정에 최적화된 프레젠테이션으로 즉시 변환",
        "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">PowerPoint 의사결정 슬라이드 생성 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "/files '수도권_코어망_증설_SOP.docx'로부터 임원 보고용 4슬라이드 프레젠테이션을 생성해줘. 장황한 본문은 3대 핵심 수치(가용성 99.999%, MTTR -35%, OPEX 절감 4.2억)로 요약하고, 마지막 슬라이드에 의사결정 요청 액션 플랜을 넣어줘."
        </p>
    </blockquote>
    <div class="grid grid-cols-3 gap-3 mt-4 text-center text-xs md:text-sm font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">🎯 핵심 결론 우선 배치</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">📊 정량적 ROI 하이라이트</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">🚀 최종 승인 타임라인</div>
    </div>
</div>
"""
    },
    {
        "num": "20",
        "badge": "MASTER PLAYBOOK",
        "title": "[마스터 플레이북] 4대 핸즈온 통합: Excel ➔ Word ➔ PPT 원스톱 크로스-앱 워크플로우",
        "subtitle": "데이터 정제부터 시뮬레이션, 다중 소스 보고서 합성, 임원 의사결정 슬라이드 완성까지 완전 정복",
        "body": """
<div class="p-6 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 rounded-3xl border-2 border-indigo-200 text-left my-2 shadow-md">
    <h4 class="font-black text-base md:text-lg text-slate-900 mb-3">데이터 기반 의사결정 엔드-투-엔드(E2E) 워크플로우</h4>
    <div class="space-y-3 text-xs md:text-sm font-semibold">
        <div class="p-3 bg-white rounded-xl border border-indigo-100 flex items-center space-x-3 shadow-2xs">
            <span class="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-bold shrink-0">1</span>
            <span><strong>Excel 핸즈온</strong>: 로그 정제 + 조건부 서식 + 이상치 원인 추론 및 What-If 시뮬레이션</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-indigo-100 flex items-center space-x-3 shadow-2xs">
            <span class="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-bold shrink-0">2</span>
            <span><strong>Word 핸즈온</strong>: 엑셀 테이블과 SharePoint 표준 매뉴얼을 다중 소스로 합성하여 SOP 작성</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-indigo-100 flex items-center space-x-3 shadow-2xs">
            <span class="w-8 h-8 rounded-lg bg-orange-600 text-white flex items-center justify-center text-xs font-bold shrink-0">3</span>
            <span><strong>PPT 핸즈온</strong>: 완성된 SOP 보고서로부터 1-Page 임원 의사결정 슬라이드 자동 생성</span>
        </div>
    </div>
</div>
"""
    }
]

cleaned_slides = []
total_units = sum(len(c["units"]) for c in standard_chapters)
curr_unit_idx = 0

for chap_idx, chap in enumerate(standard_chapters):
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

standard_portal_html = f"""<!DOCTYPE html>
<html lang="ko" class="h-full font-pretendard" id="htmlRoot">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microsoft 365 Copilot 표준 교육과정 - 실무 마스터</title>
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
    <header class="no-print h-14 bg-white/95 backdrop-blur-md border-b border-slate-200 text-slate-800 flex items-center justify-between px-4 z-40 shrink-0 shadow-xs whitespace-nowrap select-none">
        <div class="flex items-center space-x-3">
            <!-- Sidebar Toggle Button -->
            <button id="sidebarToggleBtn" onclick="toggleSidebar()" class="w-9 h-9 flex items-center justify-center rounded-xl hover:bg-slate-100 transition-colors text-slate-700 font-bold" title="사이드바 접기/펼치기 (단축키: B)">
                <span id="sidebarToggleIcon" class="text-base">☰</span>
            </button>

            <!-- App Logo with Copilot Vector -->
            <div class="flex items-center space-x-2.5">
                <span class="w-7 h-7 rounded-lg flex items-center justify-center shadow-xs">
                    {fluent_icons["copilot"]}
                </span>
                <span class="font-black text-sm md:text-base tracking-tight text-slate-900">Microsoft 365 Copilot</span>
            </div>
        </div>

        <!-- Center: 4 Official Chapters Pill Bar -->
        <div class="hidden lg:flex items-center space-x-2 overflow-x-auto py-1">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-pill-btn ms-pill-tab px-3.5 py-1.5 text-xs md:text-sm font-bold flex items-center space-x-2" data-part="{idx}" title="{c['chapter_num']}. {c['title']}">
                <span class="scale-90">{c["icon_svg"]}</span>
                <span>{c["short_title"]}</span>
            </button>
            ''' for idx, c in enumerate(standard_chapters)])}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center space-x-2.5">
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
            <!-- Sidebar Header with Official Chapter Name -->
            <div id="sidebarAppBanner" class="p-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-3">
                    <span id="activeAppIcon" class="w-8 h-8 flex items-center justify-center">{fluent_icons["copilot"]}</span>
                    <div class="min-w-0 flex-1">
                        <div id="activeAppName" class="font-black text-sm text-slate-900 leading-tight truncate">Work IQ & Copilot Core</div>
                        <div id="activePartNum" class="text-xs text-indigo-600 font-bold mt-0.5 break-keep">01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI</div>
                    </div>
                </div>
                <div class="flex items-center space-x-1.5 shrink-0 ml-2">
                    <span id="slideCounterBadge" class="text-xs font-mono font-black bg-white px-2.5 py-0.5 rounded-full border border-slate-200 text-slate-700 shadow-2xs">
                        01 / {total_units:02d}
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

            <!-- App Category Breadcrumb Bar with Official Full Chapter Name -->
            <div id="appThemeHeader" class="no-print h-11 bg-white/80 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2.5 text-xs md:text-sm font-semibold truncate">
                    <span id="bannerAppBadge" class="px-3 py-0.5 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-xs border border-slate-200 flex items-center space-x-2 shrink-0">
                        <span id="bannerAppIconSvg" class="scale-75">{fluent_icons["copilot"]}</span>
                        <span id="bannerAppText">01. M365 COPILOT의 변화</span>
                    </span>
                    <span class="text-slate-300">/</span>
                    <span id="bannerSlideTitle" class="truncate max-w-2xl text-slate-900 font-extrabold break-keep text-sm">웹 기반 범용 AI vs M365 Copilot: 기업 업무에 최적화된 차이점</span>
                </div>
                <div class="flex items-center space-x-2 text-xs md:text-sm font-bold text-slate-600 shrink-0 ml-4">
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

            <!-- Continuous Document Scroll Portal (All Units) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-6 md:p-12 space-y-12 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-5xl mx-auto ms-fluid-card p-8 md:p-12 slide-page">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider {s["badge_class"]} border flex items-center space-x-2">
                                <span class="scale-90">{s["app_icon_svg"]}</span>
                                <span>{s["full_chapter_name"]} • {s["badge"]}</span>
                            </span>
                            <span class="font-mono text-xs md:text-sm font-black text-slate-400">UNIT {s["num"]} / {total_units:02d}</span>
                        </div>
                        <h2 class="text-3xl md:text-4xl font-black text-slate-900 mb-3 leading-tight tracking-tight break-keep">{s["title"]}</h2>
                        <p class="text-base md:text-lg text-slate-600 font-medium mb-8 break-keep">{s["subtitle"]}</p>
                    </div>
                    <div class="my-auto py-2">
                        {s["body"]}
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-sm text-slate-500 font-bold text-left">
                        {s["full_chapter_name"]}
                    </div>
                </article>
                ''' for idx, s in enumerate(cleaned_slides)])}
            </div>

            <!-- Bottom Progress Track -->
            <div class="no-print h-1.5 bg-slate-200/80 shrink-0">
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 5.0%;"></div>
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

            // Render Center Card in Fluid Web Mode with Official Chapter Name
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge -->
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center space-x-2.5">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider ${{slide.badge_class}} border flex items-center space-x-2 shadow-2xs">
                                <span class="scale-90">${{slide.app_icon_svg}}</span>
                                <span>${{slide.full_chapter_name}} • ${{slide.badge}}</span>
                            </span>
                        </div>
                        <span class="font-mono text-sm font-black text-slate-400">UNIT ${{slide.num}} / {total_units:02d}</span>
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
                        <span>${{slide.full_chapter_name}}</span>
                    </span>
                    <div class="flex items-center space-x-2.5">
                        <button onclick="prevSlide()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-full transition-colors text-sm">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-5 py-2 bg-slate-900 hover:bg-indigo-600 text-white font-bold rounded-full shadow-xs transition-colors text-sm">다음 ▶</button>
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
    f.write(standard_portal_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(standard_portal_html)

# Update clean readable markdown
def html_to_clean(html_str):
    html_str = re.sub(r'<blockquote>\s*<p[^>]*>(.*?)</p>\s*</blockquote>', r'\n> 💬 **[실전 Copilot 프롬프트]**\n> \1\n', html_str, flags=re.DOTALL)
    html_str = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n##### \1\n', html_str)
    clean = re.sub(r'<[^>]+>', ' ', html_str)
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n+', '\n\n', clean)
    return clean.strip()

md_lines = []
md_lines.append("# 📘 Microsoft 365 Copilot 표준 교육과정 커리큘럼")
md_lines.append("\n> **표준 4대 챕터 구성**: 실제 표준 교안에 맞추어 4개 핵심 챕터 및 학습 도구별 실무 플레이북으로 재구성된 공식 마스터 문서입니다.\n")
md_lines.append("---\n")

unit_counter = 1
for c_idx, chap in enumerate(standard_chapters):
    md_lines.append(f"## 🌐 {chap['chapter_num']}. {chap['title']}")
    md_lines.append(f"- **학습 도구/내용**: `{chap['tools']}`\n")
    
    for u_idx, u in enumerate(chap["units"]):
        num_str = f"{unit_counter:02d}"
        md_lines.append(f"### [Unit {num_str}] {u['title']}")
        md_lines.append(f"- **배지(태그)**: `{u['badge']}`")
        md_lines.append(f"- **핵심 부제**: {u['subtitle']}\n")
        
        readable_text = html_to_clean(u["body"])
        md_lines.append("#### 📋 세부 학습 내용 및 실전 프롬프트")
        md_lines.append(readable_text)
        md_lines.append("\n" + ("=" * 60) + "\n")
        unit_counter += 1

output_clean_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/curriculum_content_readable.md"
with open(output_clean_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("Successfully compiled Chapter 04 updates and rebuilt all files!")
