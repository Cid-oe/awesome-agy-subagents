# Example: Security audit with a subagent

Goal: review `src/auth.py` for vulnerabilities using the imported
`security-auditor` subagent (see `agents/security/`).

## 1. Install the agent

```bash
mkdir -p .gemini/agents
cp agents/security/security-auditor.md .gemini/agents/
```

## 2. Invoke it

```
> ask the security-auditor subagent to audit src/auth.py for vulnerabilities
```

## 3. Expected result

The subagent returns a structured report: findings, severity, and
remediation steps — with no modifications to your files unless you ask for
them.

## 4. Automate with a workflow

Use `workflows/code-review-workflow.md` to run `security-auditor` alongside
`code-reviewer` and `performance-engineer` for a combined review.
