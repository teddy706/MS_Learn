import re
import json

new_titles = [
    ("01", "범용 AI와 M365 Copilot의 차이"),
    ("02", "AI 패러다임 전환 (작성 도우미 → 자율 에이전트)"),
    ("03", "차세대 AI 모델 선택 가이드"),
    ("04", "사내 데이터 자산화 엔진 (Work IQ)"),
    ("05", "엔지니어링 멀티모달 분석 전략 (Multi-modal)"),
    ("06", "업무 자동화의 미래 (Office Agents)"),
    ("07", "실시간 통합 워크스페이스 (BizChat)"),
    ("08", "보안을 지키는 M365 AI 활용법"),
    ("09", "Copilot과 문서 중앙화의 필요성"),
    ("10", "[개인 업무 중앙화] 클라우드 문서 자산화 (OneDrive)"),
    ("11", "[부서 지식 중앙화] 팀 지식 베이스 통합 (SharePoint)"),
    ("12", "[협업 채널 중앙화] 실시간 커뮤니케이션 (Teams)"),
    ("13", "[보안 & 거버넌스] 권한 기반 안전한 중앙화 (Purview)"),
    ("14", "네트워크 자료 자동 인덱싱 파이프라인"),
    ("15", "좋은 프롬프트 작성법 (Prompt Coach)"),
    ("16", "[Outlook 실전 1] 긴급 메일 요약과 분류"),
    ("17", "[Outlook 실전 2] 해외 벤더 기술 지원 메일 작성"),
    ("18", "[Outlook 실전 3] 회의 예약과 공지 자동화"),
    ("19", "[Teams & 패널 실전] 회의 요약과 사이드 패널 활용"),
    ("20", "[핸즈온 1-1] 대용량 KPI 데이터 정제와 시각화 (Excel)"),
    ("21", "[핸즈온 1-2] 수식 계산과 피벗 차트 자동화 (Excel)"),
    ("22", "[핸즈온 2-1] 트래픽 이상 감지와 분산 분석 (Z-Score)"),
    ("23", "[핸즈온 2-2] 증설 예측 시뮬레이션 (Python)"),
    ("24", "[핸즈온 3-1] 다중 소스 기반 통합 SOP 작성 (Word)"),
    ("25", "[핸즈온 3-2] 설비 투자 분석과 제안서 작성 (CAPEX)"),
    ("26", "[핸즈온 3-3] 코어 네트워크 토폴로지 시각화 (Mermaid)"),
    ("27", "[핸즈온 4-1] 임원 보고용 프레젠테이션 자동 생성 (PPT)"),
    ("28", "[핸즈온 4-2] 1페이지 ROI 서머리 슬라이드 디자인"),
    ("29", "[마스터 플레이북 1] 크로스앱 통합 워크플로우 (Excel-Word-PPT)"),
    ("30", "[마스터 플레이북 2] 장애 대응 협업 룸 운영 (War-Room)"),
    ("31", "[엔지니어 가이드] 프롬프트 패턴집 & 치트시트")
]

# Update curriculum_content_readable.md
with open("curriculum_content_readable.md", "r", encoding="utf-8") as f:
    md_content = f.read()

for num_str, title_str in new_titles:
    # Pattern: ### [Unit XX] Old Title
    md_content = re.sub(
        rf'###\s*\[Unit\s*{num_str}\]\s*[^\n]+',
        f'### [Unit {num_str}] {title_str}',
        md_content
    )

with open("curriculum_content_readable.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("Updated curriculum_content_readable.md with new slide titles.")

# Now execute sync_markdown_to_html.py to regenerate HTML
loc = {}
with open("sync_markdown_to_html.py", "r", encoding="utf-8") as f:
    exec(f.read(), loc)

print("Successfully updated all HTML files (AX_CA_Edu_GHLEE.html, index.html, M365_Copilot_Telecom_Master.html)!")
