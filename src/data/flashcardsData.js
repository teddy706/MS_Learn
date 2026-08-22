export const flashcardsData = [
  {
    id: 1,
    category: "아키텍처",
    question: "Agentic AI 솔루션 아키텍처에서 'Grounding'이란 무엇인가요?",
    answer: "LLM이나 AI 에이전트가 환각(Hallucination) 없이 정확한 답변을 내도록 엔터프라이즈 데이터(Dynamics 365, Dataverse, SharePoint 등)의 구체적 사실과 문맥을 기반으로 모델을 바인딩하는 프로세스입니다.",
    tags: ["Grounding", "Data Integrity", "Copilot"]
  },
  {
    id: 2,
    category: "비용 & ROI",
    question: "Model Router (모델 라우터)의 주요 목적은 무엇인가요?",
    answer: "사용자 요청의 복잡도를 분석하여 쉬운 작업은 작고 저렴한 모델(SLM)로, 복잡한 추론이 필요한 작업은 대형 언어 모델(LLM)로 자동 지능형 라우팅하여 비용과 속도를 최적화하는 구성 요소입니다.",
    tags: ["Model Router", "Cost Optimization", "SLM/LLM"]
  },
  {
    id: 3,
    category: "에이전트 설계",
    question: "Copilot Studio에서 'Autonomous Agent(자율 에이전트)'와 'Task Agent(작업 에이전트)'의 차이는?",
    answer: "Task Agent는 사용자의 명시적 요청이나 사전 정의된 스크립트 트리에 따라 작업을 처리하는 반면, Autonomous Agent는 이벤트를 트리거로 삼아 상황을 스스로 추론하고 다단계 액션을 자율적으로 결정하여 실행합니다.",
    tags: ["Autonomous Agent", "Copilot Studio", "Agentic Framework"]
  },
  {
    id: 4,
    category: "전략",
    question: "Microsoft Cloud Adoption Framework (CAF) for Azure의 핵심 역량은?",
    answer: "클라우드 및 AI 채택을 위한 조직적 준비, 비즈니스 전략 정립, 거버넌스, 보안, 관리 워크로드 수명 주기를 체계화하는 글로벌 아키텍처 표준 프레임워크입니다.",
    tags: ["CAF", "Azure", "AI Strategy"]
  },
  {
    id: 5,
    category: "확장성",
    question: "Model Context Protocol (MCP)은 Copilot Studio 확장 시 어떤 역할을 하나요?",
    answer: "에이전트가 외부 도구, 데이터베이스, API 및 가상 리소스에 안전하고 표준화된 방식으로 컨텍스트와 액션을 제공하고 연결할 수 있게 지원하는 오픈 프로토콜 표준입니다.",
    tags: ["MCP", "Extensibility", "Copilot Studio"]
  },
  {
    id: 6,
    category: "책임있는 AI",
    question: "Microsoft의 책임 있는 AI (Responsible AI) 6대 핵심 원칙은?",
    answer: "공정성(Fairness), 신뢰성 및 안전성(Reliability & Safety), 사생활 보호 및 보안(Privacy & Security), 포용성(Inclusiveness), 투명성(Transparency), 책임성(Accountability).",
    tags: ["Responsible AI", "Governance", "Compliance"]
  },
  {
    id: 7,
    category: "ALM",
    question: "AI 기반 솔루션의 ALM (애플리케이션 수명 주기 관리) 핵심 구성 요소는?",
    answer: "에이전트 프롬프트 버전 관리, 커넥터/작업의 개발-테스트-운영(Dev/Test/Prod) 환경 분리 솔루션 패키징, 모델 파인튜닝 데이터의 보안 및 변경 감사를 포함합니다.",
    tags: ["ALM", "Power Platform", "Governance"]
  },
  {
    id: 8,
    category: "모니터링",
    question: "AI 에이전트 관찰 가능성(Observability) 및 튜닝 시 측정해야 하는 핵심 지표는?",
    answer: "응답 지연 시간(Latency), 사용자 만족도/피드백 점수(CSAT/Thumbs up/down), 프롬프트 성공률, 폴백(Fallback) 발생 비율, 토큰 소비량 및 ROI 비용 메트릭.",
    tags: ["Monitoring", "Telemetry", "Performance"]
  }
];
