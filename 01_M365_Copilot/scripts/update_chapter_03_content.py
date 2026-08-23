import json
import re

loc = {}
with open("update_chapter_02_content.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)
standard_chapters = loc["standard_chapters"]
fluent_icons = loc["fluent_icons"]
slide_04_body = loc["slide_04_body"]

# Assign exact Chapter 03 specification
standard_chapters[2]["chapter_num"] = "03"
standard_chapters[2]["title"] = "산더미 같은 이메일 탈출과 스마트한 일정 관리"
standard_chapters[2]["short_title"] = "03. 이메일 & 스마트 일정"
standard_chapters[2]["app_name"] = "Prompt Coach, Outlook & Teams"
standard_chapters[2]["tools"] = "좋은 프롬프트, Prompt Coach, 메일 요약, 핵심 분류, 스마트 회의, 예약 프롬프트, Teams 회의 요약, Copilot 패널"

standard_chapters[2]["units"] = [
    {
        "num": "12",
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
        "num": "13",
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
        "num": "14",
        "badge": "SMART SCHEDULING",
        "title": "[Outlook 실전 2] 스마트 회의 잡기 & 정기 작업 공지 예약 프롬프트",
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
        "num": "15",
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

# Adjust numbering for Chapter 04 units
standard_chapters[3]["units"] = [
    {
        "num": "16",
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
        "num": "17",
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
        "num": "18",
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
        "num": "19",
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
        "num": "20",
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
        "num": "21",
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
        "num": "22",
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
        "num": "23",
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
        "num": "24",
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
                <div id="progressBar" class="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-pink-500 transition-all duration-300" style="width: 4.16%;"></div>
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

print("Successfully compiled Chapter 03 updates and rebuilt all files!")
