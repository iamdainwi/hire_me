**HireMe — Product Requirements Document (PRD)**

_Functional, Technical, AI, Workflow, API, QA, DevOps & Product Delivery Specification_

**Version 2.0 | Internal Product & Delivery Master Document | 17 August 2026**

# **1\. Product Definition**

| Item                  | Definition                                                                        |
| :-------------------- | :-------------------------------------------------------------------------------- |
| Product               | HireMe                                                                            |
| Product category      | AI-powered career intelligence \+ opportunity discovery \+ direct hiring platform |
| gePhase 1             | Students/internships/entry level                                                  |
| Phase 2               | Professionals/full-time/career growth                                             |
| Core differentiator   | Explainable AI connected to resume, jobs, learning, mentorship and applications   |
| Architecture baseline | Frontend → Backend → Database, extended with AI/services/event processing         |

# **2\. Product Principles**

- Outcome over activity: optimize qualified connections rather than application volume.
- AI as copilot: recommendations are explainable and user-controlled.
- Evidence-based career intelligence: use skills, projects, education, experience and activity.
- One profile, multiple targeted resumes.
- ATS and High-Bar analysis remain separate.
- Private career data by default.
- Phase 2 extends Phase 1 rather than creating a parallel product.
- Every important workflow must have explicit state, permission, API and failure logic.

# **3\. Product Architecture**

- Experience layer: dashboards, search, resume workspace, applications, learning, mentorship, TalentVault.
- Core platform layer: identity, profile, jobs, applications, subscriptions, notifications, permissions.
- AI layer: parsing, matching, resume analysis, career copilot, skill gap, interview generation.
- Async/event layer: scheduled job search, AI processing, notifications, document scanning, billing events.
- Data layer: relational business entities \+ secure object storage for files.
- Governance layer: verification, moderation, audit, support and analytics.

# **4\. Roles and Permissions**

| Role              | Key Capabilities                                                             | Cannot Do                                             |
| :---------------- | :--------------------------------------------------------------------------- | :---------------------------------------------------- |
| Student           | Profile, resumes, jobs, applications, AI, learning, mentors, TalentVault     | Manage company jobs or other users                    |
| Professional      | Professional profile, jobs, applications, AI, learning, mentors, TalentVault | Manage company/admin data                             |
| Company/Recruiter | Company profile, job posting, applicants, pipeline, analytics                | Access private candidate documents without permission |
| Mentor            | Mentor profile, availability, sessions, messages, shared candidate context   | Access unrelated candidate data                       |
| Admin             | Governance, moderation, verification, billing support, analytics, audit      | Use admin access outside authorized purpose           |

# **5\. Phase 1 Epics**

| Epic  | Name                  | Scope                                                                |
| :---- | :-------------------- | :------------------------------------------------------------------- |
| EP-01 | Identity & Onboarding | Registration, verification, role selection, consent, initial profile |
| EP-02 | Student Profile       | Education, skills, projects, preferences, goals                      |
| EP-03 | Opportunity Discovery | Search, filters, AI recommendations, saved jobs                      |
| EP-04 | Resume Intelligence   | Builder, 5 versions, ATS, High-Bar, job analysis, tailoring          |
| EP-05 | Applications          | Apply, status, tracking, controlled assisted apply                   |
| EP-06 | Career AI             | Copilot, readiness, skill gap, roadmap, project studio               |
| EP-07 | AI Interview          | Role/job/resume-based practice and feedback                          |
| EP-08 | Learning              | Courses, paths, assessments, certifications                          |
| EP-09 | Mentorship            | Matching, booking, sessions, goals, reviews                          |
| EP-10 | TalentVault           | Private documents, sharing, access history                           |
| EP-11 | Subscriptions         | Plans, entitlements, usage, payments                                 |
| EP-12 | Notifications         | Event-driven in-app/email                                            |
| EP-13 | Company Hiring        | Verification, jobs, applicants, pipeline                             |
| EP-14 | Admin Governance      | Users, jobs, companies, mentors, audits                              |

# **6\. Phase 2 Epics**

- Professional profile and career history.
- Professional opportunity matching.
- Career transition and target-role planning.
- Advanced High-Bar resume analysis.
- Professional portfolio and evidence.
- Salary/career intelligence where data sources permit.
- Professional mentorship/coaching.
- Advanced recruiter workflows.
- Professional subscription packaging.

# **7\. Detailed Functional Requirements**

## **7.1 Identity & Onboarding**

| ID       | Feature    | Requirement                                                                   |
| :------- | :--------- | :---------------------------------------------------------------------------- |
| FR-ID-01 | Register   | User registers with email/mobile and selects role.                            |
| FR-ID-02 | Verify     | System verifies contact details before activating relevant account functions. |
| FR-ID-03 | Consent    | User accepts terms/privacy/AI data processing choices as applicable.          |
| FR-ID-04 | Onboarding | Student completes education, target role, skills and preferences.             |
| FR-ID-05 | Session    | JWT-based authenticated session with expiration/refresh behavior.             |

## **7.2 Profile**

| ID        | Feature              | Requirement                                             |
| :-------- | :------------------- | :------------------------------------------------------ |
| FR-PRO-01 | Profile completeness | Calculate completeness from required/optional fields.   |
| FR-PRO-02 | Skills               | Support structured skills with proficiency/evidence.    |
| FR-PRO-03 | Career goal          | Store target role, industry, location and preferences.  |
| FR-PRO-04 | Evidence             | Link projects/certifications/resume evidence to skills. |

## **7.3 Opportunity Search**

| ID        | Feature        | Requirement                                                                     |
| :-------- | :------------- | :------------------------------------------------------------------------------ |
| FR-JOB-01 | Search         | Keyword and natural-language search.                                            |
| FR-JOB-02 | Filters        | Role, skill, location, mode, stipend/salary, experience, date.                  |
| FR-JOB-03 | Recommendation | AI ranks opportunities using permitted candidate data.                          |
| FR-JOB-04 | Saved          | Save/unsave opportunities.                                                      |
| FR-JOB-05 | Details        | Show description, company, requirements, match explanation and application CTA. |

## **7.4 Resume Intelligence**

| ID        | Feature       | Requirement                                                                    |
| :-------- | :------------ | :----------------------------------------------------------------------------- |
| FR-RES-01 | Create        | Create resume from profile or manually.                                        |
| FR-RES-02 | Five versions | Maintain up to five active versions according to entitlement.                  |
| FR-RES-03 | Versioning    | Duplicate, rename, archive and restore versions.                               |
| FR-RES-04 | ATS           | Analyze ATS-oriented alignment.                                                |
| FR-RES-05 | High-Bar      | Analyze technical depth, impact, ownership, scale and evidence.                |
| FR-RES-06 | Job analysis  | Parse selected job and compare with resume.                                    |
| FR-RES-07 | Tailoring     | Generate proposed job-specific edits and save as a new version after approval. |
| FR-RES-08 | Export        | Generate PDF and store secure file reference.                                  |

## **7.5 Applications**

| ID        | Feature          | Requirement                                             |
| :-------- | :--------------- | :------------------------------------------------------ |
| FR-APP-01 | Apply            | Create application against active eligible job.         |
| FR-APP-02 | Resume selection | Recommend and allow candidate to choose resume version. |
| FR-APP-03 | Consent          | Confirm application before submission.                  |
| FR-APP-04 | Tracking         | Track state transitions.                                |
| FR-APP-05 | Assisted apply   | Support controlled assistance where permitted.          |

## **7.6 Career AI**

| ID       | Feature        | Requirement                                             |
| :------- | :------------- | :------------------------------------------------------ |
| FR-AI-01 | Copilot        | Contextual career Q\&A.                                 |
| FR-AI-02 | Readiness      | Generate explainable readiness indicators.              |
| FR-AI-03 | Skill gap      | Compare current evidence with target-role requirements. |
| FR-AI-04 | Roadmap        | Generate editable career roadmap.                       |
| FR-AI-05 | Project studio | Recommend evidence-building projects.                   |

## **7.7 Learning & Mentorship**

| ID        | Feature       | Requirement                                          |
| :-------- | :------------ | :--------------------------------------------------- |
| FR-LRN-01 | Courses       | Browse/enroll/continue courses based on entitlement. |
| FR-LRN-02 | Certification | Track assessment and certification state.            |
| FR-MEN-01 | Mentor search | Search and filter verified mentors.                  |
| FR-MEN-02 | AI match      | Recommend mentors based on career context.           |
| FR-MEN-03 | Booking       | Book available sessions and prevent double booking.  |
| FR-MEN-04 | Session       | Track upcoming/completed/cancelled sessions.         |

## **7.8 TalentVault**

| ID       | Feature         | Requirement                                     |
| :------- | :-------------- | :---------------------------------------------- |
| FR-TV-01 | Upload          | Upload permitted document types.                |
| FR-TV-02 | Private default | Documents are private unless explicitly shared. |
| FR-TV-03 | Share           | Share with defined recipient/context/expiry.    |
| FR-TV-04 | Access history  | Record document access events.                  |
| FR-TV-05 | Version         | Support document replacement/version history.   |

## **7.9 Subscription**

| ID        | Feature      | Requirement                                        |
| :-------- | :----------- | :------------------------------------------------- |
| FR-SUB-01 | Plans        | Display approved plans in INR and USD.             |
| FR-SUB-02 | Entitlements | Centralize feature and usage entitlements.         |
| FR-SUB-03 | Usage        | Track AI/resume/mentor/course usage as applicable. |
| FR-SUB-04 | Billing      | Payment, invoice and renewal states.               |
| FR-SUB-05 | Lock         | Show upgrade flow when entitlement is unavailable. |

# **8\. Core State Machines**

## **8.1 Application**

| State           | Allowed Next States               | Owner             |
| :-------------- | :-------------------------------- | :---------------- |
| Draft           | Ready to Apply                    | Candidate         |
| Ready to Apply  | Applied / Cancelled               | Candidate         |
| Applied         | Under Review / Withdrawn          | Candidate/Company |
| Under Review    | Shortlisted / Rejected            | Company           |
| Shortlisted     | Assessment / Interview / Rejected | Company           |
| Interview       | Final Interview / Rejected        | Company           |
| Final Interview | Offer / Rejected                  | Company           |
| Offer           | Joined / Declined                 | Candidate/Company |

## **8.2 Mentor Session**

| State     | Transition                   |
| :-------- | :--------------------------- |
| Requested | Pending mentor confirmation  |
| Confirmed | Scheduled session            |
| Completed | Session delivered            |
| Cancelled | Cancelled by permitted party |
| No-show   | Recorded with policy action  |

# **9\. AI Logic Specifications**

## **9.1 Candidate-to-Job Matching**

1. Normalize candidate skills and job requirements.
2. Separate required and preferred requirements.
3. Calculate structured match dimensions.
4. Generate evidence-based explanation.
5. Apply eligibility constraints before ranking.
6. Rank results and surface why each result appears.
7. Log model version and analysis timestamp for reproducibility.

## **9.2 ATS Analysis**

- Parse resume sections and job description.
- Compare relevant keywords and skill concepts.
- Check structure/readability and machine-parsability indicators.
- Identify missing or weak evidence.
- Produce score \+ explanations; never claim guaranteed ATS acceptance.

## **9.3 High-Bar Analysis**

- Assess impact and measurable outcomes.
- Assess technical depth and complexity.
- Assess ownership and problem solving.
- Assess scale and system/design evidence where relevant.
- Assess leadership/collaboration evidence.
- Generate actionable improvements.
- Label as High-Bar/FAANG-style, not an actual company evaluation.

# **10\. Backend Automation & Event Logic**

| Event                      | Trigger                        | Backend Action                                                | Async?    | User Result                       |
| :------------------------- | :----------------------------- | :------------------------------------------------------------ | :-------- | :-------------------------------- |
| JOB_PUBLISHED              | Verified company publishes job | Index job, run validation, notify matching candidates         | Yes       | Job searchable/recommended        |
| RESUME_UPLOADED            | Candidate uploads resume       | Store, scan, parse, extract structured data                   | Yes       | Resume available for analysis     |
| RESUME_ANALYSIS_REQUESTED  | User requests analysis         | Queue analysis, store result with model version               | Yes       | Analysis screen                   |
| APPLICATION_CREATED        | Candidate confirms apply       | Create application, snapshot resume reference, notify company | No/Hybrid | Application tracking              |
| APPLICATION_STATUS_CHANGED | Company changes status         | Validate transition, persist, notify candidate, audit         | No        | Updated timeline                  |
| SUBSCRIPTION_PAID          | Payment provider confirms      | Activate entitlement, create invoice, audit                   | Yes       | Premium unlocked                  |
| DOCUMENT_SHARED            | Candidate shares document      | Create access grant, expiry, audit                            | No        | Recipient can access within scope |
| MENTOR_BOOKED              | Session booked                 | Validate availability, create session, notify both            | No        | Calendar/session confirmation     |
| DAILY_JOB_SEARCH           | Scheduler runs                 | Search new jobs, match, dedupe, notify                        | Yes       | New recommendations               |

# **11\. API Contract Baseline**

| Domain       | Example Endpoint                | Method    | Purpose                            |
| :----------- | :------------------------------ | :-------- | :--------------------------------- |
| Auth         | /api/v1/auth/register           | POST      | Create account                     |
| Profile      | /api/v1/profile                 | GET/PATCH | Read/update profile                |
| Jobs         | /api/v1/jobs/search             | POST      | Structured/natural-language search |
| Jobs         | /api/v1/jobs/:id                | GET       | Opportunity details                |
| Resume       | /api/v1/resumes                 | POST      | Create resume                      |
| Resume       | /api/v1/resumes/:id/analyze     | POST      | Run analysis                       |
| Resume       | /api/v1/resumes/:id/tailor      | POST      | Create tailored version            |
| Applications | /api/v1/applications            | POST      | Apply                              |
| Applications | /api/v1/applications/:id/status | PATCH     | Update authorized status           |
| AI           | /api/v1/ai/copilot              | POST      | Career Copilot request             |
| Mentors      | /api/v1/mentors/match           | POST      | AI mentor matching                 |
| Learning     | /api/v1/courses                 | GET       | Course discovery                   |
| Vault        | /api/v1/documents               | POST      | Secure document upload             |
| Vault        | /api/v1/documents/:id/share     | POST      | Share document                     |
| Billing      | /api/v1/subscriptions           | GET       | Plan/entitlement status            |
| Billing      | /api/v1/subscriptions/checkout  | POST      | Create checkout                    |

API paths are a baseline proposal for engineering; exact contracts should be finalized in API design before implementation.

# **12\. Data Model**

| Entity              | Key Data                                              | Relationships        |
| :------------------ | :---------------------------------------------------- | :------------------- |
| User                | id, role, email, status                               | Owns profile/account |
| StudentProfile      | education, skills, goals, preferences                 | User 1:1             |
| ProfessionalProfile | experience, skills, goals                             | User 1:1             |
| Company             | name, verification, industry                          | User/company users   |
| MentorProfile       | expertise, verification, availability, pricing        | User 1:1             |
| Job                 | company, title, description, skills, location, status | Company 1:N          |
| Resume              | candidate, target role, version, status               | Candidate 1:N        |
| ResumeAnalysis      | resume, mode, scores, findings, model version         | Resume 1:N           |
| Application         | candidate, job, resume snapshot, status               | Candidate/Job        |
| Course              | content, level, entitlement                           | Learning             |
| MentorSession       | mentor, candidate, slot, status                       | Mentorship           |
| Document            | owner, type, storage reference, visibility            | TalentVault          |
| Subscription        | user, plan, status, period                            | Billing              |
| Entitlement         | plan, feature, limit                                  | Subscription         |
| AuditLog            | actor, action, object, timestamp                      | Cross-domain         |

# **13\. Security & Privacy Requirements**

- RBAC across all roles and protected routes.
- Password hashing using an approved secure hashing strategy; existing SOP baseline is bcrypt.
- JWT/session expiration and refresh.
- Encrypted sensitive data at rest and in transit.
- Secure object storage for resumes/documents.
- Signed/time-bound document access where appropriate.
- Rate limiting and input validation.
- SQL injection prevention through parameterized queries/ORM controls.
- Audit logging for security, billing, document sharing and material hiring actions.
- Data deletion/export workflow must be defined before production.
- Least-privilege service credentials and secrets management.

# **14\. DevOps & Environment Requirements**

| Area          | Requirement                                                                     |
| :------------ | :------------------------------------------------------------------------------ |
| Environments  | Local, Development, QA/Staging, Production                                      |
| CI/CD         | Automated lint, unit tests, build, security checks and deployment gates         |
| Secrets       | Environment/secret manager; never commit credentials                            |
| Database      | Migration-controlled schema, backup, restore verification                       |
| Files         | Object storage with lifecycle and access controls                               |
| Observability | Application logs, metrics, traces, health checks and alerts                     |
| AI jobs       | Queue/worker pattern for long-running analysis                                  |
| Reliability   | Retries, idempotency and dead-letter handling for async jobs                    |
| Rollback      | Versioned releases and rollback strategy                                        |
| Monitoring    | API latency, errors, queue depth, AI failures, payment failures, storage errors |
| Security      | Dependency scanning, vulnerability management and access review                 |

# **15\. QA & Testing Strategy**

## **15.1 Test Layers**

- Unit testing: business rules, parsers, entitlement checks and state transitions.
- Integration testing: API \+ database \+ queue \+ storage.
- AI evaluation: fixed benchmark datasets, regression tests and human review.
- End-to-end testing: onboarding → resume → job → application → status.
- Security testing: RBAC, document access, injection, rate limiting and session controls.
- Performance testing: search, dashboard, concurrent users and async queues.
- Payment testing: successful, failed, duplicate, expired and webhook scenarios.
- Usability/accessibility testing for core candidate and recruiter workflows.

## **15.2 Critical Test Scenarios**

| Scenario                                    | Expected Result                                          |
| :------------------------------------------ | :------------------------------------------------------- |
| User exceeds resume limit                   | System prevents creation and shows upgrade/limit message |
| ATS analysis requested without valid resume | Validation error; no job queued                          |
| High-Bar requested                          | Separate High-Bar analysis result generated              |
| Tailoring accepted                          | New version created; original unchanged                  |
| User not entitled to course                 | Course content locked with upgrade path                  |
| Private document accessed without grant     | Access denied and security event logged                  |
| Application status invalid transition       | API rejects request; no DB change                        |
| Duplicate payment webhook                   | Idempotent processing; no double entitlement             |
| Mentor slot already booked                  | Booking rejected; slot remains unavailable               |
| External apply unavailable                  | User informed; no false 'applied' state                  |

# **16\. Analytics & Product Events**

| Event                      | Purpose               |
| :------------------------- | :-------------------- |
| signup_completed           | Acquisition funnel    |
| profile_completed          | Activation            |
| resume_created             | Career asset adoption |
| resume_analysis_completed  | AI engagement         |
| job_search_performed       | Discovery             |
| job_saved                  | Intent                |
| application_submitted      | Conversion            |
| application_status_changed | Hiring outcome        |
| mentor_booked              | Mentorship conversion |
| course_started             | Learning adoption     |
| subscription_started       | Revenue               |
| subscription_cancelled     | Retention/churn       |
| document_shared            | Vault usage           |

# **17\. UX / Figma Screen Inventory**

| Area          | Phase 1 Core Screens                                  | Phase 2 Extension                 |
| :------------ | :---------------------------------------------------- | :-------------------------------- |
| Dashboard     | Student Dashboard                                     | Professional Dashboard            |
| Opportunities | Recommended/Search/Details                            | Professional Jobs/Matches         |
| Resume        | Workspace/Builder/ATS/High-Bar/Job Analysis/Tailoring | Advanced Professional Resume      |
| Applications  | List/Detail/Timeline                                  | Professional Application Pipeline |
| Career AI     | Copilot/Readiness/Skill Gap/Roadmap/Projects          | Career Transition/Progression     |
| Learning      | Academy/Courses/Paths/Assessments/Certifications      | Professional Learning             |
| Mentors       | Find/Match/Profile/My Mentors/Sessions                | Professional Coaching             |
| TalentVault   | Documents/Shared/Access History                       | Expanded professional assets      |
| Subscription  | Plans/Usage/Billing                                   | Professional plans                |

# **18\. User Stories & Acceptance Criteria**

| Story     | User Story                                                                                      | Acceptance Criteria                                                                                                                            |
| :-------- | :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| US-RES-01 | As a student, I want to maintain five targeted resumes so that I can apply for different roles. | Given an active plan allowing five resumes, when I create the fifth resume, it succeeds; attempting a sixth shows the entitlement limit.       |
| US-RES-02 | As a student, I want separate ATS and High-Bar analysis.                                        | Given a resume, when I select ATS, only ATS analysis is shown; when I select High-Bar, the High-Bar analysis is generated separately.          |
| US-JOB-01 | As a student, I want AI to find relevant internships.                                           | Given a complete profile, when recommendations run, jobs are ranked by configured match logic and each recommendation explains why it matches. |
| US-APP-01 | As a student, I want to control assisted applications.                                          | Given an eligible opportunity, the system prepares the application and waits for user approval before submission.                              |
| US-MEN-01 | As a student, I want mentors from my target field.                                              | Given a target role, the system recommends verified mentors using approved matching factors.                                                   |
| US-TV-01  | As a candidate, I want private document storage.                                                | Given an uploaded document, it is private by default and only authorized viewers can access it.                                                |
| US-SUB-01 | As a subscriber, I want premium features to unlock immediately after payment.                   | Given confirmed payment, the entitlement service activates the approved plan idempotently.                                                     |
| US-CO-01  | As a recruiter, I want to review applicants efficiently.                                        | Given an active job, recruiters can view applicants, resume information and AI-assisted insights subject to permissions.                       |

# **19\. Error & Edge-Case Catalogue**

- Incomplete profile → prompt for missing information before AI matching.
- Malformed/unsupported resume → reject with actionable upload guidance.
- AI service unavailable → show retryable processing state; never fabricate result.
- Job description too short → explain insufficient analysis input.
- No suitable jobs → show search refinement and learning/skill-gap suggestions.
- Subscription payment pending → retain previous entitlement until provider confirmation rules are met.
- Mentor unavailable → offer alternative slots/mentors.
- Document sharing expired → deny access and offer owner renewal.
- External application blocked → preserve 'not submitted' state and provide manual route.
- Company verification pending → restrict publishing until approved.

# **20\. Release Strategy**

8. Foundation: identity, profiles, RBAC, company verification, job posting and direct applications.
9. Candidate intelligence: five-resume workspace, builder, ATS, High-Bar and job analysis.
10. Career intelligence: recommendations, Copilot, skill gap, readiness and roadmap.
11. Engagement: mentorship, learning, TalentVault and notifications.
12. Monetization: subscriptions, entitlements, billing and usage.
13. Automation: scheduled job discovery and controlled assisted application.
14. Phase 2: professional workflows and advanced career intelligence.

# **21\. Definition of Ready**

- Requirement has unique ID.
- Business rule is explicit.
- Role/permission is defined.
- UI entry/exit points are known.
- API contract is known or explicitly marked pending.
- Data entities are identified.
- Acceptance criteria are testable.
- Analytics event is defined if relevant.
- Security/privacy impact is reviewed.

# **22\. Definition of Done**

- Code reviewed and merged.
- Unit/integration/E2E tests pass.
- Security checks pass.
- API contract documented.
- UI matches approved Figma behavior.
- Analytics events verified.
- Error/loading/empty/locked states implemented.
- Audit/notification events verified.
- DevOps deployment and monitoring verified.
- QA sign-off completed.
- Product/BA acceptance completed.

# **23\. Team Handoff Matrix**

| Team             | Primary PRD Sections                           | Expected Deliverable              |
| :--------------- | :--------------------------------------------- | :-------------------------------- |
| Product Manager  | Vision, scope, epics, metrics, roadmap         | Prioritized backlog and decisions |
| Business Analyst | Requirements, rules, workflows, traceability   | BRD/FRD/acceptance mapping        |
| UX/UI            | IA, journeys, screen inventory, states         | Figma flows and UI                |
| Frontend         | Screen/API mapping, states, permissions        | Responsive application            |
| Backend          | Business rules, APIs, entities, events         | Services/API/database             |
| AI/ML            | AI logic, evaluation, model versioning         | AI services \+ evaluation         |
| QA               | Acceptance criteria, edge cases, test strategy | Test cases and release sign-off   |
| DevOps           | Environments, CI/CD, observability, backups    | Production platform               |
| Security         | Privacy, RBAC, document controls               | Security review                   |
| Sales            | Commercial model, personas, value proposition  | Demo, pitch, proposal package     |
| Support/Ops      | Notifications, moderation, incident flows      | Runbooks and support workflows    |

# **24\. Open Decisions**

| Decision                                       | Owner                | Status            |
| :--------------------------------------------- | :------------------- | :---------------- |
| Final subscription prices and annual discounts | Business/Finance     | DECISION REQUIRED |
| Payment gateway(s) for INR/USD                 | Finance/Engineering  | DECISION REQUIRED |
| Exact AI/LLM providers                         | AI/Engineering       | DECISION REQUIRED |
| External job data sources/APIs                 | PM/Engineering/Legal | DECISION REQUIRED |
| External auto-apply coverage                   | PM/Legal/Engineering | DECISION REQUIRED |
| Mentor payout/revenue share                    | Business             | DECISION REQUIRED |
| Data retention/deletion periods                | Security/Legal       | DECISION REQUIRED |
| Phase 2 launch scope                           | Product/Business     | DECISION REQUIRED |
| Employer pricing                               | Sales/Business       | DECISION REQUIRED |

# **25\. Alignment with Existing SOP**

This PRD preserves the current SOP baseline: direct company-to-student hiring, Student/Company/Admin roles, React \+ Tailwind frontend, Node/Express backend, MySQL, JWT authentication, NLP-based resume parsing/scoring, template-based resume generation, job posting, applications, resume analysis, resume builder and the existing security controls. The PRD adds the expanded two-phase AI career ecosystem around those foundations rather than discarding the original architecture.

The existing SOP's Resume Builder flow includes template selection, guided sections, autosave, preview and PDF generation; these behaviors are retained in the expanded product specification.
