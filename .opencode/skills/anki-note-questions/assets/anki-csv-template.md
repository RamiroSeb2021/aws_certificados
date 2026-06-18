# Anki CSV Template

Use this column order for generated cards:

```csv
Front,Back,Type,Tags,Caveat
"What is ...?","...","basic","exam::topic::section card::basic",""
"A process has {{c1::step one}} and {{c2::step two}}.","","cloze","exam::topic::section card::cloze",""
"Which service fits this scenario: ...?","...","scenario","exam::topic::section card::scenario",""
```

Rules:

- Escape quotes by doubling them.
- Keep `Back` empty for cloze cards unless extra context is necessary.
- Use lowercase tag namespaces separated by `::`.
- Put preservation warnings or source ambiguity in `Caveat`, not in the answer.
