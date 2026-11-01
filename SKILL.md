---
name: genpark-personal-agent-hrv-autonomic-recovery-readiness-skill
version: "1.0.0"
description: "Zero-dependency Heart Rate Variability (HRV) RMSSD/lnRMSSD autonomic nervous system balance evaluator, 30-day rolling baseline corridor tracker, and daily cognitive/physical capacity allocation engine."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent HRV Autonomic Recovery Readiness Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to track biological readiness, interpret nocturnal and morning heart rate variability (RMSSD), and protect executive cognitive capacity from autonomic exhaustion.

## Agent In-Context Capabilities

- **Natural Log RMSSD (lnRMSSD) Modeling**: Converts raw millisecond variance into normal Gaussian distributions for valid statistical corridor tracking.
- **Personal Baseline Corridors**: Evaluates deviations relative to individual 30-day rolling mean ($\mu$) and standard deviation ($\sigma$).
- **Cognitive & Athletic Budget Allocation**: Dictates whether the agent should schedule multi-hour deep creative architecture sessions or enforce low-friction administrative recovery.

## Tools Summary

1. `evaluate_daily_readiness`: Computes lnRMSSD, z-score, autonomic state, and overall 0-100 readiness index.
2. `allocate_cognitive_physical_capacity`: Recommends deep-work session counts, physical intensity ceilings, and stimulant management.
