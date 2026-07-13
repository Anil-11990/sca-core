# ADR-001

Title:
Domain Driven Design

Status:
Accepted

Date:
2026

---

## Context

SCA aims to become a Professional Operating System rather than a simple AI application.

This requires a domain model that represents reality instead of database tables or user interface components.

---

## Decision

The project will follow Domain Driven Design principles.

The Domain Layer will remain independent of infrastructure, AI models, databases, frameworks, and user interfaces.

Business rules always belong inside the Domain.

---

## Consequences

Advantages

- Easy to test
- Easy to extend
- Long-term maintainability
- AI independent

Trade-offs

- More initial design work
- Higher abstraction
- More classes


## Progress

Sprint 5 introduced the first immutable Value Object (FullName).

This establishes the pattern for modelling domain concepts using
Value Objects instead of primitive strings.