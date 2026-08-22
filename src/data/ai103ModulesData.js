export const ai103ModulesData = [
  // --- 학습 경로 1: Azure에서 생성 AI 앱을 개발하다 ---
  {
    id: "ai103-m1",
    code: "LP1-MOD-01",
    learningPath: "Azure에서 생성 AI 앱 개발",
    title: "Azure AI 솔루션 개발 계획 및 준비",
    url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/",
    totalTimeMinutes: 60,
    xp: 1000,
    category: "생성 AI 앱 개발",
    description: "Microsoft Azure 개발자가 놀라운 AI 기반 솔루션을 빌드할 수 있는 여러 서비스를 제공합니다. 적절한 계획 및 준비에는 사용할 서비스를 식별하고 개발 팀을 위한 최적의 작업 환경을 만드는 작업이 포함됩니다.",
    units: [
      { id: "ai103-m1-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m1-u2", title: "AI란?", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/2-what-is-ai/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m1-u3", title: "Microsoft Foundry", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/4-azure-ai-foundry/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m1-u4", title: "주조 도구", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/3-azure-ai-services/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m1-u5", title: "개발자 도구 및 SDK", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/5-tools-and-sdks/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m1-u6", title: "책임 있는 인공지능", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/6-responsible-ai/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m1-u7", title: "연습 - AI 개발 프로젝트 준비", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/7-exercise-explore-ai-foundry/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m1-u8", title: "모듈 평가 (Knowledge Check)", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/8-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m1-u9", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/prepare-azure-ai-development/9-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m2",
    code: "LP1-MOD-02",
    learningPath: "Azure에서 생성 AI 앱 개발",
    title: "Microsoft Foundry 모델 선택, 배포 및 평가",
    url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/",
    totalTimeMinutes: 63,
    xp: 900,
    category: "생성 AI 앱 개발",
    description: "벤치마크를 사용하여 모델 카탈로그에서 적절한 모델을 선택하고, 엔드포인트에 배포하고, Microsoft Foundry 포털에서 수동 및 자동화된 접근 방식을 사용하여 성능을 평가하는 방법을 알아보세요.",
    units: [
      { id: "ai103-m2-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/1-introduction/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m2-u2", title: "모델 카탈로그 살펴보기", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/2-explore-model-catalog/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m2-u3", title: "벤치마크를 사용하여 모델 선택", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/3-select-models-benchmarks/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m2-u4", title: "엔드포인트에 모델 배포", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/4-deploy-models/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m2-u5", title: "모델 성능 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/5-evaluate-performance/", timeMinutes: 10, type: "concept" },
      { id: "ai103-m2-u6", title: "연습 - 모델 선택, 배포 및 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/6-exercise/", timeMinutes: 20, type: "exercise" },
      { id: "ai103-m2-u7", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/7-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m2-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/model-catalog-evaluate/8-summary/", timeMinutes: 3, type: "summary" }
    ]
  },
  {
    id: "ai103-m3",
    code: "LP1-MOD-03",
    learningPath: "Azure에서 생성 AI 앱 개발",
    title: "Microsoft Foundry를 사용하여 생성 AI 채팅 앱 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/",
    totalTimeMinutes: 49,
    xp: 900,
    category: "생성 AI 앱 개발",
    description: "Microsoft Foundry를 사용하여 프로젝트 및 응답 API를 사용하여 생성 AI 채팅 애플리케이션을 개발합니다.",
    units: [
      { id: "ai103-m3-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/01-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m3-u2", title: "모델 플레이그라운드를 사용하여 탐색", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/02-chat-playground/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m3-u3", title: "엔드포인트 및 SDK 선택", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/03-microsoft-foundry-sdk/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m3-u4", title: "응답 API를 사용하여 응답 생성", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/04-responses-api/", timeMinutes: 10, type: "concept" },
      { id: "ai103-m3-u5", title: "ChatCompletions API를 사용하여 응답 생성", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/05-openai-api/", timeMinutes: 10, type: "concept" },
      { id: "ai103-m3-u6", title: "연습 - 생성적 AI 채팅 앱 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/06-exercise/", timeMinutes: 10, type: "exercise" },
      { id: "ai103-m3-u7", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/07-knowledge-check/", timeMinutes: 5, type: "quiz" },
      { id: "ai103-m3-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/foundry-sdk/08-summary/", timeMinutes: 3, type: "summary" }
    ]
  },
  {
    id: "ai103-m4",
    code: "LP1-MOD-04",
    learningPath: "Azure에서 생성 AI 앱 개발",
    title: "도구를 사용하는 생성 AI 앱 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/",
    totalTimeMinutes: 60,
    xp: 1000,
    category: "생성 AI 앱 개발",
    description: "도구를 사용하면 모델이 작업을 수행하고 외부 시스템과 상호 작용할 수 있으므로 기본 채팅 상호 작용을 넘어 해당 기능을 확장할 수 있습니다.",
    units: [
      { id: "ai103-m4-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/01-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m4-u2", title: "도구란?", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/02-what-are-tools/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m4-u3", title: "code_interpreter 도구 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/03-code-interpreter/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m4-u4", title: "web_search 도구 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/04-web-search/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m4-u5", title: "file_search 도구 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/05-file-search/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m4-u6", title: "함수 도구 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/06-function/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m4-u7", title: "실습 - 도구를 활용한 생성형 AI 채팅 앱 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/07-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m4-u8", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/08-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m4-u9", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/use-generative-ai-tools/09-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m5",
    code: "LP1-MOD-05",
    learningPath: "Azure에서 생성 AI 앱 개발",
    title: "Microsoft Foundry를 사용하여 생성 AI 모델 성능 최적화",
    url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/",
    totalTimeMinutes: 131,
    xp: 900,
    category: "생성 AI 앱 개발",
    description: "보완 전략을 탐색하여 생성 AI 모델 성능을 최적화합니다. 프롬프트 엔지니어링을 적용하고, RAG로 모델을 접지하고, 일관된 동작을 위해 미세 조정하는 방법 및 이러한 접근 방식을 결합하는 시기를 알아봅니다.",
    units: [
      { id: "ai103-m5-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m5-u2", title: "프롬프트 엔지니어링을 사용하여 모델 출력 최적화", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/2-prompt-engineering/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m5-u3", title: "검색 강화 생성을 사용하여 모델의 기반을 마련하다", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/3-retrieval-augmented-generation/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m5-u4", title: "일관된 동작을 위해 모델 미세 조정", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/4-fine-tune-model/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m5-u5", title: "최적화 전략 비교 및 결합", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/5-compare-combine-strategies/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m5-u6", title: "과제 - 생성 AI 모델 성능 최적화", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/6-exercise/", timeMinutes: 90, type: "exercise" },
      { id: "ai103-m5-u7", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/7-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m5-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/optimize-generative-ai-model-performance/8-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m6",
    code: "LP1-MOD-06",
    learningPath: "Azure에서 생성 AI 앱 개발",
    title: "Microsoft Foundry에서 책임 있는 생성 AI 솔루션 구현",
    url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/",
    totalTimeMinutes: 45,
    xp: 1000,
    category: "생성 AI 앱 개발",
    description: "생성 AI는 놀라운 창의적 솔루션을 가능하게 하지만 유해한 콘텐츠 생성의 위험을 최소화하기 위해 책임감 있게 구현되어야 합니다.",
    units: [
      { id: "ai103-m6-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m6-u2", title: "책임 있는 생성형 AI 솔루션 계획", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/2-plan-responsible-ai/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m6-u3", title: "잠재적인 피해를 파악하다", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/3-identify-harms/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m6-u4", title: "잠재적인 피해 측정", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/4-measure-harms/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m6-u5", title: "잠재적 피해 완화", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/5-mitigate-harms/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m6-u6", title: "생성 AI 솔루션을 책임 있게 관리", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/6-operate-responsibly/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m6-u7", title: "연습 - 유해한 콘텐츠의 출력을 방지하기 위해 가드레일 적용", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/7-exercise-content-filters/", timeMinutes: 20, type: "exercise" },
      { id: "ai103-m6-u8", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/8-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m6-u9", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/responsible-ai-studio/9-summary/", timeMinutes: 1, type: "summary" }
    ]
  },

  // --- 학습 경로 2: Azure AI 에이전트 개발 ---
  {
    id: "ai103-m7",
    code: "LP2-MOD-01",
    learningPath: "Azure AI 에이전트 개발",
    title: "Microsoft Foundry 및 Visual Studio Code를 사용하여 AI 에이전트 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/",
    totalTimeMinutes: 95,
    xp: 1200,
    category: "AI 에이전트 개발",
    description: "Azure portal 및 Visual Studio Code 확장을 통해 Microsoft Foundry 에이전트 서비스를 사용하여 AI 에이전트를 빌드, 테스트 및 배포하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m7-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/1-introduction/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m7-u2", title: "AI 에이전트 및 Microsoft Foundry 에이전트 서비스 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/2-understand-ai-agents-foundry/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m7-u3", title: "개발 방법 살펴보기", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/3-explore-development-approaches/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m7-u4", title: "Microsoft Foundry에서 첫 번째 에이전트 빌드", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/4-build-agent-azure-portal/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m7-u5", title: "에이전트 개발을 위한 Visual Studio Code 설정", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/5-set-up-vs-code/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m7-u6", title: "Visual Studio Code 에이전트 구성 및 관리", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/6-configure-manage-agents/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m7-u7", title: "도구를 사용하여 에이전트 기능 확장", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/7-extend-agent-capabilities/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m7-u8", title: "에이전트 테스트, 배포 및 통합", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/8-test-deploy-integrate/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m7-u9", title: "연습 - AI 에이전트 빌드 및 배포", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/9-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m7-u10", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/10-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m7-u11", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agents-azure-vs-code/11-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m8",
    code: "LP2-MOD-02",
    learningPath: "Azure AI 에이전트 개발",
    title: "에이전트에 사용자 지정 도구 통합",
    url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/",
    totalTimeMinutes: 53,
    xp: 800,
    category: "AI 에이전트 개발",
    description: "기본 제공 도구는 유용하지만 모든 요구 사항을 충족하지 못할 수 있습니다. 이 모듈에서는 에이전트에서 사용할 사용자 지정 도구를 통합하여 에이전트의 기능을 확장하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m8-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m8-u2", title: "사용자 지정 도구를 사용하는 이유", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/2-why-use-custom-tools/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m8-u3", title: "사용자 지정 도구 구현 옵션", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/3-custom-tool-options/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m8-u4", title: "사용자 지정 도구를 통합하는 방법", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/4-how-use-custom-tools/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m8-u5", title: "연습 - 사용자 지정 도구를 사용하여 에이전트 빌드", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/5-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m8-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m8-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-with-custom-tools/7-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m9",
    code: "LP2-MOD-03",
    learningPath: "Azure AI 에이전트 개발",
    title: "AZURE AI 에이전트와 MCP 도구 통합",
    url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/",
    totalTimeMinutes: 48,
    xp: 800,
    category: "AI 에이전트 개발",
    description: "Azure AI 에이전트에 대한 동적 도구 액세스를 활성화합니다. MCP 호스팅 도구를 연결하고 에이전트 워크플로에 원활하게 통합하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m9-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m9-u2", title: "MCP 도구 검색 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/2-understand-mcp-tool-discovery/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m9-u3", title: "MCP 서버 및 클라이언트를 사용하여 에이전트 도구 통합", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/3-mcp-client-server-setup/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m9-u4", title: "MCP 서버에서 Azure AI 에이전트 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/4-use-azure-ai-agents-with-mcp/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m9-u5", title: "연습 - AZURE AI 에이전트에 MCP 도구 연결", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/5-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m9-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m9-u7", title: "Summary", url: "https://learn.microsoft.com/ko-kr/training/modules/connect-agent-to-mcp-tools/7-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m10",
    code: "LP2-MOD-04",
    learningPath: "Azure AI 에이전트 개발",
    title: "Foundry IQ를 사용하여 지식이 강화된 AI 에이전트 빌드",
    url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/",
    totalTimeMinutes: 71,
    xp: 900,
    category: "AI 에이전트 개발",
    description: "Foundry IQ를 사용하여 엔터프라이즈 지식과 AI 에이전트를 연결하는 방법을 알아봅니다. RAG가 AI 에이전트에 대한 지식 문제를 해결하는 방법을 살펴봅니다.",
    units: [
      { id: "ai103-m10-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m10-u2", title: "에이전트에 대한 RAG 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/2-understand-rag/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m10-u3", title: "Foundry IQ 살펴보기", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/3-foundry-iq/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m10-u4", title: "지식 기반의 데이터 원본 구성", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/4-data-requirements/", timeMinutes: 9, type: "concept" },
      { id: "ai103-m10-u5", title: "Foundry IQ를 사용하여 검색 구성", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/5-configure-retrieval/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m10-u6", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m10-u7", title: "연습 - Foundry IQ와 AI 에이전트 통합", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/7-exercise/", timeMinutes: 35, type: "exercise" },
      { id: "ai103-m10-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/introduction-foundry-iq/8-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m11",
    code: "LP2-MOD-05",
    learningPath: "Azure AI 에이전트 개발",
    title: "에이전트를 Microsoft 365와 통합하세요",
    url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/",
    totalTimeMinutes: 74,
    xp: 1000,
    category: "AI 에이전트 개발",
    description: "Microsoft Foundry 에이전트를 Microsoft Teams 및 Microsoft 365 Copilot에 게시하고, Work IQ를 통해 작업장 데이터를 액세스하며, 통합 에이전트를 테스트하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m11-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/1-introduction/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m11-u2", title: "Foundry 에이전트 게시 옵션을 이해하기", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/2-understand-publishing-options/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m11-u3", title: "Foundry 포털에서 Teams에 에이전트 게시", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/3-publish-agent-foundry-portal/", timeMinutes: 10, type: "concept" },
      { id: "ai103-m11-u4", title: "고급 - Microsoft 365 에이전트 도구 키트 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/4-agents-toolkit-advanced/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m11-u5", title: "Work IQ를 사용하여 Microsoft 365 데이터를 액세스하기", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/5-access-m365-data-workiq/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m11-u6", title: "통합 에이전트 테스트 및 반복 과정", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/6-test-iterate-agent/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m11-u7", title: "실습 - Teams에 Foundry 에이전트 게시하기", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/7-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m11-u8", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/8-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m11-u9", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/integrate-foundry-agent-with-m365/9-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m12",
    code: "LP2-MOD-06",
    learningPath: "Azure AI 에이전트 개발",
    title: "Microsoft Foundry를 사용하여 에이전트 기반 워크플로 빌드",
    url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/",
    totalTimeMinutes: 64,
    xp: 1200,
    category: "AI 에이전트 개발",
    description: "워크플로를 사용하면 AI 에이전트 및 기타 구성 요소를 오케스트레이션하여 지능형 애플리케이션을 만들 수 있습니다. Microsoft Foundry를 사용하여 워크플로를 빌드하고 관리하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m12-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m12-u2", title: "워크플로 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/2-understand-workflows/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m12-u3", title: "워크플로 패턴 식별", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/3-identify-workflow-patterns/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m12-u4", title: "Microsoft Foundry에서 워크플로 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/4-create-workflows-microsoft-foundry/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m12-u5", title: "워크플로에 에이전트 추가", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/5-add-agents-to-workflow/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m12-u6", title: "워크플로에서 Power Fx 적용", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/6-apply-power-fx/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m12-u7", title: "Microsoft Foundry에서 워크플로 유지 관리", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/7-maintain-workflows/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m12-u8", title: "코드에서 워크플로 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/8-use-workflows-in-code/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m12-u9", title: "연습 - 에이전트 기반 워크플로 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/9-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m12-u10", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/10-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m12-u11", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/build-agent-workflows-microsoft-foundry/11-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m13",
    code: "LP2-MOD-07",
    learningPath: "Azure AI 에이전트 개발",
    title: "Microsoft Agent Framework를 사용하여 AI 에이전트 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/",
    totalTimeMinutes: 57,
    xp: 800,
    category: "AI 에이전트 개발",
    description: "이 모듈에서는 엔지니어에게 Microsoft Agent Framework를 사용하여 Microsoft Foundry 에이전트 서비스 에이전트 빌드를 시작할 수 있는 기술을 제공합니다.",
    units: [
      { id: "ai103-m13-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m13-u2", title: "Microsoft Agent Framework AI 에이전트 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/2-understand-semantic-kernel-agents/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m13-u3", title: "Microsoft Agent Framework를 사용하여 Azure AI 에이전트 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/3-create-azure-ai-agent/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m13-u4", title: "Azure AI 에이전트에 도구 추가", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/4-add-plugins-to-agent/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m13-u5", title: "연습 - Microsoft Agent Framework SDK를 사용하여 Azure AI 에이전트 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/5-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m13-u6", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m13-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-ai-agent-with-semantic-kernel/7-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m14",
    code: "LP2-MOD-08",
    learningPath: "Azure AI 에이전트 개발",
    title: "Microsoft 에이전트 프레임워크를 사용하여 다중 에이전트 솔루션 오케스트레이션",
    url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/",
    totalTimeMinutes: 70,
    xp: 1200,
    category: "AI 에이전트 개발",
    description: "Microsoft Agent Framework SDK를 사용하여 다중 에이전트 솔루션을 위해 공동 작업할 수 있는 자체 AI 에이전트를 개발하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m14-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m14-u2", title: "Microsoft 에이전트 프레임워크 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/2-understand-agent-framework/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m14-u3", title: "에이전트 오케스트레이션 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/3-understand-agent-orchestration/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m14-u4", title: "동시 오케스트레이션 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/4-use-concurrent-orchestration/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m14-u5", title: "순차 오케스트레이션 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/5-use-sequential-orchestration/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m14-u6", title: "그룹 채팅 조율 활용하기", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/6-use-group-chat-orchestration/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m14-u7", title: "핸드오프 오케스트레이션 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/7-use-handoff-orchestration/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m14-u8", title: "돋보기 오케스트레이션 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/8-use-magentic-orchestration/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m14-u9", title: "연습 - 다중 에이전트 솔루션 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/9-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m14-u10", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/10-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m14-u11", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/orchestrate-semantic-kernel-multi-agent-solution/11-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m15",
    code: "LP2-MOD-09",
    learningPath: "Azure AI 에이전트 개발",
    title: "A2A를 사용하여 Azure AI 에이전트 검색",
    url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/",
    totalTimeMinutes: 53,
    xp: 900,
    category: "AI 에이전트 개발",
    description: "A2A 프로토콜을 구현하여 원격 에이전트에서 에이전트 검색, 직접 통신 및 조정된 작업 실행을 사용하도록 설정하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m15-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m15-u2", title: "A2A 에이전트 정의", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/2-define-a2a-agent/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m15-u3", title: "에이전트 실행기 구현", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/3-implement-agent-executor/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m15-u4", title: "A2A 서버 호스트", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/4-host-a2a-agent-server/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m15-u5", title: "A2A 에이전트에 연결", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/5-connect-to-a2a-agent/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m15-u6", title: "연습 - A2A 프로토콜을 사용하여 원격 Azure AI 에이전트에 연결", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/6-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m15-u7", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/7-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m15-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/discover-agents-with-a2a/8-summary/", timeMinutes: 1, type: "summary" }
    ]
  },

  // --- 학습 경로 3: Azure에서 자연어 솔루션 개발 ---
  {
    id: "ai103-m16",
    code: "LP3-MOD-01",
    learningPath: "자연어 솔루션 개발",
    title: "Foundry 도구에서 Azure 언어로 텍스트 분석",
    url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/",
    totalTimeMinutes: 46,
    xp: 900,
    category: "자연어 처리 (NLP)",
    description: "Foundry 도구의 Azure 언어를 사용하면 텍스트에서 의미 체계 정보를 추출하는 지능형 앱 및 서비스를 만들 수 있습니다.",
    units: [
      { id: "ai103-m16-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m16-u2", title: "Microsoft Foundry 도구의 Azure 언어", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/2-provision-resource/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m16-u3", title: "언어 검색", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/3-detect-language/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m16-u4", title: "엔터티 추출", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/6-extract-entities/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m16-u5", title: "PII(개인 식별 정보) 추출", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/7-extract-personal-information/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m16-u6", title: "연습 - 텍스트 분석", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/8-exercise-analyze-text/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m16-u7", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/9-knowledge-check/", timeMinutes: 2, type: "quiz" },
      { id: "ai103-m16-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-text-ai-language/10-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m17",
    code: "LP3-MOD-02",
    learningPath: "자연어 솔루션 개발",
    title: "Azure Language MCP 서버를 사용하여 텍스트 분석 에이전트 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/",
    totalTimeMinutes: 52,
    xp: 700,
    category: "자연어 처리 (NLP)",
    description: "Azure Language MCP 서버를 사용하여 언어 감지, 엔터티 인식 및 개인 정보 편집과 같은 텍스트 분석 작업을 수행하는 AI 에이전트를 빌드하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m17-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/01-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m17-u2", title: "Azure Language MCP 서버 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/02-understand-language-mcp/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m17-u3", title: "에이전트와 언어 MCP 서버 연결 및 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/03-connect-use-language-mcp/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m17-u4", title: "연습 - 텍스트 분석 에이전트 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/04-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m17-u5", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/05-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m17-u6", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-text-analysis-agent-language-mcp/06-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m18",
    code: "LP3-MOD-03",
    learningPath: "자연어 솔루션 개발",
    title: "음성 지원 생성 AI 애플리케이션 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/",
    totalTimeMinutes: 43,
    xp: 800,
    category: "자연어 처리 (NLP)",
    description: "음성은 단어를 넘어서는 의미를 지니고 있습니다. 음성을 전사하고 합성하는 모델을 사용하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m18-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m18-u2", title: "음성 지원 모델 선택", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/2-deploy-multimodal-model/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m18-u3", title: "음성 대화 내용 기록", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/3-develop-audio-chat-app/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m18-u4", title: "음성 합성", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/3b-develop-speech-app/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m18-u5", title: "연습 - 음성 인식이 가능한 생성 AI 모델 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/4-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m18-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/5-knowledge-check/", timeMinutes: 2, type: "quiz" },
      { id: "ai103-m18-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-audio-apps/6-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m19",
    code: "LP3-MOD-04",
    learningPath: "자연어 솔루션 개발",
    title: "Microsoft Foundry 도구에서 Azure Speech를 사용하여 음성 지원 앱 만들기",
    url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/",
    totalTimeMinutes: 53,
    xp: 1000,
    category: "자연어 처리 (NLP)",
    description: "Microsoft Foundry Tools의 Azure Speech를 사용하면 음성 지원 애플리케이션을 빌드할 수 있습니다. 음성 텍스트 변환 API와 텍스트 음성 변환 API를 집중 학습합니다.",
    units: [
      { id: "ai103-m19-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/1-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m19-u2", title: "Azure Speech를 Foundry 도구에서 사용하기", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/2-create-speech-service/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m19-u3", title: "Speech to Text API 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/3-speech-to-text/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m19-u4", title: "텍스트 음성 변환 API 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/4-text-to-speech/", timeMinutes: 4, type: "concept" },
      { id: "ai103-m19-u5", title: "오디오 형식 및 음성 구성하기", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/5-audio-format-voices/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m19-u6", title: "Speech Synthesis Markup Language 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/6-speech-synthesis-markup/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m19-u7", title: "연습 - 음성 지원 앱 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/7-exercise-speech-app/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m19-u8", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/8-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m19-u9", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/create-speech-enabled-apps/9-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m20",
    code: "LP3-MOD-05",
    learningPath: "자연어 솔루션 개발",
    title: "Azure Speech MCP 서버를 사용하여 음성 에이전트 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/",
    totalTimeMinutes: 52,
    xp: 700,
    category: "자연어 처리 (NLP)",
    description: "Azure Speech MCP 서버를 사용하여 음성 텍스트 변환 및 텍스트 음성 변환 작업을 수행하는 AI 에이전트를 빌드하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m20-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/01-introduction/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m20-u2", title: "Azure Speech MCP 서버 이해", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/02-understand-speech-mcp/", timeMinutes: 7, type: "concept" },
      { id: "ai103-m20-u3", title: "에이전트와 Speech MCP 서버 연결 및 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/03-connect-use-speech-mcp/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m20-u4", title: "연습 - 에이전트에서 Azure Speech 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/04-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m20-u5", title: "지식 점검", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/05-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m20-u6", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-speech-agent-speech-mcp/06-summary/", timeMinutes: 2, type: "summary" }
    ]
  },
  {
    id: "ai103-m21",
    code: "LP3-MOD-06",
    learningPath: "자연어 솔루션 개발",
    title: "Microsoft Foundry에서 Azure Speech Voice Live 에이전트 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/",
    totalTimeMinutes: 52,
    xp: 800,
    category: "자연어 처리 (NLP)",
    description: "Voice Live API 및 SDK를 사용하여 Voice Live 에이전트를 개발하는 방법을 알아봅니다. API 통합, SDK 사용 및 대화형 AI 에이전트 빌드를 포함합니다.",
    units: [
      { id: "ai103-m21-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m21-u2", title: "Azure Voice Live API 살펴보기", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/2-voice-live-api/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m21-u3", title: "Python용 AI Voice Live 클라이언트 라이브러리 살펴보기", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/3-voice-live-sdk/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m21-u4", title: "Voice Live 에이전트 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/3b-voice-live-agent/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m21-u5", title: "연습 - Voice Live 에이전트 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/4-exercise-develop-agent/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m21-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/5-knowledge-check/", timeMinutes: 5, type: "quiz" },
      { id: "ai103-m21-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-voice-live-agent/6-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m22",
    code: "LP3-MOD-07",
    learningPath: "자연어 솔루션 개발",
    title: "Microsoft Foundry 도구를 사용하여 텍스트 및 음성 번역",
    url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/",
    totalTimeMinutes: 48,
    xp: 800,
    category: "자연어 처리 (NLP)",
    description: "Translator 및 Speech 서비스를 사용하면 언어 간에 텍스트와 음성을 번역할 수 있는 지능형 앱과 서비스를 만들 수 있습니다.",
    units: [
      { id: "ai103-m22-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m22-u2", title: "Microsoft Foundry의 번역", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/2-translation-foundry/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m22-u3", title: "텍스트 번역", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/3-azure-translator/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m22-u4", title: "음성 변환", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/4-speech-translation/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m22-u5", title: "연습 - 텍스트 및 음성 번역", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/5-exercise-translate/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m22-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m22-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/translate-text-speech/7-summary/", timeMinutes: 1, type: "summary" }
    ]
  },

  // --- 학습 경로 4: Azure의 시각적 데이터에서 인사이트 추출 ---
  {
    id: "ai103-m23",
    code: "LP4-MOD-01",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "비전 지원 생성형 AI 애플리케이션 개발",
    url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/",
    totalTimeMinutes: 43,
    xp: 700,
    category: "컴퓨터 비전 & 다중 모드",
    description: "그림에는 천 개의 단어가 표시되고, 다모달 생성 AI 모델은 시각적 프롬프트에 응답하도록 이미지를 해석할 수 있습니다. 비전 지원 채팅 앱을 빌드합니다.",
    units: [
      { id: "ai103-m23-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m23-u2", title: "Microsoft Foundry 포털에서 비전 지원 모델 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/2-deploy-multimodal-model/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m23-u3", title: "비전 기반 채팅 앱 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/3-develop-visual-chat-app/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m23-u4", title: "연습 - 비전 지원 채팅 앱 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/4-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m23-u5", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/5-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m23-u6", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/develop-generative-ai-vision-apps/6-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m24",
    code: "LP4-MOD-02",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "AI로 이미지 생성",
    url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/",
    totalTimeMinutes: 33,
    xp: 800,
    category: "컴퓨터 비전 & 다중 모드",
    description: "Microsoft Foundry에서는 이미지 생성 모델을 사용하여 자연어 프롬프트에 따라 원본 이미지를 만들 수 있습니다.",
    units: [
      { id: "ai103-m24-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m24-u2", title: "이미지 생성 모델이란?", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/2-what-is-dall-e/", timeMinutes: 2, type: "concept" },
      { id: "ai103-m24-u3", title: "Microsoft Foundry 포털에서 이미지 생성 모델 살펴보기", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/3-dall-e-in-openai-studio/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m24-u4", title: "이미지 생성 모델을 사용하는 클라이언트 애플리케이션 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/4-dall-e-rest-api/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m24-u5", title: "연습 - AI를 사용하여 이미지 생성", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/5-exercise-use-dall-e/", timeMinutes: 20, type: "exercise" },
      { id: "ai103-m24-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m24-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-images-azure-openai/7-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m25",
    code: "LP4-MOD-03",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "Microsoft Foundry를 사용하여 비디오 생성",
    url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/",
    totalTimeMinutes: 48,
    xp: 800,
    category: "컴퓨터 비전 & 다중 모드",
    description: "Microsoft Foundry에서 Sora 2를 사용하여 텍스트 프롬프트에서 비디오를 생성하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m25-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m25-u2", title: "비디오 생성 모델 배포", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/2-deploy-video-model/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m25-u3", title: "프롬프트에서 비디오 생성", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/3-generate-video-from-prompt/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m25-u4", title: "Python에서 비디오 생성", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/4-generate-video-in-python/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m25-u5", title: "연습 - Microsoft Foundry에서 Sora 2를 사용하여 비디오 생성", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/5-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m25-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/6-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m25-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/generate-video-with-foundry/7-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m26",
    code: "LP4-MOD-04",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "Content Understanding을 사용하여 이미지 분석",
    url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/",
    totalTimeMinutes: 43,
    xp: 700,
    category: "컴퓨터 비전 & 다중 모드",
    description: "Azure Content Understanding을 사용하여 이미지를 분석하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m26-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m26-u2", title: "Content Understanding이란?", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/2-what-is-content-understanding/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m26-u3", title: "Content Understanding을 사용하여 이미지 분석", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/3-analyze-images-with-content-understanding/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m26-u4", title: "연습 - Content Understanding을 사용하여 이미지 분석", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/4-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m26-u5", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/5-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m26-u6", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-images-with-content-understanding/6-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m27",
    code: "LP4-MOD-05",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "Azure Content Understanding을 사용하여 다중 모드 분석 솔루션 만들기",
    url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/",
    totalTimeMinutes: 60,
    xp: 800,
    category: "컴퓨터 비전 & 다중 모드",
    description: "다중 모드 콘텐츠 분석 및 정보 추출에 Azure Content Understanding을 사용합니다.",
    units: [
      { id: "ai103-m27-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/01-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m27-u2", title: "Azure Content Understanding이란?", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/02-content-understanding/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m27-u3", title: "콘텐츠 이해 분석기 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/03-create-analyzer/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m27-u4", title: "Content Understanding API 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/04-use-api/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m27-u5", title: "연습 - 다중 양식의 콘텐츠에서 정보 추출", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/05-exercise/", timeMinutes: 40, type: "exercise" },
      { id: "ai103-m27-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/06-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m27-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai/07-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m28",
    code: "LP4-MOD-06",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "Azure Content Understanding 클라이언트 애플리케이션 만들기",
    url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/",
    totalTimeMinutes: 60,
    xp: 800,
    category: "컴퓨터 비전 & 다중 모드",
    description: "다중 모드 콘텐츠 분석 및 정보 추출을 위해 Azure Content Understanding API를 사용합니다.",
    units: [
      { id: "ai103-m28-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/01-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m28-u2", title: "AI Content Understanding API 사용 준비", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/02-prepare-content-understanding/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m28-u3", title: "콘텐츠 이해 분석기 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/03-create-analyzer/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m28-u4", title: "콘텐츠 분석", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/04-analyze/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m28-u5", title: "연습 - Content Understanding 클라이언트 애플리케이션 개발", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/05-exercise/", timeMinutes: 40, type: "exercise" },
      { id: "ai103-m28-u6", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/06-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m28-u7", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/analyze-content-ai-api/07-summary/", timeMinutes: 1, type: "summary" }
    ]
  },
  {
    id: "ai103-m29",
    code: "LP4-MOD-07",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "Azure Document Intelligence를 사용하여 데이터 추출",
    url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/",
    totalTimeMinutes: 71,
    xp: 900,
    category: "지식 마이닝 & 문서 분석",
    description: "Azure Document Intelligence는 OCR 및 딥 러닝 모델을 사용하여 양식 및 문서에서 텍스트, 키-값 쌍, 테이블 및 구조적 데이터를 추출합니다.",
    units: [
      { id: "ai103-m29-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/1-introduction/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m29-u2", title: "Azure Document Intelligence란?", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/2-what-is-document-intelligence/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m29-u3", title: "Document Intelligence Studio 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/3-use-document-intelligence-studio/", timeMinutes: 6, type: "concept" },
      { id: "ai103-m29-u4", title: "미리 빌드된 모델 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/4-use-prebuilt-models/", timeMinutes: 10, type: "concept" },
      { id: "ai103-m29-u5", title: "사용자 지정 모델 학습 및 사용", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/5-train-custom-models/", timeMinutes: 8, type: "concept" },
      { id: "ai103-m29-u6", title: "연습 - 문서 인텔리전스를 사용하여 문서 분석", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/6-exercise/", timeMinutes: 30, type: "exercise" },
      { id: "ai103-m29-u7", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/7-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m29-u8", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/extract-data-with-document-intelligence/8-summary/", timeMinutes: 3, type: "summary" }
    ]
  },
  {
    id: "ai103-m30",
    code: "LP4-MOD-08",
    learningPath: "시각적 데이터 인사이트 추출",
    title: "Azure AI Search를 사용하여 지식 마이닝 솔루션 만들기",
    url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/",
    totalTimeMinutes: 68,
    xp: 1000,
    category: "지식 마이닝 & 문서 분석",
    description: "Azure AI 검색을 사용하여 데이터에 숨겨진 인사이트를 찾습니다. 지식 마이닝 솔루션을 구현하여 검색 가능하고 심층 분석을 준비하는 방법을 알아봅니다.",
    units: [
      { id: "ai103-m30-u1", title: "소개", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/1-introduction/", timeMinutes: 1, type: "concept" },
      { id: "ai103-m30-u2", title: "Azure AI 검색이란?", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/2-azure-ai-search/", timeMinutes: 3, type: "concept" },
      { id: "ai103-m30-u3", title: "인덱서로 데이터 추출", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/3-index/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m30-u4", title: "AI 기술을 사용하여 추출된 데이터 보강", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/4-ai-skills/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m30-u5", title: "인덱스 검색", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/5-search-index/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m30-u6", title: "지식 저장소에 추출된 정보 유지", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/6-knowledge-store/", timeMinutes: 5, type: "concept" },
      { id: "ai103-m30-u7", title: "연습 - 지식 마이닝 솔루션 만들기", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/7-exercise/", timeMinutes: 40, type: "exercise" },
      { id: "ai103-m30-u8", title: "모듈 평가", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/8-knowledge-check/", timeMinutes: 3, type: "quiz" },
      { id: "ai103-m30-u9", title: "요약", url: "https://learn.microsoft.com/ko-kr/training/modules/ai-knowldge-mining/9-summary/", timeMinutes: 1, type: "summary" }
    ]
  }
];
