import re
import json

# Load existing data
with open("update_slide_titles_direct.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

# Re-structure each unit's body HTML into the high-end Microsoft 365 Copilot Official Design
# Features:
# 1. Official Copilot Prompt Bubble with 'Try this prompt' chip & copy button
# 2. Modern Bento Grid Cards with Fluent Icon accents
# 3. Clean Comparison Cards (Legacy/Web AI vs M365 Copilot Work IQ)
# 4. Step-by-Step Onboarding Process Cards

# Let's craft specific high-fidelity templates for all 31 units matching MS Learn / Copilot Chat / Onboarding styles

unit_bodies = {}

# Unit 01: Web AI vs M365 Copilot (Official MS Comparison Card Style)
unit_bodies["01"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <!-- Web General AI Card -->
    <div class="p-5 lg:p-6 bg-slate-50/80 rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2.5 mb-3">
                <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-lg uppercase tracking-wide">Web AI</span>
                <h3 class="text-base lg:text-lg font-bold text-slate-800">웹 기반 범용 AI (ChatGPT 등)</h3>
            </div>
            <ul class="space-y-2.5 text-xs lg:text-sm text-slate-600">
                <li class="flex items-start space-x-2"><span class="text-rose-500 font-bold">✕</span> <span><strong>업무 맥락 부재:</strong> 사내 메일, Teams 대화, 결재 문서를 전혀 알지 못함</span></li>
                <li class="flex items-start space-x-2"><span class="text-rose-500 font-bold">✕</span> <span><strong>데이터 유출 위험:</strong> 입력 프롬프트가 외부 공용 모델 재학습에 노출</span></li>
                <li class="flex items-start space-x-2"><span class="text-rose-500 font-bold">✕</span> <span><strong>수동 복사-붙여넣기:</strong> 브라우저와 오피스 앱 간의 비효율적 단절</span></li>
                <li class="flex items-start space-x-2"><span class="text-rose-500 font-bold">✕</span> <span><strong>권한 제어 불가:</strong> 사내 보안 등급(ACL)에 따른 정보 격리 불가</span></li>
            </ul>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-200 text-2xs text-slate-600 font-semibold">범용 지식 검색 중심의 퍼블릭 웹 도우미</div>
    </div>

    <!-- Microsoft 365 Copilot Card -->
    <div class="p-5 lg:p-6 bg-gradient-to-br from-white via-indigo-50/30 to-blue-50/40 rounded-2xl border-2 border-indigo-300/80 shadow-xs flex flex-col justify-between relative overflow-hidden">
        <div class="absolute -right-6 -top-6 w-24 h-24 bg-gradient-to-br from-blue-400 to-indigo-600 rounded-full opacity-10 blur-xl"></div>
        <div>
            <div class="flex items-center space-x-2.5 mb-3">
                <span class="px-2.5 py-1 bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-xs font-black rounded-lg uppercase tracking-wide shadow-2xs">Work IQ AI</span>
                <h3 class="text-base lg:text-lg font-black text-slate-900">Microsoft 365 Copilot</h3>
            </div>
            <ul class="space-y-2.5 text-xs lg:text-sm text-slate-800">
                <li class="flex items-start space-x-2"><span class="text-emerald-600 font-bold">✓</span> <span><strong>Work IQ 사내 맥락 통합:</strong> 내 메일, 일정, SharePoint 문서를 즉시 연계 이해</span></li>
                <li class="flex items-start space-x-2"><span class="text-emerald-600 font-bold">✓</span> <span><strong>완벽한 보안 격리:</strong> Zero-Data Retention & 고객 데이터 학습 절대 배제</span></li>
                <li class="flex items-start space-x-2"><span class="text-emerald-600 font-bold">✓</span> <span><strong>오피스 내 네이티브 실행:</strong> Word, Excel, Teams, Outlook 내에서 직접 생성/수정</span></li>
                <li class="flex items-start space-x-2"><span class="text-emerald-600 font-bold">✓</span> <span><strong>Entra ID ACL 자동 준수:</strong> 내가 읽기 권한을 가진 문서에 한해서만 안전 답변</span></li>
            </ul>
        </div>
        <div class="mt-4 pt-3 border-t border-indigo-100 text-2xs text-indigo-900 font-bold">기업 내부 데이터를 안전하게 활용하는 엔터프라이즈 전담 동료</div>
    </div>
</div>
<div class="copilot-prompt-card mt-4 p-3.5 lg:p-4 bg-slate-900 text-white rounded-2xl flex items-center justify-between shadow-xs">
    <div class="flex items-center space-x-3 min-w-0">
        <span class="w-7 h-7 rounded-lg bg-gradient-to-tr from-indigo-500 to-pink-500 flex items-center justify-center shrink-0 text-xs">✨</span>
        <div class="text-xs lg:text-sm font-mono truncate text-slate-200">"웹 AI가 세상의 일반 지식을 아는 도우미라면, M365 Copilot은 '내 팀과 내 업무 맥락'을 가장 깊이 이해하는 전담 동료입니다."</div>
    </div>
    <button onclick="copyPromptText(this)" class="shrink-0 ml-3 px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20 flex items-center space-x-1">
        <span>📋</span> <span>복사</span>
    </button>
</div>
"""

# Unit 02: AI Paradigm Shift
unit_bodies["02"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 lg:p-6 bg-slate-50 rounded-2xl border border-slate-200 shadow-2xs">
        <div class="flex items-center space-x-2 mb-3">
            <span class="px-2.5 py-1 bg-slate-200 text-slate-700 text-xs font-bold rounded-lg">Gen 1</span>
            <h3 class="text-base lg:text-lg font-bold text-slate-800">어시스턴트 모드 (작성 도우미)</h3>
        </div>
        <ul class="space-y-2.5 text-xs lg:text-sm text-slate-600">
            <li>• 사람이 지시한 단일 텍스트 요약 및 초안 작성에 국한</li>
            <li>• 실시간 네트워크 상태 모니터링 및 자율적 연계 불가</li>
            <li>• 파일 복사 및 수동 프롬프트 입력에 과도한 시간 소모</li>
        </ul>
    </div>
    <div class="p-5 lg:p-6 bg-gradient-to-br from-indigo-50/50 to-blue-50/50 rounded-2xl border-2 border-indigo-200 shadow-xs">
        <div class="flex items-center space-x-2 mb-3">
            <span class="px-2.5 py-1 bg-indigo-600 text-white text-xs font-black rounded-lg">2026 Gen 2</span>
            <h3 class="text-base lg:text-lg font-black text-indigo-950">Work IQ 자율 에이전트</h3>
        </div>
        <ul class="space-y-2.5 text-xs lg:text-sm text-slate-800">
            <li>• <strong>Work IQ 자율 추론:</strong> 사내 메일, Teams 대화, 구성도 크로스 분석</li>
            <li>• <strong>멀티모달 통합 진단:</strong> 시스로그와 실시간 토폴로지 동시 판독</li>
            <li>• <strong>Office Agents 연동:</strong> Excel KPI 분석 후 Word SOP 초안 자동 작성</li>
        </ul>
    </div>
</div>
<div class="copilot-prompt-card mt-4 p-3.5 lg:p-4 bg-slate-900 text-white rounded-2xl flex items-center justify-between shadow-xs">
    <div class="flex items-center space-x-3 min-w-0">
        <span class="w-7 h-7 rounded-lg bg-gradient-to-tr from-indigo-500 to-pink-500 flex items-center justify-center shrink-0 text-xs">✨</span>
        <div class="text-xs lg:text-sm font-mono truncate text-slate-200">"지시를 기다리는 AI를 넘어, Work IQ를 바탕으로 업무 맥락을 선제적으로 이해하고 솔루션을 연결하는 오케스트레이터"</div>
    </div>
    <button onclick="copyPromptText(this)" class="shrink-0 ml-3 px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 복사</button>
</div>
"""

# Unit 03: 3 Model Choices
unit_bodies["03"] = """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 lg:gap-4 my-auto text-left w-full">
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-blue-100 text-blue-800 font-bold text-xs rounded">Advanced</span>
                <span class="font-black text-sm lg:text-base text-slate-900">GPT-5.6</span>
            </div>
            <div class="text-xs font-bold text-indigo-700 mb-2">복합 논리 & 수학적 추론</div>
            <p class="text-xs text-slate-600 leading-relaxed">5G 기지국 CAPEX 회수율 계산, Z-Score 이상 트래픽 통계 분석 및 대규모 분산 계산</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-slate-500">Excel / Python 연동</div>
    </div>
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-amber-100 text-amber-900 font-bold text-xs rounded">Precision</span>
                <span class="font-black text-sm lg:text-base text-slate-900">Claude Sonnet 5</span>
            </div>
            <div class="text-xs font-bold text-amber-700 mb-2">초정밀 코딩 & 표준 문서</div>
            <p class="text-xs text-slate-600 leading-relaxed">BGP 라우팅 구성 스크립트 작성, RFC 표준 준수 보고서 및 글로벌 기술 제안서</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-slate-500">Word / SOP 작성</div>
    </div>
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-indigo-100 text-indigo-800 font-bold text-xs rounded">Low Latency</span>
                <span class="font-black text-sm lg:text-base text-slate-900">Work IQ Small LLM</span>
            </div>
            <div class="text-xs font-bold text-indigo-700 mb-2">사내 지식 초고속 인덱싱</div>
            <p class="text-xs text-slate-600 leading-relaxed">SharePoint/OneDrive 파일 검색, 보안 ACL 권한 검증 및 실시간 사내 커뮤니케이션</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-slate-500">BizChat / Teams</div>
    </div>
</div>
"""

# Unit 04: Work IQ Engine
unit_bodies["04"] = """
<div class="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="md:col-span-6 p-5 bg-gradient-to-br from-indigo-50/60 to-blue-50/60 rounded-2xl border border-indigo-200 flex flex-col justify-between shadow-2xs">
        <div>
            <div class="flex items-center space-x-2 mb-2.5">
                <span class="px-2.5 py-1 bg-indigo-600 text-white font-bold text-xs rounded-lg">Graph Engine</span>
                <h4 class="font-black text-base lg:text-lg text-slate-900">Work IQ가 실무를 이해하는 방식</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-700 leading-relaxed">
                단순 키워드 매칭이 아닌, 엔지니어의 <strong>프로젝트 참여 이력</strong>, 최근 검토한 <strong>네트워크 구성도</strong>, <strong>Teams 장애 대화 스레드</strong>의 맥락을 결합하여 가장 정확한 답변을 도출합니다.
            </p>
        </div>
        <div class="mt-3 p-2.5 bg-white/90 rounded-xl border border-indigo-100 text-xs font-bold text-indigo-900 flex items-center space-x-2">
            <span>🔒</span> <span>Entra ID ACL 검증: 권한이 없는 문서는 검색 결과에 절대 미포함</span>
        </div>
    </div>
    <div class="md:col-span-6 p-5 bg-slate-900 text-slate-200 rounded-2xl font-mono text-xs space-y-2 flex flex-col justify-center shadow-xs">
        <div class="text-slate-400 font-bold">// Work IQ 지식 추출 파이프라인</div>
        <div class="p-2 bg-slate-800/90 rounded-lg text-cyan-300">1. User Query: "지난달 코어망 점검 이슈 요약해줘"</div>
        <div class="p-2 bg-slate-800/90 rounded-lg text-indigo-300">2. Graph Scan: Exchange 메일 + Teams 채널 + SharePoint SOP</div>
        <div class="p-2 bg-slate-800/90 rounded-lg text-emerald-300">3. Contextual Synthesis: 시간순 장애 타임라인 자동 생성</div>
    </div>
</div>
"""

# Unit 05: Multimodal Analysis
unit_bodies["05"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2.5 mb-2.5">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center text-base font-bold shadow-2xs">🖼️</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">네트워크 토폴로지 도면 분석</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                복잡한 Visio/PNG 네트워크 구성도 이미지를 업로드하면 단일 장애점(SPOF)을 식별하고 이중화 개선 권고안을 즉시 제시합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono font-semibold text-slate-700 border border-slate-200">
            "이 토폴로지 도면에서 L3 스위치 백본 이중화 링크 누락 구간을 찾아줘"
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2.5 mb-2.5">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center text-base font-bold shadow-2xs">📊</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">대용량 로그 & 수치 복합 추론</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                Excel 트래픽 급증 시간대와 장애 리포트 본문을 결합하여 복합적인 장애 인과관계를 수학적으로 검증합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono font-semibold text-slate-700 border border-slate-200">
            "CPU 점유율 90% 이상 시점과 BGP 플래핑 알람 발생의 상관계수 계산"
        </div>
    </div>
</div>
"""

# Unit 06: Office Agents
unit_bodies["06"] = """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 lg:gap-4 my-auto text-left w-full">
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <span class="px-2 py-0.5 bg-indigo-50 text-indigo-700 text-2xs font-bold rounded">01. Monitoring</span>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-1.5">NOC 정기 브리핑 에이전트</h4>
            <p class="text-xs text-slate-600 leading-relaxed">매일 아침 트래픽 요약 및 주요 장애 이슈를 자동 집계하여 Teams 채널에 정기 공유</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-slate-400">자율 모니터링</div>
    </div>
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <span class="px-2 py-0.5 bg-rose-50 text-rose-700 text-2xs font-bold rounded">02. Security</span>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-1.5">CVE 취약점 분석 에이전트</h4>
            <p class="text-xs text-slate-600 leading-relaxed">장비 펌웨어 버전과 신규 보안 패치를 자동 비교하여 긴급 조치 권고서 발행</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-slate-400">보안 자동 진단</div>
    </div>
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs hover:border-indigo-300 transition-all flex flex-col justify-between">
        <div>
            <span class="px-2 py-0.5 bg-emerald-50 text-emerald-700 text-2xs font-bold rounded">03. SOP</span>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-1.5">표준 작업 절차서 에이전트</h4>
            <p class="text-xs text-slate-600 leading-relaxed">엔지니어의 커맨드 로그를 표준 양식의 Word 매뉴얼로 자동 변환 및 지식화</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-slate-400">표준 문서화</div>
    </div>
</div>
"""

# Unit 07: BizChat
unit_bodies["07"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-gradient-to-br from-indigo-900 via-slate-900 to-slate-900 text-white rounded-2xl shadow-md border border-indigo-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-indigo-500/30 text-indigo-300 text-xs font-black rounded-full border border-indigo-400/40 flex items-center space-x-1.5">
                <span>✨</span> <span>BizChat Cross-App Query</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/teams '코어망운영팀' 채널에서 오늘 오전 9시 이후 논의된 '백본 BGP 플래핑' 관련 대화와, /files '2026_코어망_토폴로지.docx'를 대조해서 발생 원인과 현재 조치 현황을 3줄 요약하고, 담당 엔지니어에게 보낼 회신 메일 초안을 작성해줘."
        </div>
    </div>
    <div class="grid grid-cols-3 gap-3 text-center text-xs font-bold">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">📎 /files (SharePoint 문서 참조)</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">💬 /teams (채널 대화 검색)</div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">✉️ /mail (메일 스레드 통합)</div>
    </div>
</div>
"""

# Unit 08: Security (already harmonized)
# Unit 09: Centralization Necessity
unit_bodies["09"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-rose-50/50 rounded-2xl border border-rose-200 shadow-2xs">
        <div class="flex items-center space-x-2 mb-3">
            <span class="px-2.5 py-1 bg-rose-100 text-rose-800 text-xs font-bold rounded-lg">Local PC</span>
            <h4 class="font-bold text-sm lg:text-base text-slate-900">로컬 PC 파편화의 한계</h4>
        </div>
        <ul class="space-y-2.5 text-xs lg:text-sm text-slate-700">
            <li>• <strong>Copilot 인덱싱 불가:</strong> C드라이브, 바탕화면 파일은 AI가 접근 못함</li>
            <li>• <strong>팀원 간 지식 고립:</strong> 담당자 부재 시 설정 파일 및 SOP 조회 불가</li>
            <li>• <strong>버전 충돌 발생:</strong> `최종_수정_진짜최종.xlsx` 등 파일 버전 혼선</li>
        </ul>
    </div>
    <div class="p-5 bg-blue-50/50 rounded-2xl border-2 border-blue-200 shadow-xs">
        <div class="flex items-center space-x-2 mb-3">
            <span class="px-2.5 py-1 bg-blue-600 text-white text-xs font-black rounded-lg">Cloud</span>
            <h4 class="font-black text-sm lg:text-base text-slate-900">M365 클라우드 문서 중앙화</h4>
        </div>
        <ul class="space-y-2.5 text-xs lg:text-sm text-slate-800">
            <li>• <strong>Graph 실시간 인덱싱:</strong> 업로드 즉시 Copilot이 사내 지식으로 인식</li>
            <li>• <strong>3대 중앙화 축:</strong> OneDrive(개인), SharePoint(부서), Teams(프로젝트)</li>
            <li>• <strong>자동 버전 이력:</strong> 실수로 덮어써도 이전 시점으로 1초 복원</li>
        </ul>
    </div>
</div>
"""

# Unit 10: OneDrive Personal
unit_bodies["10"] = """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 lg:gap-4 my-auto text-left w-full">
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2 py-0.5 bg-blue-50 text-blue-700 text-2xs font-bold rounded">Step 1</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-1.5">PC 폴더 백업 동기화</h4>
        <p class="text-xs text-slate-600 leading-relaxed">내 컴퓨터의 바탕화면과 문서 폴더를 OneDrive에 자동 동기화하여 저장과 동시에 인덱싱</p>
    </div>
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2 py-0.5 bg-blue-50 text-blue-700 text-2xs font-bold rounded">Step 2</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-1.5">구조화된 폴더 명명</h4>
        <p class="text-xs text-slate-600 leading-relaxed">`[연도]_[프로젝트명]_[문서종류]` 표준 규칙으로 파일명을 정리하여 검색 정확도 극대화</p>
    </div>
    <div class="p-4 lg:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2 py-0.5 bg-blue-50 text-blue-700 text-2xs font-bold rounded">Step 3</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-1.5">자동 저장 (AutoSave On)</h4>
        <p class="text-xs text-slate-600 leading-relaxed">Office 앱 상단의 '자동 저장'을 켜서 작성 중인 모든 수정 사항이 즉시 Copilot 그래프에 동기화</p>
    </div>
</div>
"""

# Unit 11: SharePoint Team KB
unit_bodies["11"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="p-5 bg-gradient-to-br from-teal-50/60 to-emerald-50/60 rounded-2xl border border-teal-200 shadow-2xs">
        <h4 class="font-black text-base lg:text-lg text-slate-900 mb-2">부서 공용 매뉴얼과 장애 이력의 지식 자산화</h4>
        <p class="text-xs lg:text-sm text-slate-700 leading-relaxed">
            신규 엔지니어가 입사하거나 야간 긴급 장애 시 선임자에게 묻지 않고도 Copilot에게 질문하면, SharePoint에 축적된 매뉴얼과 보고서를 기반으로 <strong>3초 만에 검증된 해법</strong>을 답변합니다.
        </p>
    </div>
    <div class="grid grid-cols-3 gap-3 text-center text-xs font-bold">
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">📁 라우터/스위치 Config 표준 라이브러리</div>
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">📋 통신사 간 상호연동 인터페이스 가이드</div>
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs text-slate-800">🛡️ 비상 장애 대응 표준 작업 절차서(SOP)</div>
    </div>
</div>
"""

# Unit 12: Teams Workspace
unit_bodies["12"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center text-sm font-bold mb-2">📁</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">1. 채널별 파일 탭 활용</h4>
        <p class="text-xs lg:text-sm text-slate-600 leading-relaxed">
            이메일 첨부 대신 Teams 채널 '파일' 탭에 저장 ➔ SharePoint와 자동 연동되어 팀 전체 지식으로 즉시 인덱싱됩니다.
        </p>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center text-sm font-bold mb-2">🎙️</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">2. 회의 녹음 및 스크립트(Transcript)</h4>
        <p class="text-xs lg:text-sm text-slate-600 leading-relaxed">
            장애 대책 회의 시 '녹음 및 대화 기록'을 켜두면, 회의 직후 Copilot이 논의된 액션 아이템과 결정 사항을 자동 정리합니다.
        </p>
    </div>
</div>
"""

# Unit 13: Security & Governance
unit_bodies["13"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <div class="flex items-center space-x-2 mb-2.5">
            <span class="px-2 py-0.5 bg-blue-100 text-blue-800 text-xs font-bold rounded">Entra ID</span>
            <h4 class="font-black text-sm lg:text-base text-slate-900">ACL 권한 제어</h4>
        </div>
        <p class="text-xs lg:text-sm text-slate-600 leading-relaxed">
            사용자의 읽기 권한을 그대로 계승하여, 특정 폴더에 권한이 없는 직원이 질의해도 해당 문서는 검색 결과에 절대 노출되지 않습니다.
        </p>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <div class="flex items-center space-x-2 mb-2.5">
            <span class="px-2 py-0.5 bg-purple-100 text-purple-800 text-xs font-bold rounded">Purview</span>
            <h4 class="font-black text-sm lg:text-base text-slate-900">민감도 레이블 보호</h4>
        </div>
        <p class="text-xs lg:text-sm text-slate-600 leading-relaxed">
            [대외비] 레이블이 지정된 문서를 Copilot이 인용하거나 요약할 때도 원본 문서의 암호화와 보안 등급이 100% 유지됩니다.
        </p>
    </div>
</div>
"""

# Unit 14: Auto Indexing Pipeline
unit_bodies["14"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center">
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center justify-center">
            <span class="text-xl mb-1">⚙️</span>
            <div class="font-bold text-xs text-slate-900">1. 장비 자동 백업</div>
            <div class="text-2xs text-slate-500 mt-0.5">TFTP / FTP 백업</div>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center justify-center">
            <span class="text-xl mb-1">🔄</span>
            <div class="font-bold text-xs text-slate-900">2. Power Automate</div>
            <div class="text-2xs text-slate-500 mt-0.5">OneDrive 동기화</div>
        </div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center justify-center">
            <span class="text-xl mb-1">⚡</span>
            <div class="font-bold text-xs text-slate-900">3. Graph Indexing</div>
            <div class="text-2xs text-slate-500 mt-0.5">자동 벡터 인덱싱</div>
        </div>
        <div class="p-4 bg-gradient-to-br from-indigo-50 to-blue-50 rounded-xl border-2 border-indigo-200 shadow-xs flex flex-col items-center justify-center">
            <span class="text-xl mb-1">✨</span>
            <div class="font-black text-xs text-indigo-950">4. Copilot 질의</div>
            <div class="text-2xs text-indigo-700 font-bold mt-0.5">즉시 답변 가능</div>
        </div>
    </div>
</div>
"""

# Unit 15: Prompt Coach
unit_bodies["15"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <h4 class="font-black text-sm lg:text-base text-slate-900 mb-3 flex items-center space-x-2">
            <span>🎯</span> <span>좋은 프롬프트의 4대 핵심 구조</span>
        </h4>
        <ul class="space-y-2 text-xs lg:text-sm text-slate-700">
            <li><strong>1. Goal (목표):</strong> 무엇을 만들어야 하는가? (예: 회신 메일 초안)</li>
            <li><strong>2. Context (맥락):</strong> 어떤 상황인가? (예: BGP 순단 발생)</li>
            <li><strong>3. Source (출처):</strong> 어떤 파일 참조? (예: /files '로그.xlsx')</li>
            <li><strong>4. Expectation (형식):</strong> 어조와 형태는? (예: 타임라인 표)</li>
        </ul>
    </div>
    <div class="p-5 bg-indigo-50/60 rounded-2xl border-2 border-indigo-200 shadow-xs flex flex-col justify-between">
        <div>
            <h4 class="font-black text-sm lg:text-base text-indigo-950 mb-2 flex items-center space-x-2">
                <span>✨</span> <span>Prompt Coach 에이전트 실전 코칭</span>
            </h4>
            <p class="text-xs lg:text-sm text-slate-700 leading-relaxed">
                프롬프트를 보내기 전 코칭을 요청하면 누락된 맥락과 모호한 지시를 스스로 찾아내어 고품질 프롬프트로 업그레이드합니다.
            </p>
        </div>
        <div class="mt-3 p-2.5 bg-white rounded-xl text-2xs font-mono text-indigo-900 font-semibold border border-indigo-100">
            "내 프롬프트에서 엔지니어링 용어와 참조 출처가 부족한 부분을 Prompt Coach 원칙에 맞게 보완해줘."
        </div>
    </div>
</div>
"""

# Unit 16: Outlook 3-sec summary
unit_bodies["16"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-sky-100 text-sky-800 text-xs font-bold rounded">Summary</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">1. 스레드 3초 요약</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                30통이 넘는 답장 메일을 일일이 읽지 않아도 [Copilot 요약] 버튼 한 번으로 핵심 사건과 액션 아이템을 요약합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200">
            "최초 장애 알람 발생 시각, 담당자별 조치 내역, 미해결 이슈를 타임라인 표로 정리해줘"
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-sky-100 text-sky-800 text-xs font-bold rounded">Search</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">2. 핵심 분류 & 맥락 검색</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                단순 단어가 아닌 자연어 맥락 검색으로 지난 6개월간 Cisco TAC 엔지니어와 주고받은 버그 패치 메일만 정확히 필터링합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200">
            "지난 분기 코어 라우터 OS 버그 패치와 관련해 벤더사에서 보낸 권고 메일을 찾아줘"
        </div>
    </div>
</div>
"""

# Unit 17: TAC English Email
unit_bodies["17"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-slate-700">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-sky-500/30 text-sky-300 text-xs font-black rounded-full border border-sky-400/40 flex items-center space-x-1.5">
                <span>✉️</span> <span>Global TAC Support Request</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "현재 발생한 OSPF LSA 플러딩 및 패킷 드롭 현상에 대해 Cisco TAC 엔지니어에게 Severity-2 티켓을 요청하는 정중하고 전문적인 영문 메일을 작성해줘. 발생 일시, 장비 모델(ASR 9000), IOS-XR 버전, 첨부한 Show tech-support 로그를 포함해줘."
        </div>
    </div>
</div>
"""

# Unit 18: Smart Scheduling & Scheduled Prompts
unit_bodies["18"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-blue-100 text-blue-800 text-xs font-bold rounded">Meeting</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">1. 스마트 회의 잡기</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                참석자들의 캘린더를 자동 대조하여 공통 빈 시간을 찾고 회의 안건과 Teams 링크가 포함된 초대를 즉시 생성합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200">
            "이번 주 금요일 오후 전송망팀과 무선팀 팀장님들이 모두 가능한 30분 미팅을 잡아줘"
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-indigo-100 text-indigo-800 text-xs font-bold rounded">Schedule</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">2. 정기 작업 공지 예약</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                야간 작업 공지 메일을 특정 시간(예: D-1일 17:30)에 자동으로 작성하고 발송 대기 상태로 예약합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200">
            "내일 새벽 02:00 작업 영향도 안내 메일을 오늘 17:30에 발송되도록 예약해줘"
        </div>
    </div>
</div>
"""

# Unit 19: Teams Recap & Side Panel
unit_bodies["19"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-indigo-100 text-indigo-800 text-xs font-bold rounded">Recap</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">1. Teams 회의 요약하기</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                1시간 회의가 끝나면 전체 대화를 분석하여 결정된 사항(Decisions)과 담당자별 할 일(Action Items)을 5줄로 자동 정리합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200">
            "이 회의에서 김엔지니어와 박팀장이 합의한 롤백 기준과 일정을 요약해줘"
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="flex items-center space-x-2 mb-2">
                <span class="px-2 py-0.5 bg-purple-100 text-purple-800 text-xs font-bold rounded">Side Panel</span>
                <h4 class="font-black text-sm lg:text-base text-slate-900">2. Copilot 사이드 패널</h4>
            </div>
            <p class="text-xs lg:text-sm text-slate-600 leading-relaxed mb-3">
                우측 [Copilot 패널]을 열어 대화하듯 메일 초안의 어조를 정중하게 변경하거나 분량을 조절하고 사내 규정을 질의합니다.
            </p>
        </div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200">
            "작성된 회신 메일을 조금 더 격식 있는 비즈니스 어조로 수정하고 길이 줄여줘"
        </div>
    </div>
</div>
"""

# Unit 20: Hands-on 1-1 Excel Cleaning
unit_bodies["20"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2.5 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-lg">Step 1</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-2">결측치 및 비정형 로그 정제</h4>
        <div class="p-3 bg-slate-50 rounded-xl text-xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "빈 셀(N/A)을 이전 정상 측정값으로 채우고, 'Latency_ms' 열에서 비정상 음수 값을 0으로 일괄 보정해줘."
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2.5 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-lg">Step 2</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-2">조건부 파생 열 생성</h4>
        <div class="p-3 bg-slate-50 rounded-xl text-xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "'PRB_Usage'가 85% 이상이면서 'Drop_Rate'가 1.5% 초과인 경우 '위험', 그렇지 않으면 '정상'으로 분류하는 'Status' 열을 추가해줘."
        </div>
    </div>
</div>
"""

# Unit 21: Hands-on 1-2 Excel Pivot
unit_bodies["21"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-emerald-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-emerald-500/30 text-emerald-300 text-xs font-black rounded-full border border-emerald-400/40 flex items-center space-x-1.5">
                <span>📊</span> <span>Excel Copilot KPI Analysis</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "'PRB_Usage' 컬럼이 85% 이상이면서 'Drop_Rate'가 1.5%를 초과하는 과부하 기지국만 필터링하는 새 열을 추가하고, 기지국 ID별 시간대별 트래픽 추이를 피벗 차트로 생성해줘."
        </div>
    </div>
</div>
"""

# Unit 22: Hands-on 2-1 Reasoning
unit_bodies["22"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-indigo-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-indigo-500/30 text-indigo-300 text-xs font-black rounded-full border border-indigo-400/40 flex items-center space-x-1.5">
                <span>⚡</span> <span>Z-Score Anomaly Detection</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "최근 30일간의 백홀 트래픽 데이터를 바탕으로 Z-Score가 +2.5 이상인 이상 트래픽 발생 구간을 빨간색 조건부 서식으로 강조하고, 사용자 접속자 수(UE) 급증과의 상관관계를 분석해줘."
        </div>
    </div>
</div>
"""

# Unit 23: Hands-on 2-2 Python in Excel
unit_bodies["23"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2.5 py-1 bg-blue-100 text-blue-800 text-xs font-bold rounded-lg">Python in Excel</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-2">상관계수 히트맵 시각화</h4>
        <div class="p-3 bg-slate-50 rounded-xl text-xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "기지국 접속자 수, 패킷 지연 시간(RTT), 다운로드 처리량 간의 상관관계를 파이썬 seaborn heatmap으로 시각화하여 현재 시트의 G2 셀에 삽입해줘."
        </div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <span class="px-2.5 py-1 bg-indigo-100 text-indigo-800 text-xs font-bold rounded-lg">Simulation</span>
        <h4 class="font-black text-sm lg:text-base text-slate-900 mt-2 mb-2">What-If 대역폭 증설 시뮬레이션</h4>
        <div class="p-3 bg-slate-50 rounded-xl text-xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "백홀 대역폭을 10Gbps에서 20Gbps로 확장 시 피크타임 패킷 지연이 몇 % 개선되는지 파라미터 변동 모델링을 실행해줘."
        </div>
    </div>
</div>
"""

# Unit 24: Hands-on 3-1 Word Multi-Source
unit_bodies["24"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>📄</span> <span>Word Multi-Source Synthesis</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files '5G_KPI_분석결과.xlsx'의 3번 시트 통계 테이블과, /files 'L3스위치_표준매뉴얼.docx', 그리고 지난 Teams 대책 회의록을 종합하여 '수도권 코어망 긴급 증설 및 장애 대응 표준 작업 절차서(SOP)'를 작성해줘. 목적, 장비 체크리스트, 단계별 명령어, 롤백 가이드를 포함한 정형화된 서식으로 완성해줘."
        </div>
    </div>
</div>
"""

# Unit 25: Hands-on 3-2 CAPEX/OPEX
unit_bodies["25"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>📈</span> <span>CAPEX / OPEX Investment Proposal</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files '2026_장비견적서.xlsx'의 데이터를 인용하여 노후 라우터 교체 시 향후 3년간 전력 소비량 및 유지보수 비용 절감액(OPEX -18%)을 강조한 경영진 제출용 설비투자 기안서를 작성해줘."
        </div>
    </div>
</div>
"""

# Unit 26: Hands-on 3-3 Mermaid Topology
unit_bodies["26"] = """
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

# Unit 27: Hands-on 4-1 PPT
unit_bodies["27"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📑</span> <span>PowerPoint Slide Creation</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files '2026_통신망_현대화_보고서.docx' 파일로부터 프레젠테이션을 생성해줘. 임원 보고에 적합하도록 장황한 글을 줄이고, 핵심 성과 지표(KPI)와 타임라인을 시각적 카드로 구성해줘."
        </div>
    </div>
</div>
"""

# Unit 28: Hands-on 4-2 ROI Summary
unit_bodies["28"] = """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 lg:gap-4 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border-2 border-emerald-200 shadow-2xs flex flex-col justify-center items-center text-center">
        <div class="text-3xl lg:text-4xl font-black text-emerald-600 mb-1">99.999%</div>
        <div class="text-xs font-bold text-slate-900">연간 가용성 보장</div>
        <div class="text-2xs text-slate-500 mt-1">Downtime 5분 미만</div>
    </div>
    <div class="p-5 bg-white rounded-2xl border-2 border-blue-200 shadow-2xs flex flex-col justify-center items-center text-center">
        <div class="text-3xl lg:text-4xl font-black text-blue-600 mb-1">-35%</div>
        <div class="text-xs font-bold text-slate-900">장애 조치 시간 (MTTR)</div>
        <div class="text-2xs text-slate-500 mt-1">AI 자동 진단 연계</div>
    </div>
    <div class="p-5 bg-white rounded-2xl border-2 border-indigo-200 shadow-2xs flex flex-col justify-center items-center text-center">
        <div class="text-3xl lg:text-4xl font-black text-indigo-600 mb-1">₩4.2억</div>
        <div class="text-xs font-bold text-slate-900">연간 OPEX 절감</div>
        <div class="text-2xs text-slate-500 mt-1">전력 및 유지보수 최적화</div>
    </div>
</div>
"""

# Unit 29: Master Playbook 1
unit_bodies["29"] = """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 lg:gap-4 my-auto text-left w-full">
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="w-8 h-8 rounded-full bg-emerald-600 text-white font-bold flex items-center justify-center text-sm mb-2 shadow-xs">1</div>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">Excel Copilot</h4>
            <p class="text-xs text-slate-600 leading-relaxed">5G 대용량 로그 데이터 필터링 및 Z-Score 이상치 피벗 분석 완료</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-emerald-700">데이터 정제 & 추론</div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="w-8 h-8 rounded-full bg-blue-600 text-white font-bold flex items-center justify-center text-sm mb-2 shadow-xs">2</div>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">Word Copilot</h4>
            <p class="text-xs text-slate-600 leading-relaxed">엑셀 분석 테이블을 인용하여 정형화된 원인 분석 SOP 보고서 작성</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-blue-700">다중 소스 보고서 합성</div>
    </div>
    <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs flex flex-col justify-between">
        <div>
            <div class="w-8 h-8 rounded-full bg-orange-600 text-white font-bold flex items-center justify-center text-sm mb-2 shadow-xs">3</div>
            <h4 class="font-black text-sm lg:text-base text-slate-900 mb-2">PowerPoint Copilot</h4>
            <p class="text-xs text-slate-600 leading-relaxed">완성된 Word 보고서로부터 1-Page 임원 의사결정 슬라이드 변환</p>
        </div>
        <div class="mt-3 pt-2 border-t border-slate-100 text-2xs font-bold text-orange-700">의사결정 슬라이드 완성</div>
    </div>
</div>
"""

# Unit 30: Master Playbook 2 War-Room
unit_bodies["30"] = """
<div class="my-auto w-full text-left space-y-4">
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-indigo-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-indigo-500/30 text-indigo-300 text-xs font-black rounded-full border border-indigo-400/40 flex items-center space-x-1.5">
                <span>🚨</span> <span>Teams War-Room Incident Bot</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "현재 발생한 백본 라우터 다운 이슈와 관련해 '긴급_장애조치_워룸' 채널을 생성하고, 코어망팀과 전송망팀 담당자를 자동 초대하며, 지난 1시간 동안의 경보 로그 요약본을 채널 첫 공지로 게시해줘."
        </div>
    </div>
</div>
"""

# Unit 31: Cheat Sheet
unit_bodies["31"] = """
<div class="grid grid-cols-1 md:grid-cols-2 gap-3.5 lg:gap-4 my-auto text-left w-full">
    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <div class="text-xs font-bold text-indigo-700 mb-1.5">📡 망 점검 & 장애 분석 패턴</div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "/files 'syslog.txt'에서 Severity 1~2 알람만 시간순으로 정렬하고 BGP Flapping 원인을 3줄 요약해줘"
        </div>
    </div>
    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <div class="text-xs font-bold text-emerald-700 mb-1.5">📊 통계 & 시뮬레이션 패턴</div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "PRB 점유율 상위 10% 기지국의 주말 피크 트래픽 분산 효과를 파이썬 차트로 시각화해줘"
        </div>
    </div>
    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <div class="text-xs font-bold text-blue-700 mb-1.5">📝 기술 제안 & 기안서 패턴</div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "노후 스위치 교체 시 전력 절감량과 가용성 개선율을 강조한 경영진 제출용 1장 기안서 작성해줘"
        </div>
    </div>
    <div class="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
        <div class="text-xs font-bold text-purple-700 mb-1.5">✉️ 글로벌 벤더 TAC 패턴</div>
        <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-700 border border-slate-200 leading-relaxed">
            "Cisco TAC 엔지니어에게 OSPF LSA 패킷 드롭 원인 조사를 요청하는 정중한 영문 메일 작성해줘"
        </div>
    </div>
</div>
"""

# Map updated bodies into master_chapters
u_idx_counter = 1
for chap in master_chapters:
    for u in chap["units"]:
        num_str = f"{u_idx_counter:02d}"
        if num_str in unit_bodies:
            u["body"] = unit_bodies[num_str]
        u_idx_counter += 1

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

# Generate the polished HTML matching Microsoft's official Copilot Chat & Onboarding aesthetics
ms_portal_html = f"""<!DOCTYPE html>
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

        /* Microsoft Official Aurora Mesh Background */
        body {{
            background-color: #f8fafc !important;
            background-image: 
                radial-gradient(at 0% 0%, rgba(219, 234, 254, 0.7) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(243, 232, 255, 0.6) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(254, 243, 199, 0.35) 0px, transparent 50%);
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

        /* Modern Web Card Stage (FHD 75% Proportioned, Microsoft Fluent Glassmorphism) */
        .fhd-card-stage {{
            width: 100%;
            max-width: 1280px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(226, 232, 240, 0.9);
            border-radius: 28px;
            box-shadow: 0 20px 48px -12px rgba(15, 23, 42, 0.08), 0 4px 16px -2px rgba(15, 23, 42, 0.02);
            transition: all 0.25s ease-in-out;
        }}

        /* Microsoft Copilot Signature Pill Tab */
        .ms-pill-tab {{
            border-radius: 9999px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .ms-pill-tab.active {{
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            color: #ffffff;
            font-weight: 700;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.18);
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

        /* Copilot Interactive Prompt Bubble */
        .copilot-prompt-card {{
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
            border: 1px solid rgba(99, 102, 241, 0.3);
            box-shadow: 0 8px 24px -4px rgba(99, 102, 241, 0.15);
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

        /* Toast notification for prompt copy */
        #copyToast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 9999;
        }}
        #copyToast.show {{
            transform: translateY(0);
            opacity: 1;
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

        <!-- Left Journey Sidebar (25% Width) -->
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

        <!-- Center Workspace: 75% Main Stage -->
        <main class="flex-1 flex flex-col overflow-hidden relative">

            <!-- App Category Breadcrumb Bar (Refined Font) -->
            <div id="appThemeHeader" class="no-print h-11 bg-white/80 backdrop-blur-sm border-b border-slate-200 text-slate-700 px-6 flex items-center justify-between transition-all duration-500 shrink-0">
                <div class="flex items-center space-x-2.5 text-xs md:text-sm font-semibold truncate">
                    <span id="bannerAppBadge" class="px-3 py-0.5 bg-slate-100 text-slate-800 rounded-full font-bold uppercase tracking-wider text-xs border border-slate-200 flex items-center space-x-2 shrink-0">
                        <span id="bannerAppIconSvg" class="scale-75">{fluent_icons["copilot"]}</span>
                        <span id="bannerAppText">01. M365 COPILOT의 변화</span>
                    </span>
                    <span class="text-slate-300">/</span>
                    <span id="bannerSlideTitle" class="truncate max-w-2xl text-slate-900 font-bold break-keep text-xs md:text-sm">범용 AI와 M365 Copilot의 차이</span>
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

    <!-- Toast Notification for Prompt Copy -->
    <div id="copyToast" class="bg-slate-900 text-white px-4 py-2.5 rounded-xl shadow-xl flex items-center space-x-2 text-xs font-bold border border-slate-700">
        <span class="text-emerald-400">✓</span>
        <span>프롬프트가 클립보드에 복사되었습니다!</span>
    </div>

    <!-- Data Injection & Interactive Controller Script with Smart Responsive Sidebar -->
    <script>
        const slidesData = {json.dumps(cleaned_slides, ensure_ascii=False)};
        let currentSlideIndex = 0;
        let viewMode = 'slide';
        let sidebarCollapsed = window.innerWidth < 1100;
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

        // Smart Resize Observer
        window.addEventListener('resize', () => {{
            const currentWidth = window.innerWidth;
            if (currentWidth < 1100 && !sidebarCollapsed) {{
                setSidebarState(true);
            }} else if (currentWidth >= 1200 && sidebarCollapsed && !userExplicitlyToggled) {{
                setSidebarState(false);
            }}
        }});

        // Copy Prompt Helper
        function copyPromptText(btn) {{
            const card = btn.closest('.copilot-prompt-card');
            let textToCopy = '';
            if (card) {{
                const targetEl = card.querySelector('.prompt-target-text') || card.querySelector('.font-mono');
                if (targetEl) textToCopy = targetEl.textContent.trim();
            }}
            if (textToCopy) {{
                navigator.clipboard.writeText(textToCopy).then(() => {{
                    showToast();
                }});
            }}
        }}

        function showToast() {{
            const toast = document.getElementById('copyToast');
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2000);
        }}

        function renderSlide(index) {{
            if (index < 0 || index >= slidesData.length) return;
            currentSlideIndex = index;
            const slide = slidesData[index];

            // Render Center Card in FHD Mode
            const card = document.getElementById('activeSlideCard');
            card.innerHTML = `
                <div>
                    <!-- Eyebrow & Unit Badge (Microsoft Fluent Style) -->
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
master_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/M365_Copilot_Telecom_Master.html"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(ms_portal_html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(ms_portal_html)

with open(master_path, "w", encoding="utf-8") as f:
    f.write(ms_portal_html)

print("Successfully transformed internal slide design to Microsoft 365 Copilot Official Design!")
