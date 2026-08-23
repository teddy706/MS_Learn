import json
import base64

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

# Slide 04 Tenant Architecture Diagram (lossless SVGs)
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

# Define the 4 Official Standard Curriculum Chapters
standard_chapters = [
    {
        "chapter_num": "Chapter 01",
        "title": "M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI",
        "app_name": "Work IQ & Copilot Core",
        "app_key": "copilot",
        "icon_svg": fluent_icons["copilot"],
        "badge_class": "bg-indigo-50 text-indigo-900 border-indigo-200",
        "tools": "Work IQ, M365 Copilot, 멀티모달 전략, Office Agents, Copilot Work",
        "units": [
            {
                "num": "01",
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
            <li>• <strong>멀티모달 통합 진단</strong>: 시어로지 로그와 실시간 토폴로지 동시 판독</li>
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
                "num": "02",
                "badge": "MULTI-MODAL AI",
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
                "num": "03",
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
                "num": "04",
                "badge": "TENANT ARCHITECTURE",
                "title": "M365 Copilot 테넌트 아키텍처 및 보안 바운더리",
                "subtitle": "Zero-Data Retention과 기업 데이터 격리 보호 구조",
                "body": slide_04_body
            },
            {
                "num": "05",
                "badge": "OFFICE AGENTS",
                "title": "Office Agents & Copilot Studio 기반 통신 자율 에이전트",
                "subtitle": "반복적인 네트워크 점검과 정기 리포팅을 자동으로 수행하는 전용 에이전트 구축",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs">🤖</span>
            <span>NOC 일일 점검 에이전트</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3">매일 아침 8시, 전일 발생한 교환기 경보 로그와 백본 트래픽 통계를 자동 취합하여 Teams 브리핑 채널에 공유</p>
        <div class="text-xs bg-slate-50 p-2 rounded-lg text-slate-700 font-mono">Trigger: 매일 08:00 AM | Output: Teams 요약 카드 + Excel 다운로드</div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs">
        <h4 class="font-bold text-base text-slate-900 mb-2 flex items-center space-x-2">
            <span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs">🛡️</span>
            <span>보안 취약점 패치 에이전트</span>
        </h4>
        <p class="text-sm text-slate-600 mb-3">Cisco/Nokia 신규 보안 권고문(CVE) 발표 시 사내 인프라 장비 펌웨어 버전과 비교 대조하여 조치 가이드 발행</p>
        <div class="text-xs bg-slate-50 p-2 rounded-lg text-slate-700 font-mono">Trigger: 신규 CVE RSS | Output: Word 긴급 패치 권고서</div>
    </div>
</div>
"""
            },
            {
                "num": "06",
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
            }
        ]
    },
    {
        "chapter_num": "Chapter 02",
        "title": "사전 준비, Copilot 활용을 위한 업무 환경 만들기",
        "app_name": "OneDrive & SharePoint",
        "app_key": "onedrive",
        "icon_svg": fluent_icons["onedrive"],
        "badge_class": "bg-sky-50 text-sky-950 border-sky-200",
        "tools": "OneDrive, SharePoint, 데이터 구조화, 보안 권한 분리",
        "units": [
            {
                "num": "07",
                "badge": "DATA ASSET",
                "title": "Copilot 인덱싱 최적화를 위한 OneDrive 데이터 자산화 및 폴더 구조화",
                "subtitle": "AI가 빠르고 정확하게 찾아낼 수 있는 엔지니어링 파일 명명 규칙과 메타데이터 정리",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-2 text-left">
    <div class="p-5 bg-red-50/70 rounded-2xl border border-red-200">
        <h4 class="font-bold text-base text-red-900 mb-2">❌ Copilot이 헷갈리는 파일 관리</h4>
        <ul class="space-y-1.5 text-sm text-red-800">
            <li>• `최종_진짜최종_네트워크구성도_수정.vsdx`</li>
            <li>• 로컬 C드라이브 바탕화면에만 저장된 비정형 메모</li>
            <li>• 버전 관리 없이 덮어쓴 Excel IP 대장</li>
        </ul>
    </div>
    <div class="p-5 bg-emerald-50/70 rounded-2xl border border-emerald-200">
        <h4 class="font-bold text-base text-emerald-900 mb-2">✅ AI-Ready 클라우드 파일 표준화</h4>
        <ul class="space-y-1.5 text-sm text-emerald-900 font-medium">
            <li>• `[프로젝트ID]_[장비군]_[문서종류]_v1.2.docx`</li>
            <li>• OneDrive 자동 버전 기록 및 변경 이력 추적 활성화</li>
            <li>• 헤더 스타일(H1, H2, H3)이 적용된 구조화된 본문</li>
        </ul>
    </div>
</div>
"""
            },
            {
                "num": "08",
                "badge": "SHAREPOINT KB",
                "title": "SharePoint 팀 사이트 기반 통신 운영 가이드 및 지식 베이스(KB) 통합",
                "subtitle": "부서 내 흩어진 장애 조치 노하우를 하나의 지능형 지식 허브로 집중화",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">SharePoint 허브를 통한 팀 지식 증폭</h4>
    <p class="text-sm md:text-base text-slate-600 leading-relaxed mb-4">
        팀원 각자의 PC에 흩어져 있던 스위치 설정 템플릿, 광케이블 선로 도면, 과거 장애 리포트를 SharePoint 전용 라이브러리에 업로드하면 Copilot이 실시간으로 학습 인덱스에 반영합니다.
    </p>
    <div class="grid grid-cols-3 gap-3 text-center text-xs md:text-sm font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">📁 장비별 Config 표준</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">📋 통신사 연동 가이드</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">🛡️ 긴급 핫라인 비상연락망</div>
    </div>
</div>
"""
            },
            {
                "num": "09",
                "badge": "PURVIEW & ACL",
                "title": "Purview 민감도 레이블 및 권한 기반 액세스 제어(ACL) 설정",
                "subtitle": "기밀 통신망 설계도와 인증키의 부서 외 유출을 원천 방지하는 보안 정책",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <div class="flex items-center justify-between mb-4">
        <h4 class="font-bold text-base md:text-lg text-slate-900">M365 Purview 보안 레이블 등급 체계</h4>
        <span class="px-3 py-1 bg-indigo-100 text-indigo-800 text-xs font-black rounded-full">Automatic Encryption</span>
    </div>
    <div class="space-y-3 text-sm">
        <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center justify-between shadow-2xs">
            <div>
                <strong class="text-slate-800">[대외비] Confidential</strong>: 백본 라우팅 테이블, 코어망 접속 계정
            </div>
            <span class="text-xs text-indigo-600 font-bold">코어망운영팀만 Copilot 조회 가능</span>
        </div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center justify-between shadow-2xs">
            <div>
                <strong class="text-slate-800">[사내한] Internal</strong>: 일반 기지국 점검 매뉴얼, 분기별 KPI 보고서
            </div>
            <span class="text-xs text-slate-500 font-bold">사내 전 임직원 조회 가능</span>
        </div>
    </div>
</div>
"""
            },
            {
                "num": "10",
                "badge": "ENV AUTOMATION",
                "title": "분산된 네트워크 구성도 및 설정 파일의 SharePoint 인덱싱 자동화",
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
        "chapter_num": "Chapter 03",
        "title": "산더미 같은 이메일 탈출과 스마트한 일정 관리",
        "app_name": "Prompt Coach & Outlook",
        "app_key": "outlook",
        "icon_svg": fluent_icons["outlook"],
        "badge_class": "bg-blue-50 text-blue-950 border-blue-200",
        "tools": "Prompt Coach, Outlook, 메일 스레드 요약, 스마트 일정 조율",
        "units": [
            {
                "num": "11",
                "badge": "PROMPT COACH",
                "title": "Prompt Coach: 고품질 엔지니어링 프롬프트 작성을 위한 4대 원칙",
                "subtitle": "목표(Goal), 맥락(Context), 출처(Source), 기대형식(Expectation)의 정밀 코칭",
                "body": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-2 text-left">
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <span class="text-xs font-black text-indigo-600">01. GOAL (목표)</span>
        <div class="font-bold text-slate-900 text-sm mt-1">AI가 수행해야 할 명확한 행동 지시</div>
        <div class="text-xs text-slate-500 mt-1">예: "장애 원인 3가지를 도출하고 엔지니어링 개선안을 제안해줘"</div>
    </div>
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <span class="text-xs font-black text-purple-600">02. CONTEXT (맥락)</span>
        <div class="font-bold text-slate-900 text-sm mt-1">상황 및 배경 정보 제공</div>
        <div class="text-xs text-slate-500 mt-1">예: "수도권 코어 라우터에서 발생한 BGP 세션 순단 상황임"</div>
    </div>
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <span class="text-xs font-black text-blue-600">03. SOURCE (출처)</span>
        <div class="font-bold text-slate-900 text-sm mt-1">참조할 사내 파일 및 대화 지정</div>
        <div class="text-xs text-slate-500 mt-1">예: "/files '2026_BGP_Config.docx'와 지난 3일간의 스레드 참조"</div>
    </div>
    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs">
        <span class="text-xs font-black text-emerald-600">04. EXPECTATION (형식)</span>
        <div class="font-bold text-slate-900 text-sm mt-1">출력 양식 및 어조 지정</div>
        <div class="text-xs text-slate-500 mt-1">예: "전문적이고 정중한 톤으로 타임라인 표와 글머리 기호로 작성"</div>
    </div>
</div>
"""
            },
            {
                "num": "12",
                "badge": "THREAD SUMMARY",
                "title": "Outlook Copilot: 긴급 NOC 장애 스레드 3초 요약 및 액션 아이템 도출",
                "subtitle": "수십 통이 쌓인 교환기 장애 메일 타임라인과 미완료 조치 사항 즉시 파악",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">Outlook 스레드 요약 실무 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "이 메일 스레드 전체를 시간순(Timeline)으로 정렬하여 최초 알람 발생 시점, 각 담당자의 조치 내역, 그리고 아직 해결되지 않은 액션 아이템(Action Items)과 담당자를 표로 정리해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "num": "13",
                "badge": "GLOBAL VENDOR",
                "title": "글로벌 통신 벤더(Cisco/Nokia) 기술 지원 요청 및 영어 메일 정밀 작성",
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
                "num": "14",
                "badge": "SMART CALENDAR",
                "title": "정기 PM 작업 공지 및 멀티 벤더 스마트 일정 자동 조율",
                "subtitle": "작업 영향도 공지 메일 발송과 이해관계자 빈 시간 자동 탐색 미팅 예약",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">스마트 일정 조율 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "다음 주 화요일 새벽 02:00~06:00 예정된 코어 라우터 OS 업그레이드 작업 공지 메일을 작성하고, 작업 전 사전 브리핑을 위해 전송망팀과 무선운영팀 팀장님들의 캘린더에서 이번 주 금요일 오후 비는 시간 30분을 찾아 회의 초대를 생성해줘."
        </p>
    </blockquote>
</div>
"""
            }
        ]
    },
    {
        "chapter_num": "Chapter 04",
        "title": "데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북",
        "app_name": "Excel, Word, PPT 에이전트",
        "app_key": "excel",
        "icon_svg": fluent_icons["excel"],
        "badge_class": "bg-emerald-50 text-emerald-950 border-emerald-200",
        "tools": "Excel 데이터 분석, Word SOP 생성, PPT 임원 보고, 에이전트 크로스 연동",
        "units": [
            {
                "num": "15",
                "badge": "EXCEL AGENT",
                "title": "Excel Copilot: 5G 기지국 KPI 대용량 로그 수식 및 통계 자동 생성",
                "subtitle": "수작업 함수 입력 없이 자연어 명령만으로 피벗 테이블과 조건부 서식 구성",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">Excel Copilot 실전 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "'PRB_Usage' 컬럼이 85% 이상이면서 'Drop_Rate'가 1.5%를 초과하는 과부하 기지국만 필터링하는 새 열을 추가하고, 기지국 ID별 시간대별 트래픽 추이를 피벗 차트로 생성해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "num": "16",
                "badge": "ANOMALY DETECTION",
                "title": "네트워크 트래픽 이상 감지 및 Z-Score 기반 분산 분석",
                "subtitle": "통계적 이상치를 자동으로 색출하여 잠재적 DDoS 및 백홀 병목 사전 차단",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">이상치 탐지 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "최근 30일간의 백홀 트래픽 데이터를 바탕으로 Z-Score가 +2.5 이상인 이상 트래픽 발생 구간을 빨간색 조건부 서식으로 강조하고, 평일 대비 주말 트래픽의 유의미한 변동 원인을 분석해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "num": "17",
                "badge": "PYTHON IN EXCEL",
                "title": "Python in Excel: 상관계수 히트맵 및 지연 시간 시각화",
                "subtitle": "파이썬 Seaborn/Matplotlib 라이브러리를 엑셀 시트 내에서 직접 구동",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">Python in Excel 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "기지국 접속자 수, 패킷 지연 시간(RTT), 다운로드 처리량 간의 상관관계를 파이썬 seaborn heatmap으로 시각화하여 현재 시트의 G2 셀에 삽입해줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "num": "18",
                "badge": "WORD SOP",
                "title": "Word Copilot: 통신망 장애 조치 표준 작업 절차서(SOP) 원클릭 초안 생성",
                "subtitle": "메모와 로그 조각들을 공공·기업 표준 규격의 기술 문서로 완벽 구조화",
                "body": """
<div class="p-6 bg-slate-50 rounded-2xl border border-slate-200 text-left my-2">
    <h4 class="font-bold text-base md:text-lg text-slate-900 mb-2">Word SOP 초안 작성 프롬프트</h4>
    <blockquote>
        <p class="text-sm md:text-base font-mono text-indigo-950 font-semibold">
            "이번 코어망 L3 스위치 이중화 전환 작업을 위한 표준 작업 절차서(SOP)를 작성해줘. 목적, 작업 전 체크리스트, 단계별 명령어 및 예상 결과, 비상 롤백(Rollback) 절차를 포함하여 정형화된 보고서 양식으로 만들어줘."
        </p>
    </blockquote>
</div>
"""
            },
            {
                "num": "19",
                "badge": "CAPEX / OPEX",
                "title": "정량적 통신 설비 투자(CAPEX/OPEX) 분석 및 제안서 작성",
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
                "num": "20",
                "badge": "TOPOLOGY VISUAL",
                "title": "Mermaid 다이어그램을 통한 5G SA 코어 네트워크 토폴로지 시각화",
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
            {
                "num": "21",
                "badge": "PPT COPILOT",
                "title": "PPT Copilot: Word 보고서 기반 임원 보고용 프레젠테이션 자동 생성",
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
                "num": "22",
                "badge": "EXECUTIVE ROI",
                "title": "경영진 의사결정을 위한 1-Page 네트워크 ROI 서머리 슬라이드 디자인",
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
            {
                "num": "23",
                "badge": "PLAYBOOK MASTER",
                "title": "Excel ➔ Word ➔ PPT 에이전트 크로스-앱 연동 실전 플레이북",
                "subtitle": "데이터 분석부터 보고서 작성, 임원 발표 자료 완성까지 원스톱 완전 자동화 워크플로우",
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
            }
        ]
    }
]

# Flatten all units into cleaned_slides list
cleaned_slides = []
total_units = sum(len(c["units"]) for c in standard_chapters)
curr_unit_idx = 0

for chap_idx, chap in enumerate(standard_chapters):
    for u_idx, u in enumerate(chap["units"]):
        cleaned_slides.append({
            "part_idx": chap_idx,
            "part_num": chap["chapter_num"],
            "part_title": chap["title"],
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

        <!-- Center: 4 Standard Chapters Pill Bar -->
        <div class="hidden lg:flex items-center space-x-2 overflow-x-auto py-1">
            {"".join([f'''
            <button onclick="goToPart({idx})" class="part-pill-btn ms-pill-tab px-4 py-1.5 text-xs md:text-sm font-bold flex items-center space-x-2" data-part="{idx}">
                <span class="scale-90">{c["icon_svg"]}</span>
                <span>{c["chapter_num"]}</span>
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
            <!-- Sidebar Header with Chapter Info -->
            <div id="sidebarAppBanner" class="p-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between transition-colors">
                <div class="flex items-center space-x-3">
                    <span id="activeAppIcon" class="w-8 h-8 flex items-center justify-center">{fluent_icons["copilot"]}</span>
                    <div>
                        <div id="activeAppName" class="font-black text-sm text-slate-900 leading-tight">Work IQ & Copilot Core</div>
                        <div id="activePartNum" class="text-xs text-indigo-600 font-bold mt-0.5">Chapter 01. M365 Copilot의 변화</div>
                    </div>
                </div>
                <div class="flex items-center space-x-1.5">
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

            <!-- App Category Breadcrumb Bar -->
            <div id="appThemeHeader" class="no-print h-11 bg-white/80 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2.5 text-xs md:text-sm font-semibold">
                    <span id="bannerAppBadge" class="px-3 py-0.5 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-xs border border-slate-200 flex items-center space-x-2">
                        <span id="bannerAppIconSvg" class="scale-75">{fluent_icons["copilot"]}</span>
                        <span id="bannerAppText">CHAPTER 01</span>
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

            <!-- Continuous Document Scroll Portal (All Units) -->
            <div id="portalViewStage" class="flex-1 overflow-y-auto p-6 md:p-12 space-y-12 hidden">
                {"".join([f'''
                <article id="portal-slide-{idx}" class="max-w-5xl mx-auto ms-fluid-card p-8 md:p-12 slide-page">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider {s["badge_class"]} border flex items-center space-x-2">
                                <span class="scale-90">{s["app_icon_svg"]}</span>
                                <span>{s["part_num"]} • {s["badge"]}</span>
                            </span>
                            <span class="font-mono text-xs md:text-sm font-black text-slate-400">UNIT {s["num"]} / {total_units:02d}</span>
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

            // Render Center Card in Fluid Web Mode
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge -->
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center space-x-2.5">
                            <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-black uppercase tracking-wider ${{slide.badge_class}} border flex items-center space-x-2 shadow-2xs">
                                <span class="scale-90">${{slide.app_icon_svg}}</span>
                                <span>${{slide.part_num}} • ${{slide.badge}}</span>
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
                        <span>${{slide.part_num}}: ${{slide.part_title}}</span>
                    </span>
                    <div class="flex items-center space-x-2.5">
                        <button onclick="prevSlide()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-full transition-colors text-sm">◀ 이전</button>
                        <button onclick="nextSlide()" class="px-5 py-2 bg-slate-900 hover:bg-indigo-600 text-white font-bold rounded-full shadow-xs transition-colors text-sm">다음 ▶</button>
                    </div>
                </div>
            `;

            // Update Header Banner
            document.getElementById('bannerAppText').textContent = slide.part_num.toUpperCase();
            document.getElementById('bannerAppIconSvg').innerHTML = slide.app_icon_svg;
            document.getElementById('bannerSlideTitle').textContent = slide.title;

            // Update Sidebar Info
            document.getElementById('activeAppIcon').innerHTML = slide.app_icon_svg;
            document.getElementById('activeAppName').textContent = slide.app_name;
            document.getElementById('activePartNum').textContent = `${{slide.part_num}}. ${{slide.part_title}}`;
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

print(f"Successfully rebuilt portal with 4 standard curriculum chapters at {output_path} and {index_path}")
