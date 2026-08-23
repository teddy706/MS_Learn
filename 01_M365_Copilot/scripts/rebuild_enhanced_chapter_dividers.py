# -*- coding: utf-8 -*-
import sys, os, re, json, base64
sys.stdout.reconfigure(encoding='utf-8')

# Read base64 for 3D Copilot Image
with open('01_M365_Copilot/assets/copilot_3d_index_hero.png', 'rb') as f:
    copilot_3d_b64 = base64.b64encode(f.read()).decode('utf-8')

html_file = 'AX_CA_Edu_GHLEE.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract slidesData
start_idx = content.find('const slidesData = ')
if start_idx == -1:
    print('const slidesData not found')
    sys.exit(1)

start_json = start_idx + len('const slidesData = ')
end_json = content.find('let currentSlideIndex =', start_json)
semicolon_idx = content.rfind(';', start_json, end_json)

json_str = content[start_json:semicolon_idx].strip()
slides = json.loads(json_str, strict=False)
print(f'Loaded slides count: {len(slides)}')

# --- 1. Redefine Slide 0: COVER (Microsoft Build Keynote Aesthetic) ---
slides[0]['badge'] = 'KT AX • MASTER CLASS'
slides[0]['badge_class'] = 'bg-[#FCE7F3] text-black border-[#F472B6]/40'
slides[0]['tools'] = 'KT 코어/전송망 AX 엔지니어링 전용 실무 마스터'
slides[0]['title'] = 'Work IQ & M365 Copilot 실무 마스터'
slides[0]['subtitle'] = 'KT 코어/전송망 엔지니어를 위한 데이터 기반 의사결정 & 업무 자동화 워크플로우'
slides[0]['body'] = '''<div class="my-auto w-full text-left relative min-h-[420px] flex flex-col justify-between">
    <!-- Microsoft Build Style Cyber Matrix Background SVG -->
    <svg class="absolute right-0 top-0 bottom-0 w-1/2 h-full opacity-70 pointer-events-none select-none" viewBox="0 0 500 420" fill="none">
        <g opacity="0.45" stroke="#F472B6" stroke-width="1.5" stroke-dasharray="6 14">
            <line x1="280" y1="20" x2="280" y2="180" />
            <line x1="300" y1="40" x2="300" y2="240" />
            <line x1="320" y1="10" x2="320" y2="300" />
            <line x1="340" y1="80" x2="340" y2="360" />
            <line x1="360" y1="30" x2="360" y2="420" />
            <line x1="380" y1="90" x2="380" y2="410" />
            <line x1="400" y1="50" x2="400" y2="390" />
        </g>
        <g opacity="0.3" stroke="#38BDF8" stroke-width="1" stroke-dasharray="4 10">
            <line x1="240" y1="80" x2="240" y2="300" />
            <line x1="260" y1="120" x2="260" y2="380" />
            <line x1="440" y1="30" x2="440" y2="400" />
        </g>
        <rect x="360" y="60" width="10" height="10" fill="#F472B6" opacity="0.7" />
        <rect x="420" y="200" width="8" height="8" fill="#38BDF8" opacity="0.6" />
        <rect x="300" y="280" width="9" height="9" fill="#A855F7" opacity="0.5" />
    </svg>

    <!-- Top Left MS Build Style Badge -->
    <div class="relative z-10 pt-1">
        <div class="inline-block px-3.5 py-1 bg-[#FCE7F3] text-black font-black text-xs md:text-sm tracking-wider uppercase rounded-sm shadow-sm mb-4">
            WHAT'S NEW IN
        </div>

        <!-- Main Hero Title -->
        <div class="space-y-2.5">
            <div class="text-xs md:text-sm font-bold tracking-widest text-slate-400 uppercase">
                TELECOM NETWORK AI ENGINEERING
            </div>
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-none">
                Work IQ &amp; Copilot
            </h1>
            <div class="text-base md:text-xl text-slate-200 font-bold pt-1">
                KT 코어/전송망 AX 엔지니어 실무 마스터
            </div>
            <p class="text-xs md:text-sm text-slate-400 font-medium max-w-xl leading-relaxed">
                AI 시대를 주도하는 통신망 엔지니어링 &amp; 데이터 기반 의사결정 워크플로우 혁신
            </p>
        </div>
    </div>

    <!-- Bottom Left Cyan Event Tag & Specs -->
    <div class="relative z-10 pt-6 mt-4 border-t border-white/10 flex flex-col md:flex-row md:items-center justify-between gap-3">
        <div class="font-black text-xs md:text-sm text-[#00E5FF] tracking-widest uppercase">
            KT TELECOM AX • 2026
        </div>
        <div class="flex flex-wrap items-center gap-2 text-xs font-bold text-slate-300">
            <span class="px-2.5 py-0.5 bg-white/5 border border-white/10 rounded-md">4 Chapters</span>
            <span class="px-2.5 py-0.5 bg-white/5 border border-white/10 rounded-md">52 Hands-on Units</span>
            <span class="px-2.5 py-0.5 bg-white/5 border border-white/10 rounded-md">7 Hours Master</span>
            <span class="px-2.5 py-0.5 bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 rounded-md">🛡️ Enterprise Data Protection</span>
        </div>
    </div>
</div>'''

# --- 2. Redefine Slide 1: INDEX (Clean Focus: Chapter Title & Core Essence Only) ---
slides[1]['badge'] = 'CURRICULUM • ROADMAP'
slides[1]['badge_class'] = 'bg-gradient-to-r from-blue-600 via-purple-600 to-pink-500 text-white border-transparent'
slides[1]['tools'] = '전체 4대 챕터 로드맵 & 52개 유닛'
slides[1]['title'] = '전체 교육 커리큘럼 로드맵 (4 Chapters)'
slides[1]['subtitle'] = '비즈니스 AI 패러다임 전환부터 업무 환경 구축, 오피스 핵심 실무, 엔드투엔드 종합 플레이북까지'
slides[1]['body'] = f'''<div class="my-auto w-full text-left space-y-3.5 relative">
    <!-- Top Hero Banner with 3D Copilot Visual Asset -->
    <div class="p-4 lg:p-5 bg-white/95 backdrop-blur-md rounded-2xl border border-slate-200 shadow-sm relative overflow-hidden flex flex-col md:flex-row items-center justify-between gap-3">
        <!-- Ambient Glowing Background Gradient -->
        <div class="absolute -right-10 -bottom-10 w-80 h-80 bg-gradient-to-br from-purple-400/15 via-pink-400/15 to-cyan-400/15 rounded-full blur-2xl pointer-events-none"></div>

        <div class="flex-1 min-w-0 z-10">
            <div class="flex items-center space-x-2 mb-1">
                <span class="px-2.5 py-0.5 bg-gradient-to-r from-[#0078D4] via-[#8B5CF6] to-[#EA580C] text-white text-2xs font-black rounded-full shadow-xs">
                    M365 COPILOT ROADMAP
                </span>
                <span class="text-2xs text-slate-500 font-bold">4 Chapters • 52 Units</span>
            </div>
            <h3 class="text-lg md:text-xl lg:text-2xl font-black text-slate-900 tracking-tight leading-tight mb-0.5">
                KT AX 엔지니어링 전 과정 목차
            </h3>
            <p class="text-xs text-slate-600 font-medium break-keep">
                통신망 관제 AX 전환부터 클라우드 지식화, 이메일·일정 자동화, 4대 실무 플레이북까지
            </p>
        </div>

        <!-- 3D Copilot Visual Asset -->
        <div class="shrink-0 w-full md:w-48 lg:w-56 h-24 md:h-20 lg:h-24 rounded-xl overflow-hidden shadow-xs border border-slate-100 flex items-center justify-center bg-gradient-to-br from-slate-50 to-slate-100 relative group">
            <img src="data:image/png;base64,{copilot_3d_b64}" alt="Microsoft Copilot 3D Platform" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
        </div>
    </div>

    <!-- 4 Chapter Cards Grid (Pure Title & Core Content Only) -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <!-- Chapter 01 Card -->
        <div onclick="goToSlide(2)" class="p-4 bg-white/95 backdrop-blur-md rounded-2xl border-2 border-sky-200/80 hover:border-sky-500 shadow-2xs hover:shadow-xs hover:scale-[1.008] transition-all cursor-pointer flex flex-col justify-between group">
            <div>
                <div class="flex items-center justify-between mb-2">
                    <span class="px-2.5 py-0.5 bg-gradient-to-r from-sky-500 to-blue-600 text-white text-2xs font-black rounded-md shadow-2xs">Chapter 01</span>
                    <span class="text-2xs text-sky-700 font-bold bg-sky-50 px-2 py-0.5 rounded border border-sky-200">8 Units (01~08)</span>
                </div>
                <h4 class="font-black text-sm lg:text-base text-slate-900 mb-1.5 group-hover:text-sky-600 transition-colors">M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI</h4>
                <p class="text-xs text-slate-600 font-medium leading-relaxed">KT 통신 업무 맥락(Context)과 엔터프라이즈 보안을 결합한 AI 패러다임 전환 및 Work IQ 이해</p>
            </div>
            <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-2xs font-bold text-sky-600">
                <span>핵심: 보안 아키텍처 & Work IQ 융합</span>
                <span class="group-hover:translate-x-1 transition-transform">이동 ➔</span>
            </div>
        </div>

        <!-- Chapter 02 Card -->
        <div onclick="goToSlide(11)" class="p-4 bg-white/95 backdrop-blur-md rounded-2xl border-2 border-indigo-200/80 hover:border-indigo-500 shadow-2xs hover:shadow-xs hover:scale-[1.008] transition-all cursor-pointer flex flex-col justify-between group">
            <div>
                <div class="flex items-center justify-between mb-2">
                    <span class="px-2.5 py-0.5 bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-2xs font-black rounded-md shadow-2xs">Chapter 02</span>
                    <span class="text-2xs text-indigo-700 font-bold bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">6 Units (09~14)</span>
                </div>
                <h4 class="font-black text-sm lg:text-base text-slate-900 mb-1.5 group-hover:text-indigo-600 transition-colors">사전 준비, Copilot 활용을 위한 업무 환경 만들기</h4>
                <p class="text-xs text-slate-600 font-medium leading-relaxed">로컬 PC 사일로 탈피와 클라우드 중앙화를 통한 팀 지식 자산화 및 Semantic Index 구축</p>
            </div>
            <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-2xs font-bold text-indigo-600">
                <span>핵심: OneDrive & SharePoint 지식화</span>
                <span class="group-hover:translate-x-1 transition-transform">이동 ➔</span>
            </div>
        </div>

        <!-- Chapter 03 Card -->
        <div onclick="goToSlide(18)" class="p-4 bg-white/95 backdrop-blur-md rounded-2xl border-2 border-cyan-200/80 hover:border-cyan-500 shadow-2xs hover:shadow-xs hover:scale-[1.008] transition-all cursor-pointer flex flex-col justify-between group">
            <div>
                <div class="flex items-center justify-between mb-2">
                    <span class="px-2.5 py-0.5 bg-gradient-to-r from-teal-500 to-cyan-600 text-white text-2xs font-black rounded-md shadow-2xs">Chapter 03</span>
                    <span class="text-2xs text-cyan-700 font-bold bg-cyan-50 px-2 py-0.5 rounded border border-cyan-200">5 Units (15~19)</span>
                </div>
                <h4 class="font-black text-sm lg:text-base text-slate-900 mb-1.5 group-hover:text-cyan-600 transition-colors">산더미 같은 이메일 탈출과 스마트한 일정 관리</h4>
                <p class="text-xs text-slate-600 font-medium leading-relaxed">긴급 장애 메일 스레드 10초 요약, 글로벌 TAC 영문 소통 및 Schedule with Copilot 일정 조율</p>
            </div>
            <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-2xs font-bold text-cyan-600">
                <span>핵심: Outlook & 일정 실무 자동화</span>
                <span class="group-hover:translate-x-1 transition-transform">이동 ➔</span>
            </div>
        </div>

        <!-- Chapter 04 Card -->
        <div onclick="goToSlide(24)" class="p-4 bg-white/95 backdrop-blur-md rounded-2xl border-2 border-emerald-200/80 hover:border-emerald-500 shadow-2xs hover:shadow-xs hover:scale-[1.008] transition-all cursor-pointer flex flex-col justify-between group">
            <div>
                <div class="flex items-center justify-between mb-2">
                    <span class="px-2.5 py-0.5 bg-gradient-to-r from-emerald-500 to-teal-600 text-white text-2xs font-black rounded-md shadow-2xs">Chapter 04</span>
                    <span class="text-2xs text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">33 Units (20~52)</span>
                </div>
                <h4 class="font-black text-sm lg:text-base text-slate-900 mb-1.5 group-hover:text-emerald-600 transition-colors">데이터기반 의사결정, 실전 플레이북</h4>
                <p class="text-xs text-slate-600 font-medium leading-relaxed">Excel 대용량 분석, Word 정형 SOP·CAPEX 기안서, PPT 1-Page 임원보고 및 비상 장애 Teams 워룸</p>
            </div>
            <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-2xs font-bold text-emerald-600">
                <span>핵심: Office 크로스앱 실무 완결</span>
                <span class="group-hover:translate-x-1 transition-transform">이동 ➔</span>
            </div>
        </div>
    </div>

    <!-- Bottom Feature Bar -->
    <div class="p-2.5 bg-white/90 rounded-xl text-2xs text-slate-700 font-bold text-center border border-slate-200 shadow-2xs flex items-center justify-center space-x-2">
        <span class="text-rose-500 text-xs">🎯</span>
        <span>7시간 집중 마스터 과정 | 52개 실전 플레이북 | 6종 KT 통신망 실습 데이터셋 연동</span>
    </div>
</div>'''

# --- 3. Redefine Slide 2: CH 01 Divider (Microsoft 365 Navy & Logo with Prominent Chapter Title) ---
slides[2]['badge'] = 'CHAPTER 01'
slides[2]['badge_class'] = 'bg-sky-500/20 text-sky-300 border-sky-400/40'
slides[2]['tools'] = 'Microsoft 365 Copilot'
slides[2]['title'] = '01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI'
slides[2]['subtitle'] = 'KT 코어/전송망 엔지니어링 실무 마스터'
slides[2]['body'] = '''<div class="my-auto w-full text-left relative min-h-[400px] flex flex-col justify-between">
    <!-- Top Microsoft 365 Logo & Chapter Badge -->
    <div class="flex items-center justify-between border-b border-slate-700/40 pb-4 mb-6">
        <div class="flex items-center space-x-3">
            <svg class="w-8 h-8 shrink-0" viewBox="0 0 24 24" fill="none">
                <rect x="1" y="1" width="10" height="10" fill="#F25022" rx="1"/>
                <rect x="13" y="1" width="10" height="10" fill="#7FBA00" rx="1"/>
                <rect x="1" y="13" width="10" height="10" fill="#00A4EF" rx="1"/>
                <rect x="13" y="13" width="10" height="10" fill="#FFB900" rx="1"/>
            </svg>
            <span class="text-xl md:text-2xl font-bold text-white tracking-tight font-pretendard">Microsoft 365</span>
        </div>
        <span class="px-4 py-1 bg-sky-500/20 text-sky-300 font-black text-xs md:text-sm rounded-full border border-sky-400/40 shadow-sm">
            CHAPTER 01
        </span>
    </div>

    <!-- Center Prominent Chapter Title Only -->
    <div class="my-auto py-6">
        <div class="text-xs md:text-sm font-bold text-sky-400 tracking-widest uppercase mb-3 font-mono">
            SECTION 01 • 8 UNITS
        </div>
        <h1 class="text-3xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight max-w-4xl">
            01. M365 Copilot의 변화,<br/>
            <span class="text-sky-200">일을 더 잘 이해하게 된 AI</span>
        </h1>
    </div>
</div>'''

# --- 4. Redefine Slide 11: CH 02 Divider (Microsoft 365 Navy & Logo with Prominent Chapter Title) ---
slides[11]['badge'] = 'CHAPTER 02'
slides[11]['badge_class'] = 'bg-blue-500/20 text-blue-300 border-blue-400/40'
slides[11]['tools'] = 'Microsoft 365 Copilot'
slides[11]['title'] = '02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기'
slides[11]['subtitle'] = 'KT 코어/전송망 엔지니어링 실무 마스터'
slides[11]['body'] = '''<div class="my-auto w-full text-left relative min-h-[400px] flex flex-col justify-between">
    <!-- Top Microsoft 365 Logo & Chapter Badge -->
    <div class="flex items-center justify-between border-b border-slate-700/40 pb-4 mb-6">
        <div class="flex items-center space-x-3">
            <svg class="w-8 h-8 shrink-0" viewBox="0 0 24 24" fill="none">
                <rect x="1" y="1" width="10" height="10" fill="#F25022" rx="1"/>
                <rect x="13" y="1" width="10" height="10" fill="#7FBA00" rx="1"/>
                <rect x="1" y="13" width="10" height="10" fill="#00A4EF" rx="1"/>
                <rect x="13" y="13" width="10" height="10" fill="#FFB900" rx="1"/>
            </svg>
            <span class="text-xl md:text-2xl font-bold text-white tracking-tight font-pretendard">Microsoft 365</span>
        </div>
        <span class="px-4 py-1 bg-blue-500/20 text-blue-300 font-black text-xs md:text-sm rounded-full border border-blue-400/40 shadow-sm">
            CHAPTER 02
        </span>
    </div>

    <!-- Center Prominent Chapter Title Only -->
    <div class="my-auto py-6">
        <div class="text-xs md:text-sm font-bold text-blue-400 tracking-widest uppercase mb-3 font-mono">
            SECTION 02 • 6 UNITS
        </div>
        <h1 class="text-3xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight max-w-4xl">
            02. 사전 준비,<br/>
            <span class="text-blue-200">Copilot 활용을 위한 업무 환경 만들기</span>
        </h1>
    </div>
</div>'''

# --- 5. Redefine Slide 18: CH 03 Divider (Microsoft 365 Navy & Logo with Prominent Chapter Title) ---
slides[18]['badge'] = 'CHAPTER 03'
slides[18]['badge_class'] = 'bg-cyan-500/20 text-cyan-300 border-cyan-400/40'
slides[18]['tools'] = 'Microsoft 365 Copilot'
slides[18]['title'] = '03. 산더미 같은 이메일 탈출과 스마트한 일정 관리'
slides[18]['subtitle'] = 'KT 코어/전송망 엔지니어링 실무 마스터'
slides[18]['body'] = '''<div class="my-auto w-full text-left relative min-h-[400px] flex flex-col justify-between">
    <!-- Top Microsoft 365 Logo & Chapter Badge -->
    <div class="flex items-center justify-between border-b border-slate-700/40 pb-4 mb-6">
        <div class="flex items-center space-x-3">
            <svg class="w-8 h-8 shrink-0" viewBox="0 0 24 24" fill="none">
                <rect x="1" y="1" width="10" height="10" fill="#F25022" rx="1"/>
                <rect x="13" y="1" width="10" height="10" fill="#7FBA00" rx="1"/>
                <rect x="1" y="13" width="10" height="10" fill="#00A4EF" rx="1"/>
                <rect x="13" y="13" width="10" height="10" fill="#FFB900" rx="1"/>
            </svg>
            <span class="text-xl md:text-2xl font-bold text-white tracking-tight font-pretendard">Microsoft 365</span>
        </div>
        <span class="px-4 py-1 bg-cyan-500/20 text-cyan-300 font-black text-xs md:text-sm rounded-full border border-cyan-400/40 shadow-sm">
            CHAPTER 03
        </span>
    </div>

    <!-- Center Prominent Chapter Title Only -->
    <div class="my-auto py-6">
        <div class="text-xs md:text-sm font-bold text-cyan-400 tracking-widest uppercase mb-3 font-mono">
            SECTION 03 • 5 UNITS
        </div>
        <h1 class="text-3xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight max-w-4xl">
            03. 산더미 같은 이메일 탈출과<br/>
            <span class="text-cyan-200">스마트한 일정 관리</span>
        </h1>
    </div>
</div>'''

# --- 6. Redefine Slide 24: CH 04 Divider (Microsoft 365 Navy & Logo with Prominent Chapter Title) ---
slides[24]['badge'] = 'CHAPTER 04'
slides[24]['badge_class'] = 'bg-emerald-500/20 text-emerald-300 border-emerald-400/40'
slides[24]['tools'] = 'Microsoft 365 Copilot'
slides[24]['title'] = '04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북'
slides[24]['subtitle'] = 'KT 코어/전송망 엔지니어링 실무 마스터'
slides[24]['body'] = '''<div class="my-auto w-full text-left relative min-h-[400px] flex flex-col justify-between">
    <!-- Top Microsoft 365 Logo & Chapter Badge -->
    <div class="flex items-center justify-between border-b border-slate-700/40 pb-4 mb-6">
        <div class="flex items-center space-x-3">
            <svg class="w-8 h-8 shrink-0" viewBox="0 0 24 24" fill="none">
                <rect x="1" y="1" width="10" height="10" fill="#F25022" rx="1"/>
                <rect x="13" y="1" width="10" height="10" fill="#7FBA00" rx="1"/>
                <rect x="1" y="13" width="10" height="10" fill="#00A4EF" rx="1"/>
                <rect x="13" y="13" width="10" height="10" fill="#FFB900" rx="1"/>
            </svg>
            <span class="text-xl md:text-2xl font-bold text-white tracking-tight font-pretendard">Microsoft 365</span>
        </div>
        <span class="px-4 py-1 bg-emerald-500/20 text-emerald-300 font-black text-xs md:text-sm rounded-full border border-emerald-400/40 shadow-sm">
            CHAPTER 04
        </span>
    </div>

    <!-- Center Prominent Chapter Title Only -->
    <div class="my-auto py-6">
        <div class="text-xs md:text-sm font-bold text-emerald-400 tracking-widest uppercase mb-3 font-mono">
            SECTION 04 • 33 UNITS
        </div>
        <h1 class="text-3xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight max-w-4xl">
            04. 데이터기반 의사결정,<br/>
            <span class="text-emerald-200">Copilot 에이전트 모드를 활용한 실전 플레이북</span>
        </h1>
    </div>
</div>'''

clean_json = json.dumps(slides, ensure_ascii=False)

# 2. Build Sidebar Navigation Items HTML with Consistent Pretendard Font
sidebar_items_html = []
for i, s in enumerate(slides):
    num = s['num']
    badge = s['badge']
    title = s['title']
    subtitle = s['subtitle']
    icon_svg = s['app_icon_svg']
    
    is_cover = (num == 'COVER')
    is_index = (num == 'INDEX')
    is_ch_divider = num.startswith('CH ')
    
    if is_cover:
        item_html = f'''
                <div class="slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 bg-black text-white border border-zinc-800 shadow-xs mb-1" id="nav-item-{i}" onclick="goToSlide({i})">
                    <span class="shrink-0 px-2 h-6 rounded-md bg-[#FCE7F3] text-black flex items-center justify-center text-xs font-black mt-0.5 item-num-badge">COVER</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-xs md:text-sm font-bold text-white break-keep leading-snug item-title flex items-start space-x-1.5">
                            <span class="scale-75 shrink-0 mt-0.5">{icon_svg}</span>
                            <span class="truncate">{title}</span>
                        </div>
                        <div class="text-2xs text-slate-300 mt-0.5 font-medium truncate">{badge} • {subtitle}</div>
                    </div>
                </div>'''
    elif is_index:
        item_html = f'''
                <div class="slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 bg-gradient-to-r from-blue-50 via-indigo-50 to-purple-50 text-slate-900 border border-indigo-200 shadow-xs mb-2" id="nav-item-{i}" onclick="goToSlide({i})">
                    <span class="shrink-0 px-2 h-6 rounded-lg bg-gradient-to-r from-blue-600 via-purple-600 to-pink-500 text-white flex items-center justify-center text-xs font-black mt-0.5 item-num-badge shadow-xs">INDEX</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-xs md:text-sm font-bold text-slate-900 break-keep leading-snug item-title flex items-start space-x-1.5">
                            <span class="scale-75 shrink-0 mt-0.5">{icon_svg}</span>
                            <span class="truncate">{title}</span>
                        </div>
                        <div class="text-2xs text-indigo-600 mt-0.5 font-bold truncate">{badge} • {subtitle}</div>
                    </div>
                </div>'''
    elif is_ch_divider:
        # Chapter section divider card with Microsoft 365 Navy theme
        ch_colors = {
            'CH 01': ('bg-[#111F36] border-sky-400/50 text-sky-200', 'bg-sky-500 text-white', 'text-sky-300', '8 Units'),
            'CH 02': ('bg-[#111F36] border-blue-400/50 text-blue-200', 'bg-blue-600 text-white', 'text-blue-300', '6 Units'),
            'CH 03': ('bg-[#111F36] border-cyan-400/50 text-cyan-200', 'bg-cyan-600 text-white', 'text-cyan-300', '5 Units'),
            'CH 04': ('bg-[#111F36] border-emerald-400/50 text-emerald-200', 'bg-emerald-600 text-white', 'text-emerald-300', '33 Units'),
        }
        card_cls, badge_cls, sub_cls, count_str = ch_colors.get(num, ('bg-[#111F36] border-slate-700 text-white', 'bg-slate-700 text-white', 'text-slate-300', ''))
        
        item_html = f'''
                <!-- Chapter Section Divider -->
                <div class="pt-2.5 pb-1">
                    <div class="slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 {card_cls} border shadow-sm" id="nav-item-{i}" onclick="goToSlide({i})">
                        <span class="shrink-0 px-2 h-6 rounded-lg {badge_cls} flex items-center justify-center text-xs font-bold mt-0.5 item-num-badge">{num}</span>
                        <div class="flex-1 min-w-0">
                            <div class="flex items-center justify-between">
                                <span class="text-xs md:text-sm font-bold text-white truncate item-title">{title}</span>
                            </div>
                            <div class="flex items-center justify-between text-2xs {sub_cls} mt-0.5 font-bold">
                                <span class="truncate">{badge}</span>
                                <span class="bg-black/40 px-1.5 py-0.2 rounded shrink-0">{count_str}</span>
                            </div>
                        </div>
                    </div>
                </div>'''
    else:
        # Regular unit item with clean nested look
        item_html = f'''
                <div class="slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 hover:bg-slate-50 border border-transparent pl-4" id="nav-item-{i}" onclick="goToSlide({i})">
                    <span class="shrink-0 w-6 h-6 rounded-lg bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-medium mt-0.5 item-num-badge">{num}</span>
                    <div class="flex-1 min-w-0">
                        <div class="text-xs md:text-sm font-semibold text-slate-700 break-keep leading-snug item-title flex items-start space-x-1.5">
                            <span class="scale-75 shrink-0 mt-0.5">{icon_svg}</span>
                            <span class="truncate">{title}</span>
                        </div>
                        <div class="text-2xs text-slate-400 mt-0.5 font-medium truncate">{badge} • {subtitle}</div>
                    </div>
                </div>'''
    sidebar_items_html.append(item_html)

full_sidebar_nav = '\n'.join(sidebar_items_html)

# 3. Build Portal View Stage Articles HTML (All 58 slides 1:1)
portal_articles_html = []
for i, s in enumerate(slides):
    num = s['num']
    badge = s['badge']
    badge_class = s['badge_class']
    title = s['title']
    subtitle = s['subtitle']
    body = s['body']
    icon_svg = s['app_icon_svg']
    full_chapter = s['full_chapter_name']
    
    is_cover = (num == 'COVER')
    is_index = (num == 'INDEX')
    is_divider = num.startswith('CH ')
    
    if is_cover:
        # MS Build pure black cover article
        art_html = f'''
        <article class="max-w-5xl mx-auto fhd-card-stage p-6 md:p-8 lg:p-10 slide-page flex flex-col justify-between shadow-2xl relative overflow-hidden bg-black text-white border-2 border-zinc-800 my-auto min-h-[580px]" id="portal-slide-{i}">
            <div class="my-auto py-2 text-base w-full">
                {body}
            </div>
            <div class="mt-6 pt-4 border-t border-zinc-800 flex items-center justify-between text-sm text-slate-400 font-medium">
                <span class="font-bold text-slate-200 flex items-center space-x-2">
                    <span class="scale-75">{icon_svg}</span>
                    <span>{full_chapter}</span>
                </span>
                <span class="text-xs text-slate-400 font-bold">{num}</span>
            </div>
        </article>'''
    elif is_index:
        # 3D Copilot Studio Fluid Style for Index
        art_html = f'''
        <article class="max-w-5xl mx-auto fhd-card-stage p-6 md:p-8 lg:p-10 slide-page flex flex-col justify-between shadow-2xl relative overflow-hidden bg-gradient-to-br from-slate-50 via-indigo-50/20 to-purple-50/20 text-slate-900 border-2 border-indigo-100 my-auto min-h-[580px]" id="portal-slide-{i}">
            <div class="my-auto py-2 text-base w-full">
                {body}
            </div>
            <div class="mt-6 pt-4 border-t border-slate-200 flex items-center justify-between text-sm text-slate-600 font-medium">
                <span class="font-bold text-slate-800 flex items-center space-x-2">
                    <span class="scale-75">{icon_svg}</span>
                    <span>{full_chapter}</span>
                </span>
                <span class="text-xs text-slate-500 font-bold">{num}</span>
            </div>
        </article>'''
    elif is_divider:
        # Microsoft 365 Navy & Logo Divider (Prominent Title Only)
        art_html = f'''
        <article class="max-w-5xl mx-auto fhd-card-stage p-8 md:p-12 lg:p-14 slide-page flex flex-col justify-between shadow-2xl relative overflow-hidden bg-gradient-to-br from-[#16253D] via-[#0F1B2E] to-[#0A1322] text-white border-2 border-slate-700/60 my-auto min-h-[580px]" id="portal-slide-{i}">
            <div class="my-auto py-2 text-base w-full">
                {body}
            </div>
            <div class="mt-6 pt-4 border-t border-slate-700/50 flex items-center justify-between text-sm text-slate-400 font-medium">
                <span class="font-bold text-slate-200 flex items-center space-x-2">
                    <span class="scale-75">{icon_svg}</span>
                    <span>{full_chapter}</span>
                </span>
                <span class="text-xs text-slate-400 font-bold">{num}</span>
            </div>
        </article>'''
    else:
        # Standard white article for regular units
        num_label = f"UNIT {num}" if not (num.startswith('CH') or num in ['COVER', 'INDEX']) else num
        art_html = f'''
        <article class="max-w-5xl mx-auto fhd-card-stage p-6 md:p-8 lg:p-10 slide-page flex flex-col justify-between bg-white border border-slate-200 my-auto min-h-[580px]" id="portal-slide-{i}">
            <div>
                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center space-x-2.5">
                        <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-bold uppercase tracking-wider {badge_class} border flex items-center space-x-2 shadow-2xs">
                            <span class="scale-75">{icon_svg}</span>
                            <span>{full_chapter} • {badge}</span>
                        </span>
                    </div>
                    <span class="font-mono text-xs md:text-sm font-bold text-slate-400">{num_label} (SLIDE {(i + 1):02d} / {len(slides):02d})</span>
                </div>
                <h1 class="text-xl md:text-2xl lg:text-[1.85rem] font-black text-slate-900 mb-2.5 leading-tight tracking-tight text-center max-w-4xl mx-auto" title="{title}">{title}</h1>
                <p class="text-base md:text-lg text-slate-600 font-medium mb-6 max-w-3xl mx-auto break-keep text-center leading-relaxed">{subtitle}</p>
            </div>
            <div class="my-auto py-2 text-base w-full">
                {body}
            </div>
            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-sm text-slate-600 font-medium">
                <span class="font-bold text-slate-800 flex items-center space-x-2">
                    <span class="scale-75">{icon_svg}</span>
                    <span>{full_chapter}</span>
                </span>
                <span class="font-mono text-xs text-slate-400 font-bold">{num_label}</span>
            </div>
        </article>'''
    portal_articles_html.append(art_html)

full_portal_stage = '\n'.join(portal_articles_html)

# 4. Enhance renderSlideContent and updateActiveStatus JS Functions (Prominent Title on Dividers)
update_and_render_js = '''
        function updateActiveStatus(index, shouldScrollNav = true) {
            if (index < 0 || index >= slidesData.length) return;
            currentSlideIndex = index;
            const slide = slidesData[index];

            // 1. Update Top Theme Banner
            const bannerText = document.getElementById('bannerAppText');
            const bannerIcon = document.getElementById('bannerAppIconSvg');
            const bannerTitle = document.getElementById('bannerSlideTitle');
            if (bannerText) bannerText.textContent = slide.app_name.toUpperCase();
            if (bannerIcon) bannerIcon.innerHTML = slide.app_icon_svg;
            if (bannerTitle) bannerTitle.textContent = slide.title;

            // 2. Update Sidebar App Banner & Unit Counter
            const sideIcon = document.getElementById('activeAppIcon');
            const sideName = document.getElementById('activeAppName');
            const sidePart = document.getElementById('activePartNum');
            const sideCounter = document.getElementById('slideCounterBadge');
            if (sideIcon) sideIcon.innerHTML = slide.app_icon_svg;
            if (sideName) sideName.textContent = slide.app_name;
            if (sidePart) sidePart.textContent = slide.full_chapter_name;
            if (sideCounter) sideCounter.textContent = `${slide.num} / ${slidesData.length.toString().padStart(2, '0')}`;

            // 3. Highlight Active Sidebar Nav Item
            document.querySelectorAll('.slide-nav-item').forEach((item, i) => {
                const s = slidesData[i];
                const isHero = (s.num === 'COVER' || s.num === 'INDEX' || s.num.startsWith('CH '));
                
                if (i === index) {
                    if (isHero) {
                        item.classList.add('ring-2', 'ring-rose-500', 'shadow-md', 'scale-[1.02]');
                    } else {
                        item.className = `slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 bg-rose-50/80 border-rose-300 border shadow-xs pl-4`;
                        const badge = item.querySelector('.item-num-badge');
                        const title = item.querySelector('.item-title');
                        if (badge) badge.className = `shrink-0 w-6 h-6 rounded-lg bg-[#E60000] text-white flex items-center justify-center font-mono text-xs font-bold mt-0.5 item-num-badge shadow-xs`;
                        if (title) title.className = `text-xs md:text-sm font-black text-slate-950 break-keep leading-snug item-title flex items-start space-x-1.5`;
                    }
                    if (shouldScrollNav) {
                        item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }
                } else {
                    if (isHero) {
                        item.classList.remove('ring-2', 'ring-rose-500', 'scale-[1.02]');
                    } else {
                        item.className = `slide-nav-item p-2.5 rounded-xl cursor-pointer transition-all text-left flex items-start space-x-2.5 hover:bg-slate-50 border border-transparent pl-4`;
                        const badge = item.querySelector('.item-num-badge');
                        const title = item.querySelector('.item-title');
                        if (badge) badge.className = `shrink-0 w-6 h-6 rounded-lg bg-slate-100 text-slate-600 flex items-center justify-center font-mono text-xs font-medium mt-0.5 item-num-badge`;
                        if (title) title.className = `text-xs md:text-sm font-semibold text-slate-700 break-keep leading-snug item-title flex items-start space-x-1.5`;
                    }
                }
            });

            // 4. Update Top Chapter Pills
            document.querySelectorAll('.part-pill-btn').forEach((btn, pIdx) => {
                if (pIdx === slide.part_idx) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            // 5. Update Bottom Progress Bar
            const progressBar = document.getElementById('progressBar');
            if (progressBar) {
                const progress = ((index + 1) / slidesData.length) * 100;
                progressBar.style.width = `${progress}%`;
            }
        }

        function renderSlideContent(index) {
            if (index < 0 || index >= slidesData.length) return;
            const slide = slidesData[index];
            const card = document.getElementById('activeSlideCard');
            if (!card) return;

            const isCover = (slide.num === 'COVER');
            const isIndex = (slide.num === 'INDEX');
            const isDivider = slide.num.startsWith('CH ');
            const numLabel = (slide.num.startsWith("CH") || slide.num === "COVER" || slide.num === "INDEX") ? slide.num : "UNIT " + slide.num;

            if (isCover) {
                // Microsoft Build Keynote Style for Cover
                card.className = 'w-full max-w-5xl mx-auto fhd-card-stage p-6 md:p-8 lg:p-10 flex flex-col justify-between my-auto min-h-[580px] bg-black text-white rounded-3xl border-2 border-zinc-800 shadow-2xl transition-all duration-300 relative overflow-hidden';
                card.innerHTML = `
                    <div class="my-auto py-1 text-base w-full">
                        ${slide.body}
                    </div>
                    <div class="mt-4 pt-3 border-t border-zinc-800 flex items-center justify-between text-sm text-slate-400 font-medium">
                        <span class="font-bold text-slate-200 flex items-center space-x-2">
                            <span class="scale-75">${slide.app_icon_svg}</span>
                            <span>${slide.full_chapter_name}</span>
                        </span>
                        <div class="flex items-center space-x-2.5">
                            <button onclick="nextSlide()" class="px-5 py-1.5 bg-[#00E5FF] hover:bg-cyan-300 active:scale-95 text-black font-black rounded-full shadow-md transition-all text-sm">교육 시작하기 ➔</button>
                        </div>
                    </div>
                `;
            } else if (isIndex) {
                // Microsoft Copilot 3D Fluid Style for Index
                card.className = 'w-full max-w-5xl mx-auto fhd-card-stage p-6 md:p-8 lg:p-10 flex flex-col justify-between my-auto min-h-[580px] bg-gradient-to-br from-slate-50 via-indigo-50/20 to-purple-50/20 text-slate-900 rounded-3xl border-2 border-indigo-100 shadow-2xl transition-all duration-300 relative overflow-hidden';
                card.innerHTML = `
                    <div class="my-auto py-1 text-base w-full">
                        ${slide.body}
                    </div>
                    <div class="mt-4 pt-3 border-t border-slate-200 flex items-center justify-between text-sm text-slate-600 font-medium">
                        <span class="font-bold text-slate-800 flex items-center space-x-2">
                            <span class="scale-75">${slide.app_icon_svg}</span>
                            <span>${slide.full_chapter_name}</span>
                        </span>
                        <div class="flex items-center space-x-2.5">
                            <button onclick="prevSlide()" class="px-4 py-1.5 bg-slate-100 hover:bg-slate-200 active:bg-slate-300 text-slate-800 font-bold rounded-full transition-all text-sm focus-visible:ring-2 focus-visible:ring-slate-400">◀ 이전</button>
                            <button onclick="nextSlide()" class="px-5 py-1.5 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-indigo-600 hover:to-indigo-700 active:scale-95 text-white font-bold rounded-full shadow-md transition-all text-sm focus-visible:ring-2 focus-visible:ring-indigo-500">다음 ▶</button>
                        </div>
                    </div>
                `;
            } else if (isDivider) {
                // Microsoft 365 Navy & Logo Divider Card (Prominent Title Only)
                card.className = 'w-full max-w-5xl mx-auto fhd-card-stage p-8 md:p-12 lg:p-14 flex flex-col justify-between my-auto min-h-[580px] bg-gradient-to-br from-[#16253D] via-[#0F1B2E] to-[#0A1322] text-white rounded-3xl border-2 border-slate-700/60 shadow-2xl transition-all duration-300 relative overflow-hidden';
                card.innerHTML = `
                    <div class="my-auto py-2 text-base w-full">
                        ${slide.body}
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-700/50 flex items-center justify-between text-sm text-slate-400 font-medium">
                        <span class="font-bold text-slate-200 flex items-center space-x-2">
                            <span class="scale-75">${slide.app_icon_svg}</span>
                            <span>${slide.full_chapter_name}</span>
                        </span>
                        <div class="flex items-center space-x-2.5">
                            <button onclick="prevSlide()" class="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 active:bg-slate-600 text-slate-200 font-bold rounded-full transition-all text-sm focus-visible:ring-2 focus-visible:ring-slate-500">◀ 이전</button>
                            <button onclick="nextSlide()" class="px-5 py-1.5 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-indigo-600 hover:to-indigo-700 active:scale-95 text-white font-bold rounded-full shadow-md transition-all text-sm focus-visible:ring-2 focus-visible:ring-indigo-500">다음 ▶</button>
                        </div>
                    </div>
                `;
            } else {
                // Clean Standard White Card for Regular Units
                card.className = 'w-full max-w-5xl mx-auto fhd-card-stage p-6 md:p-8 lg:p-10 flex flex-col justify-between my-auto min-h-[580px] bg-white border border-slate-200 shadow-level-2 transition-all duration-300';
                card.innerHTML = `
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <div class="flex items-center space-x-2.5">
                                <span class="px-3.5 py-1 rounded-full text-xs md:text-sm font-bold uppercase tracking-wider ${slide.badge_class} border flex items-center space-x-2 shadow-2xs">
                                    <span class="scale-75">${slide.app_icon_svg}</span>
                                    <span>${slide.full_chapter_name} • ${slide.badge}</span>
                                </span>
                            </div>
                            <span class="font-mono text-xs md:text-sm font-bold text-slate-400">${numLabel} (SLIDE ${(index + 1).toString().padStart(2, "0")} / ${slidesData.length.toString().padStart(2, "0")})</span>
                        </div>
                        <h1 class="text-xl md:text-2xl lg:text-[1.85rem] font-black text-slate-900 mb-2.5 leading-tight tracking-tight whitespace-nowrap overflow-hidden text-ellipsis max-w-4xl mx-auto text-center" title="${slide.title}">${slide.title}</h1>
                        <p class="text-base md:text-lg text-slate-600 font-medium mb-6 max-w-3xl mx-auto break-keep text-center leading-relaxed">${slide.subtitle}</p>
                    </div>
                    <div class="my-auto py-2 text-base">
                        ${slide.body}
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-sm text-slate-600 font-medium">
                        <span class="font-bold text-slate-800 flex items-center space-x-2">
                            <span class="scale-75">${slide.app_icon_svg}</span>
                            <span>${slide.full_chapter_name}</span>
                        </span>
                        <div class="flex items-center space-x-2.5">
                            <button onclick="prevSlide()" class="px-4 py-1.5 bg-slate-100 hover:bg-slate-200 active:bg-slate-300 text-slate-800 font-bold rounded-full transition-all text-sm focus-visible:ring-2 focus-visible:ring-slate-400">◀ 이전</button>
                            <button onclick="nextSlide()" class="px-5 py-1.5 bg-[#111317] hover:bg-[#E60000] active:scale-95 text-white font-bold rounded-full shadow-xs transition-all text-sm focus-visible:ring-2 focus-visible:ring-rose-500">다음 ▶</button>
                        </div>
                    </div>
                `;
            }
        }
'''

# 5. Precise Assembly of HTML using exact string offsets

# Step A: Replace slidesData
content_a = content[:start_json] + clean_json + content[semicolon_idx:]

# Step B: Replace Sidebar (#slideListNav content)
nav_start = content_a.find('id="slideListNav"')
nav_tag_end = content_a.find('>', nav_start) + 1
nav_foot = content_a.find('<!-- Sidebar Footer -->', nav_start)
nav_div_end = content_a.rfind('</div>', 0, nav_foot)

content_b = content_a[:nav_tag_end] + '\n' + full_sidebar_nav + '\n            ' + content_a[nav_div_end:]

# Step C: Replace Portal View Stage (#portalViewStage content)
p_start = content_b.find('id="portalViewStage"')
p_tag_end = content_b.find('>', p_start) + 1
p_track = content_b.find('<!-- Bottom Progress Track -->', p_start)
p_div_end = content_b.rfind('</div>', 0, p_track)

content_c = content_b[:p_tag_end] + '\n' + full_portal_stage + '\n' + content_b[p_div_end:]

# Step D: Replace updateActiveStatus and renderSlideContent functions
func1_start = content_c.find('function updateActiveStatus(')
func_render_slide = content_c.find('function renderSlide(index)', func1_start)

content_final = content_c[:func1_start] + update_and_render_js.strip() + '\n\n        ' + content_c[func_render_slide:]

# Write to AX_CA_Edu_GHLEE.html
with open('AX_CA_Edu_GHLEE.html', 'w', encoding='utf-8') as f:
    f.write(content_final)

print('SUCCESS: Chapter Dividers updated with Microsoft 365 Navy background & logo with prominent titles!')
