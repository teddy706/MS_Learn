import json
import re

loc = {}
with open("rebuild_standard_curriculum_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
standard_chapters = loc["standard_chapters"]
fluent_icons = loc["fluent_icons"]
slide_04_body = loc["slide_04_body"]

# Assign exact names & short titles
standard_chapters[0]["chapter_num"] = "01"
standard_chapters[0]["title"] = "M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI"
standard_chapters[0]["short_title"] = "01. M365 Copilot의 변화"
standard_chapters[0]["app_name"] = "Work IQ & Copilot Core"
standard_chapters[0]["tools"] = "웹 AI vs M365 Copilot, Work IQ, 멀티모달 전략, Office Agents, 엔터프라이즈 보안"

standard_chapters[1]["chapter_num"] = "02"
standard_chapters[1]["title"] = "사전 준비, Copilot 활용을 위한 업무 환경 만들기"
standard_chapters[1]["short_title"] = "02. 사전 준비 & 업무 환경"

standard_chapters[2]["chapter_num"] = "03"
standard_chapters[2]["title"] = "산더미 같은 이메일 탈출과 스마트한 일정 관리"
standard_chapters[2]["short_title"] = "03. 이메일 & 스마트 일정"

standard_chapters[3]["chapter_num"] = "04"
standard_chapters[3]["title"] = "데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북"
standard_chapters[3]["short_title"] = "04. 데이터기반 의사결정"

# Chapter 01 exact curriculum units
standard_chapters[0]["units"] = [
    {
        "num": "01",
        "badge": "AI COMPARISON",
        "title": "웹 기반 범용 AI vs M365 Copilot: 기업 업무에 최적화된 차이점",
        "subtitle": "단순 웹 챗봇의 한계를 넘어, 사내 업무 맥락(Context)과 엔터프라이즈 보안을 갖춘 AI로의 전환",
        "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
        <h4 class="font-bold text-base md:text-lg text-slate-800 mb-3 flex items-center">
            <span class="w-7 h-7 rounded-lg bg-slate-200 text-slate-700 flex items-center justify-center text-xs mr-2 font-black">WEB</span>
            웹 기반 범용 AI (ChatGPT 등)
        </h4>
        <ul class="space-y-2.5 text-sm md:text-base text-slate-600">
            <li>• <strong>업무 맥락 부재</strong>: 사내 메일, Teams 대화, 결재 문서를 전혀 알지 못함</li>
            <li>• <strong>보안 및 데이터 유출 위험</strong>: 입력 데이터가 외부 모델 재학습에 활용될 위험</li>
            <li>• <strong>수동 복사-붙여넣기</strong>: 브라우저와 오피스 프로그램 간 비효율적 단절</li>
            <li>• <strong>권한 제어 불가</strong>: 사내 보안 등급(ACL)에 따른 정보 격리 불가능</li>
        </ul>
    </div>
    <div class="p-6 bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl border border-indigo-200 shadow-xs">
        <h4 class="font-bold text-base md:text-lg text-indigo-950 mb-3 flex items-center">
            <span class="w-7 h-7 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs mr-2 font-black">M365</span>
            Microsoft 365 Copilot
        </h4>
        <ul class="space-y-2.5 text-sm md:text-base text-indigo-950 font-medium">
            <li>• <strong>Work IQ 사내 맥락 통합</strong>: 내 메일, 일정, SharePoint 문서를 즉시 연계 이해</li>
            <li>• <strong>완벽한 보안 격리</strong>: Zero-Data Retention & 외부 모델 학습 절대 미사용</li>
            <li>• <strong>앱 내 원클릭 실행</strong>: Word, Excel, Teams, Outlook 내에서 직접 생성 및 수정</li>
            <li>• <strong>Entra ID ACL 자동 준수</strong>: 내가 권한을 가진 문서에 한해서만 정확히 답변</li>
        </ul>
    </div>
</div>
<blockquote>
    <p class="text-sm md:text-base font-semibold">"웹 AI가 세상의 일반 지식을 아는 도우미라면, M365 Copilot은 '내 회사, 내 팀, 내 프로젝트의 맥락'을 가장 깊이 이해하는 전담 동료입니다."</p>
</blockquote>
"""
    },
    {
        "num": "02",
        "badge": "2026 EVOLUTION",
        "title": "2026 M365 Copilot의 변화: '작성 도우미'에서 '자율 에이전트'로",
        "subtitle": "단순한 초안 작성을 넘어 복합적인 업무 플로우를 스스로 판단하고 완수하는 차세대 패러다임",
        "body": """
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div class="text-xs font-black text-indigo-600 uppercase tracking-wider mb-1">Step 1 • Work IQ</div>
        <h4 class="font-bold text-base text-slate-900 mb-2">지능형 업무 이해</h4>
        <p class="text-sm text-slate-600 leading-relaxed">단순 키워드가 아닌 프로젝트 참여도, 담당자 관계, 회의 내용을 조합하여 의도를 정확히 파악</p>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div class="text-xs font-black text-purple-600 uppercase tracking-wider mb-1">Step 2 • Multi-modal</div>
        <h4 class="font-bold text-base text-slate-900 mb-2">멀티모달 통합 분석</h4>
        <p class="text-sm text-slate-600 leading-relaxed">텍스트뿐만 아니라 복잡한 네트워크 토폴로지 다이어그램, 아키텍처 이미지, 로그 테이블을 동시 해석</p>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div class="text-xs font-black text-emerald-600 uppercase tracking-wider mb-1">Step 3 • Office Agents</div>
        <h4 class="font-bold text-base text-slate-900 mb-2">자율형 에이전트 연계</h4>
        <p class="text-sm text-slate-600 leading-relaxed">Excel 이상치 탐지부터 Word SOP 보고서 작성, Teams 브리핑까지 전 과정을 스스로 실행</p>
    </div>
</div>
"""
    },
    {
        "num": "03",
        "badge": "WORK IQ",
        "title": "일을 더 잘 이해하게 된 핵심 엔진: Work IQ",
        "subtitle": "사내 데이터(메일, 메신저, 문서, 캘린더)를 지능형 업무 그래프로 연결하여 최적의 솔루션 제시",
        "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
        <div class="space-y-3">
            <h4 class="font-bold text-base md:text-lg text-slate-900">Work IQ가 엔지니어링 실무를 지원하는 메커니즘</h4>
            <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                Work IQ는 사용자가 지시한 한 문장에서 <strong>관련 프로젝트 ID, 최근 논의된 Teams 장애 대화 스레드, SharePoint의 장비 매뉴얼</strong>을 자율적으로 크로스 매칭하여 가장 정밀한 결과를 도출합니다.
            </p>
            <div class="flex items-center space-x-2 text-xs md:text-sm font-bold text-indigo-700 bg-indigo-50 p-2.5 rounded-xl border border-indigo-100">
                <span>⚡ 지능형 인덱싱</span>
                <span>➔ 질문 작성 중 실시간으로 가장 관련성 높은 사내 파일 추천</span>
            </div>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs space-y-2.5 font-mono text-xs md:text-sm">
            <div class="text-slate-400 font-bold">// Work IQ 업무 컨텍스트 해석 예시</div>
            <div class="text-indigo-600 font-bold">Input: "어제 발생한 코어망 이슈 보고서 써줘"</div>
            <div class="text-slate-700">1. Teams '코어망운영팀' 채널 14:20 장애 로그 스캔</div>
            <div class="text-slate-700">2. Exchange 메일함 'Cisco TAC 티켓 번호' 추출</div>
            <div class="text-emerald-700 font-bold">Output: 완전한 4단 타임라인 SOP 보고서 자동 생성</div>
        </div>
    </div>
</div>
"""
    },
    {
        "num": "04",
        "badge": "MULTIMODAL AI",
        "title": "엔지니어링 멀티모달(Multi-modal) 전략: 텍스트·도면·로그 동시 판독",
        "subtitle": "비정형 구성도 이미지와 대용량 시스로그(Syslog) 테이블을 동시에 분석하는 차세대 AI 파이프라인",
        "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs">🖼️</span>
            <span>네트워크 토폴로지 도면 분석</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3 leading-relaxed">복잡한 Visio/PNG 네트워크 구성도 이미지를 Copilot에 업로드하면 단일 장애점(SPOF)을 식별하고 이중화 개선 권고안을 즉시 제시합니다.</p>
        <div class="text-xs bg-slate-50 p-2.5 rounded-lg text-indigo-900 font-mono">"이 토폴로지 도면에서 L3 스위치 백본 이중화 링크 누락 구간을 찾아줘"</div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs">📊</span>
            <span>대용량 로그 & 수치 복합 추론</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3 leading-relaxed">Excel 및 텍스트 로그의 트래픽 급증 시간대와 장애 리포트 본문을 결합하여 복합적인 장애 인과관계를 수학적으로 검증합니다.</p>
        <div class="text-xs bg-slate-50 p-2.5 rounded-lg text-purple-900 font-mono">"CPU 점유율 90% 이상 시점과 BGP 플래핑 알람 발생의 상관계수 계산"</div>
    </div>
</div>
"""
    },
    {
        "num": "05",
        "badge": "OFFICE AGENTS",
        "title": "업무 자동화의 미래: Office Agents & 자율형 전용 에이전트",
        "subtitle": "정형화된 통신 운영 절차를 전담하여 스스로 모니터링하고 조치하는 AI 에이전트 구축",
        "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="flex items-center justify-between mb-4">
        <h4 class="font-bold text-base md:text-lg text-slate-900">Office Agents의 3대 자율 운영 영역</h4>
        <span class="px-3 py-1 bg-purple-100 text-purple-800 text-xs font-black rounded-full">Copilot Studio 연동</span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-xs font-black text-indigo-600 mb-1">01. 모니터링 에이전트</div>
            <div class="font-bold text-slate-900 text-sm mb-1">NOC 정기 브리핑</div>
            <p class="text-xs text-slate-500">매일 아침 트래픽 요약 및 주요 장애 이슈 자동 집계 후 Teams 공유</p>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-xs font-black text-purple-600 mb-1">02. 취약점 분석 에이전트</div>
            <div class="font-bold text-slate-900 text-sm mb-1">CVE 보안 권고문 대조</div>
            <p class="text-xs text-slate-500">장비 펌웨어 버전과 신규 보안 패치를 자동 비교하여 긴급 조치서 발행</p>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-xs font-black text-emerald-600 mb-1">03. SOP 작성 에이전트</div>
            <div class="font-bold text-slate-900 text-sm mb-1">표준 작업 절차서 생성</div>
            <p class="text-xs text-slate-500">엔지니어의 커맨드 로그를 표준 양식의 Word 매뉴얼로 자동 변환</p>
        </div>
    </div>
</div>
"""
    },
    {
        "num": "06",
        "badge": "ENTERPRISE SECURITY",
        "title": "\"보안을 포기하지 않고 최고의 AI를 사용한다\": M365 테넌트 보안 바운더리",
        "subtitle": "기업 데이터의 외부 유출을 원천 차단하는 Zero-Data Retention과 완벽한 권한 격리",
        "body": slide_04_body
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
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 4.34%;"></div>
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

# Also update clean readable markdown
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

print("Successfully compiled Chapter 01 updates and rebuilt all portal & markdown files!")
