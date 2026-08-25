# Example: Coordinating subagents to build a feature

Goal: add a "favorites" feature across the stack using imported subagents.

## Subagents used

- `backend-developer` — `agents/backend/`
- `frontend-developer` — `agents/frontend/`
- `database-administrator` — `agents/database/`

## Session transcript

```
> design the data model for a favorites feature
  → delegates to database-administrator

> implement the favorites API endpoints
  → delegates to backend-developer

> build the favorites UI in the React app
  → delegates to frontend-developer
```

## Notes

- Give each subagent a **focused, single task**; they run with isolated
  context and return summaries.
- Subagents cannot invoke other subagents, so orchestrate them from the parent
  session (or define a reusable flow in `workflows/`).
