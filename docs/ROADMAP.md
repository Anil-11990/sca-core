# Sovereign Career Architect (SCA)

## Product Roadmap

---

# Phase 1 — Foundation ✅

- [x] Project Structure
- [x] Clean Architecture
- [x] Git Repository
- [x] Entity
- [x] Skill
- [x] Professional Aggregate
- [x] Unit Testing

Status:
Completed

---

# Phase 2 — Domain Language 🚧

Current Sprint:
Sprint 6

Objective:
Replace primitive data types with rich Domain Value Objects.

Current Tasks

- - [x] FullName
- [ ] Goal
- [ ] Location
- [ ] ProfessionalTitle

Exit Criteria

- No raw strings for important concepts.
- Professional uses Value Objects.
- All tests passing.

---

# Phase 3 — Professional Intelligence

Upcoming

- Projects
- Evidence
- Goals
- Career State
- Metrics

---

# Phase 4 — AI Layer

Upcoming

- Librarian
- Scout
- Ledger
- Architect

---

# Phase 5 — Platform

Upcoming

- Dashboard
- API
- CLI
- Docker Deployment

---

# Long-Term Vision

SCA becomes the Professional Operating System for individuals and organisations.

## Sprint 7 - Professional Aggregate

### Completed

- Professional manages Skills
- Professional manages Goals
- Read-only collections
- Duplicate protection
- Aggregate Root strengthened

### Test Status

40 passing tests

### Architecture Notes

Professional is now the central Aggregate Root responsible for managing
career-related entities through business operations instead of exposing
mutable collections.

## Sprint 8 - Application Layer

### Completed

- Created Application Layer
- Implemented first Use Case
- Added CreateProfessional use case
- Established Application → Domain interaction

### Test Status

41 passing tests

## Sprint 8 - Phase 2

### Completed

- Added AddSkill use case
- Application layer delegates to Professional aggregate
- Added application layer tests

### Test Status

42 passing tests

## Sprint 8 - Phase 3

### Completed

- Added AddGoal use case
- Application layer delegates goal management to Professional
- Added application layer tests

### Test Status

43 passing tests

## Sprint 8 - Phase 4

### Completed

- Added CompleteGoal use case
- First business workflow
- Application layer triggers domain behaviour

### Test Status

44 passing tests

## Sprint 9 - Domain Events

### Completed

- Introduced DomainEvent base class
- Added GoalCompleted event
- Created first domain event tests

### Test Status

45 passing tests

## Sprint 10 - Event Bus

### Completed

- Added EventBus
- Introduced event publishing
- Prepared architecture for event subscribers

### Test Status

46 passing tests

## Sprint 11 - Repository Pattern

### Completed

- Added ProfessionalRepository abstraction
- Added in-memory repository implementation
- Verified repository behaviour with tests

### Test Status

47 passing tests

## Sprint 12 - Dependency Injection Foundation

### Completed

- Added Composition Root
- Added Container
- Centralized dependency creation

### Test Status

48 passing tests

## Sprint 13 - Profile Completeness Service

### Completed

- Added ProfileCompletenessService
- Introduced first Domain Service
- Calculated Professional profile completeness

### Test Status

49 passing tests

## Sprint 14 – Repository Integration

### Completed

- Injected ProfessionalRepository into CreateProfessional
- Persisted Professional through repository
- Connected Application Layer with Infrastructure

### Test Status

50 passing tests

## Sprint 15 - API Foundation

### Goal

Expose the SCA Core through a FastAPI interface.

### Planned

- Install FastAPI
- Create API entry point
- Build first endpoint
- Enable Swagger documentation
## Sprint 15 - FastAPI Foundation

### Completed

- Installed FastAPI
- Created API entry point
- Started development server
- Verified Swagger UI

### Status

API foundation complete

## Sprint 16 – First API Endpoint

### Completed

- Created request model using Pydantic
- Added POST /professionals endpoint
- Connected API to CreateProfessional use case
- Returned Professional as JSON

### Result

The API can now create Professionals through HTTP requests.


## Sprint 17 ✅ REST API

Completed:

- FastAPI integration
- Dependency Injection container
- POST /professionals endpoint
- GET /professionals/{id} endpoint
- Request validation
- Response models
- API wiring

## Sprint 18 — API Integration Tests ✅

- Added FastAPI integration tests using TestClient
- Tested POST /professionals
- Tested GET /professionals/{id}
- Added error handling tests (400 and 404)
- Total test coverage increased to 54 passing tests

## Sprint 18 ✅ API Integration

- Added FastAPI integration tests
- Tested POST /professionals
- Tested GET /professionals/{id}
- Tested invalid UUID handling
- Tested missing Professional handling
- Total tests: 54

# Milestone 3 – Persistent Storage

## Sprint 19
- [ ] Install SQLAlchemy
- [ ] Configure SQLite
- [ ] Create ORM models
- [ ] Build SQLite Repository
- [ ] Replace Memory Repository
- [ ] Add Repository Tests