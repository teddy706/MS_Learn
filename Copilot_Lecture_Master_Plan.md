# 📋 KT 코어/전송망 AX 엔지니어 M365 Copilot 실무 교육 마스터 플랜

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
