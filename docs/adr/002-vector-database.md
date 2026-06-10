# ADR 002 — Vector Database

## Decision
Qdrant — self-hosted locally, Qdrant Cloud in production.

## Reasons
- Native payload filtering before ANN search
- Built-in sparse vector support for BM25 hybrid search (Milestone 4)
- Rust core — faster than Chroma/Weaviate at our document scale
- Free self-hosted; managed cloud ~$25/month

## Consequences
- Pinecone rejected: no sparse vector support on free tier
- Weaviate rejected: more complex setup, less Python-native client
