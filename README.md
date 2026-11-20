# 100 Days of Java · Spring · Spring Boot Microservices

A day-by-day plan to go from core Java to a deployed microservices system in 100 days.
**One topic per day**, each with a **real-time "ShopFast" scenario** (a running story of
building one online-order platform), a **learn** task, and a **build** task.

- 📅 **[SCHEDULE.md](SCHEDULE.md)** — the full dated table (Day 1 = 2026-11-19), links every day.
- 📂 **[days/](days/)** — one document per topic: scenario · learn · build · objectives · notes.
- 📘 **content_guide.pdf** — the detailed content guide (phases, outcomes, how to use).
- 🗓️ **schedule.pdf** — printable schedule.
- 🛠️ **generate_days.py** — the curriculum + generator (change `START_DATE` and re-run to re-date).

## The 7 phases
| Days | Phase |
|---|---|
| 1–15 | Modern Java foundations |
| 16–32 | Spring & Spring Boot fundamentals |
| 33–47 | Persistence & data (JPA) |
| 48–62 | Production-ready single service (testing + security/JWT) |
| 63–83 | Microservices & Spring Cloud (discovery, gateway, config, Feign, resilience, Kafka) |
| 84–95 | Observability, containers, CI/CD, cloud |
| 96–100 | Capstone |

## How to use it
~1.5–2 hrs/day: **learn (45m) → build (45m) → notes + commit (15m)**. Fell behind? Don't reset
the calendar — just continue at the next topic; order matters, dates don't. Use Claude Code as your
pair to explain, review, and debug.

## Regenerate / re-date
```bash
# edit START_DATE in generate_days.py, then:
python3 generate_days.py
```

Reuse your existing repos as scaffolds: `good-morning`, `spring-mysql-crud`, `task-api`,
`spring-microservices-demo`.
