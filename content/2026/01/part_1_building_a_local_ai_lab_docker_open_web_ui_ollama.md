Title: Building a Local AI Lab for Cybersecurity Research (Part 1)
Date: 2026-01-25 00:00
Category: AI
Tags: ai, environment
Authors: easydevmixin
Summary: Create a local environment to run your own AI - part 1
Status: published

# Building a Local AI Lab for Cybersecurity Research (Part 1)

## Docker + Open WebUI + Ollama + Local Models

> **Series note:** This is Part 1. The goal is to stand up a fully local AI environment that keeps prompts and documents inside your home environment. **Part 2** covers how I validated RAG behavior with a deterministic “needle” test corpus and what I learned while debugging retrieval.

---

## Context of the problem

I wanted a locally hosted AI assistant for cybersecurity work (application security, incident response, digital forensics, and penetration testing) that:

- runs on my own hardware (no required external API calls)
- keeps my data local
- helps with research and drafting (and later, document-grounded Q&A)
- supports hands-on work for PoCs (within client RoE)

Hardware context:

- **Mac Studio M2** with **32 GB RAM**
- **Alienware PC** (Intel i9) with **64 GB RAM**

This post covers the baseline install and verification:

- Docker (for repeatable services)
- Ollama (local model runtime)
- Open WebUI (local chat UI)
- pulling a small set of local models

**Accuracy check:** This post assumes you’re using the system locally (no internet exposure, no remote access requirement). RAG/Knowledge Base debugging is intentionally left for Part 2.

---

## Analysis

Before touching installation steps, I made three decisions that reduced friction later:

1. **Separate the UI from the inference runtime**

- **Ollama** runs the local models.
- **Open WebUI** provides the chat UI and connects to Ollama.

This separation makes upgrades and troubleshooting easier because you can change models (or even the model runtime) without rebuilding the UI layer.

2. **Prefer containers for “services,” not for everything**

- Open WebUI is an ideal container workload: easy lifecycle, easy version pinning.
- Ollama is simplest installed on the host OS for best local integration.

3. **Start with a minimal model set** Pull only what you need to validate end-to-end:

- a general-purpose model (research + writing)
- a coding-oriented model (PoC scaffolding)
- an embeddings model (to enable RAG later)

**Accuracy check:** At this stage we’re validating that: (a) Ollama runs locally, (b) Open WebUI connects to Ollama, and (c) models load and respond. We’re not validating hybrid search, reranking, or vector DB backends yet.

---

## Execution

### Step 0 — Prerequisites

- Sufficient disk space (models can be multiple GB)
- Admin rights to install Docker Desktop / Ollama
- A terminal (Terminal/iTerm2, PowerShell, etc.)

---

### Step 1 — Install Docker

#### macOS (Mac Studio)

1. Install **Docker Desktop**.
2. Verify:

```bash
docker version
docker compose version
```

#### Windows (Alienware) or Linux

- Install Docker Desktop (Windows) or Docker Engine + Compose (Linux).
- Verify:

```bash
docker version
docker compose version
```

**Verification checkpoint:** `docker compose version` returns a version string.

---

### Step 2 — Install Ollama

Install Ollama on the host OS.

Verify:

```bash
ollama --version
```

**Verification checkpoint:** `ollama` responds with a version.

---

### Step 3 — Pull a small starter set of models

Pick one general model, one coder model, and one embeddings model. Example set:

```bash
ollama pull qwen2.5:7b
ollama pull qwen2.5-coder:7b
ollama pull nomic-embed-text:v1.5
```

Run a quick inference test:

```bash
ollama run qwen2.5:7b "Give me a 5-bullet checklist for analyzing a suspicious OAuth redirect flow."
```

**Verification checkpoint:** You get a coherent response and no runtime errors.

---

### Step 4 — Run Open WebUI via Docker Compose

Create a working folder (example):

```bash
mkdir -p ~/projects/docker/ai
cd ~/projects/docker/ai
```

Create `docker-compose.yml`:

```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:0.7.2
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
    volumes:
      - openwebui_data:/app/backend/data
    restart: unless-stopped

volumes:
  openwebui_data:
```

Start it:

```bash
docker compose up -d
```

Open the UI:

- `http://localhost:3000`

In Open WebUI:

- select an Ollama model (e.g., `qwen2.5:7b`)
- send a test message

**Verification checkpoint:** The UI responds and you can chat with an Ollama model.

---

### Step 5 — Optional: prepare for RAG later (without enabling it yet)

You can add a vector DB later. If you want to create the container now (to keep your lab “RAG-ready”), you can add Qdrant to the compose file:

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_storage:/qdrant/storage
    restart: unless-stopped

  open-webui:
    image: ghcr.io/open-webui/open-webui:0.7.2
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
    volumes:
      - openwebui_data:/app/backend/data
    restart: unless-stopped

volumes:
  qdrant_storage:
  openwebui_data:
```

Bring services up:

```bash
docker compose up -d
```

**Verification checkpoint (optional):**

```bash
curl -s http://localhost:6333/healthz
```

---

## Conclusion

At the end of Part 1, the environment is usable and stable:

- ✅ Docker is running and your services are reproducible via Compose
- ✅ Ollama runs locally and serves models
- ✅ Open WebUI runs locally and talks to Ollama
- ✅ A small starter model set is pulled and tested
- ✅ (Optional) a vector DB container is ready for later experimentation

The key lesson is that a productive home AI setup is easiest to maintain when you keep things modular:

- **Model runtime** (Ollama)
- **User interface** (Open WebUI)
- (Later) **retrieval pipeline** (chunking, embeddings, vector DB, reranking)

That modularity pays off in Part 2, where troubleshooting becomes a matter of isolating which stage in the RAG pipeline is responsible.

---

### Next: Part 2

[Part 2]({filename}part_2_debugging_local_rag_in_open_webui.md) goes deep on retrieval validation with a deterministic “needle” corpus:

- interpreting “No sources found” as a pipeline signal
- A/B testing retrieval toggles to isolate failure modes
- why pinning versions matters when debugging behavior

