# ADR 003 — Agent Orchestration Framework

## Decision
CrewAI for agent orchestration.
LangChain for individual agent tooling (retrievers, splitters, prompts).

## Reasons
- CrewAI: clean role/goal/task model matching our 7-agent design
- CrewAI: sequential and parallel execution built in
- LangChain: mature Qdrant connector, all embedding models, chunking
- Combined they cover the full stack without custom orchestration code

## Consequences
- Pin CrewAI to a specific version — it evolves quickly
- Bypass LangChain abstractions with direct SDK calls where latency matters
