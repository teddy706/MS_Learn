import os
import sys

# Warm Editorial Tech Theme
# Background: Warm Cream / Off-white (#faf8f5 -> #f3ede2)
# Text: Deep Espresso Charcoal (#1c1917, #292524, #44403c)
# Accent: Burnt Orange (#ea580c, #c2410c), Warm Amber (#d97706), Deep Oxford Navy (#1e3a8a, #0f172a)

html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>2026 M365 Copilot 통신·네트워크 엔지니어링 실무 마스터</title>
    <!-- Reveal.js CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/beige.css" id="theme">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/atom-one-dark.css">
    <!-- Tailwind CSS Play CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        warmbg: '#faf8f5',
                        warmcard: '#ffffff',
                        warmborder: '#e7dfd5',
                        espresso: '#1c1917',
                        charcoal: '#292524',
                        muted: '#78716c',
                        burnt: '#ea580c',
                        burntDark: '#c2410c',
                        oxford: '#1e3a8a',
                        terracotta: '#9a3412',
                    }
                }
            }
        }
    </script>
    <!-- Mermaid.js for architectural diagrams -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({ startOnLoad: true, theme: 'neutral' });
    </script>
    <style>
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
        @import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..700&family=JetBrains+Mono:wght@400;600&display=swap');
        
        * {
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        }
        
        .serif-font {
            font-family: 'Newsreader', 'Pretendard', serif !important;
        }

        .mono-font {
            font-family: 'JetBrains Mono', monospace !important;
        }

        .reveal {
            background: linear-gradient(145deg, #fbf9f6 0%, #f4ede2 50%, #ede3d2 100%) !important;
            color: #292524 !important;
        }

        .reveal h1, .reveal h2, .reveal h3, .reveal h4 {
            color: #1c1917 !important;
            letter-spacing: -0.025em;
            text-transform: none !important;
            font-weight: 800;
        }

        .reveal pre {
            box-shadow: none !important;
        }

        .editorial-card {
            background: #ffffff;
            border: 1px solid #e7dfd5;
            box-shadow: 0 4px 20px -2px rgba(41, 37, 36, 0.05), 0 2px 6px -1px rgba(41, 37, 36, 0.03);
            border-radius: 16px;
        }

        .editorial-accent-card {
            background: linear-gradient(135deg, #fffaf5 0%, #fff1e6 100%);
            border: 1px solid #fed7aa;
            box-shadow: 0 4px 20px -2px rgba(234, 88, 12, 0.08);
            border-radius: 16px;
        }

        .editorial-dark-card {
            background: #1c1917;
            color: #fafaf9;
            border: 1px solid #292524;
            border-radius: 16px;
        }

        .slide-badge {
            display: inline-block;
            padding: 4px 12px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            border-radius: 9999px;
            background: #ffedd5;
            color: #c2410c;
            border: 1px solid #fdba74;
            margin-bottom: 12px;
        }

        .nav-guide {
            position: fixed;
            bottom: 16px;
            left: 20px;
            font-size: 11px;
            color: #78716c;
            z-index: 100;
            pointer-events: none;
            font-weight: 500;
        }

        .code-box {
            background: #1c1917;
            color: #fdba74;
            border: 1px solid #292524;
            border-radius: 10px;
            font-family: 'JetBrains Mono', monospace;
        }
    </style>
</head>
<body>
    <div class="nav-guide">
        <span>📖 [Space / 방향키] 슬라이드 이동 &nbsp;|&nbsp; [S] 발표자 노트 &nbsp;|&nbsp; [ESC] 전체 개요 &nbsp;|&nbsp; [F] 전체화면</span>
    </div>
    <div class="reveal">
        <div class="slides">
"""

html_end = """
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script>
        Reveal.initialize({
            hash: true,
            slideNumber: 'c/t',
            transition: 'fade',
            transitionSpeed: 'fast',
            width: 1280,
            height: 720,
            margin: 0.04,
            minScale: 0.2,
            maxScale: 2.0,
            plugins: [ RevealNotes, RevealHighlight ]
        });
        Reveal.on('slidechanged', event => {
            mermaid.run();
        });
    </script>
</body>
</html>
"""

slides = [
    # Slide 01
    {
        "badge": "2026 MASTER CLASS",
        "title": "통신·네트워크 엔지니어를 위한<br><span class='text-burnt'>Microsoft 365 Copilot</span> 실무 마스터",
        "subtitle": "단순 '작성 도우미'를 넘어 복잡한 인프라 맥락을 자율 수행하는 '능동적 에이전트'로의 진화",
        "body": """
        <div class="grid grid-cols-2 gap-8 mt-6 text-left max-w-5xl mx-auto">
            <div class="p-6 editorial-card">
                <div class="flex items-center space-x-2 mb-3">
                    <span class="px-2.5 py-0.5 bg-stone-100 text-stone-600 rounded-full text-xs font-bold uppercase border border-stone-200">Legacy (2024~2025)</span>
                </div>
                <h4 class="text-xl font-bold text-espresso mb-2">단편적 텍스트 작성 보조</h4>
                <p class="text-sm text-stone-600 leading-relaxed">사용자의 단발성 질문에만 의존하며, 사내 로그·메일·규정집 간의 맥락을 연결하지 못하는 '맥락맹(Context Blindness)' 한계</p>
            </div>
            <div class="p-6 editorial-accent-card">
                <div class="flex items-center space-x-2 mb-3">
                    <span class="px-2.5 py-0.5 bg-orange-100 text-burntDark rounded-full text-xs font-bold uppercase border border-orange-200">2026 Paradigm</span>
                </div>
                <h4 class="text-xl font-bold text-burntDark mb-2">Work IQ 기반 능동적 에이전트</h4>
                <p class="text-sm text-stone-700 leading-relaxed">사내 Graph 데이터와 결합하여 NOC 인시던트 분석부터 엔지니어 리소스 재배치까지 다단계 엔지니어링 과업을 자율 수행</p>
            </div>
        </div>
        <div class="mt-8 flex justify-center items-center space-x-6 text-xs text-stone-500 font-mono">
            <span>📅 2026 Edition</span>
            <span>•</span>
            <span>🎯 통신망 & 네트워크 엔지니어 특화</span>
            <span>•</span>
            <span>⚡ 33개 마스터 슬라이드 덱</span>
        </div>
        """,
        "notes": "오프닝: 단순 오피스 도구를 넘어 네트워크 인프라 운영의 핵심 맥락을 잇는 2026 에이전틱 AI 아키텍처를 소개합니다."
    },
    # Slide 02
    {
        "badge": "MODEL ARCHITECTURE",
        "title": "3대 차세대 AI 모델 전략적 선택 기준 <span class='text-burnt'>(Model Toggling)</span>",
        "subtitle": "통신 실무 난이도와 작업 기간에 따른 최적의 파운데이션 모델 수동 스위칭",
        "body": """
        <div class="grid grid-cols-3 gap-5 text-left max-w-6xl mx-auto mt-2">
            <div class="p-5 editorial-card flex flex-col justify-between border-t-4 border-t-blue-600">
                <div>
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs px-2.5 py-0.5 bg-blue-50 text-blue-800 font-bold rounded border border-blue-200">심층 추론 / 수치 연산</span>
                        <span class="text-xl">🧠</span>
                    </div>
                    <h3 class="text-2xl font-bold text-espresso mb-1">GPT-5.6</h3>
                    <p class="text-[11px] text-stone-500 mb-3 font-mono">Multi-Step Deep Reasoning</p>
                    <div class="p-3 bg-stone-50 rounded-xl text-xs text-stone-700 border border-stone-200 mb-2 leading-relaxed">
                        <strong class="text-blue-900">실무 권장 시나리오:</strong><br>
                        • 5G SA Core 패킷 지연 원인 분석<br>
                        • 복합 라우팅 메트릭 계산<br>
                        • 대규모 침해사고 Root Cause Analysis
                    </div>
                </div>
                <div class="text-[11px] text-blue-700 font-semibold mt-1">✓ 다단계 수치 연산 무결성</div>
            </div>

            <div class="p-5 editorial-card flex flex-col justify-between border-t-4 border-t-emerald-600">
                <div>
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs px-2.5 py-0.5 bg-emerald-50 text-emerald-800 font-bold rounded border border-emerald-200">초고속 에이전틱 실행</span>
                        <span class="text-xl">⚡</span>
                    </div>
                    <h3 class="text-2xl font-bold text-espresso mb-1">Claude Sonnet 5</h3>
                    <p class="text-[11px] text-stone-500 mb-3 font-mono">Fast Agentic Execution</p>
                    <div class="p-3 bg-stone-50 rounded-xl text-xs text-stone-700 border border-stone-200 mb-2 leading-relaxed">
                        <strong class="text-emerald-900">실무 권장 시나리오:</strong><br>
                        • 실시간 회의 기반 장비 교체 플랜<br>
                        • 긴급 고객사 장애 안내문 및 메일 회신<br>
                        • 코드 생성 및 다이어그램 즉시 변환
                    </div>
                </div>
                <div class="text-[11px] text-emerald-700 font-semibold mt-1">✓ 초고속 인터랙션 최적화</div>
            </div>

            <div class="p-5 editorial-card flex flex-col justify-between border-t-4 border-t-purple-600">
                <div>
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs px-2.5 py-0.5 bg-purple-50 text-purple-800 font-bold rounded border border-purple-200">지속성 / 장기 프로젝트</span>
                        <span class="text-xl">⏳</span>
                    </div>
                    <h3 class="text-2xl font-bold text-espresso mb-1">Claude Fable 5</h3>
                    <p class="text-[11px] text-stone-500 mb-3 font-mono">Long-term Persistence</p>
                    <div class="p-3 bg-stone-50 rounded-xl text-xs text-stone-700 border border-stone-200 mb-2 leading-relaxed">
                        <strong class="text-purple-900">실무 권장 시나리오:</strong><br>
                        • 6G 인프라 마이그레이션 프로젝트<br>
                        • 전국 국사 전수 조사 및 수개월 일정 검증<br>
                        • 분기별 망 품질 기술 백서 편찬
                    </div>
                </div>
                <div class="text-[11px] text-purple-700 font-semibold mt-1">✓ 수동 활성화 (Persistence 모드)</div>
            </div>
        </div>
        """,
        "notes": "통신 실무 상황에 따라 3대 AI 모델을 전략적으로 토글링(스위칭)하여 사용하는 최신 아키텍처 기준을 설명합니다."
    },
    # Slide 03
    {
        "badge": "CLOUD SYNERGY",
        "title": "엔지니어를 위한 <span class='text-burnt'>5대 클라우드 시너지</span> & Copilot Cowork",
        "subtitle": "데이터 사일로를 파괴하고 앱 간 경계를 허무는 통합 엔지니어링 에코시스템",
        "body": """
        <div class="grid grid-cols-5 gap-3 text-left max-w-6xl mx-auto mt-2">
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-base mb-1 font-mono">01</div>
                <h5 class="text-xs font-bold text-espresso mb-1">클라우드 컨텍스트</h5>
                <p class="text-[11px] text-stone-600 leading-tight">OneDrive 연동 데이터로 10만 행 수식 오류 10초 디버깅</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-base mb-1 font-mono">02</div>
                <h5 class="text-xs font-bold text-espresso mb-1">타임머신 버전 Diff</h5>
                <p class="text-[11px] text-stone-600 leading-tight">지난주 설정값과 현재 버전의 라우팅 차이점 자동 역추적</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-base mb-1 font-mono">03</div>
                <h5 class="text-xs font-bold text-espresso mb-1">앱 사일로 파괴</h5>
                <p class="text-[11px] text-stone-600 leading-tight">Excel 로그 + Teams 채팅 + Outlook 메일 결합 보고서</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-base mb-1 font-mono">04</div>
                <h5 class="text-xs font-bold text-espresso mb-1">제로트러스트 상속</h5>
                <p class="text-[11px] text-stone-600 leading-tight">Entra ID ACL 기반 인가된 사내 통신 데이터만 안전 검색</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-base mb-1 font-mono">05</div>
                <h5 class="text-xs font-bold text-espresso mb-1">샌드박스 연산</h5>
                <p class="text-[11px] text-stone-600 leading-tight">로컬 패키지 충돌 없는 Azure Cloud 격리 샌드박스 연산</p>
            </div>
        </div>

        <div class="mt-5 p-4 editorial-accent-card text-left max-w-6xl mx-auto flex items-center justify-between">
            <div>
                <div class="flex items-center space-x-2">
                    <span class="px-2 py-0.5 bg-orange-100 text-burntDark text-[10px] font-bold rounded border border-orange-200">2026 NEW</span>
                    <h4 class="text-base font-bold text-espresso">Copilot Cowork & Cowork Skills</h4>
                </div>
                <p class="text-xs text-stone-700 mt-1">사용자가 목표(Task)를 정의하면 여러 에이전트가 단일 흐름 안에서 앱을 넘나들며 최종 완성본을 도출하고, 성공한 장애대응 루틴을 <strong>'코워크 스킬'</strong>로 패키징하여 전사 공유합니다.</p>
            </div>
            <div class="text-3xl pl-4">🤝</div>
        </div>
        """,
        "notes": "클라우드 5대 시너지와 차세대 Copilot Cowork의 전사 스킬 공유 개념을 소개합니다."
    },
    # Slide 04
    {
        "badge": "GRAPH & EDP",
        "title": "M365 Copilot 기술 아키텍처 & <span class='text-burnt'>엔터프라이즈 데이터 보호(EDP)</span>",
        "subtitle": "사내 보안 경계를 한 치도 벗어나지 않는 안전한 그라운딩(Grounding) 파이프라인",
        "body": """
        <div class="p-4 editorial-card max-w-5xl mx-auto mb-4 text-left">
            <div class="flex items-center justify-between text-xs text-stone-700 font-mono">
                <div class="p-2.5 bg-stone-100 rounded text-center w-36 border border-stone-200">
                    <div class="text-burntDark font-bold">1. User Prompt</div>
                    <div class="text-[9px] text-stone-500 mt-0.5">엔지니어 자연어 질의</div>
                </div>
                <div class="text-burnt font-bold">➔</div>
                <div class="p-2.5 bg-orange-50 rounded text-center w-48 border border-orange-200">
                    <div class="text-burntDark font-bold">2. Microsoft Graph</div>
                    <div class="text-[9px] text-stone-600 mt-0.5">Work IQ + Entra ID ACL 인덱싱</div>
                </div>
                <div class="text-burnt font-bold">➔</div>
                <div class="p-2.5 bg-blue-50 rounded text-center w-36 border border-blue-200">
                    <div class="text-blue-900 font-bold">3. LLM Engine</div>
                    <div class="text-[9px] text-stone-600 mt-0.5">GPT-5.6 / Sonnet 5</div>
                </div>
                <div class="text-burnt font-bold">➔</div>
                <div class="p-2.5 bg-emerald-50 rounded text-center w-40 border border-emerald-200">
                    <div class="text-emerald-900 font-bold">4. Response & App</div>
                    <div class="text-[9px] text-stone-600 mt-0.5">Purview DLP 필터링 렌더링</div>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-4 text-left max-w-5xl mx-auto">
            <div class="p-4 editorial-card">
                <div class="text-burntDark font-bold text-xs mb-1">🔒 테넌트 완벽 격리</div>
                <p class="text-[11px] text-stone-600 leading-relaxed">고객 데이터는 암호화된 전용 테넌트 내에 격리되며 타 테넌트와 절대 혼합되지 않습니다.</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burntDark font-bold text-xs mb-1">🛡️ Zero-Data Retention</div>
                <p class="text-[11px] text-stone-600 leading-relaxed">기업 프롬프트와 응답 내용은 공용 LLM 기초 모델의 추가 학습에 영구히 배제됩니다.</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burntDark font-bold text-xs mb-1">🔑 권한 자동 상속</div>
                <p class="text-[11px] text-stone-600 leading-relaxed">사용자가 평소 접근 권한을 가진 사내 파일과 이메일만 그라운딩 소스로 활용됩니다.</p>
            </div>
        </div>
        """,
        "notes": "Microsoft Graph 인덱싱과 엔터프라이즈 데이터 보호(EDP)의 핵심 3대 보안 원칙을 설명합니다."
    },
    # Slide 05
    {
        "badge": "PROMPT FRAMEWORK",
        "title": "[MS Learn 공식] 통신 엔지니어링 프롬프트 4대 요소 <span class='text-burnt'>(GCS-E)</span>",
        "subtitle": "환각을 제거하고 1회 요청으로 즉시 현업에 투입 가능한 고품질 산출물 도출",
        "body": """
        <div class="grid grid-cols-2 gap-4 text-left max-w-5xl mx-auto mt-2">
            <div class="p-4 editorial-card">
                <div class="flex items-center space-x-2 mb-1">
                    <span class="w-5 h-5 rounded-full bg-orange-100 text-burntDark flex items-center justify-center font-bold text-xs">1</span>
                    <h4 class="text-sm font-bold text-espresso">Goal (목표 명시)</h4>
                </div>
                <p class="text-[11px] text-stone-600 mb-1">수행해야 할 구체적인 엔지니어링 과업 정의</p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-orange-200 border border-stone-800">
                    "5G SA Core의 GTP-U 패킷 지연 원인을 규명하고 조치안을 도출해줘."
                </div>
            </div>

            <div class="p-4 editorial-card">
                <div class="flex items-center space-x-2 mb-1">
                    <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-xs">2</span>
                    <h4 class="text-sm font-bold text-espresso">Context (배경 및 청중)</h4>
                </div>
                <p class="text-[11px] text-stone-600 mb-1">작업이 필요한 이유와 최종 보고 대상</p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-emerald-200 border border-stone-800">
                    "NOC 레벨-1 긴급 인시던트 발생 상황이며, 보고 대상은 기술본부장임."
                </div>
            </div>

            <div class="p-4 editorial-card">
                <div class="flex items-center space-x-2 mb-1">
                    <span class="w-5 h-5 rounded-full bg-purple-100 text-purple-800 flex items-center justify-center font-bold text-xs">3</span>
                    <h4 class="text-sm font-bold text-espresso">Source (참조 출처 지정)</h4>
                </div>
                <p class="text-[11px] text-stone-600 mb-1">참조할 사내 파일/스레드 슬래시(/) 지정</p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-purple-200 border border-stone-800">
                    "/[5G_Core_Syslog.csv]와 /[Ericsson_Core_Guide.pdf]를 대조해."
                </div>
            </div>

            <div class="p-4 editorial-card">
                <div class="flex items-center space-x-2 mb-1">
                    <span class="w-5 h-5 rounded-full bg-blue-100 text-blue-800 flex items-center justify-center font-bold text-xs">4</span>
                    <h4 class="text-sm font-bold text-espresso">Expectations (형식 & 제약)</h4>
                </div>
                <p class="text-[11px] text-stone-600 mb-1">출력 형식, 약어 풀이, 필수 섹션 명시</p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-blue-200 border border-stone-800">
                    "최상단에 [Review Summary]를 두고, DU/RU 약어는 풀어서 표로 작성해."
                </div>
            </div>
        </div>
        """,
        "notes": "MS Learn의 4대 프롬프트 프레임워크(GCS-E)를 통신 네트워크 실무 사례로 설명합니다."
    },
    # Slide 06
    {
        "badge": "SECURITY DEEP DIVE",
        "title": "[보안 딥다이브] Work vs Web 모드 & <span class='text-burnt'>쿼리 변환(Query Transformation)</span>",
        "subtitle": "사내 망 기밀 데이터 유출을 원천 차단하면서 글로벌 최신 표준을 조회하는 원리",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-2">
            <div class="p-4 editorial-card border-t-4 border-t-burnt">
                <div class="flex items-center justify-between mb-2">
                    <h4 class="text-sm font-bold text-burntDark">🏢 Work 모드 (사내 전용)</h4>
                    <span class="text-[10px] px-2 py-0.5 bg-orange-100 text-burntDark font-bold rounded">Internal Only</span>
                </div>
                <ul class="text-[11px] text-stone-600 space-y-1.5 list-disc list-inside">
                    <li>사내 SharePoint, Teams, Outlook, 국사 자산 데이터 전용 검색</li>
                    <li>외부 웹 검색 완전 차단으로 완벽한 제로 트러스트 기밀 보장</li>
                    <li><strong>주요 용도:</strong> 사내 장애 일지, IP 할당표, 표준 운영 절차서(SOP)</li>
                </ul>
            </div>

            <div class="p-4 editorial-card border-t-4 border-t-blue-700">
                <div class="flex items-center justify-between mb-2">
                    <h4 class="text-sm font-bold text-blue-900">🌐 Web 모드 (외부 실시간)</h4>
                    <span class="text-[10px] px-2 py-0.5 bg-blue-100 text-blue-900 font-bold rounded">Bing Grounding</span>
                </div>
                <ul class="text-[11px] text-stone-600 space-y-1.5 list-disc list-inside">
                    <li>최신 3GPP 릴리즈, IETF RFC 표준, 글로벌 벤더 공식 매뉴얼 검색</li>
                    <li>상용 LLM과 달리 2026년 최신 보안 취약점(CVE) 실시간 반영</li>
                    <li><strong>주요 용도:</strong> 신규 펌웨어 패치, 글로벌 RFC 표준 스펙 대조</li>
                </ul>
            </div>
        </div>

        <div class="mt-4 p-3.5 editorial-card text-left max-w-5xl mx-auto bg-stone-50 border-stone-200">
            <div class="text-xs font-bold text-burntDark mb-1">🛡️ 쿼리 변환(Query Transformation) 보안 메커니즘</div>
            <p class="text-[11px] text-stone-600 leading-relaxed">
                사내 호스트명(예: <code class="text-burntDark font-mono bg-orange-50 px-1 py-0.5 rounded">KR-SEL-DC1-RTR01</code>)이 포함된 질문이 외부 검색 엔진으로 전송될 때, Copilot은 내부 식별자를 제거하고 <code class="text-burntDark font-mono bg-orange-50 px-1 py-0.5 rounded">"Cisco ASR 9000 BGP EVPN flap issue"</code>와 같이 일반화된 기술 쿼리로 자동 변환하여 외부로 전송합니다.
            </p>
        </div>
        """,
        "notes": "Work 모드와 Web 모드의 전환 기준과 내부 정보 유출을 차단하는 쿼리 변환 메커니즘을 상세히 설명합니다."
    },
    # Slide 07
    {
        "badge": "EXCEL DATA INTELLIGENCE",
        "title": "[2026 신기능] 대규모 에러 로그 정제 & <span class='text-burnt'>트리밍 참조 (.:.)</span>",
        "subtitle": "수만 행의 Syslog 연산 속도를 혁신하는 =COPILOT 수식과 TRIMRANGE 최적화",
        "body": """
        <div class="p-4 editorial-dark-card text-left max-w-5xl mx-auto mb-4">
            <div class="text-xs text-stone-400 mb-1 font-mono">Excel 2026 공식 Copilot 수식:</div>
            <div class="p-3 bg-stone-950 rounded-lg text-sm font-mono text-orange-300 border border-stone-800">
                =COPILOT("B열의 에러 로그에서 [Critical] 레벨만 분류하고 N/A 값은 이전 유효 데이터로 채워줘", B7.:.E50000)
            </div>
        </div>

        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto">
            <div class="p-4 editorial-card">
                <h4 class="text-sm font-bold text-espresso mb-2">⚡ 트리밍 참조 (.:.)의 파괴력</h4>
                <p class="text-xs text-stone-600 leading-relaxed">
                    콜론 앞뒤에 마침표를 찍는 <strong>트리밍 참조(Trimming References)</strong>는 비어있는 불필요한 셀을 제외하고 실제 유효 데이터 범위만 자동 바운딩하여 계산 리소스를 90% 절감합니다.
                </p>
            </div>
            <div class="p-4 editorial-card">
                <h4 class="text-sm font-bold text-espresso mb-2">🚀 excel.new 즉시 환경 구축</h4>
                <p class="text-xs text-stone-600 leading-relaxed">
                    브라우저 주소창에 <code class="text-burntDark font-mono bg-orange-50 px-1 py-0.5 rounded">excel.new</code>를 입력하여 즉시 웹 기반 Excel Copilot 환경을 띄우고, 원클릭 표 서식화(<code class="text-burntDark font-mono bg-orange-50 px-1 py-0.5 rounded">Ctrl + T</code>)를 통해 AI 분석을 개시합니다.
                </p>
            </div>
        </div>
        """,
        "notes": "대용량 로그 처리 시 연산 병목을 해결하는 트리밍 참조 수식 기법을 설명합니다."
    },
    # Slide 08
    {
        "badge": "EXCEL DATA INTELLIGENCE",
        "title": "트래픽 피벗 집계 및 <span class='text-burnt'>피벗 자동 새로고침(Pivot Auto Refresh)</span>",
        "subtitle": "실시간 데이터 유입 시 대시보드를 수작업 없이 자동으로 갱신하는 스마트 피벗",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-2">
            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-burntDark mb-2">Top Talker 피벗 집계 프롬프트</h4>
                <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-3">
                    "방화벽 트래픽 로그에서 총 Byte_Size를 기준으로 상위 10개 출발지 IP(Src_IP)를 추출하고, 프로토콜별 비율을 보여주는 피벗 테이블을 생성해줘."
                </div>
                <ul class="text-[11px] text-stone-600 space-y-1">
                    <li>✓ 복잡한 SUMIFS/XLOOKUP 수식 자동 생성</li>
                    <li>✓ 비정상 포트(Port Scan) 다중 조건 필터링</li>
                </ul>
            </div>

            <div class="p-5 editorial-card border-t-4 border-t-emerald-600">
                <h4 class="text-sm font-bold text-emerald-800 mb-2">🔄 Pivot Auto Refresh 메커니즘</h4>
                <p class="text-xs text-stone-600 mb-3 leading-relaxed">
                    새로운 Syslog 행이 지속적으로 추가될 때 수동으로 '새로 고침'을 누를 필요 없이 대시보드와 차트가 실시간 동기화되는 2026 자동화 기능입니다.
                </p>
                <div class="p-2.5 bg-emerald-50 rounded-lg text-[11px] text-emerald-800 border border-emerald-200">
                    "원본 데이터 추가 시 실시간 반영되도록 Pivot Auto Refresh를 활성화해줘."
                </div>
            </div>
        </div>
        """,
        "notes": "피벗 자동 새로고침과 Top Talker 추출을 통한 실시간 관제 대시보드 구축을 설명합니다."
    },
    # Slide 09
    {
        "badge": "ANALYST AGENT",
        "title": "[핵심] 분석가 도구(Analyst Agent)와 <span class='text-burnt'>Python in Excel 메커니즘</span>",
        "subtitle": "자연어 질의를 수신한 AI가 Azure 격리 샌드박스에서 파이썬 코드를 자동 생성·실행",
        "body": """
        <div class="p-4 editorial-card max-w-5xl mx-auto mb-4 text-left">
            <div class="flex items-center justify-between text-xs font-mono">
                <div class="p-2.5 bg-stone-100 rounded text-center w-40 text-stone-800 font-bold border border-stone-200">1. 자연어 질문<br><span class='text-[9px] text-stone-500'>"이상 트래픽 찾아줘"</span></div>
                <div class="text-burnt font-bold">➔</div>
                <div class="p-2.5 bg-orange-50 rounded text-center w-44 text-burntDark font-bold border border-orange-200">2. Analyst Agent<br><span class='text-[9px] text-stone-600'>데이터 스키마 자율 파악</span></div>
                <div class="text-burnt font-bold">➔</div>
                <div class="p-2.5 bg-blue-50 rounded text-center w-48 text-blue-900 font-bold border border-blue-200">3. Azure Python<br><span class='text-[9px] text-stone-600'>pandas, seaborn 연산</span></div>
                <div class="text-burnt font-bold">➔</div>
                <div class="p-2.5 bg-emerald-50 rounded text-center w-40 text-emerald-900 font-bold border border-emerald-200">4. Excel 출력<br><span class='text-[9px] text-stone-600'>인터랙티브 히트맵</span></div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-4 text-left max-w-5xl mx-auto">
            <div class="p-4 editorial-card">
                <h5 class="text-xs font-bold text-espresso mb-1">🐍 표준 파이썬 라이브러리</h5>
                <p class="text-[11px] text-stone-600">pandas, numpy, statsmodels, scikit-learn 기본 내장</p>
            </div>
            <div class="p-4 editorial-card">
                <h5 class="text-xs font-bold text-espresso mb-1">🛡️ 무결점 클라우드 격리</h5>
                <p class="text-[11px] text-stone-600">로컬 PC 자원을 쓰지 않고 Azure 클라우드에서 안전하게 실행</p>
            </div>
            <div class="p-4 editorial-card">
                <h5 class="text-xs font-bold text-espresso mb-1">📊 고급 시각화 엔진</h5>
                <p class="text-[11px] text-stone-600">matplotlib & seaborn 기반 복합 이상치 히트맵 도출</p>
            </div>
        </div>
        """,
        "notes": "Analyst Agent가 자연어를 파이썬 코드로 변환하여 클라우드 샌드박스에서 실행하는 기술 구조를 설명합니다."
    },
    # Slide 10
    {
        "badge": "ANOMALY DETECTION",
        "title": "통신망 이상 트래픽(DDoS/스파이크) 탐지 & <span class='text-burnt'>히트맵 시각화</span>",
        "subtitle": "통계적 Z-Score(3σ) 및 머신러닝 Isolation Forest 알고리즘 기반 이상 징후 자동 포착",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-2">
            <div class="p-4 editorial-card">
                <h4 class="text-sm font-bold text-burntDark mb-2">1. 통계적 Z-Score 모델 (3σ 기준)</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    시간당 평균 패킷량 대비 <strong>3표준편차(Z-Score > 3)</strong>를 초과하는 급격한 스파이크 트래픽을 감지하여 DDoS 및 포트 스캔을 판별합니다.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-orange-200 border border-stone-800">
                    "Packet_Count가 3σ를 초과하는 행에 조건부 서식을 씌워줘."
                </div>
            </div>

            <div class="p-4 editorial-card">
                <h4 class="text-sm font-bold text-blue-900 mb-2">2. ML 기반 Isolation Forest & 히트맵</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    패킷 수, 바이트 크기, 접속 빈도의 다차원 데이터를 클러스터링하여 잠복형 비정상 세션을 탐지하고 시간대별 부하 히트맵으로 시각화합니다.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-blue-200 border border-stone-800">
                    "Isolation Forest를 적용해 시간대별 부하 히트맵을 그려줘."
                </div>
            </div>
        </div>
        """,
        "notes": "통계적 3-Sigma 모델과 ML Isolation Forest를 활용한 네트워크 이상치 탐지 기법을 설명합니다."
    },
    # Slide 11
    {
        "badge": "CAPACITY PLANNING",
        "title": "5G/인프라 대역폭 사이징 및 <span class='text-burnt'>시계열 예측(Forecasting)</span>",
        "subtitle": "과거 12개월 부하 추세선(Trendline) 모델링으로 회선 증설 임계치(80%) 도달 시점 예측",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">시계열 대역폭 예측 프롬프트</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4">
                "최근 12개월간의 기지국 백홀 트래픽 시계열 데이터를 분석해서, 향후 6개월간의 트래픽 증가 추세를 예측해줘. 회선 가용 용량의 80% 임계치에 도달하는 예상 월을 산출하고 증설 필요 대역폭을 제안해줘."
            </div>
            <div class="grid grid-cols-3 gap-4 text-xs text-stone-700">
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">① 지수 평활법 모델링</strong><br>
                    계절성 및 피크 트래픽 패턴 반영
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">② 80% Threshold 계산</strong><br>
                    선제적 회선 증설 예산 계획 수립
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">③ C-Level 요약 카드</strong><br>
                    인사이트 지표를 1장의 요약으로 도출
                </div>
            </div>
        </div>
        """,
        "notes": "시계열 트래픽 예측을 통한 인프라 용량 계획 및 선제적 증설 방안을 설명합니다."
    },
    # Slide 12
    {
        "badge": "HANDS-ON LAB 1",
        "title": "🧪 [실습 1] 5만 건 방화벽 로그 이상치 분석 & <span class='text-burnt'>대시보드 구축</span>",
        "subtitle": "소요시간: 20분 | 트리밍 참조 + Python 이상치 탐지 + Pivot Auto Refresh 완주",
        "body": """
        <div class="grid grid-cols-3 gap-4 text-left max-w-6xl mx-auto mt-2">
            <div class="p-4 editorial-card border-t-4 border-t-blue-600">
                <div class="text-xs font-bold text-blue-800 mb-1">Step 1. 전처리 & 트리밍</div>
                <div class="p-2 bg-stone-900 rounded text-[10px] font-mono text-stone-200 mb-2 border border-stone-800">
                    =COPILOT("Byte_Size를 기반으로 MB 계산열을 추가해줘", B7.:.F50000)
                </div>
                <p class="text-[11px] text-stone-600">Ctrl+T 표 변환 후 트리밍 참조로 고속 연산</p>
            </div>

            <div class="p-4 editorial-card border-t-4 border-t-emerald-600">
                <div class="text-xs font-bold text-emerald-800 mb-1">Step 2. Python 이상치 탐지</div>
                <div class="p-2 bg-stone-900 rounded text-[10px] font-mono text-stone-200 mb-2 border border-stone-800">
                    "Packet_Count가 3표준편차를 초과하는 구간과 Top 5 공격 IP를 피벗해줘."
                </div>
                <p class="text-[11px] text-stone-600">Analyst Agent를 통한 Z-Score 탐지</p>
            </div>

            <div class="p-4 editorial-card border-t-4 border-t-purple-600">
                <div class="text-xs font-bold text-purple-800 mb-1">Step 3. 히트맵 & Auto Refresh</div>
                <div class="p-2 bg-stone-900 rounded text-[10px] font-mono text-stone-200 mb-2 border border-stone-800">
                    "시간대별 부하 히트맵을 생성하고 Pivot Auto Refresh를 켜줘."
                </div>
                <p class="text-[11px] text-stone-600">실시간 반영 관제 대시보드 완성</p>
            </div>
        </div>
        """,
        "notes": "실습 1 진행: 방화벽 CSV 데이터를 로드하여 3단계로 완결하는 실전 랩입니다."
    },
    # Slide 13
    {
        "badge": "DIAGRAMS AS CODE",
        "title": "Diagrams as Code: <span class='text-burnt'>텍스트 기반 다이어그램</span> 생성 원리",
        "subtitle": "마우스 드로잉 도구의 한계를 극복하고 프롬프트 입력으로 아키텍처를 코드화",
        "body": """
        <div class="grid grid-cols-2 gap-6 text-left max-w-5xl mx-auto mt-4">
            <div class="p-5 editorial-card border-l-4 border-l-red-500">
                <h4 class="text-sm font-bold text-red-900 mb-2">❌ 레거시 수동 드로잉 (Visio 등)</h4>
                <ul class="text-xs text-stone-600 space-y-2 list-disc list-inside">
                    <li>장비 추가 시마다 선과 라벨을 마우스로 일일이 재배치</li>
                    <li>Git 등 형상관리 불가 (바이너리 파일 저장)</li>
                    <li>AI 자동 수정 및 다이어그램 Diff 확인 불가능</li>
                </ul>
            </div>

            <div class="p-5 editorial-accent-card border-l-4 border-l-burnt">
                <h4 class="text-sm font-bold text-burntDark mb-2">✅ 2026 Diagrams as Code (Mermaid)</h4>
                <ul class="text-xs text-stone-700 space-y-2 list-disc list-inside">
                    <li>자연어 프롬프트 1회로 L2/L3 및 시퀀스 다이어그램 생성</li>
                    <li>텍스트 코드이므로 Git 커밋 및 변경점 추적 용이</li>
                    <li>Excalidraw와 연동하여 벡터 그래픽으로 즉시 변환</li>
                </ul>
            </div>
        </div>
        """,
        "notes": "Diagrams as Code의 철학과 텍스트 기반 시각화의 생산성 혁신을 설명합니다."
    },
    # Slide 14
    {
        "badge": "MERMAID GENERATION",
        "title": "Copilot을 활용한 <span class='text-burnt'>Mermaid 통신 토폴로지</span> 코드 생성",
        "subtitle": "5G Core 인터페이스, BGP 세션, 방화벽 이중화 경로를 정확한 문법으로 자동 작성",
        "body": """
        <div class="p-4 editorial-card text-left max-w-5xl mx-auto mt-2">
            <div class="text-xs text-stone-500 font-mono mb-1">5G SA Core 토폴로지 프롬프트:</div>
            <div class="p-2.5 bg-stone-900 rounded text-xs font-mono text-orange-300 border border-stone-800 mb-3">
                "gNodeB 기지국과 5G SA Core(AMF, SMF, UPF) 및 Data Network(DN) 간의 연결 구조를 N2, N3, N4, N6 인터페이스 라벨을 포함하여 Mermaid flowchart LR 문법으로 작성해줘."
            </div>
            <div class="p-3 bg-stone-900 rounded text-[11px] font-mono text-emerald-300 border border-stone-800">
                flowchart LR<br>
                &nbsp;&nbsp;gNB["gNodeB (5G RAN)"] -- N2 (Control) --> AMF["5G Core AMF"]<br>
                &nbsp;&nbsp;gNB -- N3 (User Plane) --> UPF["5G Core UPF"]<br>
                &nbsp;&nbsp;AMF <--> SMF["5G Core SMF"]<br>
                &nbsp;&nbsp;SMF -- N4 --> UPF<br>
                &nbsp;&nbsp;UPF -- N6 --> DN["Data Network (Internet)"]
            </div>
        </div>
        """,
        "notes": "통신 네트워크 표준 인터페이스를 반영한 Mermaid 문법 생성 프롬프트를 설명합니다."
    },
    # Slide 15
    {
        "badge": "VECTOR VISUALS",
        "title": "Excalidraw 원클릭 연동 <span class='text-burnt'>(Mermaid to Diagram)</span>",
        "subtitle": "텍스트 코드를 발표 자료 및 기술 백서에 삽입 가능한 고품질 모던 벡터 그래픽으로 전환",
        "body": """
        <div class="grid grid-cols-3 gap-4 text-left max-w-6xl mx-auto mt-4">
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-xs mb-1">Step 1. 코드 복사</div>
                <p class="text-xs text-stone-600">Copilot이 생성한 Mermaid 블록 전체를 원클릭 복사</p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-burnt font-bold text-xs mb-1">Step 2. Excalidraw 삽입</div>
                <p class="text-xs text-stone-600">Excalidraw의 <code class="text-burnt font-mono bg-orange-50 px-1 py-0.5 rounded">Mermaid to Diagram</code> 메뉴에 코드 붙여넣기</p>
            </div>
            <div class="p-4 editorial-accent-card">
                <div class="text-burntDark font-bold text-xs mb-1">Step 3. 모던 벡터 커스텀</div>
                <p class="text-xs text-stone-700">사내 컬러 팔레트 적용 후 고해상도 SVG/PNG로 내보내기</p>
            </div>
        </div>
        <div class="mt-6 p-4 editorial-card max-w-5xl mx-auto text-xs text-stone-600 bg-stone-50">
            💡 <strong>Tip:</strong> 복잡한 인프라 제안서에 삽입할 때 손그림(Hand-drawn) 스타일 또는 모던 플랫 스타일로 1초 만에 테마 전환이 가능합니다.
        </div>
        """,
        "notes": "Excalidraw와 Mermaid의 원클릭 연동 워크플로를 소개합니다."
    },
    # Slide 16
    {
        "badge": "HANDS-ON LAB 2",
        "title": "🧪 [실습 2] 5G SA Core & 하이브리드 BGP 이중화 다이어그램 제작",
        "subtitle": "소요시간: 15분 | 프롬프트 작성 ➔ Mermaid 생성 ➔ Excalidraw 벡터 변환",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">실습 프롬프트 (Role-Context-Constraint)</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "너는 시니어 네트워크 아키텍트야. 본사 IDC(Core SW, Active/Standby FW, 서브넷 10.10.0.0/16)와 AWS 간 Direct Connect 10G(Primary) 및 IPsec VPN(Secondary) BGP 이중화 경로를 나타내는 Mermaid flowchart TD 코드를 작성해줘. 서브넷 대역과 포트 번호도 라벨에 포함해줘."
            </div>
            <div class="p-3 bg-emerald-50 rounded-xl text-xs text-emerald-900 border border-emerald-200">
                ✓ <strong>최종 결과물:</strong> 완성된 Mermaid 코드를 Excalidraw에 붙여넣어 제안서용 벡터 아키텍처 다이어그램 렌더링 완료.
            </div>
        </div>
        """,
        "notes": "실습 2 진행: 하이브리드 클라우드 BGP 이중화 아키텍처 다이어그램을 코드화합니다."
    },
    # Slide 17
    {
        "badge": "OUTLOOK AUTONOMOUS OPS",
        "title": "NOC Level-1 인시던트 요약 & <span class='text-burnt'>첨부파일 목록화(Attachment Listing)</span>",
        "subtitle": "밤새 누적된 수천 건의 알람 메일 스레드에서 조치 필요 항목 및 벤더 매뉴얼 즉시 추출",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">NOC 긴급 알람 요약 프롬프트</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "지난 밤 발생한 [NOC Level-1 Incident Alarms] 메일 스레드를 분석해줘. 특히 [5G Standalone Core Latency]와 관련된 Action Required 항목만 추출하고, 삼성/에릭슨 등 벤더사별 장비 매뉴얼이 포함된 <strong>첨부 파일 목록(Attachment List)</strong>을 표 형태로 정리해줘."
            </div>
            <div class="grid grid-cols-2 gap-4 text-xs text-stone-700">
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-burntDark">Action Required 자동 선별</strong><br>
                    수동 탐색 없이 즉각적인 조치 대상 우선순위화
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-burntDark">Email Attachment Listing</strong><br>
                    수십 개 메일에 분산된 매뉴얼 PDF를 표로 단일화
                </div>
            </div>
        </div>
        """,
        "notes": "Outlook의 Action Required 추출과 Attachment Listing을 통한 NOC 업무 간소화를 설명합니다."
    },
    # Slide 18
    {
        "badge": "CROSS-CONTEXT REASONING",
        "title": "[2026 신기능] 포괄적 크로스 컨텍스트 추론 <span class='text-burnt'>(Cross-Context Reasoning)</span>",
        "subtitle": "단일 메일을 넘어 전체 편지함, 캘린더, 모임 기록, 사내 Graph 데이터를 통틀어 종합 질의",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2 border-t-4 border-t-purple-600">
            <h4 class="text-sm font-bold text-purple-900 mb-2">복합 엔지니어링 지시 예시</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-purple-200 border border-stone-800 mb-4 leading-relaxed">
                "내 매니저가 보낸 읽지 않은 메일 중 [코어망 장애]와 관련된 메일을 전부 플래그 표시하고, 내일 예정된 Post-Mortem 회의 참석자들의 최근 회신 의견을 3줄로 브리핑해줘."
            </div>
            <div class="grid grid-cols-3 gap-3 text-xs text-stone-700">
                <div class="p-2.5 bg-stone-50 rounded border border-stone-200">
                    <strong class="text-espresso">① 전체 메일함 탐색</strong><br>단일 스레드 한계 극복
                </div>
                <div class="p-2.5 bg-stone-50 rounded border border-stone-200">
                    <strong class="text-espresso">② 캘린더 일정 교차 대조</strong><br>모임 참석자 매핑
                </div>
                <div class="p-2.5 bg-stone-50 rounded border border-stone-200">
                    <strong class="text-espresso">③ 선제적 플래그 설정</strong><br>우선순위 자율 정리
                </div>
            </div>
        </div>
        """,
        "notes": "편지함과 캘린더, 사내 Graph를 융합하여 연속 업무를 처리하는 포괄적 추론 기능을 설명합니다."
    },
    # Slide 19
    {
        "badge": "CALENDAR DELEGATION",
        "title": "[@Calendar Agent] 현장 엔지니어 리소스 재배치 & <span class='text-burnt'>위임 관리</span>",
        "subtitle": "일정 충돌 실시간 감지 ➔ 자동 일정 재조정 + 회의실 대신 예약 + 집중 시간(Focus Time) 보호",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2 border-t-4 border-t-emerald-600">
            <h4 class="text-sm font-bold text-emerald-800 mb-2">캘린더 에이전트 프롬프트</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "@Calendar Agent, 현재 [수도권 동부 국사] 현장 점검 엔지니어들의 일정 충돌을 확인해줘. 긴급 장애 복구를 위해 오늘 오후 미팅을 내일 오전으로 자동 재설정하고, 참석자들에게 변경 사유와 Teams 영상 Recap 링크를 포함한 알림을 발송해줘."
            </div>
            <div class="grid grid-cols-3 gap-3 text-xs text-stone-700">
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-emerald-800">충돌 자동 해결</strong><br>참석자 빈 시간 자동 탐색
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-emerald-800">회의실 자율 예약</strong><br>장비 구비된 회의실 선점
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-emerald-800">Focus Time 보호</strong><br>점검 작업 시간 블록 유지
                </div>
            </div>
        </div>
        """,
        "notes": "긴급 장애 상황에서 @Calendar Agent를 활용한 엔지니어 리소스 자율 재배치를 설명합니다."
    },
    # Slide 20
    {
        "badge": "HANDS-ON LAB 3",
        "title": "🧪 [실습 3] 글로벌 TAC 메일 분석 ➔ 고객사 회신 ➔ <span class='text-burnt'>캘린더 위임 예약</span>",
        "subtitle": "소요시간: 15분 | 영문 스레드 요약 + C-Level 안내문 작성 + @Calendar Agent 예약",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-2">
            <div class="p-4 editorial-card">
                <div class="text-xs font-bold text-burntDark mb-1">Step 1. 영문 TAC 요약 & 고객사 회신</div>
                <p class="text-xs text-stone-600 mb-2 leading-relaxed">
                    20여 통의 영문 TAC 메일에서 하드웨어 결함 원인을 요약하고, 고객사 임원 발송용 정중한 회신문 작성.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[10px] font-mono text-orange-200 border border-stone-800">
                    "원인, RMA 조치 결과, 향후 펌웨어 패치 일정을 포함해 회신문 작성해줘."
                </div>
            </div>

            <div class="p-4 editorial-card">
                <div class="text-xs font-bold text-emerald-800 mb-1">Step 2. @Calendar Agent 회의 예약</div>
                <p class="text-xs text-stone-600 mb-2 leading-relaxed">
                    인프라/보안팀 담당자들의 내일 오전 빈 시간에 45분간 Post-Mortem 회의 일정 자동 예약.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[10px] font-mono text-emerald-200 border border-stone-800">
                    "안건 3가지(RMA 분석, 알람 임계치, 페일오버 검증)를 포함해 초대장 발송해줘."
                </div>
            </div>
        </div>
        """,
        "notes": "실습 3 진행: 글로벌 장애 스레드 요약부터 캘린더 자동 예약까지의 완결형 실습입니다."
    },
    # Slide 21
    {
        "badge": "POWER BI GROUNDING",
        "title": "[2026 핵심] Power BI Grounding 기반 <span class='text-burnt'>네트워크 품질 제안서 생성</span>",
        "subtitle": "조직의 '단일 진실 공급원(SSOT)'인 Power BI 대시보드 데이터를 직접 그라운딩하여 슬라이드 빌드",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">Power BI 연동 슬라이드 생성 프롬프트</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "우리 회사의 [Power BI 'Network Quality' 대시보드] 데이터를 그라운딩하여 차세대 망 고도화 필요성 슬라이드를 생성해줘. 특히 전월 대비 통화/데이터 품질 저하 지표를 시각화하고, 이에 대응하는 기술적 로드맵을 제안해줘."
            </div>
            <div class="grid grid-cols-2 gap-4 text-xs text-stone-700">
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">수작업 캡처/복붙 종말</strong><br>
                    대시보드 지표를 실시간 데이터 바인딩으로 슬라이드 변환
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">Meeting-to-Deck 지원</strong><br>
                    Teams 회의 녹취록을 참조하여 즉시 프레젠테이션화
                </div>
            </div>
        </div>
        """,
        "notes": "Power BI 데이터를 단일 진실 공급원(SSOT)으로 삼아 제안서를 자동 생성하는 방식을 설명합니다."
    },
    # Slide 22
    {
        "badge": "BRAND KIT & RESTYLE",
        "title": "브랜드 키트 일괄 적용 <span class='text-burnt'>(Brand Kit & Style Restyle)</span>",
        "subtitle": "사내 공식 로고, 지정 컬러 팔레트, 엔지니어링 폰트, 표/차트 스타일을 원클릭 일괄 적용",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-4">
            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-espresso mb-2">🎨 Brand Kit 스킬</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    기업의 CI/BI 가이드라인을 사전 정의된 스킬로 등록해두면 슬라이드 생성 시 폰트 깨짐이나 색상 불일치를 완벽히 방지합니다.
                </p>
                <div class="p-2.5 bg-stone-900 rounded text-[11px] font-mono text-orange-200 border border-stone-800">
                    "[Brand Kit] 스킬을 적용해 공식 로고와 폰트를 맞춰줘."
                </div>
            </div>

            <div class="p-5 editorial-accent-card">
                <h4 class="text-sm font-bold text-burntDark mb-2">⚡ Style Restyle 기능</h4>
                <p class="text-xs text-stone-700 leading-relaxed mb-3">
                    기존의 낡은 텍스트 위주 슬라이드를 모던 카드 레이아웃 및 최신 테크 테마로 한 번에 재스타일링합니다.
                </p>
                <div class="p-2.5 bg-stone-900 rounded text-[11px] font-mono text-emerald-200 border border-stone-800">
                    "표와 차트의 스타일을 [Style Restyle] 해줘."
                </div>
            </div>
        </div>
        """,
        "notes": "사내 브랜드 가이드라인을 유지하면서 고품질 디자인을 일괄 적용하는 방법을 설명합니다."
    },
    # Slide 23
    {
        "badge": "COLLABORATION & SPEECH",
        "title": "댓글 내 작업 할당 & <span class='text-burnt'>발표자 노트 (Speaker Notes)</span>",
        "subtitle": "슬라이드 댓글 창에서 엔지니어에게 직접 업무 할당(@Mention) 및 구어체 스크립트 자동 생성",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-2">
            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-burntDark mb-2">1. 댓글 내 작업 할당 (Task Assignment)</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    슬라이드 검토 중 특정 영역에 대해 담당자(@홍길동 엔지니어)를 멘션하여 작업을 할당하고 Teams 알림을 즉시 발송합니다.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-stone-300 border border-stone-800">
                    "@김엔지니어 3번 슬라이드 BGP 설정 검증 부탁드립니다."
                </div>
            </div>

            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-blue-900 mb-2">2. 발표자 노트 & Q&A 방어 논리</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    슬라이드 본문 요약이 아닌, 실제 발표자가 자연스럽게 읽을 수 있는 구어체 대본과 C-Level 예상 질문 3가지를 자동 생성합니다.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-blue-200 border border-stone-800">
                    "발표자 노트와 임원진 예상 Q&A 방어 논리를 작성해줘."
                </div>
            </div>
        </div>
        """,
        "notes": "PowerPoint 내 협업 워크플로와 발표자 노트 자동 생성 기법을 설명합니다."
    },
    # Slide 24
    {
        "badge": "HANDS-ON LAB 4",
        "title": "🧪 [실습 4] Power BI 품질 지표 그라운딩 ➔ <span class='text-burnt'>3단 제안서 빌드</span>",
        "subtitle": "소요시간: 15분 | 망 품질 데이터 그라운딩 ➔ 3단 모던 슬라이드 ➔ Brand Kit 적용",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">실습 워크플로 (Meeting-to-Deck & Style Restyle)</h4>
            <div class="space-y-3 text-xs text-stone-700">
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">1단계: Power BI Grounding</strong><br>
                    <code class="text-burntDark font-mono">"Power BI 'Network Quality' 대시보드를 기반으로 3장의 제안 슬라이드를 작성해줘."</code>
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">2단계: 3단 모던 카드 구성</strong><br>
                    Slide 1(품질 저하 분석) ➔ Slide 2(기술적 고도화 로드맵) ➔ Slide 3(투자 대비 효과)
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-espresso">3단계: Brand Kit 일괄 적용 & 작업 할당</strong><br>
                    공식 컬러 팔레트 적용 후, 보안팀 담당자에게 방화벽 정책 검토 작업 할당(@Mention).
                </div>
            </div>
        </div>
        """,
        "notes": "실습 4 진행: 데이터 그라운딩 기반의 슬라이드 생성과 스타일링을 실습합니다."
    },
    # Slide 25
    {
        "badge": "WORD TRANSPARENT EDITING",
        "title": "[2026 핵심] 기술 규격 대조, Track Changes & <span class='text-burnt'>진행 메시지(Progress Messages)</span>",
        "subtitle": "DU/RU/BBU 약어 국제 표준 표기 및 Work IQ 기술규정 대조 과정을 투명하게 기록",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">RCA 보고서 정밀 검토 프롬프트</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "[변경 내용 추적] 모드를 활성화하고 이 RCA 보고서를 검토해줘. DU, RU, BBU 등 모든 약어를 국제 표준에 맞춰 풀어서 설명하고, 기술 규격 수치가 사내 기술 규정집(Work IQ 참조)과 일치하는지 정밀 대조해줘. 작업 중에 <strong>[진행 메시지(Progress Messages)]</strong>를 통해 단계별 수정 사항을 알려줘."
            </div>
            <div class="grid grid-cols-2 gap-4 text-xs text-stone-700">
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-burntDark">Track Changes 협업</strong><br>
                    단어 단위로 수정 내역이 기록되어 팀원 검토 용이
                </div>
                <div class="p-3 bg-stone-50 rounded-lg border border-stone-200">
                    <strong class="text-burntDark">Progress Messages</strong><br>
                    수정 중인 단계를 실시간으로 보고하여 무결점 검증
                </div>
            </div>
        </div>
        """,
        "notes": "Word의 변경 내용 추적과 진행 메시지를 활용한 고정밀 기술 문서 검증을 설명합니다."
    },
    # Slide 26
    {
        "badge": "WORD CITATIONS & SUMMARY",
        "title": "리스크 플래그, 참조 출처(Citations) & <span class='text-burnt'>Review Summary 섹션</span>",
        "subtitle": "기술적 근거 불명확 지점에 플래그 삽입 및 최상단 검토 요약으로 팩트체크 시간 90% 단축",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-amber-800 mb-2">리스크 플래그 & Review Summary 프롬프트</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "본문 중 기술적 근거가 불분명한 지점에 리스크 플래그를 달고, 사내 기술 베이스(Work IQ)를 참조하여 정확한 출처를 표시해줘. 작업 완료 후, 문서 최상단에 [Review Summary] 섹션을 추가하여 (1) 주요 수정 제안 사항과 (2) 기술 검증이 필요한 잔여 리스크를 요약해줘."
            </div>
            <div class="grid grid-cols-3 gap-3 text-xs text-stone-700">
                <div class="p-2.5 bg-stone-50 rounded border border-stone-200">
                    <strong class="text-espresso">① 리스크 플래그</strong><br>모호한 수치 즉시 식별
                </div>
                <div class="p-2.5 bg-stone-50 rounded border border-stone-200">
                    <strong class="text-espresso">② 명확한 Citations</strong><br>사내 규정 출처 각주 링크
                </div>
                <div class="p-2.5 bg-stone-50 rounded border border-stone-200">
                    <strong class="text-espresso">③ Review Summary</strong><br>최상단 3줄 핵심 검토 요약
                </div>
            </div>
        </div>
        """,
        "notes": "문서 최상단 Review Summary와 명확한 출처 표기로 보고서 신뢰성을 극대화하는 방법을 설명합니다."
    },
    # Slide 27
    {
        "badge": "RFC SIMPLIFICATION",
        "title": "난해한 기술 규격(RFC, 벤더 스펙)의 <span class='text-burnt'>쉬운 해설화</span>",
        "subtitle": "영문 50페이지 RFC 8365(BGP EVPN)를 초급자용 비유, 용어 5선 사전, 체크리스트로 재구성",
        "body": """
        <div class="grid grid-cols-3 gap-4 text-left max-w-6xl mx-auto mt-4">
            <div class="p-4 editorial-card">
                <div class="text-burntDark font-bold text-xs mb-1">1. 일상 비유 설명</div>
                <p class="text-xs text-stone-600 leading-relaxed">
                    BGP EVPN의 원리를 '전국 단위 택배 물류 및 허브 센터 시스템'에 빗대어 비전공자도 이해할 수 있게 해설
                </p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-emerald-800 font-bold text-xs mb-1">2. 핵심 용어 5선 정의</div>
                <p class="text-xs text-stone-600 leading-relaxed">
                    NVE, VNI, RD, RT, Anycast Gateway의 정의를 실무 관점에서 1줄씩 명쾌하게 정리
                </p>
            </div>
            <div class="p-4 editorial-card">
                <div class="text-purple-800 font-bold text-xs mb-1">3. 실무 점검 체크리스트</div>
                <p class="text-xs text-stone-600 leading-relaxed">
                    MTU 설정(점보 프레임 9000), 언더레이 라우팅 등 도입 전 필수 점검 5개 항목을 표로 변환
                </p>
            </div>
        </div>
        """,
        "notes": "난해한 기술 스펙을 쉬운 비유와 실무 체크리스트로 풀어내는 프롬프트 작성법을 소개합니다."
    },
    # Slide 28
    {
        "badge": "ONENOTE & MOBILE",
        "title": "OneNote AI 전자필기장 & <span class='text-burnt'>모바일 Word 현장 음성 보고</span>",
        "subtitle": "기지국/국사 현장에서 스마트폰 음성 입력으로 점검 보고서 초안 작성 및 OneNote 점검표 정리",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-4">
            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-espresso mb-2">📱 모바일 Word 음성 입력</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    서버실 소음 환경에서 스마트폰 음성 구술로 점검 결과를 녹음하면, Copilot이 표준 출장 보고서 양식으로 완벽히 변환합니다.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-orange-200 border border-stone-800">
                    "음성 메모를 사내 표준 국사 점검 보고서 서식으로 변환해줘."
                </div>
            </div>

            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-emerald-800 mb-2">📓 OneNote 현장 지식화</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-3">
                    두서없이 적힌 현장 필기에서 장비별 상태 표를 생성하고 긴급 조치 사항(Action Items)을 자동 추출합니다.
                </p>
                <div class="p-2 bg-stone-900 rounded text-[11px] font-mono text-emerald-200 border border-stone-800">
                    "메모를 구조화된 표로 정리하고 Action Items를 추출해줘."
                </div>
            </div>
        </div>
        """,
        "notes": "현장 엔지니어를 위한 모바일 음성 보고와 OneNote 메모 지식화 기법을 설명합니다."
    },
    # Slide 29
    {
        "badge": "HANDS-ON LAB 5",
        "title": "🧪 [실습 5] 5G Core 장애 RCA 보고서 작성 <span class='text-burnt'>(Review Summary & Progress)</span>",
        "subtitle": "소요시간: 15분 | Track Changes 켜기 ➔ 기술규격 대조 ➔ 최상단 Review Summary 도출",
        "body": """
        <div class="p-5 editorial-card text-left max-w-5xl mx-auto mt-2">
            <h4 class="text-sm font-bold text-burntDark mb-2">실습 프롬프트 (정밀 RCA 보고서 검토)</h4>
            <div class="p-3 bg-stone-900 rounded-lg text-xs font-mono text-stone-200 border border-stone-800 mb-4 leading-relaxed">
                "[변경 내용 추적]을 켜고 이 5G Core 지연 장애 RCA 초안을 검토해줘. 기술 규격을 대조하고 진행 메시지를 표시하며, 문서 최상단에 [Review Summary]를 추가해 (1)주요 수정 사항과 (2)잔여 리스크를 정리해줘."
            </div>
            <div class="p-3 bg-emerald-50 rounded-xl text-xs text-emerald-900 border border-emerald-200">
                ✓ <strong>최종 산출물:</strong> 단어 단위 수정 내역이 기록된 Word 보고서 + 최상단 Review Summary 검토표 완성.
            </div>
        </div>
        """,
        "notes": "실습 5 진행: 기술 규격 대조와 Review Summary 생성을 실습합니다."
    },
    # Slide 30
    {
        "badge": "TEAMS RECAPS",
        "title": "[2026 신기능] Teams 비디오/오디오 리캡 & <span class='text-burnt'>Meeting Recaps App</span>",
        "subtitle": "핵심 발언 영상 클립 + 한국어 음성 요약이 결합된 하이라이트 영상 및 30일간의 회의 요약 허브",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-4">
            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-espresso mb-2">🎥 Video & Audio Recap</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-2">
                    단순 텍스트 회의록을 넘어, 핵심 발언 구간의 <strong>영상 클립과 AI 요약이 결합된 하이라이트 비디오</strong>를 제공합니다.
                </p>
                <div class="text-[11px] text-burntDark font-semibold">✓ 한국어 포함 다국어 음성 요약 지원</div>
            </div>

            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-blue-900 mb-2">📱 Meeting Recaps 전용 앱</h4>
                <p class="text-xs text-stone-600 leading-relaxed mb-2">
                    Teams 사이드바에 고정하여 <strong>최근 30일간 진행된 모든 회의 요약과 오디오 하이라이트</strong>를 한곳에서 청취하고 검색합니다.
                </p>
                <div class="text-[11px] text-blue-800 font-semibold">✓ 이동 중 모바일 오디오 스트리밍 청취</div>
            </div>
        </div>
        """,
        "notes": "Teams의 비디오/오디오 리캡과 Meeting Recaps 앱을 통한 회의 생산성 극대화를 설명합니다."
    },
    # Slide 31
    {
        "badge": "CAPSTONE LAB",
        "title": "🏆 [종합 실습] Copilot Cowork 기반 <span class='text-burnt'>5G Core 대규모 장애 E2E 파이프라인</span>",
        "subtitle": "소요시간: 30분 | 로그 정제 ➔ 토폴로지 ➔ RCA ➔ PPT ➔ 캘린더 ➔ Cowork Skill 템플릿화",
        "body": """
        <div class="p-4 editorial-card text-left max-w-6xl mx-auto mt-2">
            <div class="grid grid-cols-6 gap-2 text-center text-xs font-mono mb-4">
                <div class="p-2 bg-stone-100 rounded border border-stone-200">
                    <span class="text-burntDark font-bold">1. Excel</span><br>
                    <span class="text-[10px] text-stone-500">로그 정제(.:.)</span>
                </div>
                <div class="p-2 bg-stone-100 rounded border border-stone-200">
                    <span class="text-burntDark font-bold">2. Mermaid</span><br>
                    <span class="text-[10px] text-stone-500">토폴로지 시각화</span>
                </div>
                <div class="p-2 bg-stone-100 rounded border border-stone-200">
                    <span class="text-burntDark font-bold">3. Word</span><br>
                    <span class="text-[10px] text-stone-500">RCA 보고서</span>
                </div>
                <div class="p-2 bg-stone-100 rounded border border-stone-200">
                    <span class="text-burntDark font-bold">4. PPT</span><br>
                    <span class="text-[10px] text-stone-500">Power BI 브리핑</span>
                </div>
                <div class="p-2 bg-stone-100 rounded border border-stone-200">
                    <span class="text-burntDark font-bold">5. Outlook</span><br>
                    <span class="text-[10px] text-stone-500">@Calendar 예약</span>
                </div>
                <div class="p-2 bg-orange-100 rounded border border-orange-300">
                    <span class="text-burntDark font-bold">6. Cowork</span><br>
                    <span class="text-[10px] text-stone-600">Skill 전사 공유</span>
                </div>
            </div>
            <div class="p-3 bg-stone-50 rounded-xl text-xs text-stone-700 leading-relaxed border border-stone-200">
                <strong>💡 캡스톤 최종 목표:</strong> 개별 앱의 기능을 단편적으로 쓰는 것을 넘어, Copilot Cowork를 통해 하나의 사건(5G Core 대규모 장애)을 탐지부터 사후 회의 예약 및 스킬 템플릿화까지 6단계 완결형으로 수행합니다.
            </div>
        </div>
        """,
        "notes": "종합 캡스톤 실습: 6단계 엔드투엔드 워크플로를 실습하고 코워크 스킬로 저장합니다."
    },
    # Slide 32
    {
        "badge": "GOVERNANCE & ROI",
        "title": "Agent 365 ROI 모니터링 & <span class='text-burnt'>Microsoft Purview 보안 거버넌스</span>",
        "subtitle": "MTTR(장애 복구 시간) 단축 지표 실시간 추적 및 민감도 레이블(Sensitivity Label) 자동 상속",
        "body": """
        <div class="grid grid-cols-2 gap-5 text-left max-w-5xl mx-auto mt-4">
            <div class="p-5 editorial-card">
                <h4 class="text-sm font-bold text-espresso mb-2">📊 Agent 365 대시보드 (ROI 측정)</h4>
                <ul class="text-xs text-stone-600 space-y-2 list-disc list-inside">
                    <li>에이전트 도입에 따른 <strong>MTTR(평균 장애 처리 시간) 80% 단축</strong> 수치화</li>
                    <li>부서별 Copilot 활용률 및 시간 절감 비용 실시간 집계</li>
                    <li>가장 빈번하게 사용된 '코워크 스킬' 랭킹 확인</li>
                </ul>
            </div>

            <div class="p-5 editorial-card border-t-4 border-t-burnt">
                <h4 class="text-sm font-bold text-burntDark mb-2">🔒 Purview 민감도 레이블 자동 상속</h4>
                <ul class="text-xs text-stone-600 space-y-2 list-disc list-inside">
                    <li>1급 기밀 네트워크 설계도 참조 시 생성 문서에 <strong>'기밀(Confidential)' 레이블 자동 승계</strong></li>
                    <li>외부 유출 방지를 위한 자동 RMS 암호화 적용</li>
                    <li>사내 엔지니어링 DLP 정책과 100% 무결점 호환</li>
                </ul>
            </div>
        </div>
        """,
        "notes": "Agent 365를 통한 실질적인 ROI 측정과 Purview 민감도 레이블 자동 상속의 보안 원칙을 설명합니다."
    },
    # Slide 33
    {
        "badge": "FINAL WRAP-UP",
        "title": "[실무 즉시 적용] 통신 전용 프롬프트 치트시트 & <span class='text-burnt'>Architect's Note</span>",
        "subtitle": "현업에 바로 복사해 쓰는 핵심 프롬프트 요약표와 책임 있는 AI 엔지니어링 철학",
        "body": """
        <div class="p-4 editorial-card text-left max-w-5xl mx-auto mt-1 mb-3">
            <table class="w-full text-[11px] text-stone-700">
                <thead>
                    <tr class="border-b border-stone-200 text-burntDark">
                        <th class="py-1 text-left font-bold">앱</th>
                        <th class="py-1 text-left font-bold">실무 조치 사항 (Copy & Paste 템플릿)</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-stone-100 font-mono text-[11px]">
                    <tr>
                        <td class="py-1.5 font-bold text-espresso">Outlook</td>
                        <td>[발신자]의 [인시던트] 메일 요약 및 첨부된 [벤더사] 사양서를 Attachment List로 나열해줘.</td>
                    </tr>
                    <tr>
                        <td class="py-1.5 font-bold text-espresso">Word</td>
                        <td>[문서명]에 Track Changes를 켜고 기술규격을 대조한 후 최상단에 Review Summary를 작성해줘.</td>
                    </tr>
                    <tr>
                        <td class="py-1.5 font-bold text-espresso">Excel</td>
                        <td>[B7.:.F50000] 데이터를 트리밍 참조하여 특이값을 추출하고 Pivot Auto Refresh를 설정해줘.</td>
                    </tr>
                    <tr>
                        <td class="py-1.5 font-bold text-espresso">PPT</td>
                        <td>[Power BI 망 품질 대시보드]를 그라운딩하여 제안서 초안을 잡고 Brand Kit을 적용해줘.</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="p-4 editorial-accent-card text-left max-w-5xl mx-auto">
            <div class="text-xs font-bold text-burntDark mb-1 font-mono">📜 Architect's Note</div>
            <p class="text-xs text-stone-800 italic leading-relaxed">
                "모든 AI 생성 결과물은 전문가의 최종 검토를 거쳐야 합니다. 책임은 도구가 아닌, 데이터를 제어하는 엔지니어에게 있습니다."
            </p>
        </div>
        """,
        "notes": "과정 마무리: 통신 전용 프롬프트 치트시트를 배포하고 책임 있는 AI 운영 철학을 공유하며 강의를 마칩니다."
    }
]

sections_html = []
for idx, s in enumerate(slides, 1):
    section = f"""
    <section id="slide-{idx:02d}">
        <div class="max-w-6xl mx-auto px-4 text-center">
            <span class="slide-badge">{s['badge']}</span>
            <h2 class="text-2xl md:text-3xl font-bold mb-2 leading-tight">{s['title']}</h2>
            <p class="text-xs md:text-sm text-stone-500 mb-4">{s['subtitle']}</p>
            {s['body']}
        </div>
        <aside class="notes">
            {s['notes']}
        </aside>
    </section>
    """
    sections_html.append(section)

full_html = html_start + "\n".join(sections_html) + html_end

output_path = "/Users/gwanghee/Documents/110_Github/MS_Learn/M365_Copilot_Telecom_Master.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully re-built 33 slides with Warm Editorial Tech theme at {output_path}")
