# Content Production Agency Capacity & Sprint Velocity Planner

> Stop burning out your creative team. Accurately calculate design and video capacity, revision buffers, and agency sprint velocity.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a professional content agency capacity planning system: 1) Mathematical resource model calculating realistic monthly creative throughput per FTE (designer, video editor, copywriter) with built-in revision buffers, 2) Client revision governance framework (limiting free revision rounds), 3) Python sprint calculator (`calc_capacity.py`), 4) Markdown onboarding guide for account managers.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `examples/boutique-agency-30-clients.md`
- `LICENSE`
- `models/agency-capacity-calculator.xlsx`
- `playbooks/burnout-prevention-rules.md`
- `policies/client-revision-governance.md`
- `README.md`
- `src/calc_capacity.py`
- `templates/client-retainer-tier-matrix.md`
- `templates/sprint-planning-sheet.md`
- `tests/test_capacity.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/calc_capacity.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "content",
  "repository": "content-agency-capacity-planner",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Billable Utilization Caps:** Lets teams model their own billable-capacity target alongside leave, admin work, and workload constraints.
- **Revision Buffer Scheduling:** Factors standard 2-round revision cycles into production timelines before locking client delivery milestones.
- **Skill-Based Task Allocation:** Maps high-complexity tasks (creative strategy, motion graphics) against specialist availability to avoid bottlenecking.

---

## 📚 Primary Documentation & Verifiable References

- [Project Management Institute (PMI): Resource Management & Capacity Planning](https://www.pmi.org/) - Standard methodology for estimating resource availability and project scheduling.
- [AIGA Design Agency Business Metrics & Billing Models](https://www.aiga.org/) - Industry benchmarks for creative utilization rates, overhead multipliers, and project margins.
- [Harvard Business Review: Managing Professional Service Firm Capacity](https://hbr.org/) - Managerial strategies for balancing creative team workloads and revenue targets.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
