# Usage Examples

## Common scenarios

### Technical problem debugging
```
Use gemini_prompt: "API returns 500 errors randomly. Database shows no issues. What could cause this?"
```

### Code review
```
Use gemini_analyze_codebase with question: "Review this code for security issues and performance problems"
```

### Architecture decisions
```
Use gemini_prompt: "Should I use microservices or monolith for 10k+ users app? Compare pros/cons."
```

### Performance optimization
```
Use gemini_analyze_codebase with question: "Find performance bottlenecks in this React app"
```

## Workflow

1. Check status: `gemini_status`
2. Ask question: `gemini_prompt` with clear problem description
3. Analyze code: `gemini_analyze_codebase` if needed
4. Combine insights from both Claude and Gemini

## Tips

- Give context in prompts (tech stack, constraints, goals)
- Ask specific questions rather than "how to improve?"
- Use for validation of Claude's suggestions
- Break complex problems into focused questions