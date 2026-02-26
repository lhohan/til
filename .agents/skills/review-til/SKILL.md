---
name: review-til
description: Review a TIL entry for both content guidelines compliance and spelling/grammar/clarity. Use when you want comprehensive feedback on or review a TIL before publishing.
---

Review the provided TIL file or text by running both checks in parallel:

1. **TIL Rules Check**: Invoke the `til-rules-checker` skill to verify content guidelines (word count, focus, clarity, format)

2. **Text Grading**: Invoke the `text-grader` skill to assess spelling, grammar, and clarity using UK English standards

After both checks complete, provide a unified summary with:
- TIL rules verdict (PASS/NEEDS REVISION)
- Text grade (A/B/C/D/F)
- Combined list of actionable improvements (if any)

If a file path is provided as an argument, read that file first. If text is provided directly, use that text.
