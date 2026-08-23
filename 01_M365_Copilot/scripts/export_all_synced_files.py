# -*- coding: utf-8 -*-
import os, sys, re, json, shutil
sys.stdout.reconfigure(encoding='utf-8')

html_file = 'AX_CA_Edu_GHLEE.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Sync index.html with AX_CA_Edu_GHLEE.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("1. Synced index.html with AX_CA_Edu_GHLEE.html")

# 2. Extract slidesData
start_idx = content.find('const slidesData = ')
if start_idx == -1:
    print('const slidesData not found')
    sys.exit(1)

start_json = start_idx + len('const slidesData = ')
end_json = content.find('let currentSlideIndex =', start_json)
semicolon_idx = content.rfind(';', start_json, end_json)

json_str = content[start_json:semicolon_idx].strip()
slides = json.loads(json_str, strict=False)
print(f'2. Loaded {len(slides)} slides from AX_CA_Edu_GHLEE.html')

def clean_html_to_markdown(html_str):
    # Prompts to blockquotes
    html_str = re.sub(r'<blockquote>\s*<p[^>]*>(.*?)</p>\s*</blockquote>', r'\n> 💬 **[실전 Copilot 프롬프트]**\n> \1\n', html_str, flags=re.DOTALL)
    # Headings
    html_str = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n##### \1\n', html_str)
    # Tables to readable format or clean tags
    html_str = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', html_str)
    # Strip HTML tags
    clean = re.sub(r'<[^>]+>', ' ', html_str)
    # Clean whitespace
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n+', '\n\n', clean)
    return clean.strip()

# 3. Generate curriculum_content_master_v2.md
md_master = []
md_master.append("# 📘 Work IQ & Microsoft 365 Copilot 통신·네트워크 실무 마스터 커리큘럼")
md_master.append("\n> **KT 코어/전송망 AX 엔지니어링 실무 교육 공식 마스터 교재** (4 Chapters / 52 Hands-on Units / 7 Hours)\n")
md_master.append("---\n")

current_chap = ""
for i, s in enumerate(slides):
    num = s['num']
    title = s['title'].replace("<br/>", " ").replace("<br>", " ").strip()
    subtitle = s['subtitle'].replace("<br/>", " ").replace("<br>", " ").strip()
    badge = s['badge']
    app_name = s['app_name']
    full_chapter = s['full_chapter_name']
    
    if full_chapter != current_chap:
        current_chap = full_chapter
        md_master.append(f"\n## 🏢 {full_chapter}\n")
    
    if num == 'COVER':
        md_master.append(f"### [COVER] {title}")
        md_master.append(f"- **부제**: {subtitle}")
        md_master.append(f"- **과정 요약**: KT 코어/전송망 AX 엔지니어 실무 마스터 (4 Chapters, 52 Units, 7 Hours)\n")
    elif num == 'INDEX':
        md_master.append(f"### [INDEX] {title}")
        md_master.append(f"- **부제**: {subtitle}")
        md_master.append("- **4대 챕터 로드맵**:")
        md_master.append("  1. Chapter 01: M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI (Unit 01~08)")
        md_master.append("  2. Chapter 02: 사전 준비, Copilot 활용을 위한 업무 환경 만들기 (Unit 09~14)")
        md_master.append("  3. Chapter 03: 산더미 같은 이메일 탈출과 스마트한 일정 관리 (Unit 15~19)")
        md_master.append("  4. Chapter 04: 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북 (Unit 20~52)\n")
    elif num.startswith('CH '):
        md_master.append(f"### [{num}] {title}")
        md_master.append(f"- **챕터 분류**: `{badge}`")
        md_master.append(f"- **핵심 솔루션**: `{app_name}`\n")
    else:
        md_master.append(f"### [Unit {num}] {title}")
        md_master.append(f"- **분류 태그**: `{badge}` | **솔루션**: `{app_name}`")
        md_master.append(f"- **핵심 부제**: {subtitle}\n")
        
        readable = clean_html_to_markdown(s['body'])
        md_master.append("#### 📋 세부 실무 내용 & 프롬프트 가이드")
        md_master.append(readable)
        md_master.append("\n" + ("-" * 60) + "\n")

master_text = "\n".join(md_master)

# Write to root and 01_M365_Copilot/
with open('curriculum_content_master_v2.md', 'w', encoding='utf-8') as f:
    f.write(master_text)
with open('01_M365_Copilot/curriculum_content_master_v2.md', 'w', encoding='utf-8') as f:
    f.write(master_text)
with open('01_M365_Copilot/curriculum_content_readable.md', 'w', encoding='utf-8') as f:
    f.write(master_text)
with open('01_M365_Copilot/curriculum_content.md', 'w', encoding='utf-8') as f:
    f.write(master_text)

print("3. Updated curriculum markdown files across workspace.")

# 4. Generate Copilot_Lecture_Master_Plan.md
plan_text = '''# 📋 KT 코어/전송망 AX 엔지니어 M365 Copilot 실무 교육 마스터 플랜

## 1. 교육 개요
- **과정명**: Work IQ & M365 Copilot 실무 마스터
- **부제**: KT 코어/전송망 엔지니어를 위한 데이터 기반 의사결정 & 업무 자동화 워크플로우
- **교육 대상**: KT 코어망/전송망 네트워크 운용·관제·품질 분석 엔지니어
- **총 구성**: 4 Chapters, 52 Hands-on Units, 총 7시간 집중 마스터 과정
- **보안 원칙**: Enterprise Data Protection (고객 데이터 비학습, 사내 보안 격리)

---

## 2. 4대 챕터 로드맵 & 세부 모듈

### Chapter 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI (Unit 01 ~ 08)
- **개요**: 단순 웹 AI 챗봇을 넘어 KT 통신망 업무 맥락(Context)과 엔터프라이즈 보안을 결합한 AI 패러다임 전환
- **주요 내용**:
  - Web AI vs M365 Copilot 차이 및 통신망 관제 AX 3단계 진화
  - Work IQ 지식 그래프 엔진 및 GPT-5.6 / Claude 하이브리드 모델 매칭
  - 멀티모달 망 구성도 도면·로그 분석 & Copilot Chat 통합 허브
  - 고객 데이터 비학습 보안 거버넌스 체계

### Chapter 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기 (Unit 09 ~ 14)
- **개요**: 로컬 PC 사일로를 탈피하고 클라우드 중앙화를 통한 팀 지식 자산화 및 Semantic Index 파이프라인 구축
- **주요 내용**:
  - 로컬 고립 탈피 & OneDrive KFM 자동 동기화
  - 부서 전용 SharePoint Hub 구축 & Teams 회의 녹음/스크립트 자산화
  - Microsoft Purview 보안 권한 통제 & Semantic Index 지식 인덱싱

### Chapter 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리 (Unit 15 ~ 19)
- **개요**: Outlook Copilot 기반 긴급 장애 메일 스레드 요약, 글로벌 TAC 영문 소통 및 일정 자동화
- **주요 내용**:
  - 좋은 프롬프트 4대 요소(GCSE) 및 Prompt Coach 질문 코칭
  - 수십 통 장애 스레드 10초 요약 & 핵심 원인/타임라인 추출
  - Cisco/Nokia TAC 글로벌 영문 케이스 메일 원클릭 작성
  - Schedule with Copilot 자동 조율 & 야간 점검 공지 예약 발송

### Chapter 04. 데이터기반 의사결정, 실전 플레이북 (Unit 20 ~ 52)
- **개요**: Excel, Word, PowerPoint, Teams를 아우르는 엔드투엔드 데이터 분석 및 의사결정 크로스앱 실전 플레이북
- **주요 내용**:
  - **Excel 분석 (Unit 20~28)**: 5G KPI 대용량 정제, Z-Score 이상감지, Python 회선 예측
  - **Word 문서화 (Unit 29~38)**: 20개 파일 참조 초안, 줄글→표 변환, 5G 긴급 SOP 및 CAPEX 투자 기안서
  - **PPT 시각화 (Unit 39~49)**: Word 문서 기반 1-Page 임원 보고 슬라이드 디자인 및 시각화 변환
  - **종합 워룸 (Unit 50~52)**: 크로스앱 파이프라인 연계 및 비상 장애 대응 Teams 통합 워룸 실습

---

## 3. 실습 데이터셋 (practice_files/)
1. `KT_2026_5G망_현대화_기술보고서.md`: 기술 검토 및 Word 초안 생성용 다중 소스 문서
2. `KT_5G_설비투자_CAPEX_예산안_2026.csv`: 5G 기지국 설비투자 분석 및 기안서 데이터
3. `KT_5G_수도권_기지국_품질지표_2026.csv`: 대용량 5G KPI 품질 지표 및 트래픽 분석 데이터
4. `KT_Cisco_Nokia_TAC_장애로그.txt`: 글로벌 TAC 영문 케이스 메일 작성용 라우터 장애 로그
5. `KT_L3스위치_비상점검_표준작업절차서_SOP.md`: 네트워크 긴급 대응 표준작업절차서
6. `KT_코어망_백본_트래픽_이상로그_2026.csv`: Z-Score 통계 이상 감지 및 백본 트래픽 분석 데이터

---

## 4. 슬라이드 및 포털 뷰어 가이드
- **메인 포털**: `AX_CA_Edu_GHLEE.html` (또는 루트 `index.html`)
- **단축키**:
  - `Space` / `→`: 다음 슬라이드
  - `Shift+Space` / `←`: 이전 슬라이드
  - `B`: 사이드바 토글
  - `V`: 슬라이드 모드 <-> 포털 스크롤 모드 전환
  - `F`: 전체화면 모드
'''

with open('Copilot_Lecture_Master_Plan.md', 'w', encoding='utf-8') as f:
    f.write(plan_text)
with open('01_M365_Copilot/Copilot_Lecture_Master_Plan.md', 'w', encoding='utf-8') as f:
    f.write(plan_text)

print("4. Updated Copilot_Lecture_Master_Plan.md across workspace.")

# 5. Update README.md
readme_text = '''# Microsoft Learn & KT AX AI 교육 프로젝트 통합 포털

이 저장소는 **KT 코어/전송망 엔지니어를 위한 Microsoft 365 Copilot 실무 마스터 교육 포털**과 Microsoft Learn 자격 과정(AB-100, AI-103)의 학습 자료를 체계적으로 관리합니다.

---

## 🚀 빠른 시작 & 메인 포털
- **[AX_CA_Edu_GHLEE.html](AX_CA_Edu_GHLEE.html)** / **[index.html](index.html)**: 58-Slide FHD 인터랙티브 교육 포털 (Slide 모드 & Portal 연속 스크롤 모드 지원)

---

## 📂 디렉토리 구조 및 핵심 파일

```
d:/AGY_Project/MS_Learn/
├── AX_CA_Edu_GHLEE.html                     # [MAIN] 메인 인터랙티브 슬라이드 포털 (58 슬라이드)
├── index.html                               # 루트 웹 포털 (AX_CA_Edu_GHLEE.html 동기화)
├── Copilot_Lecture_Master_Plan.md           # 강의 마스터 기획서 (4 Chapters, 52 Units, 7 Hours)
├── curriculum_content_master_v2.md          # 52개 유닛 전체 텍스트 & 실습 가이드
├── 01_M365_Copilot/                         # M365 Copilot 전용 교재 및 실습 자료
│   ├── assets/                              # 고화질 3D Copilot 및 MS 공식 앱 아이콘
│   ├── practice_files/                      # KT 통신망 실전 실습 데이터셋 (6종 CSV/MD/Log)
│   │   ├── KT_2026_5G망_현대화_기술보고서.md
│   │   ├── KT_5G_설비투자_CAPEX_예산안_2026.csv
│   │   ├── KT_5G_수도권_기지국_품질지표_2026.csv
│   │   ├── KT_Cisco_Nokia_TAC_장애로그.txt
│   │   ├── KT_L3스위치_비상점검_표준작업절차서_SOP.md
│   │   └── KT_코어망_백본_트래픽_이상로그_2026.csv
│   ├── scripts/                             # 빌드, 검증, 동기화 스크립트 모음
│   │   ├── rebuild_enhanced_chapter_dividers.py
│   │   ├── verify_slides.py
│   │   └── export_all_synced_files.py
│   ├── curriculum_content_master_v2.md
│   ├── curriculum_content_readable.md
│   └── Copilot_Lecture_Master_Plan.md
├── 02_AB-100_Agentic_AI/                    # AB-100 과정 안내
├── 03_AI-103_Azure_AI_Agents/               # AI-103 과정 안내
└── 04_MS_Learn_Resources/                  # 공통 MS Learn 링크 및 리소스
```

---

## ⌨️ 슬라이드 뷰어 단축키
| 단축키 | 동작 설명 |
| :--- | :--- |
| **`Space` / `→`** | 다음 슬라이드로 이동 |
| **`Shift+Space` / `←` / `Backspace`** | 이전 슬라이드로 이동 |
| **`B`** | 좌측 슬라이드 목록 사이드바 열기 / 닫기 |
| **`V`** | 단일 슬라이드 뷰 ↔ 전체 연속 포털 뷰 전환 |
| **`F`** | 전체화면 모드 토글 |

---

## 🛡️ 엔터프라이즈 보안 원칙
- **Enterprise Data Protection (EDP)** 준수: 모든 실습 및 프롬프트는 사내 데이터 보안 격리 환경에서 진행되며 AI 모델 학습에 사용되지 않습니다.
'''

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_text)
with open('01_M365_Copilot/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_text)

print("5. Updated README.md files across workspace.")
print("ALL RELATED FILES SUCCESSFULLY UPDATED AND SYNCHRONIZED!")
