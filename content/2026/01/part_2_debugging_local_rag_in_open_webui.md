Title: Building a Local AI Lab for Cybersecurity Research (Part 2)
Date: 2026-02-09 00:00
Category: AI
Tags: ai, environment
Authors: easydevmixin
Summary: Create a local environment to run your own AI - part 2
Status: published


# Debugging Local RAG in Open WebUI: A Hybrid Search Investigation (Part 2)

> **Series note:** This is the second post in a series. The basic installation (Docker, Open WebUI, Ollama, and local models pulled) is already done in [Part 1]({filename}part_1_building_a_local_ai_lab_docker_open_web_ui_ollama.md). This post focuses on *testing and validating retrieval behavior* with a tiny, controlled corpus.

---

## Context of the problem

In my home lab I’m building a local, privacy-preserving AI research assistant for cybersecurity work. With the baseline stack already running (Docker + Open WebUI + Ollama), the next goal was to validate and harden **RAG (Retrieval-Augmented Generation)** behavior in Open WebUI.

To make debugging deterministic, I set up a minimal “needle test” knowledge base:

- Two plain-text files that contain **only** a needle phrase
- Two Markdown files:
    - one with a needle phrase on its own line
    - one with a needle phrase embedded inside a fenced Python code block
- A control probe file: `control.txt` containing exactly:
    - `CONTROL_NEEDLE_ABC123`

The expectation was intentionally simple:

> If retrieval is working, searching for a needle should return the correct filename and the exact matching line, with sources/citations shown in the UI.

**Accuracy check:** We confirmed Open WebUI sometimes returned **“No sources found”** even when the KB was attached in the UI, which indicates the retriever returned **zero chunks** (not merely a ranking issue).

---

## Analysis

The failure pattern wasn’t random. It depended heavily on whether **Hybrid Search** was enabled.

### Symptom A: Hybrid Search ON ⇒ “No sources found”
When Hybrid Search was enabled, Open WebUI frequently returned:

- **“No sources found”** (UI)
- a generic response from the model (because it had no retrieved context)

Container logs confirmed the hybrid retrieval path ran, but returned empty results:

- `Starting hybrid search for 1 queries in 1 collections...`
- `query_doc_with_hybrid_search:result [[]] [[]]`

That signature is very specific: hybrid search executed, but both internal result sets were empty.

### Symptom B: Hybrid Search OFF ⇒ retrieval works
With Hybrid Search disabled, the same environment and corpus produced successful retrieval:

- UI reported sources (e.g., “Retrieved 5 sources”)
- the assistant returned the exact line and filename for the control needle

Logs confirmed the non-hybrid retrieval path returned non-empty results and included metadata like `source`, `file_id`, and embedding configuration.

### What we learned (the point of the exercise)
1. **“No sources found” is a retrieval signal, not a model-quality signal.**
   It means the context pipeline produced nothing. Treat it like “search returned zero results,” not “the model didn’t understand.”

2. **Hybrid mode is an entirely different code path.**
   This wasn’t “the same retrieval but with better ranking.” Hybrid mode invoked different internal retrieval functions and behaved differently than vector-only retrieval.

3. **Correct logging is a prerequisite for effective debugging.**
   Once logging was properly configured, we could confirm hybrid search was:
     - triggered at query time,
     - querying the collection,
     - returning empty arrays,
     - and doing so without an exception.

**Accuracy check:** We ran reproducible A/B tests showing:
- Hybrid ON consistently produced `result [[]] [[]]` and “No sources found.”
- Hybrid OFF consistently retrieved needles with sources.
We also pinned Open WebUI to a known release tag for reproducibility: `ghcr.io/open-webui/open-webui:0.7.2`.

---

## Execution

This section is the playbook I wish I’d had before starting.

### Step 1 — Create a deterministic test corpus
>> Notice that all needles must be different!

Build a tiny KB with:

- `control.txt`:
    - `CONTROL_NEEDLE_ABC123`
- `needle_1.txt`, `needle_2.txt`:
    - a single needle phrase each
- `04_retrieval.md`:
    - needle phrase on a standalone line
- `06_chat.md`:
    - needle phrase inside a fenced code block

Why this helps:

- If retrieval works at all, it should find `control.txt` under almost any configuration.
- Markdown + code blocks validate how parsing/splitting affects extractability.

### Step 2 — Use “sources” as the truth meter
For every query, use a strict prompt:

> “Return the exact line containing CONTROL_NEEDLE_ABC123 and the filename. If not found, say NOT FOUND.”

Treat the UI status as ground truth:
- **“Retrieved N sources”** ⇒ retrieval ran and produced chunks
- **“No sources found”** ⇒ retriever returned nothing

### Step 3 — Tail logs during queries, not only ingestion
Ingestion logs can look healthy (“embeddings generated”, “added to collection”) while query-time retrieval still fails. So log at query time and filter for retrieval keywords:

- watch for `hybrid`, `bm25`, `query_doc_with_hybrid_search`, `query_doc`, `error`, `traceback`

```shell
# inspect what's running
$ docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
# assuming Open WebUI runs as ai-open-webui-1
$ docker logs -f ai-open-webui-1 | egrep -i "hybrid|bm25|exception|traceback|error|query_doc_with_hybrid_search"
```

### Step 4 — Run controlled A/B tests on Hybrid Search
The exact sequence that isolated the issue:

1. Hybrid **OFF** → query `CONTROL_NEEDLE_ABC123` → confirm sources appear
2. Hybrid **ON** → same query → observe “No sources found” + `result [[]] [[]]`
3. Hybrid **ON** with BM25 weight near zero (semantic-only hybrid) → still “No sources found”

That third step matters because it tells you the problem is not “BM25 returned nothing.” The hybrid wrapper path itself is returning empty results.

### Step 5 — Pin Open WebUI to stabilize the investigation
To eliminate “moving target” debugging, pin Open WebUI to a known tag:

- `ghcr.io/open-webui/open-webui:0.7.2`

Verify pinning via Docker:

- `docker inspect ai-open-webui-1 --format '{{.Config.Image}}'`

Note: `/_app/version.json` may show a commit SHA; the Docker image tag is the stable identifier for reproducibility.

**Accuracy check:** We validated retrieval success in non-hybrid mode with “Retrieved sources” responses, validated hybrid failure via UI and logs (`query_doc_with_hybrid_search:result [[]] [[]]`), and confirmed pinning to `0.7.2`.

---

## Conclusion

The biggest takeaway wasn’t “hybrid mode didn’t work.” It was the set of operational lessons that make any RAG system easier to trust.

### 1) Treat RAG like a pipeline, not a feature
When an answer is wrong, the culprit could be:

- ingestion (did the text extract?)
- chunking (did it split sensibly?)
- embedding (did vectors get created?)
- retrieval (did search return candidates?)
- reranking (did it reorder them well?)
- prompting (did the model cite sources and stay grounded?)

When the UI says **“No sources found,”** the diagnosis is straightforward: **retrieval returned nothing**.

### 2) Build reusable control probes
A single-file control needle (`CONTROL_NEEDLE_ABC123`) is a perfect smoke test:

- if it fails, you’re not debugging semantics—you’re debugging plumbing

### 3) A/B toggles are the fastest path to root cause
Comparing Hybrid ON vs OFF using the same KB and the same prompt turned an ambiguous problem (“RAG is flaky”) into a precise one (“hybrid retrieval path returns empty results”).

### 4) Pin versions when debugging behavior
Pinning Open WebUI to a release tag reduced uncertainty and made observations reproducible—essential for:

- documenting behavior accurately,
- reporting issues upstream,
- and building confidence before indexing large, real-world corpora locally.

In the end, the environment remained productive by relying on the parts that behaved deterministically in this lab. But the real win was learning how to **instrument and validate** a local RAG pipeline—because that’s what turns a cool demo into a tool you can trust during real research.
