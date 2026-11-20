"""
Generator for the 100-day Java / Spring / Spring Boot microservices plan.

The curriculum is the data below. Running this produces:
  - days/day-001.md ... day-100.md   (one dated document per topic)
  - SCHEDULE.md                      (the full dated table)
  - schedule.html                    (printable schedule -> PDF)

Day 1 is START_DATE. Days are calendar-sequential; if you skip weekends/holidays,
just carry on from where you left off — the topic order is what matters.

Re-run any time (e.g. to change the start date): it overwrites the generated files.
"""

from __future__ import annotations

import html
from datetime import date, timedelta
from pathlib import Path

START_DATE = date(2026, 11, 19)  # Day 1 = today
ROOT = Path(__file__).parent
DAYS_DIR = ROOT / "days"

# (phase, title, focus [learn], build [do]) — exactly 100 entries.
PHASES = [
    ("Phase 1 · Modern Java foundations", 1, 15),
    ("Phase 2 · Spring & Spring Boot fundamentals", 16, 32),
    ("Phase 3 · Persistence & data (JPA)", 33, 47),
    ("Phase 4 · Production-ready single service", 48, 62),
    ("Phase 5 · Microservices & Spring Cloud", 63, 83),
    ("Phase 6 · Observability, containers, CI/CD, cloud", 84, 95),
    ("Phase 7 · Capstone", 96, 100),
]

CURRICULUM = [
    # ---- Phase 1: Modern Java foundations (1-15) ----
    ("Setup & first program", "Install JDK 21, IntelliJ, verify java -version. Project layout, main method, compiling & running.", "Open ~/IdeaProjects/good-morning, retype it from scratch, add a greeting-by-hour method."),
    ("Variables, types, operators, control flow", "Primitives vs objects, var, casting, if/switch (enhanced switch), loops.", "Write a program that classifies numbers (odd/even/prime) using enhanced switch."),
    ("Methods, parameters, varargs, recursion", "Method signatures, overloading, varargs, pass-by-value, recursion basics.", "Implement factorial & Fibonacci both iteratively and recursively."),
    ("OOP I: classes, objects, encapsulation", "Classes, fields, constructors, getters/setters, this, encapsulation.", "Model a BankAccount class with deposit/withdraw and balance protection."),
    ("OOP II: inheritance, polymorphism, interfaces", "extends, super, overriding, abstract classes, interfaces, default methods.", "Create a Shape interface with Circle/Rectangle and a polymorphic area() call."),
    ("Records, enums, sealed classes", "record (immutability), enum with fields/methods, sealed classes/interfaces.", "Rewrite a DTO as a record; model OrderStatus as an enum with behavior."),
    ("Review & exercises — OOP consolidation", "Revisit week 1; refactor earlier code to use records/enums where sensible.", "Build a tiny console 'library' app using classes, inheritance, and enums."),
    ("Collections: List, Set, Map", "ArrayList vs LinkedList, HashSet, HashMap, iteration, equals/hashCode.", "Count word frequencies in a text using a HashMap."),
    ("Generics", "Generic classes & methods, bounded types, wildcards (? extends / super).", "Write a generic Box<T> and a generic max() over a Comparable list."),
    ("Streams API", "stream(), map/filter/reduce/collect, Collectors, method references.", "Given a list of orders, compute totals and group by customer with streams."),
    ("Optional & null-safety", "Optional.of/ofNullable/empty, map/orElse/ifPresent, avoiding NPEs.", "Refactor a lookup method to return Optional and handle the empty case."),
    ("Lambdas & functional interfaces", "Function, Predicate, Consumer, Supplier; writing your own functional interface.", "Pass behavior into a method via a Predicate to filter a list."),
    ("Exceptions", "Checked vs unchecked, try/catch/finally, try-with-resources, custom exceptions.", "Create a custom InsufficientFundsException and throw/catch it in BankAccount."),
    ("Dates/time, String formatting, text blocks", "java.time (LocalDate/Instant/Duration), String.format, text blocks.", "Compute business-day differences and format a receipt with a text block."),
    ("Review & mini-project — plain-Java CLI", "Tie week 1-2 together; clean code & structure.", "Build an expense-tracker CLI (add/list/total) in pure Java. Commit it."),

    # ---- Phase 2: Spring & Spring Boot fundamentals (16-32) ----
    ("What is Spring? IoC & DI", "Inversion of Control, the container, dependency injection, why it matters.", "Diagram how a controller→service→repository gets wired by the container."),
    ("Spring Boot anatomy", "Starters, auto-configuration, @SpringBootApplication, embedded server.", "Generate hello-api on start.spring.io (Web) and run it."),
    ("Beans & stereotypes", "@Component/@Service/@Repository/@Controller, component scanning.", "Create a Service bean injected into a Controller; log on startup."),
    ("@Configuration, @Bean, scopes & lifecycle", "Java config, @Bean factory methods, singleton/prototype, @PostConstruct.", "Define a @Bean for a custom client; prove it's a singleton."),
    ("Externalized config", "application.yml, @Value, @ConfigurationProperties, profiles (dev/prod).", "Bind a typed @ConfigurationProperties block; switch values by profile."),
    ("Build tools: Maven (& Gradle intro)", "pom.xml, dependencies, lifecycle phases, plugins; Gradle contrast.", "Add a dependency, run mvn clean package, inspect the jar."),
    ("Review & scaffold", "Consolidate Boot basics.", "Scaffold the project you'll grow for weeks: a clean multi-layer Boot app."),
    ("REST fundamentals", "HTTP methods, status codes, resources, idempotency, content negotiation.", "Map CRUD operations to the correct HTTP verbs and status codes on paper."),
    ("Controllers & mappings", "@RestController, @GetMapping/@PostMapping, @PathVariable, @RequestParam.", "Add GET /api/items, GET /api/items/{id}, POST /api/items."),
    ("Request/response bodies & JSON", "@RequestBody/@ResponseBody, Jackson, DTOs vs entities.", "Introduce an ItemDto and map it to/from the entity."),
    ("Layered architecture", "Controller→Service→Repository separation, responsibilities of each.", "Refactor the item API into clean layers with an interface for the service."),
    ("Bean Validation", "@Valid, @NotNull/@NotBlank/@Size, validating request bodies.", "Add validation to ItemDto; return 400 on invalid input."),
    ("Global exception handling", "@RestControllerAdvice, @ExceptionHandler, consistent error responses.", "Build a GlobalExceptionHandler returning a structured error body + 404/400."),
    ("REST API design", "Versioning, pagination, filtering, sorting, HATEOAS basics.", "Add /v1 prefix and pagination params to the list endpoint."),
    ("OpenAPI / Swagger", "springdoc-openapi, documenting endpoints, trying them in Swagger UI.", "Add springdoc; open /swagger-ui and exercise your endpoints."),
    ("Review & build — in-memory CRUD API", "Consolidate web layer.", "Finish a full CRUD REST API backed by an in-memory store."),
    ("Logging", "SLF4J + Logback, log levels, structured/JSON logging, correlation.", "Add meaningful logs across layers; configure levels per profile."),

    # ---- Phase 3: Persistence & data (33-47) ----
    ("Relational DB & SQL refresher", "Tables, keys, normalization, SELECT/INSERT/UPDATE/DELETE, joins.", "Design the schema for your items/orders domain; write the DDL."),
    ("JDBC & JdbcTemplate (brief)", "Raw JDBC pain points; JdbcTemplate as the thin abstraction.", "Run a couple of queries with JdbcTemplate to feel the baseline."),
    ("JPA & Hibernate concepts", "ORM, entities, persistence context, identity, dirty checking.", "Explain (in notes) how Hibernate tracks and flushes changes."),
    ("Spring Data JPA", "JpaRepository, derived query methods, CrudRepository.", "Swap your in-memory store for a JpaRepository<Item, Long>."),
    ("Entity mapping", "@Entity, @Id, @GeneratedValue, @Column, @Table, types.", "Map the Item entity precisely; generate schema with H2 first."),
    ("Relationships", "@OneToMany/@ManyToOne/@ManyToMany, fetch (LAZY/EAGER), cascade, mappedBy.", "Add Order→OrderItem (1:M) with proper ownership and cascade."),
    ("JPQL, @Query, projections", "JPQL vs native, @Query, DTO projections, @Param.", "Write a custom @Query returning a DTO projection."),
    ("Pagination & sorting", "Pageable, Page<T>, Sort, slice vs page.", "Return a Page<Item> from the repository to the controller."),
    ("Transactions", "@Transactional, propagation, isolation, rollback rules.", "Make a multi-step service method transactional; prove rollback on error."),
    ("Connection pooling", "HikariCP, pool sizing, datasource properties, leaks.", "Tune Hikari pool settings; observe connections under load."),
    ("Database migrations", "Flyway (or Liquibase), versioned migrations, repeatable scripts.", "Add Flyway; create V1__init.sql; let it manage the schema."),
    ("MySQL/Postgres & profiles", "Real DB setup, JDBC URLs, switching DB by profile.", "Point your service at MySQL (reuse spring-mysql-crud datasource)."),
    ("Caching basics", "Spring Cache abstraction, @Cacheable/@CacheEvict, cache providers.", "Cache an expensive read; evict on update."),
    ("Review & build — CRUD on a real DB", "Consolidate persistence.", "Full CRUD service on MySQL with migrations, pagination, transactions."),
    ("N+1 & query tuning", "The N+1 problem, fetch joins, @EntityGraph, indexes, EXPLAIN.", "Reproduce an N+1, then fix it with a fetch join / entity graph."),

    # ---- Phase 4: Production-ready single service (48-62) ----
    ("JUnit 5 basics", "@Test, assertions, lifecycle (@BeforeEach), parameterized tests.", "Write unit tests for a pure business rule (e.g. pricing/tolerance)."),
    ("Mockito", "Mocking collaborators, @Mock/@InjectMocks, when/thenReturn, verify.", "Test a service with a mocked repository."),
    ("Unit-testing services", "Test behavior not implementation; edge cases; AssertJ.", "Cover the item/order service with meaningful unit tests + edge cases."),
    ("Controller tests", "@WebMvcTest, MockMvc, asserting status + JSON.", "Write MockMvc tests for your controller endpoints."),
    ("Integration tests & Testcontainers", "@SpringBootTest, test slices, Testcontainers for a real DB.", "Spin up a Testcontainers MySQL and run a repository integration test."),
    ("Test coverage & strategy", "Coverage tools, the test pyramid, what to test where.", "Add coverage reporting; identify and fill the biggest gaps."),
    ("Review & build — full test suite", "Consolidate testing.", "Bring the service to a solid unit + web + integration test suite."),
    ("Spring Security fundamentals", "Filter chain, SecurityFilterChain bean, authn vs authz.", "Add Spring Security; lock everything down, then open a public endpoint."),
    ("Password encoding & users", "BCryptPasswordEncoder, UserDetailsService, DB-backed users.", "Store users with hashed passwords; authenticate against the DB."),
    ("JWT structure & stateless auth", "Header.payload.signature, claims, signing, why stateless.", "Decode a sample JWT; map iss/sub/exp claims (reuse your task-api notes)."),
    ("Securing endpoints with JWT", "Resource server, bearer token filter, token validation.", "Protect the API as an OAuth2 resource server validating JWTs."),
    ("Authorization", "Roles/authorities, @PreAuthorize, method security, URL rules.", "Add role-based access: read for USER, write for ADMIN."),
    ("OAuth2 / OIDC concepts", "Authorization code flow, tokens, scopes, identity providers.", "Diagram the auth-code flow; note where Appian/Cognito fit from past work."),
    ("Actuator", "Health, metrics, info, env endpoints; exposing/securing them.", "Enable Actuator; secure /actuator; check health & metrics."),
    ("Review & build — secure the service", "Consolidate security.", "Ship a JWT-secured, role-aware, Actuator-enabled service end-to-end."),

    # ---- Phase 5: Microservices & Spring Cloud (63-83) ----
    ("Monolith vs microservices", "Trade-offs, when to split, distributed-system costs (Fallacies).", "List the forces for/against splitting your domain into services."),
    ("Microservice design", "Bounded contexts, DDD basics, API-first, service ownership.", "Define 2-3 services and their APIs (contracts) for your domain."),
    ("Build service A", "Stand up the first independent service with its own data.", "Create product-service (reuse spring-microservices-demo as a scaffold)."),
    ("Build service B + sync calls", "Second service; service-to-service HTTP with RestClient/WebClient.", "Create order-service that calls product-service over REST."),
    ("Service discovery concepts + Eureka", "Why discovery, client vs server-side, Eureka server.", "Stand up a Eureka server; register nothing yet — just run it."),
    ("Registering with Eureka", "Eureka client, service registration, client-side load balancing.", "Register both services; call by service-id instead of host:port."),
    ("API Gateway", "Spring Cloud Gateway, routes, predicates, filters, cross-cutting.", "Put a gateway in front; route /products and /orders through it."),
    ("Centralized config", "Spring Cloud Config server, Git-backed config, refresh.", "Externalize both services' config to a Config server."),
    ("OpenFeign", "Declarative REST clients, Feign + discovery, error decoding.", "Replace the manual REST call with a Feign client."),
    ("Resilience: circuit breaker", "Resilience4j circuit breaker, states, fallback.", "Wrap the inter-service call in a circuit breaker with a fallback."),
    ("Resilience: retry/rate-limiter/bulkhead/timeout", "The other Resilience4j patterns and when to use each.", "Add retry + timeout; simulate a slow/failing dependency."),
    ("Review & build — wire the mesh", "Consolidate Spring Cloud.", "Two services behind a gateway, via discovery + config + resilience."),
    ("Async messaging intro", "Sync vs async, when to use messaging, Kafka vs RabbitMQ.", "Decide which interactions in your domain should be events."),
    ("Kafka fundamentals", "Brokers, topics, partitions, offsets, producers/consumers, groups.", "Run Kafka locally (Docker); create a topic; produce/consume via CLI."),
    ("Spring Kafka", "KafkaTemplate, @KafkaListener, serializers, config.", "Publish an OrderPlaced event from order-service."),
    ("Event-driven patterns", "Choreography vs orchestration, event design, versioning events.", "Have product-service consume OrderPlaced and react."),
    ("Saga pattern", "Distributed transactions, choreography/orchestration sagas, compensation.", "Design a 2-step saga with a compensating action (on paper + stub)."),
    ("Distributed data", "Database-per-service, CQRS intro, the outbox pattern, eventual consistency.", "Add a simple outbox table + publisher to avoid dual-write issues."),
    ("Idempotency & contracts", "Idempotency keys, correlation IDs, API/event contract testing.", "Make the event consumer idempotent with a processed-id check."),
    ("Distributed tracing", "Micrometer Tracing / OpenTelemetry, trace & span IDs, context propagation.", "Add tracing; follow one request across gateway→A→B in logs."),
    ("Review & build — add events", "Consolidate messaging.", "One synchronous and one event-driven interaction working across services."),

    # ---- Phase 6: Observability, containers, CI/CD, cloud (84-95) ----
    ("Centralized logging", "Log aggregation (ELK / Loki), structured logs, correlation IDs.", "Make all services log JSON with a shared correlation id."),
    ("Metrics with Micrometer + Prometheus", "Micrometer meters, /actuator/prometheus, counters/timers/gauges.", "Expose custom metrics (e.g. orders placed) to Prometheus format."),
    ("Dashboards & the 3 pillars", "Grafana dashboards; logs vs metrics vs traces.", "Stand up Prometheus+Grafana (Docker) and chart a metric."),
    ("Docker fundamentals", "Images vs containers, Dockerfile, layers, registries.", "Write a Dockerfile for one service; build and run it."),
    ("Dockerizing Spring Boot", "Layered jars, Buildpacks (bootBuildImage), image size, JVM flags.", "Build an optimized image; run the service in a container."),
    ("Docker Compose", "Multi-container local stacks, networks, env, depends_on.", "Compose: all services + DB + Kafka + gateway up with one command."),
    ("Kubernetes fundamentals", "Pods, Deployments, Services, kubectl, the control loop.", "Run a local cluster (kind/minikube); deploy one service."),
    ("Deploying to Kubernetes", "Manifests, ConfigMaps, Secrets, env injection.", "Deploy a service with a ConfigMap + Secret; expose it."),
    ("Probes, scaling, rollouts", "liveness/readiness probes, replicas, HPA, rolling updates.", "Add probes; scale replicas; do a rolling update."),
    ("CI/CD with GitHub Actions", "Workflow YAML, build/test on push, build & push image, deploy.", "Write an Actions workflow that builds, tests, and builds an image."),
    ("Cloud deploy concepts", "AWS ECS/EKS, managed DB, secrets/config in the cloud, 12-factor.", "Map your stack to cloud services; note what changes vs local."),
    ("Review & build — containerize everything", "Consolidate ops.", "One-command Compose bring-up of the whole system, with metrics."),

    # ---- Phase 7: Capstone (96-100) ----
    ("Capstone design", "Pick a domain; define services, data, contracts, events, non-functionals.", "Write a 1-page design + architecture diagram for the capstone."),
    ("Capstone build 1 — core services + data", "Apply phases 2-4.", "Build the core services with their databases and REST APIs + tests."),
    ("Capstone build 2 — cloud patterns", "Apply phase 5.", "Add gateway, discovery, config, Feign, and resilience."),
    ("Capstone build 3 — events + observability + Docker", "Apply phases 5-6.", "Add async events, tracing/metrics, and a Docker Compose bring-up."),
    ("Capstone polish & present", "Testing, docs, diagram, deploy, retro.", "Finish README + diagram, run the full stack, record a short demo; plan next steps."),
]

assert len(CURRICULUM) == 100, f"expected 100 topics, got {len(CURRICULUM)}"

# One real-time scenario per topic, told as a running story of building "ShopFast",
# an online order platform — so each abstract topic lands on a concrete system.
SCENARIOS = [
    "A new ShopFast engineer installs the exact JDK/IDE the team uses so their first service builds identically to everyone else's.",
    "Checkout must classify each incoming order as standard / express / bulk by item count before routing it.",
    "Compute a loyalty-points total that compounds across nested referral tiers.",
    "A customer Wallet must never go negative, even if other code tries to set the balance directly.",
    "Card, UPI, and NetBanking all implement a Payment interface so checkout treats every method the same way.",
    "Represent an immutable OrderPlaced event and a fixed, safe set of OrderStatus values.",
    "Model a small catalog (Product, Category) to prove the week's OOP actually fits together.",
    "Deduplicate a shopping cart and tally the quantity per SKU.",
    "A reusable ApiResponse<T> wrapper that every endpoint returns.",
    "From a day's orders, compute total revenue and the top-5 products in a few lines.",
    "findCustomerByEmail returns Optional so 'not found' isn't a null surprise during checkout.",
    "Apply a configurable discount rule that's passed into the pricing method as a function.",
    "Throw InsufficientStockException when a cart exceeds inventory, caught and shown to the shopper.",
    "Compute the delivery-SLA date skipping weekends, and format the invoice date on the receipt.",
    "A back-office CLI to add products and total daily sales before any UI exists.",
    "Swap the real PaymentGateway for a sandbox one in tests without touching checkout code.",
    "Spin up the ShopFast order service in minutes with an embedded server for a stakeholder demo.",
    "An OrderService bean injected into OrderController instead of being new-ed up by hand.",
    "One shared, thread-safe HTTP client bean reused by every outbound call.",
    "Different payment-gateway URLs for dev vs prod via profiles — no code change to promote.",
    "Add the validation starter and package the service into a runnable jar for the demo.",
    "Stand up the clean order-service skeleton the team will grow for months.",
    "Decide that 'place order' is POST /orders returning 201 Created, not a GET.",
    "Expose GET /orders/{id} so the mobile app can fetch a single order.",
    "Return an OrderDto to the app that hides internal fields like cost price.",
    "Keep pricing logic in the service layer so two different controllers can reuse it.",
    "Reject a checkout with quantity 0 or a blank address with a clear 400 and message.",
    "Every error returns the same JSON shape so the mobile app handles failures uniformly.",
    "Paginate order history so a customer with 5,000 orders doesn't crash the app.",
    "Hand the frontend team live, always-current API docs instead of a stale wiki page.",
    "A complete products API the catalog team can start calling today.",
    "Trace a single failed checkout across all layers using correlated log lines.",
    "Design orders / order_items tables so a report can sum revenue per day.",
    "A quick raw-SQL revenue report before the full entity model exists.",
    "Understand why flipping an order's status inside a transaction auto-persists it.",
    "findByCustomerIdAndStatus(...) without hand-writing any SQL.",
    "Map the Order entity precisely so money amounts are stored exactly.",
    "One Order has many OrderItems; deleting the order cleans up its items via cascade.",
    "A lightweight 'order summary' projection that doesn't load the full item list.",
    "Serve order history 25 rows at a time to the app.",
    "Placing an order debits stock and writes the order atomically — both succeed or neither does.",
    "Size the DB connection pool so a flash sale doesn't exhaust connections.",
    "Every environment automatically gets the new 'discount_code' column via a Flyway migration.",
    "Run on H2 locally but MySQL in production from the exact same codebase.",
    "Cache the rarely-changing product catalog so the DB isn't hit on every page view.",
    "The order service now persists to MySQL with migrations managing the schema.",
    "An order-list page firing 200 queries (N+1) is fixed with a single fetch join.",
    "Prove the tiered-discount rule produces the right total for each loyalty tier.",
    "Test the checkout flow without actually calling the real payment gateway.",
    "Cover the stock-reservation logic, including the 'exactly enough stock' boundary.",
    "Assert that POST /orders returns 201 and the expected body, without a running DB.",
    "Run the repository against a real MySQL in a throwaway container in CI.",
    "Find the untested refund path and add tests before it ever ships.",
    "The order service has a green test pyramid before go-live.",
    "Lock down every admin endpoint so only staff can issue refunds.",
    "Store staff passwords hashed with BCrypt — never in plain text.",
    "The mobile app logs in once and sends a token on each request — no server session.",
    "Validate the customer's JWT before showing them their orders.",
    "Customers can view their orders; only ADMIN can cancel someone else's.",
    "Let shoppers 'Sign in with Google' instead of creating yet another password.",
    "Ops watches /actuator/health to auto-restart the service if it turns unhealthy.",
    "ShopFast's order service is now JWT-secured and role-aware end to end.",
    "The single ShopFast app can't scale checkout alone during a sale — time to split it.",
    "Carve ShopFast into product, order, and payment as separate bounded contexts.",
    "Stand up product-service owning the catalog and its own database.",
    "order-service asks product-service for live price and stock at checkout.",
    "Services find each other by name as instances scale up and down automatically.",
    "Add a second order-service instance and watch calls load-balance across both.",
    "One public URL: the gateway routes /products and /orders and checks the token.",
    "Change the sale discount in Git once and every service picks it up.",
    "order-service calls product-service through a clean typed client, not manual HTTP.",
    "If payment-service is down, checkout fails fast with a friendly message instead of hanging.",
    "Retry a flaky stock check once, but time out so the app always stays responsive.",
    "Two services behind a gateway, wired with discovery, config, and resilience.",
    "Sending the order-confirmation email shouldn't block the checkout response.",
    "An OrderPlaced topic that several teams can consume independently.",
    "order-service publishes OrderPlaced the instant an order is saved.",
    "email-service, inventory-service, and analytics each react to OrderPlaced on their own.",
    "If payment fails after stock is reserved, a compensating event releases the stock (saga).",
    "Each service owns its DB; an outbox guarantees the OrderPlaced event is never lost.",
    "A retried OrderPlaced event must not send two confirmation emails (idempotency).",
    "Follow one slow checkout across gateway → order → payment with a single trace id.",
    "Checkout now fires an event and the confirmation email arrives asynchronously.",
    "Search every service's logs in one place to debug a failed order.",
    "Chart orders-per-minute to watch a sale unfold in real time.",
    "A Grafana board shows latency, error rate, and order volume on one screen.",
    "Package order-service into an image that runs identically on any machine.",
    "A slim, fast-starting order-service image pushed to the registry.",
    "A brand-new dev runs the whole ShopFast stack with one 'docker compose up'.",
    "Deploy order-service to Kubernetes so it survives a node dying.",
    "Inject DB credentials via a Secret and the sale discount via a ConfigMap.",
    "Auto-scale checkout to 10 pods during the sale and roll out a fix with zero downtime.",
    "Merging to main auto-builds, tests, and images the service via GitHub Actions.",
    "Map the full stack to AWS: EKS for services, RDS for data, Secrets Manager for creds.",
    "The entire ShopFast system comes up with one command, metrics included.",
    "Design your own platform end to end (e.g. event ticketing or food delivery).",
    "Build its core services, data, and APIs with a solid test suite.",
    "Add gateway, discovery, centralized config, and resilience across the services.",
    "Add async events, tracing/metrics, and a one-command Docker Compose bring-up.",
    "Run the full system, write the README + architecture diagram, and record a short demo.",
]
assert len(SCENARIOS) == 100, f"expected 100 scenarios, got {len(SCENARIOS)}"


def phase_for(day: int) -> str:
    for name, lo, hi in PHASES:
        if lo <= day <= hi:
            return name
    return "?"


def day_file(n: int) -> str:
    title, focus, build = CURRICULUM[n - 1]
    scenario = SCENARIOS[n - 1]
    d = START_DATE + timedelta(days=n - 1)
    phase = phase_for(n)
    return f"""# Day {n:02d} — {title}

**Date:** {d:%Y-%m-%d} ({d:%A}) · **{phase}** · **Topic {n}/100**

## 🏬 Real-time scenario (ShopFast)
{scenario}

## Focus — learn (~45 min)
{focus}

## Build — hands-on (~45 min)
{build}

## Objectives
- [ ] Understand: {title}
- [ ] Complete the build task above
- [ ] Write the 3-line note below
- [ ] Commit today's work to Git

## Notes (fill in — 3 lines)
- **Learned:**
- **Built:**
- **Confusing / revisit:**

## Resources
- Official Spring / Spring Boot reference docs for this topic
- Baeldung tutorials · spring.io guides
- Ask Claude Code to explain, review, or debug today's build

---
_Prev: {"— (start)" if n == 1 else f"[Day {n-1:02d}](day-{n-1:03d}.md)"} · Next: {"— (done!)" if n == 100 else f"[Day {n+1:02d}](day-{n+1:03d}.md)"} · [Schedule](../SCHEDULE.md)_
"""


def write_days() -> None:
    DAYS_DIR.mkdir(parents=True, exist_ok=True)
    for n in range(1, 101):
        (DAYS_DIR / f"day-{n:03d}.md").write_text(day_file(n), encoding="utf-8")


def write_schedule_md() -> None:
    lines = [
        "# 100-Day Schedule — Java · Spring · Spring Boot Microservices",
        "",
        f"**Start:** {START_DATE:%Y-%m-%d} · **End:** {START_DATE + timedelta(days=99):%Y-%m-%d}",
        "",
        "One topic per day. Days are calendar-sequential — if you skip a day, just continue;",
        "the order is what matters. Click a day for its full document.",
        "",
    ]
    last_phase = None
    for n in range(1, 101):
        phase = phase_for(n)
        if phase != last_phase:
            lines += ["", f"## {phase}", "", "| Day | Date | Topic |", "|----|------|-------|"]
            last_phase = phase
        title = CURRICULUM[n - 1][0]
        d = START_DATE + timedelta(days=n - 1)
        lines.append(f"| [{n:02d}](days/day-{n:03d}.md) | {d:%a %Y-%m-%d} | {title} |")
    (ROOT / "SCHEDULE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_schedule_html() -> None:
    rows = []
    last_phase = None
    for n in range(1, 101):
        phase = phase_for(n)
        if phase != last_phase:
            rows.append(f'<tr class="ph"><td colspan="3">{html.escape(phase)}</td></tr>')
            last_phase = phase
        title, _, _ = CURRICULUM[n - 1]
        d = START_DATE + timedelta(days=n - 1)
        rows.append(
            f"<tr><td class='d'>{n:02d}</td><td class='dt'>{d:%a %d %b %Y}</td>"
            f"<td>{html.escape(title)}</td></tr>"
        )
    body = "\n".join(rows)
    doc = f"""<title>100-Day Schedule — Java Spring Microservices</title>
<style>
 @page {{ margin: 14mm 14mm 16mm; }}
 :root{{--ink:#15202b;--muted:#5a6473;--line:#dde2e8;--accent:#148f5b;--accent2:#0c6b43;--soft:#e7f4ee;}}
 *{{box-sizing:border-box;}}
 body{{font-family:"Charter","Georgia",serif;color:var(--ink);font-size:9.6pt;line-height:1.4;margin:0;}}
 h1{{font-size:20pt;margin:0 0 2px;letter-spacing:-0.3px;}}
 .sub{{color:var(--muted);margin:0 0 10px;font-size:9.6pt;}}
 .eyebrow{{text-transform:uppercase;letter-spacing:2px;font-size:7.5pt;color:var(--accent2);
          font-family:"Helvetica Neue",sans-serif;}}
 table{{width:100%;border-collapse:collapse;}}
 th{{background:var(--accent2);color:#fff;text-align:left;padding:4px 7px;font-size:8pt;
    font-family:"Helvetica Neue",sans-serif;}}
 td{{border-bottom:1px solid var(--line);padding:3px 7px;vertical-align:top;}}
 td.d{{font-family:"SF Mono","Menlo",monospace;color:var(--accent2);width:30px;font-weight:700;}}
 td.dt{{color:var(--muted);white-space:nowrap;width:95px;font-size:9pt;}}
 tr.ph td{{background:var(--soft);color:var(--accent2);font-weight:700;
          font-family:"Helvetica Neue",sans-serif;font-size:9pt;padding:6px 7px;letter-spacing:.3px;}}
</style>
<p class="eyebrow">Java · Spring · Spring Boot · Microservices</p>
<h1>100-Day Learning Schedule</h1>
<p class="sub">Start {START_DATE:%d %b %Y} → End {START_DATE + timedelta(days=99):%d %b %Y} ·
one topic per day · full per-day documents in <code>days/</code> on GitHub.</p>
<table>
<tr><th>Day</th><th>Date</th><th>Topic</th></tr>
{body}
</table>
"""
    (ROOT / "schedule.html").write_text(doc, encoding="utf-8")


if __name__ == "__main__":
    write_days()
    write_schedule_md()
    write_schedule_html()
    print(f"Generated 100 day files, SCHEDULE.md, schedule.html (start {START_DATE}).")
