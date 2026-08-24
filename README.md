# Microsoft Learn & KT AX AI 교육 프로젝트 통합 포털

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
├── 01_M365_Copilot/                         # M365 Copilot 실습 자료 (교재 텍스트는 루트 파일 참조, 중복 보관 안 함)
│   ├── assets/                              # 고화질 3D Copilot 및 MS 공식 앱 아이콘
│   ├── practice_files/                      # KT 통신망 실전 실습 데이터셋 (6종 CSV/MD/Log, 루트와 동기화)
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
│   └── curriculum_content_readable.md       # 마스터 교재의 읽기 편한 축약 버전
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
