# HireMe — 30-Day Build Plan (task.md)

Source: `HireMe_PRD_Master_v2.md`

## Reality check

The PRD has 14 Phase 1 epics + a full Phase 2. That is a multi-person, multi-month scope. One person cannot ship all of it in 30 days. This plan builds the **core loop only**:

> onboarding → profile → resume (builder + ATS + High-Bar) → job search → apply → company pipeline → notifications

Everything else is stubbed, simplified, or cut. Cuts are listed below. Don't argue with them mid-month.

## Assumptions (change if wrong)

- Solo developer, ~6–8 focused hrs/day, 30 days, no buffer days. Cuts are the buffer.
- Stack: **Next.js + Tailwind** (frontend), **FastAPI** (backend, structured: `features/<name>/{router,service,models,schemas}`), **MySQL** (PRD SOP baseline), Redis + RQ/Celery-lite worker for async, S3-compatible storage (Cloudflare R2 / Supabase Storage), JWT + bcrypt.
- One LLM provider (Claude or Gemini API). No multi-provider abstraction.
- Jobs come from **company postings only**. No external job APIs, no scraping.
- Payments: Razorpay **test mode** only. INR only.

## Hard cuts (not in this 30 days)

| Cut                                        | PRD ref          | Why                                               |
| ------------------------------------------ | ---------------- | ------------------------------------------------- |
| All of Phase 2                             | §6               | Extension of a product that doesn't exist yet     |
| External auto-apply / assisted apply       | FR-APP-05, EP-05 | Legal + brittle; PRD itself lists it as undecided |
| External job data sources                  | §24              | Undecided + legal risk                            |
| AI Interview                               | EP-07            | Not in core loop                                  |
| Learning assessments + certifications      | FR-LRN-02        | Static course list only                           |
| Mentor payouts, reviews, no-show policy    | EP-09            | Basic booking only                                |
| USD billing, annual plans, invoices PDF    | FR-SUB-01/04     | INR monthly test-mode only                        |
| Data export/deletion workflow              | §13              | Document it, don't build it                       |
| Projects Studio, professional salary intel | FR-AI-05         | Cut                                               |
| Full analytics pipeline                    | §16              | Log events to a table; no dashboard               |

## If you fall behind, cut in this order

1. Mentorship booking UI polish → keep API only
2. Learning module → static page
3. Roadmap generation
4. Copilot chat
5. Billing → hardcode plan flag in DB
6. Never cut: auth, RBAC, resume, ATS, jobs, applications, company pipeline

---

## Phase 0 — Setup & Decisions (Day 1–2)

**Goal:** repo runs locally, DB migrates, CI green, nothing blocked by undecided items.

### 0.1 Decisions (lock on Day 1, write in `DECISIONS.md`)

- [x] LLM provider + model
- [x] Storage provider
- [x] Plan tiers + limits (e.g., Free: 1 resume, 3 analyses/mo; Pro: 5 resumes, unlimited analyses)
- [x] Email provider (Resend / SMTP)
- [x] Resume templates: pick **2** only

### 0.2 Repo & infra

- [x] Monorepo: `/web`, `/api`, `/worker`, `/docs`
- [x] FastAPI skeleton with structured dirs, `/api/v1` prefix, health check
- [x] Next.js app, Tailwind, layout shell, role-based route groups
- [ ] MySQL + Alembic migrations, Docker Compose (db, redis, api, web)
- [x] `.env` handling, no secrets committed
- [ ] GitHub Actions: lint + test + build
- [ ] Deploy target decided (Vercel web + Railway/Render api)

### 0.3 Data model v1

- [ ] Tables: `users, student_profiles, companies, company_users, jobs, resumes, resume_analyses, applications, application_events, documents, document_grants, mentor_profiles, mentor_sessions, courses, subscriptions, entitlements, usage_counters, notifications, audit_logs, product_events`
- [ ] Indexes: job search fields, application (candidate, job) unique, mentor slot unique
- [ ] Seed script: admin, 2 companies, 20 jobs, 5 mentors, 6 courses

**Exit:** `docker compose up` gives running web + api + db; migration + seed work.

---

## Phase 1 — Foundation: Identity, RBAC, Profile (Day 3–6)

**Epics:** EP-01, EP-02 · **PRD:** FR-ID-01..05, FR-PRO-01..04

### 1.1 Auth (Day 3)

- [ ] Register (email + role), bcrypt hash — FR-ID-01
- [ ] Login, JWT access + refresh, expiry handling — FR-ID-05
- [ ] Email verification token flow — FR-ID-02
- [ ] Rate limiting on auth routes
- [ ] Consent capture (terms, privacy, AI processing) stored with timestamp — FR-ID-03

### 1.2 RBAC (Day 4)

- [ ] Roles: student, company, mentor, admin
- [ ] Auth dependency + role guard middleware
- [ ] Frontend route guards per role
- [ ] Audit log helper (`audit(actor, action, object)`) used from here on

### 1.3 Student profile & onboarding (Day 5–6)

- [ ] Onboarding wizard: education → target role → skills → preferences — FR-ID-04
- [ ] `GET/PATCH /profile` — FR-PRO-03
- [ ] Structured skills with proficiency + evidence link — FR-PRO-02, FR-PRO-04
- [ ] Projects + certifications CRUD
- [ ] Completeness score (weighted required/optional fields) — FR-PRO-01
- [ ] Student dashboard shell

**Exit:** a student can register, verify, onboard, and see a completeness score. Unauthorised role access returns 403 (tested).

---

## Phase 2 — Companies, Jobs, Applications (Day 7–11)

**Epics:** EP-13, EP-03 (basic), EP-05 · **PRD:** FR-JOB-01,02,04,05, FR-APP-01..04, §8.1

### 2.1 Company (Day 7)

- [ ] Company registration + profile
- [ ] Verification status (pending/approved/rejected)
- [ ] Block publishing until approved (§19)

### 2.2 Jobs (Day 7–8)

- [ ] Job CRUD (company) with required vs preferred skills split
- [ ] Publish / close / draft states
- [ ] Keyword search + filters: role, skill, location, mode, stipend, experience, date — FR-JOB-01/02
- [ ] Job details page — FR-JOB-05 (match explanation slot left empty until Phase 4)
- [ ] Save/unsave jobs — FR-JOB-04
- [ ] `JOB_PUBLISHED` event stub (no matching yet)

### 2.3 Applications (Day 9–10)

- [ ] `POST /applications`: eligibility check (active job, no duplicate) — FR-APP-01
- [ ] Resume selection step (uses placeholder until Phase 3) — FR-APP-02
- [ ] Explicit confirm before submit — FR-APP-03
- [ ] State machine per §8.1 enforced server-side; invalid transition → 4xx, no DB write
- [ ] `application_events` timeline table — FR-APP-04
- [ ] Withdraw (candidate)
- [ ] Resume snapshot reference stored on application

### 2.4 Recruiter pipeline (Day 11)

- [ ] Applicant list per job
- [ ] Status change `PATCH /applications/:id/status` with ownership check
- [ ] Candidate timeline view
- [ ] Company cannot see private documents (RBAC test)

**Exit:** student applies to a company job, company moves it through states, student sees timeline. Invalid transitions rejected.

---

## Phase 3 — Resume Intelligence (Day 12–17)

**Epic:** EP-04 · **PRD:** FR-RES-01..08, §9.2, §9.3

### 3.1 Builder (Day 12–13)

- [ ] Resume CRUD, create from profile or blank — FR-RES-01
- [ ] Guided sections, autosave, live preview
- [ ] 2 templates
- [ ] PDF export → object storage → secure signed URL — FR-RES-08

### 3.2 Versions & limits (Day 14)

- [ ] Duplicate, rename, archive, restore — FR-RES-03
- [ ] Active-resume limit via entitlement check (hardcoded limits for now) — FR-RES-02
- [ ] 6th resume rejected with limit message (US-RES-01)

### 3.3 Upload & parsing (Day 14)

- [ ] Upload PDF/DOCX, type + size validation
- [ ] Worker job: extract text → LLM structured parse → store
- [ ] Reject malformed files with clear message (§19)

### 3.4 Async analysis infra (Day 15)

- [ ] Queue + worker, retries, idempotency key
- [ ] Job status endpoint + frontend polling
- [ ] AI failure → retryable state, never fake result (§19)
- [ ] Store `model_version` + timestamp on every analysis

### 3.5 ATS analysis (Day 15–16)

- [ ] Section parsing, keyword/skill match vs JD, structure checks
- [ ] Score + explanations; copy never claims guaranteed ATS pass — §9.2
- [ ] Block on empty resume (no job queued)

### 3.6 High-Bar analysis (Day 16)

- [ ] Separate prompt + separate result: impact, depth, ownership, scale, collaboration — §9.3
- [ ] UI labels it "High-Bar / FAANG-style", not company evaluation
- [ ] ATS and High-Bar never share a result screen (US-RES-02)

### 3.7 Job analysis + tailoring (Day 17)

- [ ] Select job → compare vs resume — FR-RES-06
- [ ] Short JD → "insufficient input" message
- [ ] Tailoring returns proposed diffs; save as **new version** only after approval; original untouched — FR-RES-07

**Exit:** create resume, export PDF, run ATS and High-Bar separately, tailor to a job, apply with that version.

---

## Phase 4 — Career Intelligence (Day 18–21)

**Epics:** EP-03 (AI), EP-06 · **PRD:** FR-JOB-03, FR-AI-01..04, §9.1

### 4.1 Matching engine (Day 18–19)

- [ ] Normalize skills (alias map + lowercasing; no vector DB)
- [ ] Eligibility filters first, then rank
- [ ] Dimensions: required skills, preferred skills, location/mode, experience
- [ ] Explanation per result from evidence
- [ ] Log model/algorithm version + timestamp — §9.1
- [ ] "Recommended" feed + match explanation on job details
- [ ] Incomplete profile → prompt, no matching (§19)
- [ ] Empty results → refinement + skill-gap suggestion

### 4.2 Skill gap + readiness (Day 20)

- [ ] Compare profile evidence vs target-role requirements — FR-AI-03
- [ ] Readiness indicators with reasons (not a bare number) — FR-AI-02

### 4.3 Roadmap + Copilot (Day 21)

- [ ] Editable roadmap generated from skill gap — FR-AI-04
- [ ] Copilot: contextual Q&A with profile context, history capped — FR-AI-01
- [ ] Usage counter increments per call

### 4.4 Daily discovery (Day 21, minimal)

- [ ] Scheduled worker: match new jobs → dedupe → notification record

**Exit:** a student sees ranked jobs with explanations, a skill-gap view, and can chat with Copilot.

---

## Phase 5 — Engagement Lite (Day 22–25)

**Epics:** EP-12, EP-10, EP-09, EP-08 (reduced)

### 5.1 Notifications (Day 22)

- [ ] `notifications` table + in-app bell + unread count
- [ ] Email via provider for: application status change, new application (company), mentor booking
- [ ] Event handlers wired to Phase 2–4 events

### 5.2 TalentVault (Day 23)

- [ ] Upload allowed types, private by default — FR-TV-01/02
- [ ] Share with recipient + expiry → grant record — FR-TV-03
- [ ] Access check on every download; denied access logs a security event — FR-TV-04
- [ ] Replacement/version history — FR-TV-05
- [ ] Expired grant → denied, owner can renew (§19)

### 5.3 Mentorship (Day 24)

- [ ] Mentor profile + availability slots
- [ ] Search/filter mentors — FR-MEN-01
- [ ] Rule-based match from target role + skills (no LLM) — FR-MEN-02
- [ ] Booking with DB-level unique constraint on slot (no double booking) — FR-MEN-03
- [ ] States: Requested → Confirmed → Completed / Cancelled — §8.2
- [ ] Unavailable → alternative slots

### 5.4 Learning (Day 25)

- [ ] Course list + detail + enroll/progress (static content) — FR-LRN-01
- [ ] Locked state when not entitled

**Exit:** notifications fire, vault sharing works with expiry, mentor slot can't be double-booked.

---

## Phase 6 — Entitlements, Billing, Admin (Day 26–27)

**Epics:** EP-11, EP-14

### 6.1 Entitlements (Day 26)

- [ ] Central `can(user, feature)` + `usage(user, feature)` service
- [ ] Replace every hardcoded limit from earlier phases with this — FR-SUB-02
- [ ] Usage counters: AI analyses, resumes, mentor sessions, courses — FR-SUB-03
- [ ] Lock / upgrade UI states — FR-SUB-05

### 6.2 Billing (Day 26–27)

- [ ] Plans page (INR) — FR-SUB-01
- [ ] Razorpay checkout creation (test mode)
- [ ] Webhook with signature verification + idempotency key
- [ ] Duplicate webhook → no double entitlement (tested)
- [ ] Pending payment keeps old entitlement (§19)

### 6.3 Admin (Day 27, bare minimum)

- [ ] Approve/reject companies
- [ ] Approve mentors
- [ ] Disable job / user
- [ ] Audit log viewer (read-only, filterable)

**Exit:** payment in test mode unlocks Pro once, admin can approve companies.

---

## Phase 7 — Hardening, Tests, Deploy (Day 28–30)

### 7.1 Security pass (Day 28)

- [ ] RBAC test on every route group
- [ ] Document access without grant → denied + logged
- [ ] Input validation, parameterized queries only
- [ ] Rate limits on auth, AI, upload routes
- [ ] No secrets in repo; dependency audit

### 7.2 Tests (Day 28–29)

Must-have from PRD §15.2:

- [ ] Resume limit exceeded
- [ ] ATS without valid resume → no job queued
- [ ] High-Bar produces separate result
- [ ] Tailoring leaves original unchanged
- [ ] Invalid application transition rejected, no DB change
- [ ] Duplicate payment webhook idempotent
- [ ] Mentor slot double-book rejected
- [ ] Private document without grant denied
- [ ] One E2E: onboarding → resume → job → apply → status change

### 7.3 UX states (Day 29)

- [ ] Loading / empty / error / locked states on every screen
- [ ] Mobile responsive pass on core flows

### 7.4 Deploy (Day 30)

- [ ] Production env, migrations run, seed admin
- [ ] Health check + error logging (Sentry or equivalent)
- [ ] DB backup verified
- [ ] Smoke test on prod
- [ ] README: setup, env vars, architecture, known cuts

**Exit:** live URL, core loop works end-to-end on prod.

---

## Weekly checkpoints

| End of          | Must be true                                                                       |
| --------------- | ---------------------------------------------------------------------------------- |
| Week 1 (Day 7)  | Auth, RBAC, profile done; company + job CRUD started                               |
| Week 2 (Day 14) | Jobs + applications + recruiter pipeline done; resume builder + PDF export working |
| Week 3 (Day 21) | ATS, High-Bar, tailoring, matching, Copilot working                                |
| Week 4 (Day 30) | Engagement lite, billing, admin, tests, deployed                                   |

If a checkpoint is missed by more than a day, apply the cut list. Do not extend the deadline.

## Definition of done (per task, trimmed from PRD §22)

- [ ] Works end-to-end, including error, loading, empty, and locked states
- [ ] RBAC checked server-side
- [ ] Audit/notification events fire where the PRD requires
- [ ] At least one test on the business rule
- [ ] Merged to main, CI green
