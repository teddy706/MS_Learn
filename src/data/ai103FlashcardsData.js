export const ai103FlashcardsData = [
  {
    id: 101,
    category: "Microsoft Foundry",
    question: "Microsoft Foundry SDK에서 ChatCompletions API와 Responses API의 차이는?",
    answer: "ChatCompletions API는 OpenAI 표준 포맷 호환 방식인 반면, Responses API는 Microsoft Foundry 프로젝트 컨텍스트, 에이전트 상태 및 세션 가드레일을 통합하여 확장된 AI 응답 생성을 제공합니다.",
    tags: ["Foundry SDK", "Responses API", "ChatCompletions"]
  },
  {
    id: 102,
    category: "AI 에이전트",
    question: "A2A (Agent-to-Agent) 프로토콜이란 무엇인가요?",
    answer: "원격에 존재하는 이종 AI 에이전트 간의 자동 검색(Discovery), 인증, 세션 직접 통신 및 작업 조율(Coordinated Execution)을 안전하게 연결하는 인터-에이전트 통신 프로토콜 표준입니다.",
    tags: ["A2A Protocol", "Multi-agent", "Discovery"]
  },
  {
    id: 103,
    category: "AI 에이전트",
    question: "Foundry IQ는 AI 에이전트 RAG 구조에서 어떤 역할을 수행하나요?",
    answer: "엔터프라이즈 데이터 원본(SharePoint, Azure AI Search 등)을 벡터 및 의미론적으로 인덱싱하고, 여러 AI 에이전트가 공유하여 액세스할 수 있는 지식 파이프라인과 출처 인용(Citation)을 자동화합니다.",
    tags: ["Foundry IQ", "RAG", "Knowledge Base"]
  },
  {
    id: 104,
    category: "자연어 처리 (NLP)",
    question: "Azure Speech Voice Live API 및 SDK의 핵심 활용 시나리오는?",
    answer: "실시간 양방향 음성 대화형 에이전트를 위한 초저지연(Low latency) 음성 전사(STT), LLM 추론 및 자연스러운 음성 합성(TTS) 스트리밍 파이프라인을 지원합니다.",
    tags: ["Voice Live", "Azure Speech", "Real-time Voice"]
  },
  {
    id: 105,
    category: "시각적 인사이트",
    question: "Microsoft Foundry의 Sora 2 모델은 어떤 기능을 제공하나요?",
    answer: "자연어 프롬프트나 시각적 입력을 바탕으로 일관된 물리 법칙과 다이나믹 렌더링을 적용한 고품질 시네마틱 비디오(Video Generation)를 생성하는 모델입니다.",
    tags: ["Sora 2", "Video Generation", "Multimodal"]
  },
  {
    id: 106,
    category: "지식 마이닝",
    question: "Azure Content Understanding 분석기(Analyzer)의 주요 특징은?",
    answer: "텍스트뿐 아니라 이미지, PDF 문서, 양식, 오디오, 비디오 등 다중 양식(Multimodal) 콘텐츠에서 구조화된 정보 및 키-값 쌍(Key-Value Pairs)을 일괄적으로 자동 추출합니다.",
    tags: ["Content Understanding", "Multimodal Analysis", "OCR"]
  },
  {
    id: 107,
    category: "책임있는 AI",
    question: "Azure AI Foundry의 Content Safety (콘텐츠 안전) 가드레일 완화 단계는?",
    answer: "시스템 프롬프트 지침 설계 -> 입력 필터링 및 조작(Prompt Injection) 감지 -> 출력 가드레일 (유해 콘텐츠/욕설/개인정보 차단) -> 원격 측정 감사로 단계별 위험을 예방합니다.",
    tags: ["Content Filters", "Guardrails", "Responsible AI"]
  }
];
