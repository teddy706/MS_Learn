import re
import json

# Load base setup
with open("render_mermaid_mindmaps.py", "r", encoding="utf-8") as f:
    code = f.read()

loc = {}
exec(code, loc)
master_chapters = loc["master_chapters"]
fluent_icons = loc["fluent_icons"]

# High-End Excalidraw / Modern Fluent Technical Architecture Maps (Replacing clunky mermaid)

# 1. EXCEL COPILOT ARCHITECTURE MAP (Unit 20)
unit_20_body = """
<div class="space-y-4 my-auto text-left w-full">
    <!-- Excalidraw / Modern Tech Architecture Map -->
    <div class="p-5 lg:p-6 bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl border border-indigo-500/30 shadow-md relative overflow-hidden">
        <!-- Header -->
        <div class="flex items-center justify-between mb-4 border-b border-indigo-800/40 pb-3">
            <div class="flex items-center space-x-2.5">
                <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 flex items-center justify-center text-sm font-black">📊</span>
                <div>
                    <h4 class="font-black text-sm lg:text-base text-white tracking-tight">Excel Copilot 기능 아키텍처 맵</h4>
                    <div class="text-2xs text-indigo-300 font-medium">운영 모드 • .Rules 시트 • 페더레이션 커넥터 • Skills 기술</div>
                </div>
            </div>
            <span class="px-2.5 py-1 bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-2xs font-bold rounded-full">Excalidraw Map</span>
        </div>

        <!-- 4 Architecture Pillars -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-3">
            <!-- Branch 1 -->
            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-indigo-500/20 hover:border-emerald-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-emerald-400 text-xs font-bold mb-1.5">
                        <span>⚡</span> <span>1. 3대 운영 모드</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>편집:</strong> 셀/수식 직접 수정</li>
                        <li>• <strong>계획:</strong> 단계별 파이프라인</li>
                        <li>• <strong>채팅:</strong> 데이터 인사이트 질의</li>
                    </ul>
                </div>
            </div>

            <!-- Branch 2 -->
            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-indigo-500/20 hover:border-blue-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-blue-400 text-xs font-bold mb-1.5">
                        <span>📋</span> <span>2. '.Rules' 전용 시트</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>A열 나열:</strong> 셀당 1개 규칙 기술</li>
                        <li>• <strong>동작 전환:</strong> 드롭다운 수식 제어</li>
                        <li>• <strong>공유 보존:</strong> 파일과 함께 전파</li>
                    </ul>
                </div>
            </div>

            <!-- Branch 3 -->
            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-indigo-500/20 hover:border-purple-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-purple-400 text-xs font-bold mb-1.5">
                        <span>🌐</span> <span>3. 데이터 & 페더레이션</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>사내 지식:</strong> 회사 문서, 대화</li>
                        <li>• <strong>커넥터:</strong> Salesforce, FactSet</li>
                        <li>• <strong>출처 인용:</strong> 웹 검색 결합</li>
                    </ul>
                </div>
            </div>

            <!-- Branch 4 -->
            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-indigo-500/20 hover:border-pink-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-pink-400 text-xs font-bold mb-1.5">
                        <span>🧩</span> <span>4. 기술 (Skills)</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>MS 기술:</strong> @brandkit, @theme</li>
                        <li>• <strong>사용자 정의:</strong> `SKILL.md`</li>
                        <li>• <strong>모델:</strong> GPT-5.6 / Claude</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- Hands-on 1-1 Workflow -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
            <div class="text-2xs font-bold text-emerald-700 uppercase tracking-wide mb-1">Step 1. 결측치 및 비정형 로그 정제</div>
            <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-800 border border-slate-200">
                "빈 셀(N/A)을 이전 정상 측정값으로 채우고, 'Latency_ms' 열에서 비정상 음수 값을 0으로 일괄 보정해줘."
            </div>
        </div>
        <div class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-2xs">
            <div class="text-2xs font-bold text-emerald-700 uppercase tracking-wide mb-1">Step 2. 조건부 파생 열 생성</div>
            <div class="p-2.5 bg-slate-50 rounded-xl text-2xs font-mono text-slate-800 border border-slate-200">
                "'PRB_Usage'가 85% 이상이면서 'Drop_Rate'가 1.5% 초과인 경우 '위험', 그렇지 않으면 '정상'으로 분류하는 'Status' 열 추가해줘."
            </div>
        </div>
    </div>
</div>
"""

# 2. WORD COPILOT ARCHITECTURE MAP (Unit 24)
unit_24_body = """
<div class="space-y-4 my-auto text-left w-full">
    <!-- Excalidraw / Modern Tech Architecture Map -->
    <div class="p-5 lg:p-6 bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl border border-blue-500/30 shadow-md relative overflow-hidden">
        <!-- Header -->
        <div class="flex items-center justify-between mb-4 border-b border-blue-800/40 pb-3">
            <div class="flex items-center space-x-2.5">
                <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-400 border border-blue-500/30 flex items-center justify-center text-sm font-black">📄</span>
                <div>
                    <h4 class="font-black text-sm lg:text-base text-white tracking-tight">Word Copilot 5대 기능 아키텍처 맵</h4>
                    <div class="text-2xs text-blue-300 font-medium">다중 소스 초안 • 다시 쓰기 & 표 변환 • DALL-E 3 배너 • 모바일 음성 노트</div>
                </div>
            </div>
            <span class="px-2.5 py-1 bg-blue-500/20 text-blue-300 border border-blue-500/40 text-2xs font-bold rounded-full">Excalidraw Map</span>
        </div>

        <!-- 4 Architecture Pillars -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-3">
            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-blue-500/20 hover:border-blue-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-blue-400 text-xs font-bold mb-1.5">
                        <span>✍️</span> <span>1. 콘텐츠 초안 작성</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>소스 참조:</strong> `/files`, 메일, 회의록</li>
                        <li>• <strong>섹션 추가:</strong> 특정 단락 보강</li>
                        <li>• <strong>상세 프롬프트:</strong> 서식/어조 제어</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-blue-500/20 hover:border-indigo-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-indigo-400 text-xs font-bold mb-1.5">
                        <span>🔄</span> <span>2. 다시 쓰기 & 표 변환</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>Rewrite:</strong> 문법/명확성 제안</li>
                        <li>• <strong>실시간 편집:</strong> 대화형 튜닝</li>
                        <li>• <strong>표 시각화:</strong> 텍스트 ➔ 표 변환</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-blue-500/20 hover:border-purple-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-purple-400 text-xs font-bold mb-1.5">
                        <span>🎨</span> <span>3. DALL-E 3 & 배너</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>AI 이미지:</strong> 맞춤형 삽화 생성</li>
                        <li>• <strong>헤더 배너:</strong> 챕터별 그래픽</li>
                        <li>• <strong>브랜드 키트:</strong> 표준 색상 반영</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-blue-500/20 hover:border-emerald-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-emerald-400 text-xs font-bold mb-1.5">
                        <span>📱</span> <span>4. 분석 & 모바일</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>요약/Q&A:</strong> 차트/도면 질의</li>
                        <li>• <strong>출처 인용:</strong> 근거 파일 제시</li>
                        <li>• <strong>음성 노트:</strong> 보고서 자동 변환</li>
                    </ul>
                </div>
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

# 3. POWERPOINT COPILOT ARCHITECTURE MAP (Unit 27)
unit_27_body = """
<div class="space-y-4 my-auto text-left w-full">
    <!-- Excalidraw / Modern Tech Architecture Map -->
    <div class="p-5 lg:p-6 bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl border border-orange-500/30 shadow-md relative overflow-hidden">
        <!-- Header -->
        <div class="flex items-center justify-between mb-4 border-b border-orange-800/40 pb-3">
            <div class="flex items-center space-x-2.5">
                <span class="w-8 h-8 rounded-xl bg-orange-500/20 text-orange-400 border border-orange-500/30 flex items-center justify-center text-sm font-black">📑</span>
                <div>
                    <h4 class="font-black text-sm lg:text-base text-white tracking-tight">PowerPoint Copilot 기능 아키텍처 맵</h4>
                    <div class="text-2xs text-orange-300 font-medium">에이전트 모드 • Word 문서 연동 • 액션 아이템 추출 • 40,000단어 요약 한도</div>
                </div>
            </div>
            <span class="px-2.5 py-1 bg-orange-500/20 text-orange-300 border border-orange-500/40 text-2xs font-bold rounded-full">Excalidraw Map</span>
        </div>

        <!-- 4 Architecture Pillars -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-3">
            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-orange-500/20 hover:border-orange-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-orange-400 text-xs font-bold mb-1.5">
                        <span>🚀</span> <span>1. 에이전트 모드</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>스타일 설정:</strong> 청중/톤 맞춤</li>
                        <li>• <strong>개요 생성:</strong> 목차 자동 제안</li>
                        <li>• <strong>슬라이드 빌드:</strong> 시각적 생성</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-orange-500/20 hover:border-blue-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-blue-400 text-xs font-bold mb-1.5">
                        <span>📄</span> <span>2. Word 문서 연동</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>구조 인식:</strong> 제목 스타일 파싱</li>
                        <li>• <strong>이미지 통합:</strong> 보고서 사진 유지</li>
                        <li>• <strong>서식 파일:</strong> 24MB 이하 권장</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-orange-500/20 hover:border-indigo-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-indigo-400 text-xs font-bold mb-1.5">
                        <span>📑</span> <span>3. 분석 & 액션 아이템</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>핵심 요약:</strong> 글머리 기호 서머리</li>
                        <li>• <strong>키 슬라이드:</strong> 중요 장표 식별</li>
                        <li>• <strong>Action Items:</strong> 과업 자동 추출</li>
                    </ul>
                </div>
            </div>

            <div class="p-3.5 bg-slate-800/80 rounded-2xl border border-orange-500/20 hover:border-emerald-400/50 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex items-center space-x-1.5 text-emerald-400 text-xs font-bold mb-1.5">
                        <span>⚖️</span> <span>4. 지침 및 규정</span>
                    </div>
                    <ul class="text-slate-300 space-y-1 text-2xs">
                        <li>• <strong>요약 한도:</strong> 최대 40,000단어</li>
                        <li>• <strong>책임 있는 AI:</strong> RAI 원칙 준수</li>
                        <li>• <strong>메타데이터:</strong> 출처 워터마크</li>
                    </ul>
                </div>
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
    generated_html = eval(f'f"""{html_raw_template}"""', loc)
    
    with open("AX_CA_Edu_GHLEE.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    with open("M365_Copilot_Telecom_Master.html", "w", encoding="utf-8") as f:
        f.write(generated_html)
    print("Successfully replaced clunky diagrams with gorgeous Modern Technical Architecture Maps!")
