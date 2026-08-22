import os
import html

slides_data = [
    # Part 1. 2026 통신 AI 아키텍처 & 모델 토글링 (Slide 01~06)
    {
        "id": "slide-01",
        "badge": "2026 MASTER COURSE",
        "title": "네트워크·통신 엔지니어를 위한<br><span class='text-cyan-400'>Microsoft 365 Copilot</span> 실무 마스터",
        "subtitle": "단순 '작성 도우미'를 넘어 복잡한 인프라 맥락을 자율 수행하는 '능동적 에이전트'로의 진화",
        "type": "hero",
        "content": """
        <div class="grid grid-cols-2 gap-8 mt-6 text-left max-w-5xl mx-auto">
            <div class="p-6 bg-slate-800/80 rounded-2xl border border-slate-700/80 shadow-xl backdrop-blur-md">
                <div class="flex items-center space-x-3 mb-3">
                    <span class="px-3 py-1 bg-red-500/20 text-red-400 rounded-full text-xs font-bold uppercase">Legacy (2024~2025)</span>
                </div>
                <h4 class="text-xl font-bold text-white mb-2">단편적 텍스트 작성 도우미</h4>
                <p class="text-sm text-slate-300">사용자가 주는 단순 명령에만 의존하며, 사내 분산된 로그·이메일·문서 간의 맥락을 연결하지 못하는 '맥락맹(Context Blindness)' 한계</p>
            </div>
            <div class="p-6 bg-cyan-950/40 rounded-2xl border border-cyan-500/40 shadow-xl backdrop-blur-md">
                <div class="flex items-center space-x-3 mb-3">
                    <span class="px-3 py-1 bg-cyan-500/20 text-cyan-300 rounded-full text-xs font-bold uppercase">2026 Paradigm</span>
                </div>
                <h4 class="text-xl font-bold text-cyan-200 mb-2">Work IQ 기반 능동적 에이전트</h4>
                <p class="text-sm text-slate-300">사내 Graph 데이터와 결합하여 NOC 인시던트 분석부터 엔지니어 리소스 재배치까지 다단계 작업을 자율 수행</p>
            </div>
        </div>
        <div class="mt-8 flex justify-center items-center space-x-6 text-xs text-slate-400 font-mono">
            <span>📅 2026 Edition</span>
            <span>•</span>
            <span>🎯 통신망 & 네트워크 엔지니어 특화</span>
            <span>•</span>
            <span>⚡ 33개 마스터 슬라이드 덱</span>
        </div>
        """,
        "notes": "오프닝: 단순한 오피스 작성이 아닌 통신 네트워크 인프라 운영의 핵심 패러다임 전환과 2026 에이전틱 AI 아키텍처를 소개합니다."
    },
    {
        "id": "slide-02",
        "badge": "MODEL ARCHITECTURE",
        "title": "3대 차세대 AI 모델 전략적 선택 기준 <span class='text-cyan-400'>(Model Toggling)</span>",
        "subtitle": "통신 실무 난이도와 작업 기간에 따른 최적의 파운데이션 모델 수동 스위칭",
        "type": "standard",
        "content": """
        <div class="grid grid-cols-3 gap-6 text-left max-w-6xl mx-auto mt-4">
            <div class="p-6 bg-slate-800/80 rounded-2xl border border-blue-500/30 hover:border-blue-400 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex justify-between items-center mb-3">
                        <span class="text-xs px-2.5 py-1 bg-blue-500/20 text-blue-300 font-bold rounded-lg">논리 연산 / 심층 추론</span>
                        <span class="text-lg">🧠</span>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-2">GPT-5.6</h3>
                    <p class="text-xs text-slate-400 mb-4 font-mono">Multi-Step Deep Reasoning</p>
                    <div class="p-3 bg-slate-900/80 rounded-xl text-xs text-slate-300 border border-slate-700/50 mb-3">
                        <strong class="text-cyan-300">권장 시나리오:</strong><br>
                        • 5G SA Core 패킷 지연 원인 분석<br>
                        • 복합 라우팅 프로토콜 메트릭 계산<br>
                        • 대규모 침해사고 Root Cause Analysis (RCA)
                    </div>
                </div>
                <div class="text-[11px] text-blue-400 font-semibold mt-2">✓ 정밀도 99.8% 논리 검증</div>
            </div>

            <div class="p-6 bg-slate-800/80 rounded-2xl border border-emerald-500/30 hover:border-emerald-400 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex justify-between items-center mb-3">
                        <span class="text-xs px-2.5 py-1 bg-emerald-500/20 text-emerald-300 font-bold rounded-lg">초고속 에이전틱 실행</span>
                        <span class="text-lg">⚡</span>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-2">Claude Sonnet 5</h3>
                    <p class="text-xs text-slate-400 mb-4 font-mono">Fast Agentic Execution</p>
                    <div class="p-3 bg-slate-900/80 rounded-xl text-xs text-slate-300 border border-slate-700/50 mb-3">
                        <strong class="text-emerald-300">권장 시나리오:</strong><br>
                        • 실시간 워룸 회의 기반 장비 교체 플랜<br>
                        • 긴급 고객사 장애 안내문 및 메일 회신<br>
                        • 코드 생성 및 다이어그램 즉시 변환
                    </div>
                </div>
                <div class="text-[11px] text-emerald-400 font-semibold mt-2">✓ 실시간 인터랙션 최적화</div>
            </div>

            <div class="p-6 bg-slate-800/80 rounded-2xl border border-purple-500/30 hover:border-purple-400 transition-all flex flex-col justify-between">
                <div>
                    <div class="flex justify-between items-center mb-3">
                        <span class="text-xs px-2.5 py-1 bg-purple-500/20 text-purple-300 font-bold rounded-lg">지속성 / 장기 프로젝트</span>
                        <span class="text-lg">⏳</span>
                    </div>
                    <h3 class="text-2xl font-bold text-white mb-2">Claude Fable 5</h3>
                    <p class="text-xs text-slate-400 mb-4 font-mono">Long-term Persistence</p>
                    <div class="p-3 bg-slate-900/80 rounded-xl text-xs text-slate-300 border border-slate-700/50 mb-3">
                        <strong class="text-purple-300">권장 시나리오:</strong><br>
                        • 6G 인프라 마이그레이션 장기 프로젝트<br>
                        • 전국 국사 전수 조사 및 수개월 일정 검증<br>
                        • 분기별 망 품질 기술 백서 편찬
                    </div>
                </div>
                <div class="text-[11px] text-purple-400 font-semibold mt-2">✓ 수동 활성화 (Persistence 모드)</div>
            </div>
        </div>
        """,
        "notes": "통신 실무의 상황과 긴급도에 따라 GPT-5.6(심층분석), Sonnet 5(빠른실행), Fable 5(장기프로젝트)를 모델 토글링하여 활용하는 아키텍처 원리를 설명합니다."
    },
    {
        "id": "slide-03",
        "badge": "CLOUD SYNERGY",
        "title": "엔지니어를 위한 <span class='text-cyan-400'>5대 클라우드 시너지</span> & Copilot Cowork",
        "subtitle": "데이터 사일로를 파괴하고 앱 간 경계를 허무는 통합 엔지니어링 에코시스템",
        "type": "standard",
        "content": """
        <div class="grid grid-cols-5 gap-3 text-left max-w-6xl mx-auto mt-2">
            <div class="p-4 bg-slate-800/90 rounded-xl border border-slate-700">
                <div class="text-cyan-400 text-xl font-bold mb-1">01</div>
                <h5 class="text-sm font-bold text-white mb-1">클라우드 컨텍스트</h5>
                <p class="text-xs text-slate-400">OneDrive/SharePoint 연동 데이터를 읽고 10만 행 ACL 수식 10초 디버깅</p>
            </div>
            <div class="p-4 bg-slate-800/90 rounded-xl border border-slate-700">
                <div class="text-cyan-400 text-xl font-bold mb-1">02</div>
                <h5 class="text-sm font-bold text-white mb-1">타임머신 버전 Diff</h5>
                <p class="text-xs text-slate-400">지난주 설정 파일과 비교해 변경된 라우팅/수식값 자동 역추적</p>
            </div>
            <div class="p-4 bg-slate-800/90 rounded-xl border border-slate-700">
                <div class="text-cyan-400 text-xl font-bold mb-1">03</div>
                <h5 class="text-sm font-bold text-white mb-1">앱 간 사일로 파괴</h5>
                <p class="text-xs text-slate-400">Excel 로그 + Teams 채팅 + Outlook 메일을 결합한 단일 뷰 보고서</p>
            </div>
            <div class="p-4 bg-slate-800/90 rounded-xl border border-slate-700">
                <div class="text-cyan-400 text-xl font-bold mb-1">04</div>
                <h5 class="text-sm font-bold text-white mb-1">제로 트러스트 상속</h5>
                <p class="text-xs text-slate-400">Entra ID ACL 기반으로 로그인 계정에 인가된 데이터만 안전 검색</p>
            </div>
            <div class="p-4 bg-slate-800/90 rounded-xl border border-slate-700">
                <div class="text-cyan-400 text-xl font-bold mb-1">05</div>
                <h5 class="text-sm font-bold text-white mb-1">샌드박스 연산</h5>
                <p class="text-xs text-slate-400">로컬 패키지 충돌 없이 Azure Cloud 격리 샌드박스에서 Python 실행</p>
            </div>
        </div>

        <div class="mt-6 p-5 bg-gradient-to-r from-cyan-950/60 to-indigo-950/60 rounded-2xl border border-cyan-500/40 text-left max-w-6xl mx-auto flex items-center justify-between">
            <div>
                <div class="flex items-center space-x-2">
                    <span class="px-2.5 py-0.5 bg-cyan-500/20 text-cyan-300 text-xs font-bold rounded">2026 NEW</span>
                    <h4 class="text-lg font-bold text-white">Copilot Cowork & Cowork Skills</h4>
                </div>
                <p class="text-xs text-slate-300 mt-1">목표(Task)를 정의하면 여러 에이전트가 단일 흐름으로 앱을 넘나들며 최종 완성본을 도출하고, 검증된 장애 대응 루틴을 '스킬'로 저장하여 전사 공유합니다.</p>
            </div>
            <div class="text-3xl pl-6">🤝</div>
        </div>
        """,
        "notes": "클라우드 5대 시너지와 차세대 Copilot Cowork의 팀 단위 스킬 공유 개념을 설명합니다."
    },
    {
        "id": "slide-04",
        "badge": "GRAPH & EDP",
        "title": "M365 Copilot 기술 아키텍처 & <span class='text-cyan-400'>엔터프라이즈 데이터 보호(EDP)</span>",
        "subtitle": "사내 보안 경계를 한 치도 벗어나지 않는 안전한 그라운딩(Grounding) 파이프라인",
        "type": "standard",
        "content": """
        <div class="p-5 bg-slate-900/90 rounded-2xl border border-slate-700 max-w-5xl mx-auto mb-6 text-left">
            <div class="flex items-center justify-between text-xs text-slate-300 font-mono mb-2">
                <div class="p-3 bg-slate-800 rounded-lg border border-slate-700 text-center w-40">
                    <div class="text-cyan-400 font-bold">1. User Prompt</div>
                    <div class="text-[10px] text-slate-400 mt-1">엔지니어 자연어 질의</div>
                </div>
                <div class="text-cyan-400 font-bold">➔</div>
                <div class="p-3 bg-indigo-950/80 rounded-lg border border-indigo-500/40 text-center w-52">
                    <div class="text-indigo-300 font-bold">2. Microsoft Graph</div>
                    <div class="text-[10px] text-slate-400 mt-1">Work IQ + Entra ID ACL 인덱싱</div>
                </div>
                <div class="text-cyan-400 font-bold">➔</div>
                <div class="p-3 bg-blue-950/80 rounded-lg border border-blue-500/40 text-center w-40">
                    <div class="text-blue-300 font-bold">3. LLM Orchestrator</div>
                    <div class="text-[10px] text-slate-400 mt-1">GPT-5.6 / Sonnet 5</div>
                </div>
                <div class="text-cyan-400 font-bold">➔</div>
                <div class="p-3 bg-emerald-950/80 rounded-lg border border-emerald-500/40 text-center w-44">
                    <div class="text-emerald-300 font-bold">4. Response & App</div>
                    <div class="text-[10px] text-slate-400 mt-1">Purview DLP 필터링 후 렌더링</div>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-6 text-left max-w-5xl mx-auto">
            <div class="p-4 bg-slate-800/70 rounded-xl border border-slate-700">
                <div class="text-cyan-400 font-bold text-sm mb-1">🔒 테넌트 완벽 격리</div>
                <p class="text-xs text-slate-300">고객 데이터는 암호화된 전용 테넌트 내에 격리되며 타 테넌트와 절대 혼합되지 않습니다.</p>
            </div>
            <div class="p-4 bg-slate-800/70 rounded-xl border border-slate-700">
                <div class="text-cyan-400 font-bold text-sm mb-1">🛡️ Zero-Data Retention</div>
                <p class="text-xs text-slate-300">기업 프롬프트와 응답 내용은 공용 LLM 기초 모델의 추가 학습에 영구히 배제됩니다.</p>
            </div>
            <div class="p-4 bg-slate-800/70 rounded-xl border border-slate-700">
                <div class="text-cyan-400 font-bold text-sm mb-1">🔑 권한 자동 상속</div>
                <p class="text-xs text-slate-300">사용자가 평소 접근 권한을 가진 사내 파일과 이메일만 그라운딩 소스로 활용됩니다.</p>
            </div>
        </div>
        """,
        "notes": "Microsoft Graph의 실시간 인덱싱과 테넌트 경계 내 보안 파이프라인(EDP)을 설명합니다."
    },
    {
        "id": "slide-05",
        "badge": "PROMPT FRAMEWORK",
        "title": "[MS Learn 공식] 통신 엔지니어링 프롬프트 4대 요소 <span class='text-cyan-400'>(GCS-E)</span>",
        "subtitle": "환각을 제거하고 1회 요청으로 즉시 현업에 투입 가능한 고품질 산출물 도출",
        "type": "standard",
        "content": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-2">
            <div class="p-5 bg-slate-800/90 rounded-2xl border border-blue-500/40">
                <div class="flex items-center space-x-2 mb-2">
                    <span class="w-6 h-6 rounded-full bg-blue-500/20 text-blue-300 flex items-center justify-center font-bold text-xs">1</span>
                    <h4 class="text-base font-bold text-white">Goal (목표 명시)</h4>
                </div>
                <p class="text-xs text-slate-300 mb-2">Copilot이 완수해야 하는 궁극적인 엔지니어링 과업을 구체적인 동사로 정의</p>
                <div class="p-2.5 bg-slate-900 rounded-lg text-xs font-mono text-cyan-300 border border-slate-700">
                    "5G SA Core의 GTP-U 패킷 지연 원인을 규명하고 기술적 완화 조치안을 도출해줘."
                </div>
            </div>

            <div class="p-5 bg-slate-800/90 rounded-2xl border border-emerald-500/40">
                <div class="flex items-center space-x-2 mb-2">
                    <span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-300 flex items-center justify-center font-bold text-xs">2</span>
                    <h4 class="text-base font-bold text-white">Context (배경 및 청중)</h4>
                </div>
                <p class="text-xs text-slate-300 mb-2">왜 이 작업이 필요한지, 최종 보고 대상자가 누구인지 맥락을 제공</p>
                <div class="p-2.5 bg-slate-900 rounded-lg text-xs font-mono text-emerald-300 border border-slate-700">
                    "NOC 레벨-1 긴급 인시던트 발생 상황이며, 최종 보고 대상은 기술본부장 및 벤더사 TAC 엔지니어임."
                </div>
            </div>

            <div class="p-5 bg-slate-800/90 rounded-2xl border border-purple-500/40">
                <div class="flex items-center space-x-2 mb-2">
                    <span class="w-6 h-6 rounded-full bg-purple-500/20 text-purple-300 flex items-center justify-center font-bold text-xs">3</span>
                    <h4 class="text-base font-bold text-white">Source (참조 출처 지정)</h4>
                </div>
                <p class="text-xs text-slate-300 mb-2">정확한 사내 파일, 메일 스레드, 규정집을 슬래시(/)로 지정</p>
                <div class="p-2.5 bg-slate-900 rounded-lg text-xs font-mono text-purple-300 border border-slate-700">
                    "/[5G_Core_Syslog.csv]와 /[Ericsson_Core_Guide.pdf]의 기술 규격을 상호 대조해."
                </div>
            </div>

            <div class="p-5 bg-slate-800/90 rounded-2xl border border-amber-500/40">
                <div class="flex items-center space-x-2 mb-2">
                    <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center font-bold text-xs">4</span>
                    <h4 class="text-base font-bold text-white">Expectations (형식 & 제약조건)</h4>
                </div>
                <p class="text-xs text-slate-300 mb-2">출력 스타일, 테이블 서식, 분량, 약어 풀이 규칙을 명시</p>
                <div class="p-2.5 bg-slate-900 rounded-lg text-xs font-mono text-amber-300 border border-slate-700">
                    "최상단에 [Review Summary]를 추가하고, DU/RU/BBU 약어는 국제 표준으로 풀어서 표로 작성해."
                </div>
            </div>
        </div>
        """,
        "notes": "MS Learn 공식 4대 프롬프트 구성 요소인 GCS-E (Goal, Context, Source, Expectations)를 통신 네트워크 실무 예시와 함께 제시합니다."
    },
    {
        "id": "slide-06",
        "badge": "SECURITY DEEP DIVE",
        "title": "[보안 딥다이브] Work vs Web 모드 & <span class='text-cyan-400'>쿼리 변환(Query Transformation)</span>",
        "subtitle": "사내 망 기밀 데이터 유출을 원천 차단하면서 글로벌 최신 표준을 조회하는 원리",
        "type": "standard",
        "content": """
        <div class="grid grid-cols-2 gap-6 text-left max-w-5xl mx-auto mt-2">
            <div class="p-5 bg-slate-800/90 rounded-2xl border border-cyan-500/40">
                <div class="flex items-center justify-between mb-3">
                    <h4 class="text-base font-bold text-cyan-300">🏢 Work 모드 (사내 전용)</h4>
                    <span class="text-xs px-2 py-0.5 bg-cyan-500/20 text-cyan-400 rounded">Internal Only</span>
                </div>
                <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                    <li>사내 SharePoint, Teams, Outlook, 국사 자산 데이터 전용 검색</li>
                    <li>외부 웹 검색 완전 차단으로 완벽한 제로 트러스트 기밀 보장</li>
                    <li><strong>주요 용도:</strong> 사내 장애 일지, IP 할당표, 표준 운영 절차서(SOP)</li>
                </ul>
            </div>

            <div class="p-5 bg-slate-800/90 rounded-2xl border border-indigo-500/40">
                <div class="flex items-center justify-between mb-3">
                    <h4 class="text-base font-bold text-indigo-300">🌐 Web 모드 (외부 실시간)</h4>
                    <span class="text-xs px-2 py-0.5 bg-indigo-500/20 text-indigo-400 rounded">Bing Grounding</span>
                </div>
                <ul class="text-xs text-slate-300 space-y-2 list-disc list-inside">
                    <li>최신 3GPP 릴리즈, IETF RFC 표준, 글로벌 벤더 공식 매뉴얼 검색</li>
                    <li>상용 LLM과 달리 2026년 최신 보안 취약점(CVE) 실시간 반영</li>
                    <li><strong>주요 용도:</strong> 신규 펌웨어 패그, 글로벌 RFC 표준 스펙 대조</li>
                </ul>
            </div>
        </div>

        <div class="mt-6 p-4 bg-slate-900/90 rounded-xl border border-slate-700 text-left max-w-5xl mx-auto">
            <div class="text-xs font-bold text-amber-300 mb-1">🛡️ 쿼리 변환(Query Transformation) 보안 메커니즘</div>
            <p class="text-xs text-slate-400">
                사내 호스트명(예: <code class="text-cyan-300">KR-SEL-DC1-RTR01</code>)이 포함된 질문이 외부 검색 엔진으로 전송될 때, Copilot은 내부 식별자를 제거하고 <code class="text-cyan-300">"Cisco ASR 9000 BGP EVPN flap issue"</code>와 같이 일반화된 기술 쿼리로 자동 변환하여 외부로 전송합니다.
            </p>
        </div>
        """,
        "notes": "Work 모드와 Web 모드의 전환 기준과 내부 정보 유출을 차단하는 쿼리 변환 메커니즘을 상세히 설명합니다."
    }
]

print(f"Loaded {len(slides_data)} slides in preview list.")
