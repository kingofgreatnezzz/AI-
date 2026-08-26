# 🧠 RAG System Architecture

```text
                         ┌──────────────────────────────┐
                         │      🧠 RAG SYSTEM           │
                         └──────────────┬───────────────┘
                                        │
                  ┌─────────────────────┴─────────────────────┐
                  │                                           │
                  ▼                                           ▼

       ┌───────────────────────────┐              ┌───────────────────────────┐
       │ 📥 1. INGESTION PIPELINE │              │ 🔎 2. QUERY PIPELINE     │
       │       ✍️ WRITE-HEAVY      │              │       📖 READ-HEAVY       │
       └─────────────┬─────────────┘              └─────────────┬─────────────┘
                     │                                          │
                     ▼                                          ▼
              ┌─────────────┐                            ┌─────────────┐
              │ 📄 Upload  │                            │ ❓ Question │
              │    PDF      │                            │    from User│
              └──────┬──────┘                            └──────┬──────┘
                     │                                          │
                     ▼                                          ▼
              ┌─────────────┐                            ┌─────────────┐
              │ 🚪 API      │                            │ 🧮 Embedding│
              │   Receiver  │                            │    Model    │
              └──────┬──────┘                            └──────┬──────┘
                     │                                          │
                     ▼                                          │
              ┌─────────────┐                                   │
              │ 🛡️ Security │                                   │
              │ & Validation│                                   │
              └──────┬──────┘                                   │
                     │                                          │
                     ▼                                          ▼
              ┌─────────────┐                     ┌────────────────────────┐
              │ 📖 Document │                     │ 🗄️ Vector Database    │
              │    Parser   │                     │ 🔍 Similarity Search   │
              │ PDF → Text  │                     └────────────┬───────────┘
              └──────┬──────┘                                  │
                     │                                          │ 🎯 Top Chunks
                     ▼                                          ▼
              ┌─────────────┐                     ┌────────────────────────┐
              │ ✂️ Chunker  │                     │ 🎯 Reranker           │
              │ Text →      │                     │ Score • Filter • Rank  │
              │ Chunks      │                     └────────────┬───────────┘
              └──────┬──────┘                                  │
                     │                                          ▼
                     ▼                              ┌────────────────────────┐
              ┌─────────────┐                       │ 🧩 Context Assembly    │
              │ 🧮 Embedding│                       │ Question + Top Chunks  │
              │    Model    │                       └────────────┬───────────┘
              │Chunks→Vector│                                    │
              └──────┬──────┘                                    ▼
                     │                              ┌────────────────────────┐
                     │                              │ 🤖 LLM                 │
                     │                              │ Generate Answer        │
                     │                              │ 🚫 Reduce Hallucination│
                     │                              └────────────┬───────────┘
                     │                                           │
                     ▼                                           ▼
              ┌─────────────────┐                    ┌────────────────────────┐
              │ 🗄️ Vector DB   │                    │ 💬 Final Answer        │
              │                 │                    │          ↓             │
              │ 🔢 Vectors     │                    │          👤 User        │
              │ 🏷️ Metadata   │                    └────────────────────────┘
              └─────────────────┘


                    📥 INGESTION                         🔎 QUERY
                         │                                  │
                         ▼                                  ▼
                 "Teach the system"                "Ask the system"
                         │                                  │
                         └──────────────┬───────────────────┘
                                        ▼
                              🗄️ KNOWLEDGE BASE
                              Vector Database
```

### 🧠 The Big Picture

**📥 Ingestion = Build the knowledge**

`📄 PDF → 📖 Text → ✂️ Chunks → 🧮 Embeddings → 🗄️ Vector DB`

**🔎 Query = Use the knowledge**

`❓ Question → 🧮 Embedding → 🔍 Search → 🎯 Rerank → 🧩 Context → 🤖 LLM → 💬 Answer`
