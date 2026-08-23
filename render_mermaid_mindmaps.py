import re
import json

with open("integrate_mindmaps_to_chapter4.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

# Unit 20: Excel Copilot Mermaid Mindmap Architecture
unit_20_body = """
<div class="space-y-3.5 my-auto text-left w-full">
    <!-- Excel Mindmap Interactive Mermaid Card -->
    <div class="p-4 bg-gradient-to-br from-emerald-50/50 via-white to-slate-50 rounded-2xl border-2 border-emerald-300/80 shadow-xs">
        <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-2">
                <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-black shadow-2xs">🗺️</span>
                <span class="font-black text-sm text-slate-900">Excel Copilot 8대 기능 아키텍처 맵</span>
            </div>
            <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 text-2xs font-bold rounded-full">Interactive Mindmap</span>
        </div>
        <div class="mermaid text-center overflow-x-auto py-1">
        mindmap
          root((📊 Excel Copilot))
            시작하기 & 모드
              편집 모드[직접 수정]
              계획 모드[단계별 접근]
              채팅 모드[데이터 분석]
            통합문서 규칙
              .Rules 전용 시트
              A열 셀당 1개 규칙
              드롭다운 동작 전환
            데이터 & Skills
              사내 문서 및 대화
              페더레이션[Canva/Salesforce]
              Skills[SKILL.md/@brandkit]
            수식 & 모델
              입력 즉시 수식 추천
              패턴 감지 자동 채우기
              GPT-5.6 / Claude Sonnet
        </div>
    </div>

    <!-- Hands-on 1-1 Workflow -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-2xs font-bold text-emerald-700 uppercase tracking-wide mb-1">Step 1. 결측치 및 비정형 로그 정제</div>
            <div class="p-2 bg-slate-50 rounded-lg text-2xs font-mono text-slate-800 border border-slate-200">
                "빈 셀(N/A)을 이전 정상 측정값으로 채우고, 'Latency_ms' 열에서 비정상 음수 값을 0으로 일괄 보정해줘."
            </div>
        </div>
        <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs">
            <div class="text-2xs font-bold text-emerald-700 uppercase tracking-wide mb-1">Step 2. 조건부 파생 열 생성</div>
            <div class="p-2 bg-slate-50 rounded-lg text-2xs font-mono text-slate-800 border border-slate-200">
                "'PRB_Usage'가 85% 이상이면서 'Drop_Rate'가 1.5% 초과인 경우 '위험', 그렇지 않으면 '정상'으로 분류하는 'Status' 열 추가해줘."
            </div>
        </div>
    </div>
</div>
"""

# Unit 24: Word Copilot Mermaid Mindmap Architecture
unit_24_body = """
<div class="space-y-3.5 my-auto text-left w-full">
    <!-- Word Mindmap Interactive Mermaid Card -->
    <div class="p-4 bg-gradient-to-br from-blue-50/50 via-white to-slate-50 rounded-2xl border-2 border-blue-300/80 shadow-xs">
        <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-2">
                <span class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-black shadow-2xs">🗺️</span>
                <span class="font-black text-sm text-slate-900">Word Copilot 5대 기능 아키텍처 맵</span>
            </div>
            <span class="px-2 py-0.5 bg-blue-100 text-blue-800 text-2xs font-bold rounded-full">Interactive Mindmap</span>
        </div>
        <div class="mermaid text-center overflow-x-auto py-1">
        mindmap
          root((📄 Word Copilot))
            초안 작성
              새 문서 시작
              기존 파일/메일 연동
              상세 프롬프트 제어
            다시 쓰기 & 변환
              Rewrite 자동 제안
              대화형 실시간 편집
              텍스트 ➔ 정형 표 변환
            이미지 & 디자인
              DALL-E 3 AI 생성
              헤더 배너 제작
              브랜드 키트 제안
            분석 & 모바일
              원클릭 핵심 요약
              차트/도면 질의응답
              모바일 음성 노트 문서화
        </div>
    </div>

    <!-- Main Synthesis Prompt Card -->
    <div class="copilot-prompt-card p-3.5 lg:p-4 bg-slate-900 text-white rounded-2xl shadow-md border border-blue-700/50">
        <div class="flex items-center justify-between mb-1.5">
            <span class="px-2.5 py-0.5 bg-blue-500/30 text-blue-300 text-xs font-black rounded-full border border-blue-400/40 flex items-center space-x-1.5">
                <span>📄</span> <span>Word Multi-Source Synthesis Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-2.5 py-0.5 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 복사</button>
        </div>
        <div class="font-mono text-xs leading-relaxed text-slate-100 prompt-target-text">
            "/files '5G_KPI_분석결과.xlsx'의 3번 시트 통계 테이블과, /files 'L3스위치_표준매뉴얼.docx', 그리고 지난 Teams 대책 회의록을 종합하여 '수도권 코어망 긴급 증설 및 장애 대응 표준 작업 절차서(SOP)'를 작성해줘."
        </div>
    </div>
</div>
"""

# Unit 27: PowerPoint Copilot Mermaid Mindmap Architecture
unit_27_body = """
<div class="space-y-3.5 my-auto text-left w-full">
    <!-- PowerPoint Mindmap Interactive Mermaid Card -->
    <div class="p-4 bg-gradient-to-br from-orange-50/50 via-white to-slate-50 rounded-2xl border-2 border-orange-300/80 shadow-xs">
        <div class="flex items-center justify-between mb-2">
            <div class="flex items-center space-x-2">
                <span class="w-6 h-6 rounded-lg bg-orange-600 text-white flex items-center justify-center text-xs font-black shadow-2xs">🗺️</span>
                <span class="font-black text-sm text-slate-900">PowerPoint Copilot 기능 아키텍처 맵</span>
            </div>
            <span class="px-2 py-0.5 bg-orange-100 text-orange-800 text-2xs font-bold rounded-full">Interactive Mindmap</span>
        </div>
        <div class="mermaid text-center overflow-x-auto py-1">
        mindmap
          root((📑 PPT Copilot))
            생성 에이전트
              에이전트 모드[개요 생성]
              Word 문서 연동[24MB 권장]
              조직 표준 서식 적용
            분석 & 요약
              핵심 요점 요약
              키 슬라이드 식별
              Action Items 추출
            편집 & 디자인
              전문가 톤 다시 쓰기
              DALL-E 3 이미지 생성
              슬라이드 재사용
            규정 & 한도
              40,000단어 요약 한도
              책임 있는 AI[RAI] 메타데이터
        </div>
    </div>

    <!-- Main PPT Creation Prompt Card -->
    <div class="copilot-prompt-card p-3.5 lg:p-4 bg-slate-900 text-white rounded-2xl shadow-md border border-orange-700/50">
        <div class="flex items-center justify-between mb-1.5">
            <span class="px-2.5 py-0.5 bg-orange-500/30 text-orange-300 text-xs font-black rounded-full border border-orange-400/40 flex items-center space-x-1.5">
                <span>📑</span> <span>PowerPoint Executive Presentation Prompt</span>
            </span>
            <button onclick="copyPromptText(this)" class="px-2.5 py-0.5 bg-white/10 hover:bg-white/20 text-white rounded-lg text-xs font-bold transition-all border border-white/20">📋 복사</button>
        </div>
        <div class="font-mono text-xs leading-relaxed text-slate-100 prompt-target-text">
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
        elif "다중 소스 기반 통합 SOP 작성" in u["title"]:
            u["body"] = unit_24_body
        elif "임원 보고용 프레젠테이션 자동 생성" in u["title"]:
            u["body"] = unit_27_body

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

loc["cleaned_slides"] = cleaned_slides
loc["master_chapters"] = master_chapters

# Read template and build
with open("upgrade_to_ms_official_design.py", "r", encoding="utf-8") as f:
    template_code = f.read()

html_part = re.search(r'ms_portal_html = f"""(.*?)"""\n\noutput_path', template_code, re.DOTALL)
if html_part:
    html_raw_template = html_part.group(1)
    # Inject Mermaid theme neutral initialization with custom font
    html_raw_template = html_raw_template.replace(
        "mermaid.initialize({ startOnLoad: true, theme: 'neutral' });",
        "mermaid.initialize({ startOnLoad: true, theme: 'neutral', themeVariables: { fontFamily: 'Pretendard', fontSize: '13px', primaryColor: '#f1f5f9', primaryTextColor: '#0f172a', primaryBorderColor: '#cbd5e1', lineEditColor: '#6366f1' } });"
    )
    generated_html = eval(f'f"""{html_raw_template}"""', loc)
    
    with open("AX_CA_Edu_GHLEE.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("M365_Copilot_Telecom_Master.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    print("Successfully rendered live interactive Mermaid Mindmaps for Excel, Word, and PPT!")
