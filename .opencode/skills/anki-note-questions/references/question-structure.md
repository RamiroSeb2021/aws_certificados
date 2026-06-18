# Anki Question Structure

Use these rules when turning notes into cards.

## Core shape

```text
Front: one brief, specific question
Back: short answer; add one minimal example only when it improves recall
```

The card should make the learner actively remember, not reread. If the answer is long enough to become a paragraph, split it.

## Atomicity rules

- One card tests one concept, step, service feature, caveat, or distinction.
- Convert large questions into mini-questions.
- Ask from multiple angles when it strengthens understanding:
  - term → definition
  - definition/scenario → term
  - symptom/use case → service/concept
- Avoid vague prompts like “Explain X” unless the expected answer is tightly scoped.

## Cloze deletion

Use cloze cards for lists, processes, formulas, sequences, and exact phrases.

Step-by-step reveal:

```text
The habit loop is {{c1::cue}}, {{c2::craving}}, {{c3::response}}, and {{c4::reward}}.
```

Reveal together:

```text
The three terms are {{c1::regular}}, {{c1::needed}}, and {{c1::desired}}.
```

## Visual cards

When notes mention a diagram, screenshot, architecture, graph, or process image, create one of these:

- Basic visual prompt: “What does this image/process show?”
- Image Occlusion suggestion: “Hide labels X, Y, Z and reveal one by one.”

## Review behavior assumed by the card

The learner should answer in their own words before showing the answer, then grade honestly:

- `Again`: wrong, missing, or too slow.
- `Good`: correct but effortful.
- `Easy`: correct and fast.
