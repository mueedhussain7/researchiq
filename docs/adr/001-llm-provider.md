# ADR 001 — LLM Provider

## Decision
Primary: Anthropic Claude Sonnet 4 (claude-sonnet-4-6)
Cost tasks: Claude Haiku
Fallback: OpenAI GPT-4o-mini

## Reasons
- 200k token context window — handles full research papers
- Structured Pydantic output natively supported
- Lower hallucination rate on factual research tasks
- Competitive cost at our usage patterns

## Consequences
- All LLM calls go through a LLMService abstraction for easy swapping
- Local Ollama documented but deferred to post v1.0
