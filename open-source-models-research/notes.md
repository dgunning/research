# Open Source Models Research - Focus on Chinese Models

## Research Goal
Deep dive into open source LLM models with particular focus on Chinese models, analyzing capabilities, progress, innovations, and comparison with Western models.

## Investigation Started
2025-11-09

## Research Areas
- Major Chinese open source models (capabilities, benchmarks)
- Progress and timeline of development
- Technical innovations and unique approaches
- Licensing and availability
- Comparison with Western models (Llama, Mistral, etc.)
- Real-world performance and applications

## Research Progress

### Major Chinese Open Source Models Identified

**1. DeepSeek Series**
- DeepSeek-V3: 671B total params, 37B active (MoE)
- DeepSeek-R1: 97.3% MATH-500, 79.8% AIME 2024
- Cost: $5.6M training (vs GPT-4's $100M+)
- Key innovation: Auxiliary-loss-free load balancing
- 88.5 MMLU, 89% HumanEval Python coding

**2. Qwen 3 (Alibaba)**
- Models: 0.5B to 235B parameters (dense + MoE)
- Qwen3-235B: 235B total, 22B active
- Training: 36 trillion tokens
- Context: 262,144 tokens
- Dual-mode: Thinking & Non-thinking
- 119 languages supported (vs 29 in Qwen 2.5)
- Top 10 models on HuggingFace use Qwen base

**3. Kimi K2 (Moonshot AI)**
- 1 trillion params, 32B active
- #1 on LMArena for open source
- 77.5 AIME (vs GPT-4o's 9.3)
- 96.2 MATH 500
- Native tool-thinking fusion
- 47.3 LiveCodeBench

**4. GLM-4.5/4.6 (Zhipu AI / Z.ai)**
- GLM-4.5: 355B total, 32B active
- GLM-4.5-Air: 106B total, 12B active
- Context: 200K input, 128K output
- Tool-calling: 90.6% success rate
- SWE-bench: 64.2%
- Pricing: $0.11/M input tokens

**5. Yi Series (01.AI - Kai-Fu Lee)**
- Yi-34B matches GPT-3.5
- Yi-Large on par with GPT-4 & Claude
- Context: 200K tokens
- Strong needle-in-haystack retrieval
- Multimodal capabilities
- Apache 2.0 license

**6. MiniMax M1**
- Released June 17, 2025
- 456B total, 45.9B active
- First hybrid-attention reasoning model
- Context: 1 million input, 80K output
- Lightning Attention (linear complexity)
- CISPO training algorithm

**7. Baichuan**
- Baichuan 2: 7B and 13B models
- Trained on 2.6T tokens
- Baichuan 4: Domain-specific (law, finance, medical)
- Strong multilingual (101 languages tested)
- Baichuan-Omni: Multi-modal model

### Western Open Source Models (Comparison)

**Meta Llama 4**
- Three models: Scout, Maverick, Behemoth
- Maverick: ELO 1,417 (2nd on LMArena)
- Context: 10 million tokens (longest open-weight)
- 73.4% MMMU (vs GPT-4o's 69.1%)
- 43.4% LiveCodeBench
- Native multimodality
- Sparse MoE architecture

**Mistral AI**
- Mistral Small 3: 24B params
- Facing competition from Chinese models
- Falling behind on benchmarks
- European positioning

### Key Benchmarks & Rankings

**LMArena Global Rankings (2025):**
1. Kimi K2 (China)
2. MiniMax M1 (China)
3. Qwen 3 (China)
4. DeepSeek R1 (China)
...then Google Gemma, Meta Llama

**Market Share:**
- China: 1,509 of 3,755 LLMs (40%) by July 2025
- US still 70%+ market control on platforms
- Performance gap nearly vanished

### Technical Innovations from Chinese Models

**MoE Architecture Dominance:**
- DeepSeek: 671B total, 37B active
- Qwen3: 235B total, 22B active
- Kimi K2: 1T total, 32B active
- MiniMax M1: 456B total, 45.9B active
- GLM-4.5: 355B total, 32B active

**Key Innovations:**
1. Hybrid attention mechanisms (MiniMax Lightning Attention)
2. Ultra-long context (MiniMax 1M, Qwen 262K)
3. Native tool-thinking fusion (Kimi K2)
4. Dual-mode operation (thinking/non-thinking)
5. Cost efficiency (DeepSeek $5.6M vs GPT-4 $100M+)
6. Multi-head Latent Attention (DeepSeek MLA)
7. Auxiliary-loss-free load balancing

**Training Efficiency:**
- DeepSeek-V3: 2.788M H800 GPU hours
- 250 GFLOPS/token (vs LLaMA 2,448 GFLOPS)
- MiniMax M1: 3 weeks on 512 H800 GPUs
- Novel algorithms: CISPO, MuonClip

### Performance Comparisons

**Math & Reasoning:**
- DeepSeek-R1: 97.3% MATH-500
- Kimi K2: 96.2 MATH-500
- Qwen3: 92.3 AIME25

**Coding:**
- DeepSeek-V3: 89% HumanEval
- GLM-4.6: 64.2% SWE-bench
- Kimi K2: 72% SWE-bench
- Qwen3: 74.1 LiveCodeBench

**General Capabilities:**
- DeepSeek-V3: 88.5 MMLU
- Performance parity with GPT-4, Claude

### Licensing & Availability

**Open Source Models:**
- Qwen 3: Apache 2.0
- Yi: Apache 2.0
- GLM-4.5: Apache/MIT
- DeepSeek: Available on HuggingFace
- Baichuan 2: Open source

**Accessibility:**
- All major Chinese models on HuggingFace
- API access available
- Local deployment supported
- Competitive pricing

### Strategic Differences

**Chinese Approach:**
- Cost efficiency focus
- Open access strategy
- Rapid iteration
- MoE architecture preference
- Multilingual emphasis

**Western Approach:**
- Proprietary models (OpenAI, Anthropic)
- Commercial licensing
- Meta: Open weights strategy
- Mistral: European positioning

### Next Research Areas
- Specific benchmark deep-dives
- Timeline of releases
- Technical architecture details
- Real-world adoption metrics
- Geopolitical implications
