# HireMe

HireMe is an AI-powered career intelligence and hiring platform designed to connect candidates, companies, mentors, and career workflows in one system.

The product is being developed in phases. The initial scope focuses on students, internships, and entry-level hiring, with later phases extending the platform to professionals and broader career growth workflows.

> **Development status:** Early development. The repository currently contains the platform foundation and partial authentication implementation. Many product capabilities described in the PRD are still planned or scaffolded and should not be considered production-ready.

## What HireMe is intended to provide

HireMe is designed around a single career profile that can power:

- Candidate onboarding and career profiles
- Job discovery and explainable job matching
- Resume creation, versioning, ATS analysis, and High-Bar analysis
- Job-specific resume tailoring
- Application tracking and recruiter workflows
- Career AI, skill-gap analysis, readiness, and roadmaps
- Mentorship and learning workflows
- Private document storage through TalentVault
- Subscriptions, entitlements, notifications, and administration

The product is intentionally designed around explainable, user-controlled AI rather than fully autonomous decision making.

## Current scope

The current repository is focused on the platform foundation. The main areas already represented in the codebase are:

- FastAPI backend structure under `api/`
- Authentication models, schemas, services, and routes
- JWT access/refresh token handling
- Password hashing with bcrypt
- Email verification flow scaffolding
- Next.js frontend under `web/`
- Worker package structure under `worker/`
- Docker-based infrastructure scaffolding
- Product requirements and engineering planning under `docs/`

Most higher-level workflows remain under active implementation.

## Architecture

The target architecture is organized into separate application layers:

```text
                    ┌─────────────────────┐
                    │      Web App        │
                    │ Next.js + Tailwind  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      API Layer      │
                    │ FastAPI + SQLAlchemy│
                    └───────┬───────┬─────┘
                            │       │
                  ┌─────────┘       └─────────┐
                  ▼                           ▼
        ┌─────────────────┐         ┌─────────────────┐
        │ Relational DB   │         │ Async / Worker  │
        │                 │         │ Processing      │
        └─────────────────┘         └────────┬────────┘
                                             │
                                   ┌─────────┴─────────┐
                                   ▼                   ▼
                              AI / LLM            Storage / Email
```

The architecture is intentionally modular so that product features can evolve without turning the backend into a single monolithic feature layer.

## Repository structure

```text
hire_me/
├── api/                 # FastAPI backend
│   ├── app/
│   │   ├── core/       # configuration, DB, security, dependencies
│   │   ├── features/   # feature-oriented backend modules
│   │   ├── integrations/# external service integrations
│   │   └── shared/     # shared backend utilities
│   ├── scripts/
│   └── tests/
├── web/                 # Next.js frontend
├── worker/              # Background/async processing
├── docs/                # PRD, decisions, and engineering plan
├── docker-compose.yaml
├── .env.example
└── README.md
```

## Technology stack

### Core application stack

- Frontend: Next.js, React, TypeScript, Tailwind CSS
- Backend: Python, FastAPI, SQLAlchemy
- Database: PostgreSQL 16 with SQLAlchemy
- Infrastructure: Docker and Docker Compose
- Authentication: JWT with bcrypt password hashing

### Planned integrations

The current engineering decisions document selects:

- LLM: Ollama with `gemma4:e2b-mlx`
- Object storage: AWS S3
- Email: Resend
- Resume templates: two selected templates

These integrations are decisions for the product roadmap; not every selected integration is implemented yet.

## Development setup

The repository is still in the infrastructure/bootstrap phase. The local environment is therefore not yet a stable one-command developer experience.

The intended workflow is:

```bash
git clone https://github.com/iamdainwi/hire_me.git
cd hire_me
```

Create the local environment files from the committed examples:

```bash
cp .env.example .env
cp api/.env.example api/.env
```

The project uses Docker Compose for local infrastructure:

```bash
docker compose up --build
```

The local database is PostgreSQL 16 and is provided by Docker Compose. PostgreSQL is the project's intended database; any remaining MySQL references in older planning/configuration files are stale and should be removed as part of repository cleanup.

## API

The FastAPI application is mounted under the `/api/v1` prefix.

The authentication domain currently exposes endpoints including:

```text
POST  /api/v1/auth/register
POST  /api/v1/auth/login
POST  /api/v1/auth/refresh
POST  /api/v1/auth/verify-email
POST  /api/v1/auth/resend-verification
GET   /api/v1/auth/me
PATCH /api/v1/auth/me
POST  /api/v1/auth/change-password
```

API contracts should be treated as evolving until the corresponding product phase is completed.

## Configuration

Do not commit real credentials or secrets.

The repository already provides example environment files. Important API configuration includes:

- `DATABASE_URL`
- `SECRET_KEY`
- `JWT_ALGORITHM`
- `ACCESS_TTL_MIN`
- `REFRESH_TTL_DAYS`
- `VERIFY_TTL_HOURS`
- `FRONTEND_URL`

Use the example files as the source of truth for variable names and keep actual values local.

## Documentation

The project documentation is intentionally split from the root README.

- [Product Requirements Document](./docs/HIRE_ME_PRD.md) — product definition, architecture, functional requirements, API baseline, AI logic, security, and delivery requirements.
- [30-Day Build Plan](./docs/TASK.md) — current implementation plan, phased scope, cuts, milestones, and definition of done.
- [Engineering Decisions](./docs/DECISIONS.md) — selected infrastructure and product decisions.

The README is an orientation document; detailed product and engineering decisions belong in `docs/`.

## Roadmap

The implementation plan is organized into these stages:

1. Foundation — setup, identity, RBAC, and profile
2. Companies, jobs, and applications
3. Resume intelligence
4. Career intelligence and matching
5. Notifications, TalentVault, mentorship, and learning
6. Entitlements, billing, and administration
7. Security hardening, testing, and deployment

The detailed plan and scope cuts are maintained in [docs/TASK.md](./docs/TASK.md).

## Contributing

This project is currently maintained as an active development repository. Before changing a feature, review:

1. The relevant requirements in [docs/HIRE_ME_PRD.md](./docs/HIRE_ME_PRD.md)
2. The implementation plan in [docs/TASK.md](./docs/TASK.md)
3. Existing decisions in [docs/DECISIONS.md](./docs/DECISIONS.md)

When a decision changes the intended architecture or product behavior, update the relevant documentation alongside the code.

## Project status

HireMe is not yet a production application.

Current state:

| Area | Status |
| --- | --- |
| Repository structure | In progress |
| FastAPI foundation | In progress |
| Authentication | Partially implemented |
| Frontend | Initial Next.js scaffold |
| Worker | Initial scaffold |
| Jobs and applications | Planned / not implemented |
| Resume intelligence | Planned |
| Career AI | Planned |
| Mentorship and learning | Planned |
| Billing | Planned |
| CI/CD | Not yet implemented |
| Production deployment | Not yet finalized |

## Contact

Primary maintainer: [@iamdainwi](https://github.com/iamdainwi)

For project questions, implementation discussion, or issues, use the repository's [GitHub Issues](https://github.com/iamdainwi/hire_me/issues).

## License

A project license has not been defined yet.
