# Personal Contribution Standard

This guide defines how I contribute to this project while keeping code quality high and complexity low.

## Goal

Ship changes that:
- Work reliably
- Are easy to understand
- Are easy to maintain
- Avoid unnecessary complexity

## Core Principles

1. If a change does not improve clarity, testability, or reliability, do not add it.
2. Prefer the simplest solution that satisfies the requirement.
3. Readability today is better than cleverness that is hard to maintain.
4. Keep changes small and focused.

## Before Starting Any Change

1. Define the problem in one sentence.
2. Define success criteria in one sentence.
3. Define scope boundaries: what is included and what is not.

## Coding Rules

1. One responsibility per function or module.
2. Use explicit names that describe intent.
3. Avoid creating new layers unless there is a clear, current need.
4. Avoid duplication, but only extract shared code when repetition is real.
5. Keep API contracts stable unless there is a strong reason to change them.

## Error Handling And Logging

1. Return clear, user-safe error messages.
2. Keep technical details in logs.
3. Use structured logging in backend code.
4. Do not use `print` for backend diagnostics.

## Testing Standard (Pragmatic)

For relevant changes, cover at least:
1. Happy path
2. Expected failure path
3. Main business rule

Notes:
- Aim for meaningful tests, not artificial coverage inflation.
- Keep tests fast and easy to understand.

## When Not To Abstract

Do not introduce extra abstractions when:
1. There is only one real use case.
2. There is no real duplication.
3. The abstraction adds more moving parts than value.
4. The only reason is a hypothetical future need.

## When To Abstract

Introduce abstraction when:
1. The same logic appears in multiple places.
2. Dependency isolation significantly improves testing.
3. New features repeatedly require the same pattern.

## Commit And PR Rules

1. One logical change per commit.
2. Use clear English commit messages explaining what changed and why.
3. Keep pull requests focused and reviewable in a short time.
4. Do not mix refactors with behavior changes unless necessary.

## Definition Of Done

A change is done when:
1. Tests pass.
2. No significant lint/type issues remain.
3. The code is understandable to a future maintainer.
4. Documentation is updated only where behavior changed.

## Recommended Commit Message Patterns

- `feat: add v1 endpoint for stack categories`
- `fix: handle formspree timeout with structured logging`
- `refactor: move use case wiring to dependency providers`
- `test: cover contact endpoint dependency override`
