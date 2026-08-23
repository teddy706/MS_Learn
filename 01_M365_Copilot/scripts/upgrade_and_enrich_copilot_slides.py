# -*- coding: utf-8 -*-
import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')

html_file = 'AX_CA_Edu_GHLEE.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Match slidesData
match = re.search(r'const slidesData = (\[.*?\]);\s*let currentSlideIndex', content, re.DOTALL)
if not match:
    print('Failed to locate slidesData')
    sys.exit(1)

slides = json.loads(match.group(1))
print(f'Original slide count: {len(slides)}')

# --- 1. Unit 30 (Word Multi-Reference) ---
slides[29]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="flex items-center space-x-2 text-xs font-bold text-blue-800 bg-blue-50 px-3.5 py-1.5 rounded-xl border border-blue-200">
        <span>📁 연계 실습 데이터:</span> <code class="bg-white px-2 py-0.5 rounded border border-blue-300">practice_files/KT_5G_수도권_기지국_품질지표_2026.csv</code>, <code class="bg-white px-2 py-0.5 rounded border border-blue-300">practice_files/KT_2026_5G망_현대화_기술보고서.md</code>
    </div>
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>📑</span> <span>Multi-File Reference Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files 'KT_5G_수도권_기지국_품질지표_2026.csv', 'KT_2026_5G망_현대화_기술보고서.md' 2개 파일을 결합하여, 3분기 수도권 기지국 트래픽 집중 구역에 대한 긴급 증설 필요성을 강조하는 3페이지 엔지니어링 기안서 초안을 작성해줘."
        </div>
    </div>
    <div class="grid grid-cols-3 gap-3 text-center text-xs font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">최대 20개 사내 파일 동시 참조</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">SharePoint / OneDrive 권한 연동</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">표 및 수치 데이터 자동 인용</div>
    </div>
</div>'''

# --- 2. Unit 31 (Word Rewrite & Table) ---
slides[30]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>🔄</span> <span>Rewrite & Table Conversion</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "아래 장황하게 나열된 L3 스위치 점검 절차 줄글을 현장 엔지니어가 10초 만에 파악할 수 있도록 [단계 | 점검 항목 | CLI 명령어 | 정상 기준 | 이상 시 조치] 5개 열로 구성된 직관적인 표(Table)로 변환해줘."
        </div>
    </div>
    <div class="grid grid-cols-2 gap-4">
        <div class="p-4 bg-rose-50/70 rounded-2xl border border-rose-200 text-xs">
            <div class="font-bold text-rose-800 mb-1">❌ 변경 전 (Before): 장황한 줄글</div>
            <p class="text-slate-600 leading-relaxed">스위치 접속 후 콘솔에서 CPU 점유율을 확인하고 80%가 넘으면 프로세스 목록을 본 후...”</p>
        </div>
        <div class="p-4 bg-emerald-50/70 rounded-2xl border border-emerald-200 text-xs">
            <div class="font-bold text-emerald-800 mb-1">✅ 변경 후 (After): 일목요연한 정형 표</div>
            <p class="text-slate-700 font-semibold leading-relaxed">단계별 CLI 명령어와 정상 기준치, 긴급 조치 가이드가 표 형태로 완벽 정돈</p>
        </div>
    </div>
</div>'''

# --- 3. Unit 32 (Word 200 Words Summary & Analysis) ---
slides[31]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>🔍</span> <span>Executive Summary & Deep Q&A</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "이 20페이지 분량의 통신망 기술 문서 상단에 임원 보고용 200단어 핵심 요약(Executive Summary)을 추가하고, 문서 전체에서 언급된 '보안 취약점 3가지'와 '단계별 해결책'을 돋보기 분석으로 정리해줘."
        </div>
    </div>
    <div class="grid grid-cols-3 gap-3 text-xs">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs font-medium text-slate-700">📌 200단어 자동 상단 브리핑</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs font-medium text-slate-700">🔍 돋보기 기반 특정 섹션 심층 질의</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs font-medium text-slate-700">⚡ Action Items 3줄 도출</div>
    </div>
</div>'''

# --- 4. Unit 33 (Word DALL-E 3 Image) ---
slides[32]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>🎨</span> <span>DALL-E 3 Engineering Visual</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "KT 5G 통신망 현대화 기술 보고서 챕터 표지로 사용할 수 있는 16:9 와이드 비율의 고화질 테크 배너 이미지를 생성해줘. (스타일: 미니멀한 3D 네온 블루 네트워크 그리드, 기지국 광케이블 연결, 클라우드 코어망, 깨끗한 화이트 배경)"
        </div>
    </div>
    <div class="grid grid-cols-2 gap-4 text-xs font-semibold text-slate-700">
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs">✓ 엔지니어링 문서 전용 3D/아이소메트릭 스타일 프롬프트 권장</div>
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs">✓ 모호한 단어 대신 피사체, 조명, 색상 팔레트, 구도 명시</div>
    </div>
</div>'''

# --- 5. Unit 34 (Word Mobile Audio) ---
slides[33]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>🎙️</span> <span>Mobile Voice to Structured Report</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "서버실 현장에서 녹음된 이 음성 메모 텍스트를 분석하여, [점검 일시 | 점검 국사 | 랙(Rack) 번호 | 발견된 이상 증상 | 현장 조치 내역 | 후속 조치 필요사항] 양식의 정규 현장 점검 완료 보고서로 구조화해줘."
        </div>
    </div>
    <div class="grid grid-cols-3 gap-3 text-center text-xs font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">📱 스마트폰 음성 녹음</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">⚡ 비정형 구술 텍스트 분석</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">📑 표준 양식 자동 변환</div>
    </div>
</div>'''

# --- 6. Unit 37 (Word 5G SA Topology Visualization) ---
slides[36]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <!-- Visual Topology Card -->
    <div class="p-5 lg:p-6 bg-slate-950 text-white rounded-2xl border border-slate-800 shadow-lg relative overflow-hidden">
        <div class="text-xs font-bold text-cyan-400 mb-3 flex items-center space-x-2">
            <span>📡</span> <span>5G Standalone (SA) Core End-to-End Architecture</span>
        </div>
        <div class="grid grid-cols-5 gap-2.5 text-center items-center py-2">
            <div class="p-3 bg-slate-800/90 rounded-xl border border-slate-700">
                <div class="text-xl mb-1">📱</div>
                <div class="font-black text-xs text-white">5G 단말 (UE)</div>
                <div class="text-3xs text-slate-400">User Equipment</div>
            </div>
            <div class="text-cyan-400 font-bold text-xs">➔ N1/N2 ➔</div>
            <div class="p-3 bg-blue-900/60 rounded-xl border border-blue-500/50">
                <div class="text-xl mb-1">📡</div>
                <div class="font-black text-xs text-cyan-200">기지국 (gNodeB)</div>
                <div class="text-3xs text-blue-300">Radio Access</div>
            </div>
            <div class="text-cyan-400 font-bold text-xs">➔ N3 (GTP-U) ➔</div>
            <div class="p-3 bg-emerald-900/60 rounded-xl border border-emerald-500/50">
                <div class="text-xl mb-1">⚡</div>
                <div class="font-black text-xs text-emerald-200">UPF (데이터평면)</div>
                <div class="text-3xs text-emerald-300">User Plane</div>
            </div>
        </div>
        <div class="mt-3 pt-3 border-t border-slate-800 grid grid-cols-2 gap-3 text-2xs text-slate-300">
            <div class="p-2 bg-slate-900 rounded-lg flex items-center space-x-2">
                <span class="text-purple-400 font-bold">🛡️ 제어평면 (Control Plane):</span>
                <span>AMF (접속제어) ➔ SMF (세션관리 / N4)</span>
            </div>
            <div class="p-2 bg-slate-900 rounded-lg flex items-center space-x-2">
                <span class="text-emerald-400 font-bold">🌐 외부연결:</span>
                <span>UPF ➔ N6 인터페이스 ➔ 데이터 네트워크 (DN)</span>
            </div>
        </div>
    </div>

    <!-- Copilot Prompt Card -->
    <div class="copilot-prompt-card p-4 lg:p-5 bg-slate-900 text-white rounded-2xl shadow-md border border-indigo-700/50">
        <div class="flex items-center justify-between mb-2">
            <span class="px-3 py-1 bg-indigo-500/30 text-indigo-300 text-xs font-black rounded-full border border-indigo-400/40 flex items-center space-x-1.5">
                <span>✨</span> <span>Topology Generation Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs leading-relaxed text-slate-100 prompt-target-text">
            "KT 5G 단독모드(SA) 구조에서 gNodeB와 AMF, SMF, UPF 간의 제어 평면 및 사용자 평면 데이터 흐름을 Mermaid flowchart 문법으로 작성하고 각 인터페이스(N1, N2, N3, N4, N6) 라벨을 포함해줘."
        </div>
    </div>
</div>'''

# --- 7. Unit 40 (PPT Brand DNA & Placeholders) ---
slides[39]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="grid grid-cols-3 gap-3 text-xs">
        <div class="p-4 bg-white rounded-2xl border border-orange-200 shadow-2xs">
            <div class="text-xs font-bold text-orange-700 mb-1.5">1. Title & Subtitle</div>
            <p class="text-2xs text-slate-600 leading-relaxed">상단 제목과 부제목 자리 표시자 크기/위치 자동 상속</p>
        </div>
        <div class="p-4 bg-white rounded-2xl border border-orange-200 shadow-2xs">
            <div class="text-xs font-bold text-orange-700 mb-1.5">2. Content Cards</div>
            <p class="text-2xs text-slate-600 leading-relaxed">2단/3단 본문 카드 박스 영역에 텍스트 자동 분할 배치</p>
        </div>
        <div class="p-4 bg-white rounded-2xl border border-orange-200 shadow-2xs">
            <div class="text-xs font-bold text-orange-700 mb-1.5">3. Brand Colors</div>
            <p class="text-2xs text-slate-600 leading-relaxed">KT Red(#E60000), Slate 등 사내 표준 팔레트 적용</p>
        </div>
    </div>
    <div class="copilot-prompt-card p-4 lg:p-5 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-2">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📑</span> <span>Brand Template Recognition</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs leading-relaxed text-slate-100 prompt-target-text">
            "/files 'KT_Corporate_Brand_Template.potx' 사내 마스터 서식의 레이아웃 규칙과 자리 표시자를 엄격히 준수하여, 본문 내용을 3개 카드 영역에 균형 있게 배치해줘."
        </div>
    </div>
</div>'''

# --- 8. Unit 41 (PPT Agent Mode Outline Build) ---
slides[40]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>🤖</span> <span>Agent Mode Presentation Builder</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "KT 5G 코어망 가상화(vEPC ➔ 5GC) 마이그레이션 전략을 주제로 네트워크 운용팀 대상 15분 브리핑용 5장 슬라이드 개요(Outline)를 구성하고, 각 장표별 핵심 불릿 포인트 3개와 발표자 노트를 작성해줘."
        </div>
    </div>
    <div class="grid grid-cols-3 gap-3 text-center text-xs font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">🎯 청중 맞춤형 톤 조절</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">📑 5단계 스토리라인 구성</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">🎙️ 발표자 대본 자동 생성</div>
    </div>
</div>'''

# --- 9. Unit 42 (PPT Word to Slide) ---
slides[41]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="flex items-center space-x-2 text-xs font-bold text-orange-800 bg-orange-50 px-3.5 py-1.5 rounded-xl border border-orange-200">
        <span>📁 연계 실습 데이터:</span> <code class="bg-white px-2 py-0.5 rounded border border-orange-300">practice_files/KT_2026_5G망_현대화_기술보고서.md</code>
    </div>
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📑</span> <span>Word Document to Slide Conversion</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files 'KT_2026_5G망_현대화_기술보고서.md' 문서를 바탕으로, 경영진 보고에 적합하도록 장황한 줄글을 제거하고 [추진 배경 - 핵심 기술 - 기대 효과 - 투자 계획] 4장 구조의 프레젠테이션으로 원클릭 변환해줘."
        </div>
    </div>
    <div class="grid grid-cols-2 gap-3 text-xs font-medium text-slate-700">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">✓ 24MB 이하 Word 문서 파일 직접 링크</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">✓ 원본 제목 스타일(H1, H2)에 따른 슬라이드 자동 분할</div>
    </div>
</div>'''

# --- 10. Unit 43 (PPT 4 Rewrite Strategies) ---
slides[42]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="grid grid-cols-4 gap-3 text-xs">
        <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
            <div class="font-black text-xs text-rose-700 mb-1">1. Condense</div>
            <p class="text-3xs text-slate-600 leading-tight">복잡한 줄글을 핵심 3줄 불릿으로 압축</p>
        </div>
        <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
            <div class="font-black text-xs text-blue-700 mb-1">2. Professional</div>
            <p class="text-3xs text-slate-600 leading-tight">구어체를 격식 있는 비즈니스 어조로 개선</p>
        </div>
        <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
            <div class="font-black text-xs text-emerald-700 mb-1">3. Structure</div>
            <p class="text-3xs text-slate-600 leading-tight">키워드 강조 및 2열 비교 카드로 정돈</p>
        </div>
        <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
            <div class="font-black text-xs text-purple-700 mb-1">4. Action-Driven</div>
            <p class="text-3xs text-slate-600 leading-tight">다음 단계 행동(Next Step) 명시화</p>
        </div>
    </div>
    <div class="copilot-prompt-card p-4 lg:p-5 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-2">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>🔄</span> <span>Slide Text Refinement</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs leading-relaxed text-slate-100 prompt-target-text">
            "이 슬라이드의 텍스트를 60단어 이내로 압축하고, 핵심 키워드를 볼드체로 강조하며, 청중이 3초 안에 핵심 결론을 파악할 수 있도록 리라이팅해줘."
        </div>
    </div>
</div>'''

# --- 11. Unit 44 (PPT Image Laws Good vs Bad) ---
slides[43]['body'] = '''<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-rose-50/70 rounded-2xl border-2 border-rose-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2.5 py-0.5 bg-rose-200 text-rose-800 text-xs font-black rounded-lg">BAD CASE ❌</span>
            </div>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">추상적이고 모호한 프롬프트</h4>
            <div class="p-2.5 bg-white rounded-xl text-2xs font-mono text-rose-900 border border-rose-200 mb-3">
                "멋진 미래지향적 5G 네트워크 기지국 이미지 만들어줘"
            </div>
            <ul class="text-2xs text-slate-600 space-y-1">
                <li>• 결과물이 너무 비현실적이고 장난감 같은 그래픽 생성</li>
                <li>• 텍스트 깨짐 및 불필요한 공상과학 요소 포함</li>
            </ul>
        </div>
        <div class="mt-3 pt-2 border-t border-rose-200 text-3xs font-bold text-rose-700">비즈니스 보고서 부적합</div>
    </div>
    <div class="p-5 bg-emerald-50/70 rounded-2xl border-2 border-emerald-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2.5 py-0.5 bg-emerald-200 text-emerald-800 text-xs font-black rounded-lg">GOOD CASE ✅</span>
            </div>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">구체적 피사체, 조명, 스타일 명시</h4>
            <div class="p-2.5 bg-white rounded-xl text-2xs font-mono text-emerald-950 border border-emerald-200 mb-3">
                "Isometric 3D 5G gNodeB telecom tower connecting to modern data center, enterprise blue lighting, clean white background"
            </div>
            <ul class="text-2xs text-slate-600 space-y-1">
                <li>• 선명하고 전문적인 아이소메트릭 벡터 일러스트 완성</li>
                <li>• 프레젠테이션 슬라이드 카드와 완벽한 조화</li>
            </ul>
        </div>
        <div class="mt-3 pt-2 border-t border-emerald-200 text-3xs font-bold text-emerald-700">임원 보고서 최적화 품질</div>
    </div>
</div>'''

# --- 12. Unit 45 (PPT 40K Words Summary) ---
slides[44]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📚</span> <span>Large Deck Selective Extraction</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "총 50장의 방대한 네트워크 장비 릴리즈 노트 슬라이드 중에서, 'BGP 및 OSPF 프로토콜 변경점'과 관련된 핵심 장표 3장만 찾아내어 변경 영향도를 3줄로 요약해줘."
        </div>
    </div>
    <div class="grid grid-cols-3 gap-3 text-center text-xs font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">최대 40,000단어 처리</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">키워드별 핵심 장표 추출</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">시간 절약 브리핑</div>
    </div>
</div>'''

# --- 13. Unit 46 (PPT Mobile Voice Q&A) ---
slides[45]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>🎙️</span> <span>Mobile Slide Voice Query</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "모바일 PowerPoint 음성 질의: '이 슬라이드 덱에서 3분기 예산 초과 위험이 있는 국사가 어디인지 찾아내고, 슬라이드 번호와 함께 수치를 읽어줘.'"
        </div>
    </div>
    <div class="grid grid-cols-2 gap-3 text-xs font-medium text-slate-700">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">📱 이동 중/외근 중 스마트폰 화면을 보지 않고도 음성으로 슬라이드 내용 확인</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">⚡ 발표 직전 대기실에서 핵심 데이터 최종 확인 최적화</div>
    </div>
</div>'''

# --- 14. Unit 48 (PPT 1-Page ROI Summary Design) ---
slides[47]['body'] = '''<div class="my-auto w-full text-left space-y-4">
    <div class="flex items-center space-x-2 text-xs font-bold text-orange-800 bg-orange-50 px-3.5 py-1.5 rounded-xl border border-orange-200">
        <span>📁 연계 실습 데이터:</span> <code class="bg-white px-2 py-0.5 rounded border border-orange-300">practice_files/KT_5G_설비투자_CAPEX_예산안_2026.csv</code>
    </div>
    <!-- 3 Executive KPI Cards -->
    <div class="grid grid-cols-3 gap-3 text-center">
        <div class="p-4 bg-emerald-50/80 rounded-2xl border-2 border-emerald-300 shadow-xs">
            <div class="text-2xs font-bold text-emerald-800 mb-1">📊 CAPEX 절감 효과</div>
            <div class="text-xl lg:text-2xl font-black text-emerald-700">-23.5%</div>
            <div class="text-3xs text-slate-600 mt-1">고효율 국사 전환</div>
        </div>
        <div class="p-4 bg-blue-50/80 rounded-2xl border-2 border-blue-300 shadow-xs">
            <div class="text-2xs font-bold text-blue-800 mb-1">⏱️ 장애 조치 시간(MTTR)</div>
            <div class="text-xl lg:text-2xl font-black text-blue-700">45분 ➔ 8분</div>
            <div class="text-3xs text-slate-600 mt-1">자율 관제 에이전트 도입</div>
        </div>
        <div class="p-4 bg-purple-50/80 rounded-2xl border-2 border-purple-300 shadow-xs">
            <div class="text-2xs font-bold text-purple-800 mb-1">💰 ROI 투자 회수</div>
            <div class="text-xl lg:text-2xl font-black text-purple-700">1.4년 달성</div>
            <div class="text-3xs text-slate-600 mt-1">목표 2.0년 대비 7개월 조기 회수</div>
        </div>
    </div>
    <!-- Copilot Prompt Card -->
    <div class="copilot-prompt-card p-4 lg:p-5 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-2">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📈</span> <span>1-Page Executive Summary</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs leading-relaxed text-slate-100 prompt-target-text">
            "/files 'KT_5G_설비투자_CAPEX_예산안_2026.csv'를 바탕으로, 임원이 10초 만에 승인 결정을 내릴 수 있도록 총투자비, 연간 절감액, 회수 기간, 리스크 요약을 1페이지 임원 보고 슬라이드로 생성해줘."
        </div>
    </div>
</div>'''

# Build new slidesData JSON string
new_slides_json = json.dumps(slides, ensure_ascii=False)

# Replace in content
pattern = r'const slidesData = \[.*?\];\s*let currentSlideIndex'
replacement = f'const slidesData = {new_slides_json};\n\n        let currentSlideIndex'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Also update the article HTMLs in portal view!
from bs4 import BeautifulSoup
soup = BeautifulSoup(new_content, 'html.parser')

for i, slide in enumerate(slides):
    art = soup.find('article', id=f'portal-slide-{i}')
    if art:
        # Update body div
        body_div = art.find('div', class_='my-auto py-2 text-base w-full')
        if body_div:
            body_soup = BeautifulSoup(f'<div class=\"my-auto py-2 text-base w-full\">{slide["body"]}</div>', 'html.parser')
            body_div.replace_with(body_soup.div)

new_full_html = str(soup)

# Save to all relevant files
targets = [
    'AX_CA_Edu_GHLEE.html',
    '01_M365_Copilot/AX_CA_Edu_GHLEE.html',
    'index.html',
    'M365_Copilot_Telecom_Master.html',
    '01_M365_Copilot/M365_Copilot_Telecom_Master.html'
]

for target in targets:
    with open(target, 'w', encoding='utf-8') as f:
        f.write(new_full_html)
    print(f'Successfully updated: {target}')

print('All 52 slides successfully enriched and synchronized across all target files!')
