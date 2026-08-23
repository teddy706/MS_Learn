import json
import re

# Fluent SVGs
fluent_icons = {
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
    "onedrive": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#0078D4"/>
        <path d="M33 22C32.4 18.5 29.5 16 26 16C23.6 16 21.5 17.2 20.2 19.2C19.6 19 18.8 18.8 18.2 18.8C15.2 18.8 12.6 21 12 24C10.2 24.8 9 26.6 9 28.8C9 31.7 11.3 34 14.2 34H33C35.8 34 38 31.8 38 29C38 26.4 36.1 24.1 33.6 23.8C33.5 23.3 33.3 22.6 33 22Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <path d="M26 16C29.5 16 32.4 18.5 33 22C33.3 22.6 33.5 23.3 33.6 23.8C36.1 24.1 38 26.4 38 29C38 31.8 35.8 34 33 34H24.5L26 16Z" fill="#0067B8" opacity="0.3"/>
    </svg>""",
    "outlook": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#0078D4"/>
        <path d="M24 13L36 21V32C36 33.1 35.1 34 34 34H14C12.9 34 12 33.1 12 32V21L24 13Z" fill="#2899F5" opacity="0.6"/>
        <path d="M12 20L24 27L36 20V17L24 24L12 17V20Z" fill="#FFFFFF"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#005A9E" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <circle cx="15" cy="23" r="3.5" stroke="#FFFFFF" stroke-width="2" fill="none"/>
    </svg>""",
    "excel": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#107C41"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#33C481" opacity="0.3"/>
        <path d="M18 17L22.5 23.5L17.5 30H21.5L24.5 25.5L27.5 30H31.5L26.5 23.5L31 17H27L24.5 21.2L22 17H18Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#0E6435" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M11.5 20L14.2 23.8L11.2 27.5H13.6L15.4 25L17.2 27.5H19.6L16.6 23.8L19.3 20H16.9L15.4 22.5L13.9 20H11.5Z" fill="#FFFFFF"/>
    </svg>""",
    "word": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#185ABD"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#2B88D8" opacity="0.3"/>
        <path d="M16 17L18.8 30H22L24.5 20.5L27 30H30.2L33 17H29.8L28.2 25.8L25.8 17H23.2L20.8 25.8L19.2 17H16Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#106EBE" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M11 20L12.8 27H14.8L16.2 21.8L17.6 27H19.6L21.4 20H19.6L18.5 24.8L17.1 20H15.3L13.9 24.8L12.8 20H11Z" fill="#FFFFFF"/>
    </svg>""",
    "powerpoint": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#C43E1C"/>
        <path d="M14 11H34C35.7 11 37 12.3 37 14V34C37 35.7 35.7 37 34 37H14C12.3 37 11 35.7 11 34V14C11 12.3 12.3 11 14 11Z" fill="#EA580C" opacity="0.3"/>
        <path d="M19 17H26.5C29 17 31 18.6 31 21C31 23.4 29 25 26.5 25H22.5V30H19V17ZM22.5 22.2H26.2C27.3 22.2 28.1 21.7 28.1 21C28.1 20.3 27.3 19.8 26.2 19.8H22.5V22.2Z" fill="#FFFFFF" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#A43214" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M12.5 20H16.5C17.8 20 18.8 20.8 18.8 22C18.8 23.2 17.8 24 16.5 24H14.5V27H12.5V20ZM14.5 22.5H16.2C16.8 22.5 17.2 22.3 17.2 22C17.2 21.7 16.8 21.5 16.2 21.5H14.5V22.5Z" fill="#FFFFFF"/>
    </svg>""",
    "teams": """<svg class="w-7 h-7 inline-block shrink-0" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="10" fill="#464EB8"/>
        <circle cx="33" cy="17" r="4.5" fill="#7B83EB"/>
        <path d="M38.5 23H32.5C30.6 23 29.5 24 29 25.2C31.5 26.2 33 28.5 33 31.5V35H39C40.1 35 41 34.1 41 33V25.5C41 24.1 39.9 23 38.5 23Z" fill="#7B83EB"/>
        <circle cx="21" cy="18" r="6" fill="#FFFFFF"/>
        <path d="M29 27C29 24.8 27.2 23 25 23H17C14.8 23 13 24.8 13 27V34C13 35.1 13.9 36 15 36H27C28.1 36 29 35.1 29 34V27Z" fill="#FFFFFF"/>
        <rect x="7" y="15" width="16" height="16" rx="4" fill="#505AC9" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
        <path d="M12 20H18M15 20V27" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
    </svg>"""
}

# Slide 04 Tenant Architecture Body
slide_04_body = f"""
<div class="p-6 md:p-8 bg-white/95 rounded-3xl border border-slate-200 shadow-sm w-full max-w-5xl mx-auto text-left my-2">
    <div class="grid grid-cols-12 gap-6 items-start">
        
        <!-- Left Column: Users & Apps -->
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
                    <div class="flex items-center space-x-2 p-2 bg-sky-50/80 rounded-lg text-sm font-bold text-sky-900 border border-sky-100">{fluent_icons['onedrive']} <span>OneDrive</span></div>
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
                                    <div class="font-bold text-slate-800 text-sm">OneDrive & SharePoint</div>
                                    <div class="text-xs text-slate-500">files & team sites</div>
                                </div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center space-x-3 shadow-2xs">
                                {fluent_icons['teams']}
                                <div>
                                    <div class="font-bold text-slate-800 text-sm">Teams & BizChat</div>
                                    <div class="text-xs text-slate-500">chats & meetings</div>
                                </div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center space-x-3 shadow-2xs">
                                <span class="w-7 h-7 rounded-lg bg-teal-600 text-white flex items-center justify-center text-sm font-bold">🛡️</span>
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

# Load original 33 slides content from generate_m365_portal.py
orig_loc = {}
with open("generate_m365_portal.py", "r", encoding="utf-8") as f:
    exec(f.read(), orig_loc)
orig_modules = orig_loc["modules"]

# Flatten all original slides into a dictionary by title/topic for perfect preservation
orig_slides_map = {}
for m in orig_modules:
    for s in m["slides"]:
        clean_title = s["title"].replace("<br>", " ").strip()
        orig_slides_map[clean_title] = s

# Comprehensive Integrated 4-Chapter Master Curriculum
master_chapters = [
    {
        "chapter_num": "01",
        "title": "M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI",
        "short_title": "01. M365 Copilot의 변화",
        "app_name": "Work IQ & Copilot Core",
        "icon_svg": fluent_icons["copilot"],
        "badge_class": "bg-indigo-50 text-indigo-900 border-indigo-200",
        "tools": "웹 AI vs M365 Copilot, Work IQ, 멀티모달 전략, Office Agents, Copilot Work, 엔터프라이즈 보안",
        "units": [
            {
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
                "badge": "PARADIGM SHIFT",
                "title": "2026 통신 네트워크 패러다임: '작성 도우미'에서 '자율 에이전트'로",
                "subtitle": "단순 문서 작성을 넘어 네트워크 장애 분석 및 조치 명령을 직접 수행하는 Autonomous AI로의 진화",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
        <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3 flex items-center">
            <span class="w-7 h-7 rounded-lg bg-red-100 text-red-600 flex items-center justify-center text-xs mr-2 font-black">OLD</span>
            Gen 1: 어시스턴트 모드
        </h4>
        <ul class="space-y-2 text-sm md:text-base text-slate-600">
            <li>• 사람이 지시한 단일 텍스트 요약 및 초안 작성에 국한</li>
            <li>• 실시간 네트워크 상태 모니터링 및 자율적 연계 불가</li>
            <li>• 파일 복사 및 수동 프롬프트 입력에 과도한 시간 소모</li>
        </ul>
    </div>
    <div class="p-6 bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl border border-indigo-200">
        <h4 class="font-bold text-base md:text-lg text-indigo-900 mb-3 flex items-center">
            <span class="w-7 h-7 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs mr-2 font-black">2026</span>
            Gen 2: Work IQ 자율 에이전트
        </h4>
        <ul class="space-y-2 text-sm md:text-base text-indigo-950 font-medium">
            <li>• <strong>Work IQ 기반 자율 추론</strong>: 사내 메일, Teams 대화, 구성도 크로스 분석</li>
            <li>• <strong>멀티모달 통합 진단</strong>: 시스로그와 실시간 토폴로지 동시 판독</li>
            <li>• <strong>Office Agents 연동</strong>: Excel KPI 분석 후 Word SOP 초안 자동 작성</li>
        </ul>
    </div>
</div>
<blockquote>
    <p class="text-sm md:text-base font-medium">"2026 M365 Copilot의 핵심은 지시를 기다리는 AI가 아니라, Work IQ를 바탕으로 업무 맥락을 선제적으로 이해하고 솔루션 간 작업을 연결하는 오케스트레이터입니다."</p>
</blockquote>
"""
            },
            {
                "badge": "MODEL ARCHITECTURE",
                "title": "3대 차세대 AI 모델 전략적 선택 가이드",
                "subtitle": "GPT-5.6, Claude Sonnet 5, Work IQ 엔진의 엔지니어링 최적 조합",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div class="text-xs font-black text-indigo-600 uppercase tracking-wider mb-1">GPT-5.6 Advanced</div>
        <h4 class="font-bold text-base text-slate-900 mb-2">복합 논리 & 수학적 추론</h4>
        <p class="text-sm text-slate-600 leading-relaxed mb-3">5G 기지국 CAPEX 회수율 계산, Z-Score 이상 트래픽 통계 분석 및 대규모 분산 계산</p>
        <span class="px-2.5 py-0.5 bg-indigo-50 text-indigo-700 text-xs font-bold rounded-full border border-indigo-100">Excel / Python 연동</span>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div class="text-xs font-black text-purple-600 uppercase tracking-wider mb-1">Claude Sonnet 5</div>
        <h4 class="font-bold text-base text-slate-900 mb-2">초정밀 코딩 & 표준 문서</h4>
        <p class="text-sm text-slate-600 leading-relaxed mb-3">BGP 라우팅 구성 스크립트 작성, RFC 표준 준수 보고서 및 글로벌 기술 제안서</p>
        <span class="px-2.5 py-0.5 bg-purple-50 text-purple-700 text-xs font-bold rounded-full border border-purple-100">Word / SOP 작성</span>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <div class="text-xs font-black text-emerald-600 uppercase tracking-wider mb-1">Work IQ & Small LLM</div>
        <h4 class="font-bold text-base text-slate-900 mb-2">초저지연 사내 지식 인덱싱</h4>
        <p class="text-sm text-slate-600 leading-relaxed mb-3">SharePoint/OneDrive 파일 검색, 보안 ACL 권한 검증 및 실시간 사내 커뮤니케이션 조율</p>
        <span class="px-2.5 py-0.5 bg-emerald-50 text-emerald-700 text-xs font-bold rounded-full border border-emerald-100">BizChat / Teams</span>
    </div>
</div>
"""
            },
            {
                "badge": "WORK IQ ENGINE",
                "title": "사내 데이터 자산화 엔진: Work IQ & Entra ID ACL 인덱싱",
                "subtitle": "흩어져 있는 사내 지식(메일, 채팅, 문서, 회의록)을 지능형 업무 그래프로 연결",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
        <div class="space-y-3">
            <h4 class="font-bold text-base md:text-lg text-slate-900">Work IQ가 엔지니어링 실무를 이해하는 방식</h4>
            <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                단순 키워드 매칭이 아닌, <strong>엔지니어의 프로젝트 참여 이력, 최근 검토한 네트워크 구성도, Teams 장애 대화 스레드</strong>의 맥락을 결합하여 가장 정확한 답변을 도출합니다.
            </p>
            <div class="flex items-center space-x-2 text-xs md:text-sm font-bold text-indigo-700 bg-indigo-50 p-2.5 rounded-xl">
                <span>🔒 Entra ID ACL 검증</span>
                <span>➔ 사용자 권한이 없는 문서는 AI 결과에 절대 미포함</span>
            </div>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs space-y-2.5 font-mono text-xs md:text-sm">
            <div class="text-slate-400 font-bold">// Work IQ 지식 추출 파이프라인</div>
            <div class="text-indigo-600">1. User Query: "지난달 코어망 점검 이슈 요약해줘"</div>
            <div class="text-emerald-700">2. Graph Scan: Exchange 메일 + Teams 채널 + SharePoint SOP</div>
            <div class="text-slate-800">3. Contextual Synthesis: 시간순 장애 타임라인 자동 생성</div>
        </div>
    </div>
</div>
"""
            },
            {
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
                "badge": "COPILOT WORK",
                "title": "Copilot Work (BizChat): 실시간 크로스-앱 통합 워크스페이스",
                "subtitle": "M365 앱 전체를 관통하는 중앙 커맨드 센터 활용법",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">통신망 긴급 장애 시 BizChat 프롬프트 실전 예시</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "/teams '코어망운영팀' 채널에서 오늘 오전 9시 이후 논의된 '백본 BGP 플래핑' 관련 대화와, /files '2026_코어망_토폴로지.docx'를 대조해서 발생 원인과 현재 조치 현황을 3줄 요약하고, 담당 엔지니어에게 보낼 회신 메일 초안을 작성해줘."
        </p>
    </blockquote>
    <div class="mt-4 flex flex-wrap gap-2 text-xs font-bold text-slate-600">
        <span class="px-3 py-1 bg-white rounded-full border border-slate-200 shadow-2xs">📎 /files (SharePoint 문서 참조)</span>
        <span class="px-3 py-1 bg-white rounded-full border border-slate-200 shadow-2xs">💬 /teams (채널 대화 검색)</span>
        <span class="px-3 py-1 bg-white rounded-full border border-slate-200 shadow-2xs">✉️ /mail (메일 스레드 통합)</span>
    </div>
</div>
"""
            },
            {
                "badge": "ENTERPRISE SECURITY",
                "title": "\"보안을 포기하지 않고 최고의 AI를 사용한다\": M365 테넌트 보안 바운더리",
                "subtitle": "기업 데이터의 외부 유출을 원천 차단하는 Zero-Data Retention과 완벽한 권한 격리",
                "body": slide_04_body
            }
        ]
    },
    {
        "chapter_num": "02",
        "title": "사전 준비, Copilot 활용을 위한 업무 환경 만들기",
        "short_title": "02. 사전 준비 & 업무 환경",
        "app_name": "OneDrive, SharePoint & Teams",
        "icon_svg": fluent_icons["onedrive"],
        "badge_class": "bg-sky-50 text-sky-950 border-sky-200",
        "tools": "문서 중앙화, OneDrive, SharePoint, Teams, 클라우드 환경 세팅",
        "units": [
            {
                "badge": "PREPARATION & SETUP",
                "title": "왜 Copilot은 내 로컬 C드라이브를 읽지 못하는가? - 문서 중앙화의 필요성",
                "subtitle": "Copilot의 성능을 100% 이끌어내기 위한 필수 선결 과제: 파편화된 로컬 문서를 클라우드로 통합",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-6 bg-red-50/70 rounded-2xl border border-red-200">
        <h4 class="font-bold text-base md:text-lg text-red-900 mb-3 flex items-center">
            <span class="w-7 h-7 rounded-lg bg-red-200 text-red-700 flex items-center justify-center text-xs mr-2 font-black">LOCAL</span>
            로컬 PC 파편화의 한계
        </h4>
        <ul class="space-y-2.5 text-sm md:text-base text-red-800">
            <li>• <strong>Copilot 인덱싱 불가</strong>: 내 PC 바탕화면, 다운로드 폴더의 파일은 AI가 접근 못함</li>
            <li>• <strong>팀원 간 지식 고립</strong>: 담당자가 부재중일 때 네트워크 설정 파일 및 SOP 조회 불가</li>
            <li>• <strong>버전 충돌 발생</strong>: `최종_수정_진짜최종.xlsx` 등 파일 중복 및 버전 혼선</li>
        </ul>
    </div>
    <div class="p-6 bg-emerald-50/70 rounded-2xl border border-emerald-200 shadow-xs">
        <h4 class="font-bold text-base md:text-lg text-emerald-950 mb-3 flex items-center">
            <span class="w-7 h-7 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs mr-2 font-black">CLOUD</span>
            M365 클라우드 문서 중앙화
        </h4>
        <ul class="space-y-2.5 text-sm md:text-base text-emerald-950 font-medium">
            <li>• <strong>Microsoft Graph 실시간 인덱싱</strong>: 업로드 즉시 Copilot이 사내 지식으로 인식</li>
            <li>• <strong>3대 중앙화 축 구축</strong>: OneDrive(개인), SharePoint(부서), Teams(프로젝트)</li>
            <li>• <strong>자동 버전 이력 관리</strong>: 실수로 덮어써도 이전 시점으로 1초 복원</li>
        </ul>
    </div>
</div>
<blockquote>
    <p class="text-sm md:text-base font-semibold">"Copilot 도입의 첫 단추는 AI 모델을 고르는 것이 아니라, 사내 데이터가 AI가 읽을 수 있는 클라우드(OneDrive/SharePoint)에 중앙화되어 있는가입니다."</p>
</blockquote>
"""
            },
            {
                "badge": "ONEDRIVE CENTRAL",
                "title": "[개인 업무 중앙화] OneDrive: 내 작업 문서의 클라우드 자산화",
                "subtitle": "개인 분석 데이터, 임시 메모, 일일 업무 로그를 Copilot이 즉시 참조할 수 있도록 세팅",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="flex items-center justify-between mb-4">
        <h4 class="font-bold text-base md:text-lg text-slate-900">OneDrive 환경 세팅 핵심 3단계</h4>
        <span class="px-3 py-1 bg-sky-100 text-sky-900 text-xs font-black rounded-full">Personal Workspace</span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-xs font-black text-sky-700 mb-1">Step 1. PC 폴더 백업 동기화</div>
            <div class="font-bold text-slate-900 text-sm mb-1">바탕화면·문서 폴더 자동 연결</div>
            <p class="text-xs text-slate-500">내 컴퓨터의 바탕화면과 문서 폴더를 OneDrive에 자동 동기화하여 저장과 동시에 인덱싱</p>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-xs font-black text-indigo-700 mb-1">Step 2. 구조화된 폴더 트리</div>
            <div class="font-bold text-slate-900 text-sm mb-1">명확한 명명 규칙 적용</div>
            <p class="text-xs text-slate-500">`[연도]_[프로젝트명]_[문서종류]` 표준 규칙으로 파일명을 정리하여 Copilot 검색 정확도 극대화</p>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-xs font-black text-emerald-700 mb-1">Step 3. 실시간 자동 저장 활성화</div>
            <div class="font-bold text-slate-900 text-sm mb-1">AutoSave On 설정</div>
            <p class="text-xs text-slate-500">Office 앱 상단의 '자동 저장'을 켜서 작성 중인 모든 수정 사항이 즉시 Copilot 그래프에 동기화</p>
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "SHAREPOINT HUB",
                "title": "[부서 지식 중앙화] SharePoint: 팀 표준 가이드 및 지식 베이스(KB) 통합",
                "subtitle": "장비 설정 표준(Config), 망 구성도, 과거 장애 이력을 하나의 지능형 팀 허브로 일원화",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">SharePoint 지식 베이스가 Copilot과 결합할 때의 효과</h4>
    <p class="text-sm md:text-base text-slate-600 leading-relaxed mb-4">
        신규 엔지니어가 입사하거나 긴급 야간 장애가 발생했을 때, 선임자에게 묻지 않고도 Copilot에게 질문하면 <strong>SharePoint에 축적된 부서 공용 매뉴얼과 과거 장애 보고서</strong>를 기반으로 3초 만에 검증된 해법을 답변합니다.
    </p>
    <div class="grid grid-cols-3 gap-3 text-center text-xs md:text-sm font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">📁 라우터/스위치 Config 표준 라이브러리</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">📋 통신사 간 상호연동 인터페이스 가이드</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">🛡️ 비상 장애 대응 표준 작업 절차서(SOP)</div>
    </div>
</div>
"""
            },
            {
                "badge": "TEAMS COLLABORATION",
                "title": "[협업 채널 중앙화] Teams: 프로젝트별 실시간 커뮤니케이션 & 파일 연계",
                "subtitle": "채팅, 회의 녹화본, 채널 공유 파일이 Copilot을 통해 하나의 유기적 컨텍스트로 융합",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="flex items-center justify-between mb-4">
        <h4 class="font-bold text-base md:text-lg text-slate-900">Teams 채널 기반 협업 세팅</h4>
        <span class="px-3 py-1 bg-indigo-100 text-indigo-900 text-xs font-black rounded-full">Channel Workspace</span>
    </div>
    <div class="space-y-3 text-sm">
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 flex items-center justify-between shadow-2xs">
            <div>
                <strong class="text-slate-900">1. 채널별 파일 탭 활용</strong>
                <p class="text-xs text-slate-500 mt-0.5">이메일 첨부파일 대신 Teams 채널 '파일' 탭에 저장 ➔ SharePoint와 자동 연동되어 팀 전체 인덱싱</p>
            </div>
            <span class="text-xs text-indigo-600 font-bold">협업 중앙화</span>
        </div>
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 flex items-center justify-between shadow-2xs">
            <div>
                <strong class="text-slate-900">2. 회의 녹음 및 스크립트(Transcript) 활성화</strong>
                <p class="text-xs text-slate-500 mt-0.5">장애 대책 회의 시 '녹음 및 대화 기록'을 켜두면, 회의 직후 Copilot이 논의된 액션 아이템 자동 정리</p>
            </div>
            <span class="text-xs text-purple-600 font-bold">음성 지식 자산화</span>
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "SECURITY GOVERNANCE",
                "title": "[보안 & 거버넌스] Entra ID ACL 및 Purview 권한 기반 안전한 중앙화",
                "subtitle": "중앙화된 사내 문서 중 비인가자나 타 부서에 기밀이 노출되지 않도록 완벽 통제",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">권한 없는 정보는 AI 답변에서도 100% 제외</h4>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <span class="text-xs font-black text-indigo-600">Entra ID (ACL 권한 제어)</span>
            <div class="font-bold text-slate-900 mt-1">사용자의 읽기 권한을 그대로 계승</div>
            <p class="text-xs text-slate-500 mt-1">SharePoint 특정 폴더에 권한이 없는 직원이 Copilot에게 질문해도 해당 문서 내용은 검색 결과에 절대 나타나지 않음</p>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <span class="text-xs font-black text-purple-600">Microsoft Purview (민감도 레이블)</span>
            <div class="font-bold text-slate-900 mt-1">자동 암호화 및 외부 유출 방지</div>
            <p class="text-xs text-slate-500 mt-1">[대외비] 레이블이 지정된 문서를 Copilot이 요약할 때도 원본의 보안 등급과 암호화가 그대로 유지됨</p>
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "ENV PIPELINE",
                "title": "분산된 네트워크 구성도 및 장비 백업 파일의 SharePoint 자동 인덱싱 파이프라인",
                "subtitle": "주기적으로 업데이트되는 장비 백업 파일의 자동 인덱싱 구축 파이프라인",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">자동화된 지식 축적 파이프라인</h4>
    <div class="flex items-center space-x-2 text-xs md:text-sm font-bold text-slate-700 overflow-x-auto py-2">
        <span class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">1. TFTP/FTP 장비 백업</span>
        <span>➔</span>
        <span class="p-3 bg-indigo-50 text-indigo-900 rounded-xl border border-indigo-200 shadow-2xs">2. Power Automate OneDrive 동기화</span>
        <span>➔</span>
        <span class="p-3 bg-emerald-50 text-emerald-900 rounded-xl border border-emerald-200 shadow-2xs">3. Microsoft Graph 자동 인덱싱</span>
        <span>➔</span>
        <span class="p-3 bg-slate-900 text-white rounded-xl shadow-2xs">4. Copilot 즉시 답변 가능</span>
    </div>
</div>
"""
            }
        ]
    },
    {
        "chapter_num": "03",
        "title": "산더미 같은 이메일 탈출과 스마트한 일정 관리",
        "short_title": "03. 이메일 & 스마트 일정",
        "app_name": "Prompt Coach, Outlook & Teams",
        "icon_svg": fluent_icons["outlook"],
        "badge_class": "bg-blue-50 text-blue-950 border-blue-200",
        "tools": "좋은 프롬프트, Prompt Coach, 메일 요약, 핵심 분류, 스마트 회의, 예약 프롬프트, Teams 회의 요약, Copilot 패널",
        "units": [
            {
                "badge": "PROMPT COACH",
                "title": "좋은 프롬프트의 조건과 Prompt Coach 에이전트를 통한 프롬프트 교정",
                "subtitle": "목표(Goal), 맥락(Context), 출처(Source), 기대형식(Expectation) 4대 요소와 AI 코칭",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-3 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs">🎯</span>
            <span>좋은 프롬프트의 4대 핵심 구조</span>
        </h4>
        <div class="space-y-2 text-xs md:text-sm">
            <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-indigo-600">1. Goal (목표)</strong>: "무엇을 만들어야 하는가?" (예: 회신 메일 초안 작성)
            </div>
            <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-purple-600">2. Context (맥락)</strong>: "어떤 상황인가?" (예: BGP 세션 순단 발생 상황)
            </div>
            <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-blue-600">3. Source (출처)</strong>: "어떤 데이터를 참조할 것인가?" (예: /files '장애로그.xlsx')
            </div>
            <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-emerald-600">4. Expectation (기대형식)</strong>: "어조와 형태는?" (예: 공손한 톤, 타임라인 표)
            </div>
        </div>
    </div>
    <div class="p-5 bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl border border-indigo-200 shadow-xs">
        <h4 class="font-bold text-base text-indigo-950 mb-3 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs">✨</span>
            <span>Prompt Coach 에이전트 실전 코칭</span>
        </h4>
        <p class="text-xs md:text-sm text-indigo-950 leading-relaxed mb-3 font-medium">
            프롬프트를 보내기 전, Prompt Coach에게 검토를 요청하면 누락된 맥락과 모호한 지시를 스스로 찾아내어 <strong>성공 확률 100%의 고품질 프롬프트로 업그레이드</strong>해 줍니다.
        </p>
        <div class="text-xs bg-white p-3 rounded-xl border border-indigo-200 text-slate-700 font-mono">
            "내 프롬프트에서 엔지니어링 용어와 참조 출처가 부족한 부분을 Prompt Coach 원칙에 맞게 보완해줘."
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "OUTLOOK MASTERY",
                "title": "[Outlook 실전 1] 긴급 장애 메일 3초 요약 & 핵심 분류 및 맥락 검색",
                "subtitle": "수십 통이 얽힌 스레드 타임라인 요약과 수천 통의 편지함에서 원하는 기술 메일 즉시 추출",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
        <div class="space-y-3">
            <h4 class="font-bold text-base md:text-lg text-slate-900">1. 스레드 3초 요약 (By Copilot)</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
                출근 직후나 장애 발생 시 30통이 넘는 답장 메일을 일일이 읽지 않아도, 상단의 <strong>[Copilot으로 요약]</strong> 버튼 한 번으로 핵심 사건과 미완료 액션 아이템을 표로 요약합니다.
            </p>
            <div class="text-xs bg-white p-2.5 rounded-xl border border-slate-200 text-indigo-900 font-mono">
                "최초 장애 알람 발생 시각, 담당자별 조치 내역, 미해결 이슈를 타임라인 표로 정리해줘"
            </div>
        </div>
        <div class="space-y-3">
            <h4 class="font-bold text-base md:text-lg text-slate-900">2. 핵심 분류 & 맥락 검색</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
                단순 단어 검색이 아닌, 자연어 맥락 검색으로 지난 6개월간 Cisco TAC 엔지니어와 주고받은 펌웨어 버그 관련 메일만 정확히 필터링합니다.
            </p>
            <div class="text-xs bg-white p-2.5 rounded-xl border border-slate-200 text-purple-900 font-mono">
                "지난 분기 코어 라우터 OS 버그 패치와 관련해 벤더사에서 보낸 권고 메일을 찾아줘"
            </div>
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "GLOBAL TAC",
                "title": "[Outlook 실전 2] 글로벌 통신 벤더(Cisco/Nokia) 기술 지원 요청 및 영어 메일 정밀 작성",
                "subtitle": "정확한 영문 기술 용어와 로그 첨부를 반영한 고품질 TAC 케이스 오픈 메일 생성",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">글로벌 TAC 지원 요청 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "현재 발생한 OSPF LSA 플러딩 및 패킷 드롭 현상에 대해 Cisco TAC 엔지니어에게 Severity-2 티켓을 요청하는 정중하고 전문적인 영문 메일을 작성해줘. 발생 일시, 장비 모델(ASR 9000), IOS-XR 버전, 첨부한 Show tech-support 로그를 포함해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "badge": "SMART SCHEDULING",
                "title": "[Outlook 실전 3] 스마트 회의 잡기 & 정기 작업 공지 예약 프롬프트",
                "subtitle": "참석자 캘린더 빈 시간 자동 탐색 및 특정 시간대 자동 발송 예약 프롬프트",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs">📅</span>
            <span>스마트 회의 잡기 (Smart Scheduling)</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3 leading-relaxed">
            전송망팀, 코어운영팀 팀장님들의 일정을 수동으로 대조할 필요 없이, 공통 비는 시간을 AI가 찾아 회의 제목, 안건, Teams 링크가 포함된 초대를 자동 생성합니다.
        </p>
        <div class="text-xs bg-slate-50 p-2.5 rounded-lg text-blue-900 font-mono">
            "이번 주 금요일 오후 전송망팀과 무선팀 팀장님들이 모두 가능한 30분 미팅을 잡아줘"
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs">⏰</span>
            <span>예약 프롬프트 (Scheduled Prompts)</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3 leading-relaxed">
            새벽 야간 작업 공지나 정기 점검 알림 메일을 특정 시간(예: D-1일 18:00)에 자동으로 작성하고 발송 대기 상태로 예약할 수 있습니다.
        </p>
        <div class="text-xs bg-slate-50 p-2.5 rounded-lg text-indigo-900 font-mono">
            "내일 새벽 02:00 작업 영향도 안내 메일을 오늘 17:30에 발송되도록 예약해줘"
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "TEAMS RECAP & PANEL",
                "title": "[Teams & 패널 실전] Teams 회의 요약하기 & Copilot 사이드 패널 활용",
                "subtitle": "회의 직후 자동 생성되는 지능형 Recap과 앱 우측 사이드 패널을 통한 실시간 초안 튜닝",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
        <div class="space-y-3">
            <h4 class="font-bold text-base md:text-lg text-slate-900">1. Teams 회의 요약하기 (Meeting Recap)</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
                1시간 동안 진행된 장애 대책 회의가 끝나면, Copilot이 전체 음성 대화를 분석하여 <strong>결정된 사항(Decisions)과 담당자별 할 일(Action Items)</strong>을 5줄로 자동 정리합니다.
            </p>
            <div class="text-xs bg-white p-2.5 rounded-xl border border-slate-200 text-indigo-900 font-mono">
                "이 회의에서 김엔지니어와 박팀장이 합의한 롤백 기준과 일정을 요약해줘"
            </div>
        </div>
        <div class="space-y-3">
            <h4 class="font-bold text-base md:text-lg text-slate-900">2. Copilot 패널 기능 (Side Panel)</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
                Outlook 및 Teams 우측의 <strong>[Copilot 패널]</strong>을 열어 대화하듯 메일 초안의 어조를 정중하게 바꾸거나, 분량을 조절하고, 사내 규정을 실시간으로 질의할 수 있습니다.
            </p>
            <div class="text-xs bg-white p-2.5 rounded-xl border border-slate-200 text-purple-900 font-mono">
                "작성된 회신 메일을 조금 더 격식 있는 비즈니스 어조로 수정하고 길이 줄여줘"
            </div>
        </div>
    </div>
</div>
"""
            }
        ]
    },
    {
        "chapter_num": "04",
        "title": "데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북",
        "short_title": "04. 데이터기반 의사결정",
        "app_name": "Excel, Word, PPT 에이전트",
        "icon_svg": fluent_icons["excel"],
        "badge_class": "bg-emerald-50 text-emerald-950 border-emerald-200",
        "tools": "데이터 정제+시각화, 심층 추론+시뮬레이션, 다중 소스 합성, 의사결정 슬라이드, 종합 플레이북",
        "units": [
            # Hands-on 1: Excel Data Cleaning & Visualization
            {
                "badge": "HANDS-ON 1 • CLEANING",
                "title": "[핸즈온 1-1] 엑셀 데이터 정제 + 시각화: 대용량 KPI 로그 전처리 및 파생 열 생성",
                "subtitle": "비정형 로그 정제, 결측치 보정, 다중 조건부 서식과 상태 분류 자동화",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="flex items-center justify-between mb-4">
        <h4 class="font-bold text-base md:text-lg text-slate-900">핸즈온 실습 1단계: 데이터 정제 & 파생 열 워크플로우</h4>
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
    </div>
</div>
"""
            },
            {
                "badge": "HANDS-ON 1 • VISUALIZATION",
                "title": "[핸즈온 1-2] Excel Copilot: 5G 기지국 KPI 대용량 수식 계산 및 피벗 차트 자동화",
                "subtitle": "복잡한 엑셀 수식 작성 없이 자연어로 기지국별 시간대별 트래픽 피벗 차트 구축",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">Excel Copilot 피벗 차트 자동화 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "'PRB_Usage' 컬럼이 85% 이상이면서 'Drop_Rate'가 1.5%를 초과하는 과부하 기지국만 필터링하는 새 열을 추가하고, 기지국 ID별 시간대별 트래픽 추이를 피벗 차트로 생성해줘."
        </p>
    </blockquote>
</div>
"""
            },
            # Hands-on 2: Deep Reasoning & What-If Simulation
            {
                "badge": "HANDS-ON 2 • REASONING",
                "title": "[핸즈온 2-1] 심층 추론: 네트워크 트래픽 이상 감지 및 Z-Score 기반 분산 분석",
                "subtitle": "통계적 이상치를 자동으로 색출하여 잠재적 DDoS 및 백홀 병목 원인 규명",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">이상치 탐지 & 원인 추론 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "최근 30일간의 백홀 트래픽 데이터를 바탕으로 Z-Score가 +2.5 이상인 이상 트래픽 발생 구간을 빨간색 조건부 서식으로 강조하고, 사용자 접속자 수(UE) 급증과의 상관관계를 분석해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "badge": "HANDS-ON 2 • SIMULATION",
                "title": "[핸즈온 2-2] What-If 시뮬레이션 & Python in Excel: 상관계수 히트맵 및 증설 예측",
                "subtitle": "파이썬 Seaborn 라이브러리 구동 및 대역폭 증설 시나리오별 패킷 지연율 시뮬레이션",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <h5 class="font-bold text-slate-900 text-sm mb-1">Python in Excel 시각화</h5>
            <p class="text-xs text-slate-600">"기지국 접속자 수, 패킷 지연 시간(RTT), 다운로드 처리량 간의 상관관계를 파이썬 seaborn heatmap으로 시각화하여 현재 시트의 G2 셀에 삽입해줘."</p>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <h5 class="font-bold text-slate-900 text-sm mb-1">What-If 증설 시뮬레이션</h5>
            <p class="text-xs text-slate-600">"백홀 대역폭을 10Gbps에서 20Gbps로 확장 시 피크타임 패킷 지연이 몇 % 개선되는지 파라미터 변동 모델링을 실행해줘."</p>
        </div>
    </div>
</div>
"""
            },
            # Hands-on 3: Word Multi-Source Synthesis
            {
                "badge": "HANDS-ON 3 • SYNTHESIS",
                "title": "[핸즈온 3-1] 워드 다중 소스 합성: 엑셀·매뉴얼·회의록을 결합한 통합 SOP 작성",
                "subtitle": "분산된 사내 파일(`/files`)들을 교차 인용하여 공공·기업 표준 규격의 기술 보고서로 원클릭 완성",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">다중 소스(Multi-Source) 크로스 합성 실전 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "/files '5G_KPI_분석결과.xlsx'의 3번 시트 통계 테이블과, /files 'L3스위치_표준매뉴얼.docx', 그리고 지난 Teams 대책 회의록을 종합하여 '수도권 코어망 긴급 증설 및 장애 대응 표준 작업 절차서(SOP)'를 작성해줘. 목적, 장비 체크리스트, 단계별 명령어, 롤백 가이드를 포함한 정형화된 서식으로 완성해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "badge": "HANDS-ON 3 • CAPEX",
                "title": "[핸즈온 3-2] 정량적 통신 설비 투자(CAPEX/OPEX) 분석 및 제안서 작성",
                "subtitle": "장비 도입 비용 및 유지보수 절감 효과를 수치 기반으로 설득하는 비즈니스 문서화",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">설비 투자 제안 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "/files '2026_장비견적서.xlsx'의 데이터를 인용하여 노후 라우터 교체 시 향후 3년간 전력 소비량 및 유지보수 비용 절감액(OPEX -18%)을 강조한 경영진 제출용 설비투자 기안서를 작성해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "badge": "HANDS-ON 3 • TOPOLOGY",
                "title": "[핸즈온 3-3] Mermaid 다이어그램을 통한 5G SA 코어 네트워크 토폴로지 시각화",
                "subtitle": "복잡한 네트워크 흐름을 프롬프트만으로 깔끔한 구조도로 즉시 렌더링",
                "body": """
<div class="p-6 bg-white rounded-2xl border border-slate-200 text-left my-2 shadow-sm">
    <div class="mermaid text-center">
    graph LR
        UE["📱 5G 단말 (UE)"] --> gNB["📡 5G 기지국 (gNodeB)"]
        gNB --> UPF["⚡ 사용자 평면 (UPF)"]
        gNB --> AMF["🛡️ 접속제어 (AMF)"]
        AMF --> SMF["⚙️ 세션관리 (SMF)"]
        UPF --> DN["🌐 데이터 네트워크 (인터넷 / 사내망)"]
    </div>
</div>
"""
            },
            # Hands-on 4: PowerPoint Executive Decision
            {
                "badge": "HANDS-ON 4 • PPT",
                "title": "[핸즈온 4-1] PPT 의사결정 슬라이드: Word 보고서 기반 임원 보고용 프레젠테이션 자동 생성",
                "subtitle": "수십 페이지의 기술 보고서를 핵심 4대 슬라이드로 즉시 변환",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">PowerPoint 슬라이드 생성 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "/files '2026_통신망_현대화_보고서.docx' 파일로부터 프레젠테이션을 생성해줘. 임원 보고에 적합하도록 장황한 글을 줄이고, 핵심 성과 지표(KPI)와 타임라인을 시각적 카드로 구성해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "badge": "HANDS-ON 4 • ROI",
                "title": "[핸즈온 4-2] 경영진 의사결정을 위한 1-Page 네트워크 ROI 서머리 슬라이드 디자인",
                "subtitle": "비전문가 임원도 5초 만에 이해하는 시각적 헤드라인 및 데이터 하이라이트",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-2 text-center">
    <div class="p-5 bg-blue-50 rounded-2xl border border-blue-200">
        <div class="text-3xl font-black text-blue-700">99.999%</div>
        <div class="text-sm font-bold text-slate-800 mt-1">연간 가용성 보장</div>
        <div class="text-xs text-slate-500 mt-1">Downtime 5분 미만</div>
    </div>
    <div class="p-5 bg-emerald-50 rounded-2xl border border-emerald-200">
        <div class="text-3xl font-black text-emerald-700">-35%</div>
        <div class="text-sm font-bold text-slate-800 mt-1">장애 조치 시간 (MTTR)</div>
        <div class="text-xs text-slate-500 mt-1">AI 자동 진단 연계</div>
    </div>
    <div class="p-5 bg-purple-50 rounded-2xl border border-purple-200">
        <div class="text-3xl font-black text-purple-700">₩4.2억</div>
        <div class="text-sm font-bold text-slate-800 mt-1">연간 OPEX 절감</div>
        <div class="text-xs text-slate-500 mt-1">전력 및 유지보수 최적화</div>
    </div>
</div>
"""
            },
            # Master Cross-App Workflows & Cheat Sheet
            {
                "badge": "MASTER PLAYBOOK",
                "title": "[마스터 플레이북 1] 4대 핸즈온 통합: Excel ➔ Word ➔ PPT 원스톱 크로스-앱 워크플로우",
                "subtitle": "데이터 정제부터 시뮬레이션, 다중 소스 보고서 합성, 임원 의사결정 슬라이드 완성까지 완전 정복",
                "body": """
<div class="p-6 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 rounded-3xl border-2 border-indigo-200 text-left my-2 shadow-md">
    <h4 class="font-black text-base md:text-lg text-slate-900 mb-3">통신 엔지니어링 마스터 크로스-플레이북</h4>
    <div class="space-y-2.5 text-sm md:text-base font-semibold">
        <div class="p-3 bg-white rounded-xl border border-indigo-100 flex items-center space-x-3 shadow-2xs">
            <span class="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-bold">1</span>
            <span><strong>Excel</strong>: 5G 로그 데이터 필터링 및 이상치 피벗 분석 완료</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-indigo-100 flex items-center space-x-3 shadow-2xs">
            <span class="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-bold">2</span>
            <span><strong>Word</strong>: 엑셀 분석 테이블을 참조하여 정형화된 원인 분석 SOP 보고서 작성</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-indigo-100 flex items-center space-x-3 shadow-2xs">
            <span class="w-8 h-8 rounded-lg bg-orange-600 text-white flex items-center justify-center text-xs font-bold">3</span>
            <span><strong>PowerPoint</strong>: 완성된 Word 보고서로부터 1-Page 임원 의사결정 슬라이드 변환</span>
        </div>
    </div>
</div>
"""
            },
            {
                "badge": "WAR-ROOM COLLAB",
                "title": "[마스터 플레이북 2] Teams 실시간 협업 기반 장애 상황 전파 및 조치 룸(War-Room) 운영",
                "subtitle": "비상 장애 상황 시 전송망, 코어망, 무선망 엔지니어가 실시간으로 공유하는 지능형 워룸",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-3">Teams 비상 워룸(War-Room) 운영 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "현재 발생한 백본 라우터 다운 이슈와 관련해 '긴급_장애조치_워룸' 채널을 생성하고, 코어망팀과 전송망팀 담당자를 자동 초대하며, 지난 1시간 동안의 경보 로그 요약본을 채널 첫 공지로 게시해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "badge": "CHEAT SHEET",
                "title": "[엔지니어 가이드] 2026 통신 네트워크 엔지니어를 위한 프롬프트 패턴집 & 치트시트",
                "subtitle": "실무에서 복사하여 바로 쓸 수 있는 핵심 프롬프트 모음",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-left my-2 text-xs md:text-sm">
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <strong class="text-indigo-600">📡 망 점검 & 장애 분석 패턴</strong>
        <p class="text-slate-600 mt-1 font-mono">"/files 'syslog.txt'에서 Severity 1~2 알람만 시간순으로 정렬하고 BGP Flapping 원인을 3줄 요약해줘"</p>
    </div>
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <strong class="text-purple-600">📊 통계 & 시뮬레이션 패턴</strong>
        <p class="text-slate-600 mt-1 font-mono">"PRB 점유율 상위 10% 기지국의 주말 피크 트래픽 분산 효과를 파이썬 차트로 시각화해줘"</p>
    </div>
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <strong class="text-emerald-600">📝 기술 제안 & 기안서 패턴</strong>
        <p class="text-slate-600 mt-1 font-mono">"노후 스위치 교체 시 전력 절감량과 가용성 개선율을 강조한 경영진 제출용 1장 기안서 작성해줘"</p>
    </div>
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <strong class="text-orange-600">✉️ 글로벌 벤더 TAC 패턴</strong>
        <p class="text-slate-600 mt-1 font-mono">"Cisco TAC 엔지니어에게 OSPF LSA 패킷 드롭 원인 조사를 요청하는 정중한 영문 메일 작성해줘"</p>
    </div>
</div>
"""
            }
        ]
    }
]

# Flatten all master slides
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

standard_portal_html = f"""<!DOCTYPE html>
<html lang="ko" class="h-full font-pretendard" id="htmlRoot">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microsoft 365 Copilot 표준 교육과정 - 통신·네트워크 실무 마스터</title>
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
            ''' for idx, c in enumerate(master_chapters)])}
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

            <!-- Slide List Scroll Area (31 Full Units) -->
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
md_lines.append("# 📘 Microsoft 365 Copilot 표준 교육과정 커리큘럼 (전체 통합 마스터)")
md_lines.append("\n> **표준 4대 챕터 완전 통합본**: 표준 교안의 4대 챕터 체계 하에, 기존에 제작된 모든 실무 시나리오(통신망 KPI, 토폴로지, TAC 메일, SOP, ROI)가 100% 온전히 복원되어 적재적소에 배치된 완전체 문서입니다.\n")
md_lines.append("---\n")

unit_counter = 1
for c_idx, chap in enumerate(master_chapters):
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

print(f"Successfully integrated all 31 full units across 4 official chapters at {output_path} and {output_clean_path}")
