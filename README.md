# 🍽️ Multimodal Restaurant Recommendation AI

> An end-to-end **GenAI and MLOps project** that transforms unstructured restaurant and food data into a structured multimodal knowledge base for intelligent restaurant recommendations.

[![CI](https://github.com/milad15A/multimodal-recommendation-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/milad15A/multimodal-recommendation-ai/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-Package%20Manager-DE5FE9)](https://docs.astral.sh/uv/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Kubeflow](https://img.shields.io/badge/Kubeflow-MLOps-0072CE?logo=kubeflow&logoColor=white)](https://www.kubeflow.org/)

> 🚧 **Status: Work in Progress**

---

## 📖 About

Restaurant recommendation systems often need to work with information that comes from many different sources and formats:

- 📝 Unstructured restaurant descriptions
- 🍲 Recipe metadata
- ⭐ User reviews
- 🖼️ Food images

These sources cannot always be used directly by a recommendation system.

This project builds a **multimodal GenAI pipeline** that extracts useful information from these sources, converts unstructured information into structured data, enriches it with visual information, and prepares the resulting knowledge base for a future recommendation engine.

### Core idea

```text
Unstructured & Multimodal Data
              │
              ▼
       ┌──────────────┐
       │    GenAI     │
       │  Processing  │
       └──────┬───────┘
              │
              ▼
      Structured Knowledge
           Base
              │
              ▼
     Recommendation System
