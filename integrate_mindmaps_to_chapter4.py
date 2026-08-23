import re
import json

# Load base setup
with open("upgrade_to_ms_official_design.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

# Unit 20: [핸즈온 1-1] Excel Copilot - Integrated with Excel Mindmap (Operating Modes & .Rules)
unit_20_body = """
<div class="space-y-4 my-auto text-left w-full">
    <!-- Excel Mindmap Feature Map Card (Interactive Bento) -->
    <div class="p-4 lg:p-5 bg-gradient-to-br from-emerald-50/70 via-white to-slate-50 rounded-2xl border-2 border-emerald-200/90 shadow-xs">
        <div class="flex items-center justify-between mb-3">
            <div class="flex items-center space-x-2.5">
                <span class="w-7 h-7 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-black shadow-xs">🗺️</span>
                <div>
                    <h4 class="font-black text-sm lg:text-base text-slate-900 leading-tight">Excel Copilot 아키텍처 & 운영 체계</h4>
                    <div class="text-2xs text-emerald-800 font-bold">3대 운영 모드 • 통합 문서 규칙(.Rules) • Skills 연동</div>
                </div>
            </div>
            <span class="px-2.5 py-0.5 bg-emerald-100 text-emerald-800 text-2xs font-bold rounded-full">Excel Architecture</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <!-- Mode 1 -->
            <div class="p-3 bg-white rounded-xl border border-emerald-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 flex items-center space-x-1.5 text-emerald-700">
                    <span>⚡</span> <span>3대 운영 모드</span>
                </div>
                <ul class="text-slate-600 space-y-1 text-2xs">
                    <li>• <strong>편집 모드:</strong> 워크시트/셀 직접 수정</li>
                    <li>• <strong>계획 모드:</strong> 단계별 파이프라인 접근</li>
                    <li>• <strong>채팅 모드:</strong> 심층 분석 및 질의응답</li>
                </ul>
            </div>

            <!-- Mode 2 -->
            <div class="p-3 bg-white rounded-xl border border-emerald-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 flex items-center space-x-1.5 text-blue-700">
                    <span>📋</span> <span>'.Rules' 전용 시트</span>
                </div>
                <ul class="text-slate-600 space-y-1 text-2xs">
                    <li>• <strong>규칙 나열:</strong> A열에 셀당 1개 규칙 기술</li>
                    <li>• <strong>동작 전환:</strong> 드롭다운 수식 연동 제어</li>
                    <li>• <strong>공유 보존:</strong> 통합 문서와 함께 규칙 전파</li>
                </ul>
            </div>

            <!-- Mode 3 -->
            <div class="p-3 bg-white rounded-xl border border-emerald-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 flex items-center space-x-1.5 text-indigo-700">
                    <span>🧩</span> <span>데이터 원본 & Skills</span>
                </div>
                <ul class="text-slate-600 space-y-1 text-2xs">
                    <li>• <strong>사내 지식:</strong> 회사 문서, 메일, 대화</li>
                    <li>• <strong>페더레이션:</strong> Salesforce, FactSet 등</li>
                    <li>• <strong>사용자 기술:</strong> OneDrive `SKILL.md`</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Hands-on 1-1 Workflow -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-2xs font-bold text-emerald-700 uppercase tracking-wide mb-1">Step 1. 결측치 및 비정형 로그 정제</div>
            <div class="p-2.5 bg-slate-50 rounded-lg text-2xs font-mono text-slate-800 border border-slate-200">
                "빈 셀(N/A)을 이전 정상 측정값으로 채우고, 'Latency_ms' 열에서 비정상 음수 값을 0으로 일괄 보정해줘."
            </div>
        </div>
        <div class="p-3.5 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-2xs font-bold text-emerald-700 uppercase tracking-wide mb-1">Step 2. 조건부 파생 열 생성</div>
            <div class="p-2.5 bg-slate-50 rounded-lg text-2xs font-mono text-slate-800 border border-slate-200">
                "'PRB_Usage'가 85% 이상이면서 'Drop_Rate'가 1.5% 초과인 경우 '위험', 그렇지 않으면 '정상'으로 분류하는 'Status' 열 추가해줘."
            </div>
        </div>
    </div>
</div>
"""

# Unit 21: [핸즈온 1-2] Excel Copilot - Formula suggestions & Pivot Chart
unit_21_body = """
<div class="my-auto w-full text-left space-y-4">
    <!-- Excel Formula & Insight Card -->
    <div class="p-4 bg-emerald-50/60 rounded-2xl border border-emerald-200 shadow-2xs flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <span class="text-2xl">💡</span>
            <div>
                <div class="text-xs font-black text-emerald-950">수식 제안 관리 & 예제 기반 패턴 수식 (Formula Suggestions)</div>
                <div class="text-2xs text-slate-600 font-medium">수식 입력 즉시 최적 함수 추천 • 예제 기반 패턴 감지로 열 자동 채우기</div>
            </div>
        </div>
        <span class="px-2.5 py-1 bg-white text-emerald-800 text-2xs font-bold rounded-lg border border-emerald-200 shadow-2xs shrink-0">Excel AI Engine</span>
    </div>

    <!-- Main Prompt Card -->
    <div class="copilot-prompt-card p-5 lg:p-6 bg-slate-900 text-white rounded-2xl shadow-md border border-emerald-700/50">
        <div class="flex items-center justify-between mb-3">
            <span class="px-3 py-1 bg-emerald-500/30 text-emerald-300 text-xs font-black rounded-full border border-emerald-400/40 flex items-center space-x-1.5">
                <span>📊</span> <span>Excel Copilot KPI Pivot Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "'PRB_Usage' 컬럼이 85% 이상이면서 'Drop_Rate'가 1.5%를 초과하는 과부하 기지국만 필터링하는 새 열을 추가하고, 기지국 ID별 시간대별 트래픽 추이를 피벗 차트로 생성해줘."
        </div>
    </div>
</div>
"""

# Unit 24: [핸즈온 3-1] Word Copilot - Integrated with Word Mindmap (Drafting, Rewrite, DALL-E 3)
unit_24_body = """
<div class="space-y-4 my-auto text-left w-full">
    <!-- Word Mindmap Feature Map Card -->
    <div class="p-4 lg:p-5 bg-gradient-to-br from-blue-50/70 via-white to-slate-50 rounded-2xl border-2 border-blue-200/90 shadow-xs">
        <div class="flex items-center justify-between mb-3">
            <div class="flex items-center space-x-2.5">
                <span class="w-7 h-7 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-black shadow-xs">🗺️</span>
                <div>
                    <h4 class="font-black text-sm lg:text-base text-slate-900 leading-tight">Word Copilot 기능 아키텍처 맵</h4>
                    <div class="text-2xs text-blue-800 font-bold">다중 소스 합성 • 텍스트 재작성(Rewrite) • DALL-E 3 배너 • 모바일 음성 노트</div>
                </div>
            </div>
            <span class="px-2.5 py-0.5 bg-blue-100 text-blue-800 text-2xs font-bold rounded-full">Word Architecture</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 text-xs">
            <div class="p-2.5 bg-white rounded-xl border border-blue-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-blue-700">✍️ 초안 작성</div>
                <div class="text-slate-600 text-2xs leading-snug">기존 파일(`/files`), 전자 메일, 회의록 기반 원클릭 생성</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-blue-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-indigo-700">🔄 다시 쓰기 & 표 변환</div>
                <div class="text-slate-600 text-2xs leading-snug">대화형 실시간 편집 및 텍스트 ➔ 정형 표(Table) 시각화</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-blue-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-purple-700">🎨 DALL-E 3 이미지</div>
                <div class="text-slate-600 text-2xs leading-snug">문서 헤더 배너 제작 & 브랜드 키트 이미지 제안</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-blue-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-emerald-700">📱 모바일 & 음성</div>
                <div class="text-slate-600 text-2xs leading-snug">iOS/Android 현장 음성 노트를 표준 보고서로 변환</div>
            </div>
        </div>
    </div>

    <!-- Main Synthesis Prompt Card -->
    <div class="copilot-prompt-card p-4 lg:p-5 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-2">
            <span class="px-3 py-1 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>📄</span> <span>Word Multi-Source Synthesis Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files '5G_KPI_분석결과.xlsx'의 3번 시트 통계 테이블과, /files 'L3스위치_표준매뉴얼.docx', 그리고 지난 Teams 대책 회의록을 종합하여 '수도권 코어망 긴급 증설 및 장애 대응 표준 작업 절차서(SOP)'를 작성해줘. 목적, 장비 체크리스트, 단계별 명령어, 롤백 가이드를 포함한 정형화된 서식으로 완성해줘."
        </div>
    </div>
</div>
"""

# Unit 27: [핸즈온 4-1] PPT Copilot - Integrated with PowerPoint Mindmap (Agent Mode, Outline, Word Sync)
unit_27_body = """
<div class="space-y-4 my-auto text-left w-full">
    <!-- PowerPoint Mindmap Feature Map Card -->
    <div class="p-4 lg:p-5 bg-gradient-to-br from-orange-50/70 via-white to-slate-50 rounded-2xl border-2 border-orange-200/90 shadow-xs">
        <div class="flex items-center justify-between mb-3">
            <div class="flex items-center space-x-2.5">
                <span class="w-7 h-7 rounded-lg bg-orange-600 text-white flex items-center justify-center text-xs font-black shadow-xs">🗺️</span>
                <div>
                    <h4 class="font-black text-sm lg:text-base text-slate-900 leading-tight">PowerPoint Copilot 기능 아키텍처 맵</h4>
                    <div class="text-2xs text-orange-800 font-bold">에이전트 모드 • Word 문서 연동 • 키 슬라이드 식별 • 40,000단어 요약 한도</div>
                </div>
            </div>
            <span class="px-2.5 py-0.5 bg-orange-100 text-orange-800 text-2xs font-bold rounded-full">PPT Architecture</span>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 text-xs">
            <div class="p-2.5 bg-white rounded-xl border border-orange-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-orange-700">🚀 에이전트 모드</div>
                <div class="text-slate-600 text-2xs leading-snug">청중/스타일 설정 ➔ 개요(Outline) 생성 ➔ 슬라이드 자동 빌드</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-orange-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-blue-700">📄 Word 문서 연동</div>
                <div class="text-slate-600 text-2xs leading-snug">Word 스타일 구조 이해, 이미지 통합, 표준 서식 파일(24MB 이하)</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-orange-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-indigo-700">📑 요약 & 액션 아이템</div>
                <div class="text-slate-600 text-2xs leading-snug">핵심 요점 요약, 키 슬라이드 식별, 도표/차트 질의응답</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-orange-100 shadow-2xs">
                <div class="font-black text-slate-900 mb-1 text-2xs text-emerald-700">⚖️ 규정 및 한도</div>
                <div class="text-slate-600 text-2xs leading-snug">최대 40,000단어 요약, 책임 있는 AI(RAI) 출처 메타데이터</div>
            </div>
        </div>
    </div>

    <!-- Main PPT Creation Prompt Card -->
    <div class="copilot-prompt-card p-4 lg:p-5 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-2">
            <span class="px-3 py-1 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📑</span> <span>PowerPoint Executive Presentation Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 프롬프트 복사</button>
        </div>
        <div class="font-mono text-xs lg:text-sm leading-relaxed text-slate-100 prompt-target-text">
            "/files '2026_통신망_현대화_보고서.docx' 파일로부터 프레젠테이션을 생성해줘. 임원 보고에 적합하도록 장황한 글을 줄이고, 핵심 성과 지표(KPI)와 타임라인을 시각적 카드로 구성해줘."
        </div>
    </div>
</div>
"""

# Update master chapters
for chap in master_chapters:
    for u in chap["units"]:
        if "대용량 KPI 데이터 정제와 시각화" in u["title"]:
            u["body"] = unit_20_body
        elif "수식 계산과 피벗 차트 자동화" in u["title"]:
            u["body"] = unit_21_body
        elif "다중 소스 기반 통합 SOP 작성" in u["title"]:
            u["body"] = unit_24_body
        elif "임원 보고용 프레젠테이션 자동 생성" in u["title"]:
            u["body"] = unit_27_body

# Re-run full build
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

# Re-write HTML file
with open("upgrade_to_ms_official_design.py", "r", encoding="utf-8") as f:
    template_code = f.read()

# Execute template script to generate new AX_CA_Edu_GHLEE.html
loc["cleaned_slides"] = cleaned_slides
loc["master_chapters"] = master_chapters

# Read the HTML generation part
html_part = re.search(r'ms_portal_html = f"""(.*?)"""\n\noutput_path', template_code, re.DOTALL)
if html_part:
    html_raw_template = html_part.group(1)
    # Generate final html
    generated_html = eval(f'f"""{html_raw_template}"""', loc)
    
    with open("AX_CA_Edu_GHLEE.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("M365_Copilot_Telecom_Master.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    print("Successfully integrated rich Mindmap Architecture cards into Chapter 04!")
