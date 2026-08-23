# KT AX | Microsoft 365 Copilot 통신 엔지니어링 표준 교재 (마스터 텍스트 & 실습 가이드)

> **문서 버전:** 2026 Final Master Edition (52 Units Complete)  
> **작성자:** 이광희  
> **목적:** 52개 슬라이드 전체의 세부 텍스트 검토/수정 및 실습 예제 파일(Sample Dataset) 연계 가이드

---

## 📂 실습 예제 파일 디렉토리 안내 (`practice_files/`)

| 파일명 | 형식 | 설명 및 용도 | 연계 유닛 |
|---|---|---|---|
| `KT_5G_수도권_기지국_품질지표_2026.csv` | CSV/Excel | 수도권 주요 50개 국사 트래픽, PRB 사용률, 드롭률 | Unit 07, 20, 24, 25, 29, 30 |
| `KT_코어망_백본_트래픽_이상로그_2026.csv` | CSV/Excel | 라우터별 대역폭, 패킷 손실, 지연시간 통계 | Unit 26, 35 |
| `KT_5G_설비투자_CAPEX_예산안_2026.csv` | CSV/Excel | 코어망/무선망 증설 비용, 운용비 절감액, ROI | Unit 27, 36, 48 |
| `KT_2026_5G망_현대화_기술보고서.md` | Word/MD | 15페이지 분량의 5G 네트워크 고도화 보고서 초안 | Unit 07, 30, 39, 42, 47 |
| `KT_L3스위치_비상점검_표준작업절차서_SOP.md` | Word/MD | L3 스위치 과부하 시 단계별 비상 복구 절차서 | Unit 30, 31, 35 |
| `KT_Cisco_Nokia_TAC_장애로그.txt` | Text/Log | BGP 플래핑 및 ASIC 라인 에러 시스로그 원본 | Unit 17 |

---

## 📑 52개 슬라이드 마스터 텍스트 & 실습 가이드 전수 목록

## 🌐 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI

### [Unit 01] 범용 AI와 M365 Copilot의 핵심 차이
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `AI COMPARISON`
- **부제목(Subtitle):** 단순 웹 챗봇의 한계를 넘어, KT 사내 통신 업무 맥락(Context)과 엔터프라이즈 보안을 갖춘 AI로의 전환

#### 📝 슬라이드 본문 구조 및 핵심 내용
Web AI 웹 기반 범용 AI (ChatGPT 등) ✕ 업무 맥락 부재: 사내 메일, Teams 대화, 결재 문서를 전혀 알지 못함 ✕ 데이터 유출 위험: 입력 프롬프트가 외부 공용 모델 재학습에 노출 ✕ 수동 복사-붙여넣기: 브라우저와 오피스 앱 간의 비효율적 단절 ✕ 권한 제어 불가: 사내 보안 등급(ACL)에 따른 정보 격리 불가 범용 지식 검색 중심의 퍼블릭 웹 도우미 Work IQ AI Microsoft 365 Copilot ✓ Work IQ 사내 맥락 통합: 내 메일, 일정, SharePoint 문서를 즉시 연계 이해 ✓ 완벽한 보안 격리: Zero-Data Retention & 고객 데이터 학습 절대 배제 ✓ 오피스 내 네이티브 실행: Word, Excel, Teams, Outlook 내에서 직접 생성/수정 ✓ Entra ID ACL 자동 준수: 내가 읽기 권한을 가진 문서에 한해서만 안전 답변 기업 내부 데이터를 안전하게 활용하는 엔터프라이즈 전담 동료 💡 핵심 통찰: 웹 AI가 세상의 일반 지식을 아는 도우미라면, M365 Copilot은 사내 맥락(Context)과 보안을 완벽히 이해하는 전담 동료입니다.

---

### [Unit 02] 문서 작성 도우미에서 자율 관제 에이전트로의 전환
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `PARADIGM SHIFT`
- **부제목(Subtitle):** 단순 문서 작성을 넘어 KT 네트워크 장애 분석 및 조치 명령을 직접 수행하는 Autonomous AI로의 진화

#### 📝 슬라이드 본문 구조 및 핵심 내용
Phase 1 Assistive (보조 도우미) 사용자가 구체적인 프롬프트를 입력하면 텍스트를 단순 생성하거나 문법을 다듬어주는 수동적 보조 단계 단순 텍스트 작성 & 오탈자 교정 Phase 2 Copilot (협업 동료) 사내 메일, Teams, 문서 데이터를 Work IQ로 결합하여 사용자의 질문에 지능형 맥락 기반으로 답변하는 단계 사내 맥락 융합 & 회의/데이터 요약 Phase 3 (Next) Autonomous Agent (자율 관제) KT 통신망 트래픽 이상을 스스로 감지하고, 표준 작업 절차(SOP)에 따라 조치 제안 및 명령을 직접 실행하는 에이전트 이상 징후 자동 색출 & 조치 자율 실행 💡 핵심 패러다임: 지시를 기다리는 단순 작성 보조를 넘어, Work IQ와 Office Agents를 기반으로 KT 네트워크 이상을 선제적으로 감지하고 조치를 주도하는 자율 협업 파트너로 진화합니다.

---

### [Unit 03] 차세대 AI 모델 선택 가이드
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `MODEL ARCHITECTURE`
- **부제목(Subtitle):** GPT-5.6, Claude Sonnet 5, Work IQ 엔진의 KT 엔지니어링 최적 조합

#### 📝 슬라이드 본문 구조 및 핵심 내용
Advanced GPT-5.6 복합 논리 & 수학적 추론 5G 기지국 CAPEX 회수율 계산, Z-Score 이상 트래픽 통계 분석 및 대규모 분산 계산 Excel / Python 연동 Precision Claude Sonnet 5 초정밀 코딩 & 표준 문서 BGP 라우팅 구성 스크립트 작성, RFC 표준 준수 보고서 및 글로벌 기술 제안서 Word / SOP 작성 Low Latency Work IQ Small LLM 사내 지식 초고속 인덱싱 SharePoint/OneDrive 파일 검색, 보안 ACL 권한 검증 및 실시간 사내 커뮤니케이션 BizChat / Teams

---

### [Unit 04] KT 사내 데이터 자산화 엔진 (Work IQ)
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `WORK IQ ENGINE`
- **부제목(Subtitle):** KT 전사 메일, 국사 점검 일지, 장애 보고서를 지능형 업무 그래프로 연결

#### 📝 슬라이드 본문 구조 및 핵심 내용
Graph Engine Work IQ가 실무를 이해하는 방식 단순 키워드 매칭이 아닌, 엔지니어의 프로젝트 참여 이력 , 최근 검토한 네트워크 구성도 , Teams 장애 대화 스레드 의 맥락을 결합하여 가장 정확한 답변을 도출합니다. 🔒 Entra ID ACL 검증: 권한이 없는 문서는 검색 결과에 절대 미포함 // Work IQ 지식 추출 파이프라인 1. User Query: "지난달 코어망 점검 이슈 요약해줘" 2. Graph Scan: Exchange 메일 + Teams 채널 + SharePoint SOP 3. Contextual Synthesis: 시간순 장애 타임라인 자동 생성

---

### [Unit 05] 엔지니어링 멀티모달 분석 파이프라인
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `MULTIMODAL AI`
- **부제목(Subtitle):** KT 5G 코어망 구성도 이미지와 대용량 라우터 시스로그(Syslog)를 동시에 분석하는 차세대 파이프라인

#### 📝 슬라이드 본문 구조 및 핵심 내용
🖼️ 네트워크 토폴로지 도면 분석 복잡한 Visio/PNG 네트워크 구성도 이미지를 업로드하면 단일 장애점(SPOF)을 식별하고 이중화 개선 권고안을 즉시 제시합니다. "이 토폴로지 도면에서 L3 스위치 백본 이중화 링크 누락 구간을 찾아줘" 📊 대용량 로그 & 수치 복합 추론 Excel 트래픽 급증 시간대와 장애 리포트 본문을 결합하여 복합적인 장애 인과관계를 수학적으로 검증합니다. "CPU 점유율 90% 이상 시점과 BGP 플래핑 알람 발생의 상관계수 계산"

---

### [Unit 06] KT 업무 자동화 에이전트 (Office Agents)
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `OFFICE AGENTS`
- **부제목(Subtitle):** KT 통신 운영 및 품질 관리 표준 절차를 전담하여 스스로 모니터링하고 조치하는 AI 에이전트 구축

#### 📝 슬라이드 본문 구조 및 핵심 내용
01. Monitoring NOC 정기 브리핑 에이전트 매일 아침 트래픽 요약 및 주요 장애 이슈를 자동 집계하여 Teams 채널에 정기 공유 자율 모니터링 02. Security CVE 취약점 분석 에이전트 장비 펌웨어 버전과 신규 보안 패치를 자동 비교하여 긴급 조치 권고서 발행 보안 자동 진단 03. SOP 표준 작업 절차서 에이전트 엔지니어의 커맨드 로그를 표준 양식의 Word 매뉴얼로 자동 변환 및 지식화 표준 문서화

---

### [Unit 07] 실시간 통합 워크스페이스 (BizChat)
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `COPILOT WORK`
- **부제목(Subtitle):** KT M365 앱 전체를 관통하는 중앙 커맨드 센터 활용법

#### 📝 슬라이드 본문 구조 및 핵심 내용
✨ BizChat Cross-App Query "/teams '코어망운영팀' 채널에서 오늘 오전 9시 이후 논의된 '백본 BGP 플래핑' 관련 대화와, /files '2026_코어망_토폴로지.docx'를 대조해서 발생 원인과 현재 조치 현황을 3줄 요약하고, 담당 엔지니어에게 보낼 회신 메일 초안을 작성해줘." 📎 /files (SharePoint 문서 참조) 💬 /teams (채널 대화 검색) ✉️ /mail (메일 스레드 통합)

---

### [Unit 08] 보안 거버넌스를 준수하는 M365 활용법
- **소속 챕터:** 01. M365 Copilot의 변화, 일을 더 잘 이해하게 된 AI
- **도구 / 영역:** `Work IQ & Copilot Core`
- **핵심 배지:** `ENTERPRISE SECURITY`
- **부제목(Subtitle):** KT 통신망 보안 규정을 100% 준수하며 기업 데이터 외부 유출을 원천 차단하는 Zero-Data Retention

#### 📝 슬라이드 본문 구조 및 핵심 내용
User Authentication 👤 💻 사내 인증 엔지니어 Entra ID SSO 로그인 Apps on Your Devices 📄 Word 📊 Excel 📑 PPT ✉️ Outlook 💬 Teams ☁️ OneDrive Your Microsoft 365 Tenant Encrypted Boundary Microsoft Graph (Work IQ + Entra ID ACL 실시간 인덱싱) Customer Data Boundary (외부 재학습 원천 차단) ✉️ Exchange ☁️ SharePoint 💬 Teams 🛡️ Purview ✨ Microsoft 365 Copilot Core Azure OpenAI Private Service GPT-5.6 / Claude Sonnet 5 (Zero-Retention) 🛡️ 고객 데이터는 테넌트 내에서 완벽히 보호되며, AI 모델 재학습에 절대 사용되지 않습니다.

---

## 🌐 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기

### [Unit 09] Copilot 도입과 문서 중앙화의 필요성
- **소속 챕터:** 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기
- **도구 / 영역:** `Cloud Document Centralization`
- **핵심 배지:** `PREPARATION & SETUP`
- **부제목(Subtitle):** Copilot 성능을 100% 이끌어내기 위한 필수 선결 과제: 파편화된 로컬 문서를 클라우드로 통합

#### 📝 슬라이드 본문 구조 및 핵심 내용
Local PC 로컬 PC 파편화의 한계 • Copilot 인덱싱 불가: C드라이브, 바탕화면 파일은 AI가 접근 못함 • 팀원 간 지식 고립: 담당자 부재 시 설정 파일 및 SOP 조회 불가 • 버전 충돌 발생: `최종_수정_진짜최종.xlsx` 등 파일 버전 혼선 Cloud M365 클라우드 문서 중앙화 • Graph 실시간 인덱싱: 업로드 즉시 Copilot이 사내 지식으로 인식 • 3대 중앙화 축: OneDrive(개인), SharePoint(부서), Teams(프로젝트) • 자동 버전 이력: 실수로 덮어써도 이전 시점으로 1초 복원

---

### [Unit 10] OneDrive를 활용한 개인 업무 문서 중앙화
- **소속 챕터:** 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기
- **도구 / 영역:** `Cloud Document Centralization`
- **핵심 배지:** `ONEDRIVE CENTRAL`
- **부제목(Subtitle):** KT 엔지니어 개인의 망 분석 데이터, 로그 메모를 Copilot이 즉시 참조할 수 있도록 세팅

#### 📝 슬라이드 본문 구조 및 핵심 내용
Step 1 PC 폴더 백업 동기화 내 컴퓨터의 바탕화면과 문서 폴더를 OneDrive에 자동 동기화하여 저장과 동시에 인덱싱 Step 2 구조화된 폴더 명명 `[연도]_[프로젝트명]_[문서종류]` 표준 규칙으로 파일명을 정리하여 검색 정확도 극대화 Step 3 자동 저장 (AutoSave On) Office 앱 상단의 '자동 저장'을 켜서 작성 중인 모든 수정 사항이 즉시 Copilot 그래프에 동기화

---

### [Unit 11] SharePoint 기반 팀 지식 베이스 통합
- **소속 챕터:** 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기
- **도구 / 영역:** `Cloud Document Centralization`
- **핵심 배지:** `SHAREPOINT HUB`
- **부제목(Subtitle):** KT 관제 센터 및 부서의 장비 Config 표준, 망 구성도, 과거 장애 이력을 하나의 팀 허브로 일원화

#### 📝 슬라이드 본문 구조 및 핵심 내용
부서 공용 매뉴얼과 장애 이력의 지식 자산화 신규 엔지니어가 입사하거나 야간 긴급 장애 시 선임자에게 묻지 않고도 Copilot에게 질문하면, SharePoint에 축적된 매뉴얼과 보고서를 기반으로 3초 만에 검증된 해법 을 답변합니다. 📁 라우터/스위치 Config 표준 라이브러리 📋 통신사 간 상호연동 인터페이스 가이드 🛡️ 비상 장애 대응 표준 작업 절차서(SOP)

---

### [Unit 12] Teams를 통한 실시간 협업 채널 중앙화
- **소속 챕터:** 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기
- **도구 / 영역:** `Cloud Document Centralization`
- **핵심 배지:** `TEAMS COLLABORATION`
- **부제목(Subtitle):** KT 현장 출동팀, 관제 센터, 엔지니어링 부서 간 실시간 대화와 회의 녹화본의 유기적 컨텍스트 융합

#### 📝 슬라이드 본문 구조 및 핵심 내용
📁 1. 채널별 파일 탭 활용 이메일 첨부 대신 Teams 채널 '파일' 탭에 저장 ➔ SharePoint와 자동 연동되어 팀 전체 지식으로 즉시 인덱싱됩니다. 🎙️ 2. 회의 녹음 및 스크립트(Transcript) 장애 대책 회의 시 '녹음 및 대화 기록'을 켜두면, 회의 직후 Copilot이 논의된 액션 아이템과 결정 사항을 자동 정리합니다.

---

### [Unit 13] Purview 기반 권한 관리와 보안 거버넌스
- **소속 챕터:** 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기
- **도구 / 영역:** `Cloud Document Centralization`
- **핵심 배지:** `SECURITY GOVERNANCE`
- **부제목(Subtitle):** 중앙화된 사내 문서 중 비인가자나 타 부서에 기밀이 노출되지 않도록 완벽 통제

#### 📝 슬라이드 본문 구조 및 핵심 내용
Entra ID ACL 권한 제어 사용자의 읽기 권한을 그대로 계승하여, 특정 폴더에 권한이 없는 직원이 질의해도 해당 문서는 검색 결과에 절대 노출되지 않습니다. Purview 민감도 레이블 보호 [대외비] 레이블이 지정된 문서를 Copilot이 인용하거나 요약할 때도 원본 문서의 암호화와 보안 등급이 100% 유지됩니다.

---

### [Unit 14] 네트워크 기술 자료 자동 인덱싱 파이프라인
- **소속 챕터:** 02. 사전 준비, Copilot 활용을 위한 업무 환경 만들기
- **도구 / 영역:** `Cloud Document Centralization`
- **핵심 배지:** `ENV PIPELINE`
- **부제목(Subtitle):** 주기적으로 업데이트되는 장비 백업 파일의 자동 인덱싱 구축 파이프라인

#### 📝 슬라이드 본문 구조 및 핵심 내용
⚙️ 1. 장비 자동 백업 TFTP / FTP 백업 🔄 2. Power Automate OneDrive 동기화 ⚡ 3. Graph Indexing 자동 벡터 인덱싱 ✨ 4. Copilot 질의 즉시 답변 가능

---

## 🌐 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리

### [Unit 15] 좋은 프롬프트 작성법과 Prompt Coach
- **소속 챕터:** 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리
- **도구 / 영역:** `Outlook & Teams Productivity`
- **핵심 배지:** `PROMPT COACH`
- **부제목(Subtitle):** 목표(Goal), 맥락(Context), 출처(Source), 기대형식(Expectation) 4대 요소와 AI 코칭

#### 📝 슬라이드 본문 구조 및 핵심 내용
🎯 좋은 프롬프트의 4대 핵심 구조 1. Goal (목표): 무엇을 만들어야 하는가? (예: 회신 메일 초안) 2. Context (맥락): 어떤 상황인가? (예: BGP 순단 발생) 3. Source (출처): 어떤 파일 참조? (예: /files '로그.xlsx') 4. Expectation (형식): 어조와 형태는? (예: 타임라인 표) ✨ Prompt Coach 에이전트 실전 코칭 프롬프트를 보내기 전 코칭을 요청하면 누락된 맥락과 모호한 지시를 스스로 찾아내어 고품질 프롬프트로 업그레이드합니다. "내 프롬프트에서 엔지니어링 용어와 참조 출처가 부족한 부분을 Prompt Coach 원칙에 맞게 보완해줘."

---

### [Unit 16] 긴급 장애 메일 요약 및 핵심 분류
- **소속 챕터:** 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리
- **도구 / 영역:** `Outlook & Teams Productivity`
- **핵심 배지:** `OUTLOOK MASTERY`
- **부제목(Subtitle):** 수십 통이 얽힌 KT 백본망 트래픽 급증 스레드 타임라인 요약 및 긴급 기술 메일 즉시 추출

#### 📝 슬라이드 본문 구조 및 핵심 내용
Summary 1. 스레드 3초 요약 30통이 넘는 답장 메일을 일일이 읽지 않아도 [Copilot 요약] 버튼 한 번으로 핵심 사건과 액션 아이템을 요약합니다. "최초 장애 알람 발생 시각, 담당자별 조치 내역, 미해결 이슈를 타임라인 표로 정리해줘" Search 2. 핵심 분류 & 맥락 검색 단순 단어가 아닌 자연어 맥락 검색으로 지난 6개월간 Cisco TAC 엔지니어와 주고받은 버그 패치 메일만 정확히 필터링합니다. "지난 분기 코어 라우터 OS 버그 패치와 관련해 벤더사에서 보낸 권고 메일을 찾아줘"

---

### [Unit 17] 해외 벤더 기술 지원(TAC) 영문 메일 작성
- **소속 챕터:** 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리
- **도구 / 영역:** `Outlook & Teams Productivity`
- **핵심 배지:** `GLOBAL TAC`
- **부제목(Subtitle):** KT 코어 장비(Cisco/Nokia/Ericsson) 오류 로그를 첨부한 영문 TAC 케이스 오픈 메일 자동 생성

#### 📝 슬라이드 본문 구조 및 핵심 내용
✉️ Global TAC Support Request "현재 발생한 OSPF LSA 플러딩 및 패킷 드롭 현상에 대해 Cisco TAC 엔지니어에게 Severity-2 티켓을 요청하는 정중하고 전문적인 영문 메일을 작성해줘. 발생 일시, 장비 모델(ASR 9000), IOS-XR 버전, 첨부한 Show tech-support 로그를 포함해줘."

---

### [Unit 18] 스마트 회의 예약 및 공지 자동화
- **소속 챕터:** 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리
- **도구 / 영역:** `Outlook & Teams Productivity`
- **핵심 배지:** `SMART SCHEDULING`
- **부제목(Subtitle):** 참석자 캘린더 빈 시간 자동 탐색 및 특정 시간대 자동 발송 예약 프롬프트

#### 📝 슬라이드 본문 구조 및 핵심 내용
Meeting 1. 스마트 회의 잡기 참석자들의 캘린더를 자동 대조하여 공통 빈 시간을 찾고 회의 안건과 Teams 링크가 포함된 초대를 즉시 생성합니다. "이번 주 금요일 오후 전송망팀과 무선팀 팀장님들이 모두 가능한 30분 미팅을 잡아줘" Schedule 2. 정기 작업 공지 예약 야간 작업 공지 메일을 특정 시간(예: D-1일 17:30)에 자동으로 작성하고 발송 대기 상태로 예약합니다. "내일 새벽 02:00 작업 영향도 안내 메일을 오늘 17:30에 발송되도록 예약해줘"

---

### [Unit 19] Teams 회의 요약과 Copilot 사이드 패널 활용
- **소속 챕터:** 03. 산더미 같은 이메일 탈출과 스마트한 일정 관리
- **도구 / 영역:** `Outlook & Teams Productivity`
- **핵심 배지:** `TEAMS RECAP & PANEL`
- **부제목(Subtitle):** 회의 직후 자동 생성되는 지능형 Recap과 앱 우측 사이드 패널을 통한 실시간 초안 튜닝

#### 📝 슬라이드 본문 구조 및 핵심 내용
Recap 1. Teams 회의 요약하기 1시간 회의가 끝나면 전체 대화를 분석하여 결정된 사항(Decisions)과 담당자별 할 일(Action Items)을 5줄로 자동 정리합니다. "이 회의에서 김엔지니어와 박팀장이 합의한 롤백 기준과 일정을 요약해줘" Side Panel 2. Copilot 사이드 패널 우측 [Copilot 패널]을 열어 대화하듯 메일 초안의 어조를 정중하게 변경하거나 분량을 조절하고 사내 규정을 질의합니다. "작성된 회신 메일을 조금 더 격식 있는 비즈니스 어조로 수정하고 길이 줄여줘"

---

## 🌐 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북

### [Unit 20] Excel Copilot 엔지니어링 활용 4대 핵심 기능
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • CORE 4 PILLARS`
- **부제목(Subtitle):** KT 5G 무선망 품질 지표(PRB Usage, Drop Rate) 정제, 생성, 시각화, 통계 분석 4대 핵심 기능

#### 📝 슬라이드 본문 구조 및 핵심 내용
🔧 01. 편집 & 02. 생성 • 편집 (Edit): 서식 적용, 레이아웃 정리, 조건부 서식 강조 • 생성 (Create): 수식 자동 생성, 예시 기반 데이터 열 자동 채우기 📈 03. 시각화 & 04. 분석 • 시각화 (Visualize): 차트 즉시 생성, 피벗 테이블 1초 빌드 • 분석 (Analyze): 텍스트 요약, 이상치(Outlier) 발견, 데이터 필터링 ✨ "이 시트의 KT 수도권 5G 기지국 전체 트래픽 통계를 분석하고, 이상치가 발생한 주요 시간대를 피벗 테이블로 요약해줘."

---

### [Unit 21] 전역 설정과 '.Rules' 시트 기반 규칙 제어
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • CUSTOM RULES`
- **부제목(Subtitle):** 계정 전체에 적용되는 전역 설정과 '.Rules' 워크시트를 통한 파일 단위 동적 규칙 제어

#### 📝 슬라이드 본문 구조 및 핵심 내용
🌐 계정 전체 적용 (Global) • 통화 기호(₩), 날짜 형식(DD-MMM-YYYY) 기본값 • 어조(Tone) 및 설명 상세도(Detail Level) 설정 • 모든 통합 문서에 공통으로 계승 적용 📋 특정 파일 전용 (Local '.Rules') • '.Rules' 전용 시트 생성 : A열에 셀당 1개 규칙 나열 • IF 수식 동적 규칙 적용: =IF(B1="Executive", "1페이지 요약", "상세 테이블") • 공유 보존: 파일과 함께 규칙이 다른 사용자에게 전달

---

### [Unit 22] 사내 파일 및 Power BI 데이터 연동 전략
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • DATA SOURCES`
- **부제목(Subtitle):** 웹 검색 인용, SharePoint 사내 문서, 페더레이션 커넥터(Canva, HubSpot, FactSet), Power BI 대시보드

#### 📝 슬라이드 본문 구조 및 핵심 내용
🌐 웹 (Web) 실시간 검색 & 출처 연동 ☁️ 사내 작업 파일 SharePoint / OneDrive 🔌 페더레이션 커넥터 Canva, Salesforce, FactSet 📊 Power BI 대시보드 실시간 분석

---

### [Unit 23] 수식 자동 제안과 SKILL.md 매크로 연동
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • SKILLS & AUTOMATION`
- **부제목(Subtitle):** 컨텍스트 기반 수식 자동 완성, 패턴 인식 채우기, SKILL.md 사용자 정의 반복 프로세스 매크로화

#### 📝 슬라이드 본문 구조 및 핵심 내용
⚡ 수식 제안 (Formula Suggestion) • 컨텍스트 기반 자동 완성 & 예시 패턴 인식 • 파일 > 옵션 에서 Copilot 수식 제안 On/Off 가능 • 복잡한 INDEX-MATCH 수식을 1초 만에 자동 생성 🧩 기술 (Skills) 연동 • 반복 프로세스 매크로화: @mention 또는 메뉴 호출 • 기본 기술: @brandkit , @chart_design • 사용자 지정 기술: OneDrive '기술' 폴더 내 SKILL.md 정의

---

### [Unit 24] 대용량 5G KPI 데이터 정제 및 시각화
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • HANDS-ON 1-1`
- **부제목(Subtitle):** KT 기지국 비정형 로그 정제, 결측치 자동 보정, 과부하 기지국(PRB 85% 이상) 조건부 상태 분류

#### 📝 슬라이드 본문 구조 및 핵심 내용
📊 Excel Copilot 기능 아키텍처 맵 운영 모드 • .Rules 시트 • 페더레이션 커넥터 • Skills 기술 Excalidraw Map ⚡ 1. 3대 운영 모드 • 편집: 셀/수식 직접 수정 • 계획: 단계별 파이프라인 • 채팅: 데이터 인사이트 질의 📋 2. '.Rules' 전용 시트 • A열 나열: 셀당 1개 규칙 기술 • 동작 전환: 드롭다운 수식 제어 • 공유 보존: 파일과 함께 전파 🌐 3. 데이터 & 페더레이션 • 사내 지식: 회사 문서, 대화 • 커넥터: Salesforce, FactSet • 출처 인용: 웹 검색 결합 🧩 4. 기술 (Skills) • MS 기술: @brandkit, @theme • 사용자 정의: `SKILL.md` • 모델: GPT-5.6 / Claude Step 1. 결측치 및 비정형 로그 정제 "빈 셀(N/A)을 이전 정상 측정값으로 채우고, 'Latency_ms' 열에서 비정상 음수 값을 0으로 일괄 보정해줘." Step 2. 조건부 파생 열 생성 "'PRB_Usage'가 85% 이상이면서 'Drop_Rate'가 1.5% 초과인 경우 '위험', 그렇지 않으면 '정상'으로 분류하는 'Status' 열 추가해줘."

---

### [Unit 25] 기지국 수식 계산과 피벗 차트 자동화
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • HANDS-ON 1-2`
- **부제목(Subtitle):** KT 기지국 ID별 시간대별 트래픽 추이 및 패킷 드롭률 상관관계 피벗 차트 자동 생성

#### 📝 슬라이드 본문 구조 및 핵심 내용
💡 수식 제안 관리 & 예제 기반 패턴 수식 (Formula Suggestions) 수식 입력 즉시 최적 함수 추천 • 예제 기반 패턴 감지로 열 자동 채우기 Excel AI Engine 📊 Excel Copilot KPI Pivot Prompt "'PRB_Usage' 컬럼이 85% 이상이면서 'Drop_Rate'가 1.5%를 초과하는 과부하 기지국만 필터링하는 새 열을 추가하고, 기지국 ID별 시간대별 트래픽 추이를 피벗 차트로 생성해줘."

---

### [Unit 26] 백본 트래픽 이상 감지와 Z-Score 분산 분석
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • HANDS-ON 2-1`
- **부제목(Subtitle):** KT 코어망 통계적 이상치를 자동으로 색출하여 잠재적 DDoS 공격 및 백홀 병목 원인 규명

#### 📝 슬라이드 본문 구조 및 핵심 내용
⚡ Z-Score Anomaly Detection "최근 30일간의 백홀 트래픽 데이터를 바탕으로 Z-Score가 +2.5 이상인 이상 트래픽 발생 구간을 빨간색 조건부 서식으로 강조하고, 사용자 접속자 수(UE) 급증과의 상관관계를 분석해줘."

---

### [Unit 27] 회선 증설 예측 시뮬레이션 (Python in Excel)
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel & Python`
- **핵심 배지:** `EXCEL • HANDS-ON 2-2`
- **부제목(Subtitle):** KT 트래픽 급증 국사 대상 대역폭 증설 시나리오별 패킷 지연율(Latency) 시뮬레이션 구동

#### 📝 슬라이드 본문 구조 및 핵심 내용
Python in Excel 상관계수 히트맵 시각화 "기지국 접속자 수, 패킷 지연 시간(RTT), 다운로드 처리량 간의 상관관계를 파이썬 seaborn heatmap으로 시각화하여 현재 시트의 G2 셀에 삽입해줘." Simulation What-If 대역폭 증설 시뮬레이션 "백홀 대역폭을 10Gbps에서 20Gbps로 확장 시 피크타임 패킷 지연이 몇 % 개선되는지 파라미터 변동 모델링을 실행해줘."

---

### [Unit 28] 정답을 부르는 엑셀 프롬프트 작성 원칙
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Excel`
- **핵심 배지:** `EXCEL • CHEAT SHEET`
- **부제목(Subtitle):** 구체적 목표, 정확한 열 이름 지정, 점진적 구체화(Refinement) 및 사용자 검증(Check) 원칙

#### 📝 슬라이드 본문 구조 및 핵심 내용
✅ 정답을 부르는 4대 프롬프트 원칙 ☑ 구체적인 목표 설정 (두루뭉술한 질문 X) ☑ 정확한 열 이름 / 범위 명시 ☑ 포괄적 질문 후 점진적 구체화 (Refinement) ☑ 이전 결과를 바탕으로 추가 질문 (Context 유지) ⚠️ 엔지니어 주의사항 (Check!) 생성된 수식과 계산 결과는 항상 원본 비즈니스 로직과 일치하는지 엔지니어의 최종 검증(Validation)이 필수적입니다.

---

### [Unit 29] Word Copilot 엔지니어링 5대 핵심 비법
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • 5 MAGIC SECRETS`
- **부제목(Subtitle):** KT 통신 표준 문서, 긴급 점검 보고서, 제안서 작성을 위한 5가지 실무 작성 비법

#### 📝 슬라이드 본문 구조 및 핵심 내용
1. 초안 생성 (Draft) 백지 상태 탈출, /files 최대 20개 사내 파일 동시 참조 2. 문장 다듬기 (Rewrite) 전문 엔지니어링 어조 전환, 줄글의 정형 표(Table) 변환 3. 요약 & 모바일 200단어 상단 자동 요약, 현장 마이크 음성 메모 보고서화 ✨ "/files KT_5G_품질보고서.xlsx 를 기반으로 통신망 긴급 점검 SOP 초안을 표 형식으로 작성해줘."

---

### [Unit 30] 최대 20개 파일 참조 기반 초안 자동 생성
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • MULTI-REFERENCE`
- **부제목(Subtitle):** 막막한 백지 상태에서 최대 20개 사내 파일(/files)을 결합하여 완벽한 초안 완성

#### 📝 슬라이드 본문 구조 및 핵심 내용
📁 연계 실습 데이터: practice_files/KT_5G_수도권_기지국_품질지표_2026.csv , practice_files/KT_2026_5G망_현대화_기술보고서.md 📑 Multi-File Reference Prompt "/files 'KT_5G_수도권_기지국_품질지표_2026.csv', 'KT_2026_5G망_현대화_기술보고서.md' 2개 파일을 결합하여, 3분기 수도권 기지국 트래픽 집중 구역에 대한 긴급 증설 필요성을 강조하는 3페이지 엔지니어링 기안서 초안을 작성해줘." 최대 20개 사내 파일 동시 참조 SharePoint / OneDrive 권한 연동 표 및 수치 데이터 자동 인용

---

### [Unit 31] 자동 다시 쓰기(Rewrite)와 정형 표 변환
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • REWRITE & TABLE`
- **부제목(Subtitle):** 어조/명확성 자동 개선, 톤앤매너 실시간 조절, 장황한 글의 정형 표(Table) 변환

#### 📝 슬라이드 본문 구조 및 핵심 내용
🔄 Rewrite & Table Conversion "아래 장황하게 나열된 L3 스위치 점검 절차 줄글을 현장 엔지니어가 10초 만에 파악할 수 있도록 [단계 | 점검 항목 | CLI 명령어 | 정상 기준 | 이상 시 조치] 5개 열로 구성된 직관적인 표(Table)로 변환해줘." ❌ 변경 전 (Before): 장황한 줄글 스위치 접속 후 콘솔에서 CPU 점유율을 확인하고 80%가 넘으면 프로세스 목록을 본 후...” ✅ 변경 후 (After): 일목요연한 정형 표 단계별 CLI 명령어와 정상 기준치, 긴급 조치 가이드가 표 형태로 완벽 정돈

---

### [Unit 32] 200단어 상단 자동 요약 및 돋보기 질의
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • ANALYSIS & Q&A`
- **부제목(Subtitle):** 200단어 이상 문서의 자동 요약 생성, 돋보기 심층 분석 및 특정 단락 Q&A

#### 📝 슬라이드 본문 구조 및 핵심 내용
🔍 Executive Summary & Deep Q&A "이 20페이지 분량의 통신망 기술 문서 상단에 임원 보고용 200단어 핵심 요약(Executive Summary)을 추가하고, 문서 전체에서 언급된 '보안 취약점 3가지'와 '단계별 해결책'을 돋보기 분석으로 정리해줘." 📌 200단어 자동 상단 브리핑 🔍 돋보기 기반 특정 섹션 심층 질의 ⚡ Action Items 3줄 도출

---

### [Unit 33] DALL-E 3 기반 맞춤형 이미지 및 배너 제작
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • DALL-E 3 VISUALS`
- **부제목(Subtitle):** 자연어 프롬프트로 보고서 맞춤형 고화질 삽화 및 챕터 헤더 배너 제작

#### 📝 슬라이드 본문 구조 및 핵심 내용
🎨 DALL-E 3 Engineering Visual "KT 5G 통신망 현대화 기술 보고서 챕터 표지로 사용할 수 있는 16:9 와이드 비율의 고화질 테크 배너 이미지를 생성해줘. (스타일: 미니멀한 3D 네온 블루 네트워크 그리드, 기지국 광케이블 연결, 클라우드 코어망, 깨끗한 화이트 배경)" ✓ 엔지니어링 문서 전용 3D/아이소메트릭 스타일 프롬프트 권장 ✓ 모호한 단어 대신 피사체, 조명, 색상 팔레트, 구도 명시

---

### [Unit 34] 모바일 음성 메모의 정형 보고서 변환
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • MOBILE AUDIO`
- **부제목(Subtitle):** iOS/Android 모바일 환경에서 이동 중 음성 노트를 녹음하여 정형화된 보고서로 변환

#### 📝 슬라이드 본문 구조 및 핵심 내용
🎙️ Mobile Voice to Structured Report "서버실 현장에서 녹음된 이 음성 메모 텍스트를 분석하여, [점검 일시 | 점검 국사 | 랙(Rack) 번호 | 발견된 이상 증상 | 현장 조치 내역 | 후속 조치 필요사항] 양식의 정규 현장 점검 완료 보고서로 구조화해줘." 📱 스마트폰 음성 녹음 ⚡ 비정형 구술 텍스트 분석 📑 표준 양식 자동 변환

---

### [Unit 35] 다중 소스 결합 통신망 긴급 점검 SOP 작성
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • HANDS-ON 3-1`
- **부제목(Subtitle):** KT 엑셀 분석 테이블, L3스위치 표준 매뉴얼, Teams 회의록을 결합한 통합 표준 작업 절차서 작성

#### 📝 슬라이드 본문 구조 및 핵심 내용
📄 Word Copilot 5대 기능 아키텍처 맵 다중 소스 초안 • 다시 쓰기 & 표 변환 • DALL-E 3 배너 • 모바일 음성 노트 Excalidraw Map ✍️ 1. 콘텐츠 초안 작성 • 소스 참조: `/files`, 메일, 회의록 • 섹션 추가: 특정 단락 보강 • 상세 프롬프트: 서식/어조 제어 🔄 2. 다시 쓰기 & 표 변환 • Rewrite: 문법/명확성 제안 • 실시간 편집: 대화형 튜닝 • 표 시각화: 텍스트 ➔ 표 변환 🎨 3. DALL-E 3 & 배너 • AI 이미지: 맞춤형 삽화 생성 • 헤더 배너: 챕터별 그래픽 • 브랜드 키트: 표준 색상 반영 📱 4. 분석 & 모바일 • 요약/Q&A: 차트/도면 질의 • 출처 인용: 근거 파일 제시 • 음성 노트: 보고서 자동 변환 📄 Word Multi-Source Synthesis Prompt "/files '5G_KPI_분석결과.xlsx'의 3번 시트 통계 테이블과, /files 'L3스위치_표준매뉴얼.docx', 그리고 지난 Teams 대책 회의록을 종합하여 '수도권 코어망 긴급 증설 및 장애 대응 표준 작업 절차서(SOP)'를 작성해줘. 목적, 장비 체크리스트, 단계별 명령어, 롤백 가이드를 포함한 정형화된 서식으로 완성해줘."

---

### [Unit 36] 5G 설비 투자 분석과 제안서(CAPEX) 작성
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • HANDS-ON 3-2`
- **부제목(Subtitle):** KT 5G 기지국 장비 증설 비용(CAPEX) 및 유지보수 절감 효과(OPEX) 정량 분석 제안서 완성

#### 📝 슬라이드 본문 구조 및 핵심 내용
📈 CAPEX / OPEX Investment Proposal "/files '2026_장비견적서.xlsx'의 데이터를 인용하여 노후 라우터 교체 시 향후 3년간 전력 소비량 및 유지보수 비용 절감액(OPEX -18%)을 강조한 경영진 제출용 설비투자 기안서를 작성해줘."

---

### [Unit 37] 5G SA 코어 네트워크 토폴로지 시각화
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word & Mermaid`
- **핵심 배지:** `WORD • HANDS-ON 3-3`
- **부제목(Subtitle):** KT 5G 단독모드(SA) gNodeB, AMF, UPF, SMF 간 데이터 흐름을 프롬프트만으로 다이어그램 렌더링

#### 📝 슬라이드 본문 구조 및 핵심 내용
📡 5G Standalone (SA) Core End-to-End Architecture 📱 5G 단말 (UE) User Equipment ➔ N1/N2 ➔ 📡 기지국 (gNodeB) Radio Access ➔ N3 (GTP-U) ➔ ⚡ UPF (데이터평면) User Plane 🛡️ 제어평면 (Control Plane): AMF (접속제어) ➔ SMF (세션관리 / N4) 🌐 외부연결: UPF ➔ N6 인터페이스 ➔ 데이터 네트워크 (DN) ✨ Topology Generation Prompt "KT 5G 단독모드(SA) 구조에서 gNodeB와 AMF, SMF, UPF 간의 제어 평면 및 사용자 평면 데이터 흐름을 Mermaid flowchart 문법으로 작성하고 각 인터페이스(N1, N2, N3, N4, N6) 라벨을 포함해줘."

---

### [Unit 38] 실무에 바로 쓰는 Word 마스터 프롬프트 모음
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Word`
- **핵심 배지:** `WORD • CHEAT SHEET`
- **부제목(Subtitle):** 백지일 때, 글이 어색할 때, 시간이 없을 때 즉시 복사하여 사용할 수 있는 프롬프트 모음

#### 📝 슬라이드 본문 구조 및 핵심 내용
상황 1. 백지일 때 "/files [파일이름]을 바탕으로 [주제]에 대한 초안 작성" 상황 2. 글이 어색할 때 "이 문단을 더 전문적이고 명확한 엔지니어링 비즈니스 어조로 재작성" 상황 3. 시간이 없을 때 "이 문서의 핵심 요약 및 담당자별 Action Items 5줄 생성"

---

### [Unit 39] PowerPoint 프레젠테이션 제작 4단계 여정
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • 4-STEP JOURNEY`
- **부제목(Subtitle):** KT 임원 보고 프레젠테이션 구축을 위한 브리프 ➔ 초안 ➔ 다듬기 ➔ 검토 4단계 프로세스

#### 📝 슬라이드 본문 구조 및 핵심 내용
Step 1 1. 브리프 (Brief) 보고 목적, 발표 청중, 분량 명확화 Step 2 2. 초안 (Draft) 24MB 이하 Word 연동 & 개요 생성 Step 3 3. 다듬기 (Refine) 전문가 톤, 문장 압축, DALL-E 3 Step 4 4. 검토 (Review) 4만단어 요약, Action Items 추출 ✨ "KT_2026_5G망_현대화_보고서.docx 를 기반으로 임원 의사결정용 4대 핵심 슬라이드를 생성해줘."

---

### [Unit 40] 브랜드 템플릿의 DNA와 자리 표시자 인식
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • BRAND DNA`
- **부제목(Subtitle):** 기업 전용 서식 파일의 자리 표시자 인식과 Copilot의 자동 레이아웃 최적화 원리

#### 📝 슬라이드 본문 구조 및 핵심 내용
1. Title & Subtitle 상단 제목과 부제목 자리 표시자 크기/위치 자동 상속 2. Content Cards 2단/3단 본문 카드 박스 영역에 텍스트 자동 분할 배치 3. Brand Colors KT Red(#E60000), Slate 등 사내 표준 팔레트 적용 📑 Brand Template Recognition "/files 'KT_Corporate_Brand_Template.potx' 사내 마스터 서식의 레이아웃 규칙과 자리 표시자를 엄격히 준수하여, 본문 내용을 3개 카드 영역에 균형 있게 배치해줘."

---

### [Unit 41] 에이전트 모드 기반 개요 및 슬라이드 빌드
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • AGENT MODE`
- **부제목(Subtitle):** 단 한 줄의 주제 설명으로 청중 분석, 목차 개요(Outline) 생성 후 전체 장표 자동 빌드

#### 📝 슬라이드 본문 구조 및 핵심 내용
🤖 Agent Mode Presentation Builder "KT 5G 코어망 가상화(vEPC ➔ 5GC) 마이그레이션 전략을 주제로 네트워크 운용팀 대상 15분 브리핑용 5장 슬라이드 개요(Outline)를 구성하고, 각 장표별 핵심 불릿 포인트 3개와 발표자 노트를 작성해줘." 🎯 청중 맞춤형 톤 조절 📑 5단계 스토리라인 구성 🎙️ 발표자 대본 자동 생성

---

### [Unit 42] Word 문서 기반 슬라이드 원클릭 변환 가이드
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • WORD COMPRESSION`
- **부제목(Subtitle):** 수십 페이지의 Word 기술 문서를 핵심 프레젠테이션으로 완벽 변환하는 베스트 프랙티스

#### 📝 슬라이드 본문 구조 및 핵심 내용
📁 연계 실습 데이터: practice_files/KT_2026_5G망_현대화_기술보고서.md 📑 Word Document to Slide Conversion "/files 'KT_2026_5G망_현대화_기술보고서.md' 문서를 바탕으로, 경영진 보고에 적합하도록 장황한 줄글을 제거하고 [추진 배경 - 핵심 기술 - 기대 효과 - 투자 계획] 4장 구조의 프레젠테이션으로 원클릭 변환해줘." ✓ 24MB 이하 Word 문서 파일 직접 링크 ✓ 원본 제목 스타일(H1, H2)에 따른 슬라이드 자동 분할

---

### [Unit 43] 슬라이드 텍스트 다시 쓰기 4대 핵심 전략
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • REWRITE STRATEGIES`
- **부제목(Subtitle):** 자동 다시 쓰기, 내용 압축(Condense), 비즈니스 톤 변경, 글머리 목록으로 시각화

#### 📝 슬라이드 본문 구조 및 핵심 내용
1. Condense 복잡한 줄글을 핵심 3줄 불릿으로 압축 2. Professional 구어체를 격식 있는 비즈니스 어조로 개선 3. Structure 키워드 강조 및 2열 비교 카드로 정돈 4. Action-Driven 다음 단계 행동(Next Step) 명시화 🔄 Slide Text Refinement "이 슬라이드의 텍스트를 60단어 이내로 압축하고, 핵심 키워드를 볼드체로 강조하며, 청중이 3초 안에 핵심 결론을 파악할 수 있도록 리라이팅해줘."

---

### [Unit 44] AI 슬라이드 이미지 생성의 법칙 (Bad vs Good)
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • IMAGE LAWS`
- **부제목(Subtitle):** 추상적 키워드의 실패 사례(Bad)와 구체적 피사체/조명/스타일 지시의 성공 사례(Good)

#### 📝 슬라이드 본문 구조 및 핵심 내용
BAD CASE ❌ 추상적이고 모호한 프롬프트 "멋진 미래지향적 5G 네트워크 기지국 이미지 만들어줘" • 결과물이 너무 비현실적이고 장난감 같은 그래픽 생성 • 텍스트 깨짐 및 불필요한 공상과학 요소 포함 비즈니스 보고서 부적합 GOOD CASE ✅ 구체적 피사체, 조명, 스타일 명시 "Isometric 3D 5G gNodeB telecom tower connecting to modern data center, enterprise blue lighting, clean white background" • 선명하고 전문적인 아이소메트릭 벡터 일러스트 완성 • 프레젠테이션 슬라이드 카드와 완벽한 조화 임원 보고서 최적화 품질

---

### [Unit 45] 대용량 문서 요약 및 핵심 슬라이드 선별
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • 40K WORDS SUMMARY`
- **부제목(Subtitle):** 최대 40,000단어의 초대형 프레젠테이션에서 핵심 슬라이드 식별 및 과업 자동 추출

#### 📝 슬라이드 본문 구조 및 핵심 내용
📚 Large Deck Selective Extraction "총 50장의 방대한 네트워크 장비 릴리즈 노트 슬라이드 중에서, 'BGP 및 OSPF 프로토콜 변경점'과 관련된 핵심 장표 3장만 찾아내어 변경 영향도를 3줄로 요약해줘." 최대 40,000단어 처리 키워드별 핵심 장표 추출 시간 절약 브리핑

---

### [Unit 46] 이동 중 전문가를 위한 모바일 음성 Q&A
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • MOBILE Q&A`
- **부제목(Subtitle):** iPhone/Android 스마트폰에서 이동 중 슬라이드 요약 확인 및 마이크 음성 질의

#### 📝 슬라이드 본문 구조 및 핵심 내용
🎙️ Mobile Slide Voice Query "모바일 PowerPoint 음성 질의: '이 슬라이드 덱에서 3분기 예산 초과 위험이 있는 국사가 어디인지 찾아내고, 슬라이드 번호와 함께 수치를 읽어줘.'" 📱 이동 중/외근 중 스마트폰 화면을 보지 않고도 음성으로 슬라이드 내용 확인 ⚡ 발표 직전 대기실에서 핵심 데이터 최종 확인 최적화

---

### [Unit 47] 임원 보고용 프레젠테이션 4대 슬라이드 생성
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `POWERPOINT • HANDS-ON 4-1`
- **부제목(Subtitle):** KT 통신망 현대화 보고서 Word 파일을 바탕으로 임원 의사결정용 4대 핵심 슬라이드 자동 생성

#### 📝 슬라이드 본문 구조 및 핵심 내용
📑 PowerPoint Copilot 기능 아키텍처 맵 에이전트 모드 • Word 문서 연동 • 액션 아이템 추출 • 40,000단어 요약 한도 Excalidraw Map 🚀 1. 에이전트 모드 • 스타일 설정: 청중/톤 맞춤 • 개요 생성: 목차 자동 제안 • 슬라이드 빌드: 시각적 생성 📄 2. Word 문서 연동 • 구조 인식: 제목 스타일 파싱 • 이미지 통합: 보고서 사진 유지 • 서식 파일: 24MB 이하 권장 📑 3. 분석 & 액션 아이템 • 핵심 요약: 글머리 기호 서머리 • 키 슬라이드: 중요 장표 식별 • Action Items: 과업 자동 추출 ⚖️ 4. 지침 및 규정 • 요약 한도: 최대 40,000단어 • 책임 있는 AI: RAI 원칙 준수 • 메타데이터: 출처 워터마크 📑 PowerPoint Executive Presentation Prompt "/files '2026_통신망_현대화_보고서.docx' 파일로부터 프레젠테이션을 생성해줘. 임원 보고에 적합하도록 장황한 글을 줄이고, 핵심 성과 지표(KPI)와 타임라인을 시각적 카드로 구성해줘."

---

### [Unit 48] 경영진 의사결정용 1페이지 ROI 서머리 디자인
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `POWERPOINT • HANDS-ON 4-2`
- **부제목(Subtitle):** KT 경영진이 5초 만에 핵심 투자 회수 기간과 품질 개선 지표를 파악하는 원페이지 대시보드 슬라이드

#### 📝 슬라이드 본문 구조 및 핵심 내용
📁 연계 실습 데이터: practice_files/KT_5G_설비투자_CAPEX_예산안_2026.csv 📊 CAPEX 절감 효과 -23.5% 고효율 국사 전환 ⏱️ 장애 조치 시간(MTTR) 45분 ➔ 8분 자율 관제 에이전트 도입 💰 ROI 투자 회수 1.4년 달성 목표 2.0년 대비 7개월 조기 회수 📈 1-Page Executive Summary "/files 'KT_5G_설비투자_CAPEX_예산안_2026.csv'를 바탕으로, 임원이 10초 만에 승인 결정을 내릴 수 있도록 총투자비, 연간 절감액, 회수 기간, 리스크 요약을 1페이지 임원 보고 슬라이드로 생성해줘."

---

### [Unit 49] PowerPoint 실전 치트키 마스터 가이드
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft PowerPoint`
- **핵심 배지:** `PPT • CHEAT SHEET`
- **부제목(Subtitle):** 시작(24MB 이하 Word 연동), 편집(전문가 톤/DALL-E 3), 검토(4만 단어 요약) 핵심 치트키

#### 📝 슬라이드 본문 구조 및 핵심 내용
1. 시작 치트키 "24MB 이하 Word 문서 연동 + 에이전트 모드 개요 빌드" 시작 2. 편집 치트키 "문장 압축(Condense) + 전문가 톤 + DALL-E 3 상세 피사체 묘사" 편집 3. 검토 치트키 "4만 단어 요약 + 핵심 슬라이드 3장 추출 + Action Items 정리" 검토

---

### [Unit 50] 크로스앱 통합 엔지니어링 워크플로우
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Cross-App Master Flow`
- **핵심 배지:** `MASTER PLAYBOOK • CROSS-APP`
- **부제목(Subtitle):** KT 엑셀 데이터 정제 ➔ 파이썬 시뮬레이션 ➔ 워드 SOP 작성 ➔ 파워포인트 임원 보고 원스톱 완성

#### 📝 슬라이드 본문 구조 및 핵심 내용
1 Excel Copilot 5G 대용량 로그 데이터 필터링 및 Z-Score 이상치 피벗 분석 완료 데이터 정제 & 추론 2 Word Copilot 엑셀 분석 테이블을 인용하여 정형화된 원인 분석 SOP 보고서 작성 다중 소스 보고서 합성 3 PowerPoint Copilot 완성된 Word 보고서로부터 1-Page 임원 의사결정 슬라이드 변환 의사결정 슬라이드 완성

---

### [Unit 51] 비상 장애 대응 지능형 협업 룸 (War-Room)
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Microsoft Teams`
- **핵심 배지:** `TEAMS • WAR-ROOM COLLAB`
- **부제목(Subtitle):** KT 전송망, 코어망, 무선망 엔지니어와 관제 센터가 실시간으로 공유하는 지능형 장애 복구 워룸

#### 📝 슬라이드 본문 구조 및 핵심 내용
🚨 Teams War-Room Incident Bot "현재 발생한 백본 라우터 다운 이슈와 관련해 '긴급_장애조치_워룸' 채널을 생성하고, 코어망팀과 전송망팀 담당자를 자동 초대하며, 지난 1시간 동안의 경보 로그 요약본을 채널 첫 공지로 게시해줘."

---

### [Unit 52] 통신 엔지니어를 위한 프롬프트 패턴 치트시트
- **소속 챕터:** 04. 데이터기반 의사결정, Copilot 에이전트 모드를 활용한 실전 플레이북
- **도구 / 영역:** `Copilot Engineer Guide`
- **핵심 배지:** `ENGINEER GUIDE • CHEAT SHEET`
- **부제목(Subtitle):** KT 기지국 관제, 백본 트래픽 분석, 장애 복구 SOP, 해외 TAC 메일 작성을 위한 10대 실무 치트시트

#### 📝 슬라이드 본문 구조 및 핵심 내용
📡 망 점검 & 장애 분석 패턴 "/files 'syslog.txt'에서 Severity 1~2 알람만 시간순으로 정렬하고 BGP Flapping 원인을 3줄 요약해줘" 📊 통계 & 시뮬레이션 패턴 "PRB 점유율 상위 10% 기지국의 주말 피크 트래픽 분산 효과를 파이썬 차트로 시각화해줘" 📝 기술 제안 & 기안서 패턴 "노후 스위치 교체 시 전력 절감량과 가용성 개선율을 강조한 경영진 제출용 1장 기안서 작성해줘" ✉️ 글로벌 벤더 TAC 패턴 "Cisco TAC 엔지니어에게 OSPF LSA 패킷 드롭 원인 조사를 요청하는 정중한 영문 메일 작성해줘"

---
