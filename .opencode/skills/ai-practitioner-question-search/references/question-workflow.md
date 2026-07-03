# AI Practitioner Question Workflow

## Service map

- Translation: `Amazon Translate.md`.
- Natural language/entity/sentiment: `Amazon Comprehend.md`.
- Speech to text: `Amazon Transcribe.md`.
- Text to speech: `Amazon Polly.md`.
- Image/video analysis: `Amazon Rekognition.md`.
- Document text/forms/tables: `Amazon Textract.md`.
- Enterprise search: `Amazon Kendra.md`.
- Chatbots/contact center: `Amazon Lex & Connect.md`.
- Recommendations/personalization: `Amazon Personalize.md`.
- Generative AI, FM, RAG, guardrails, agents: `Amazon Bedrock.md`.
- Prompt patterns: `Fundamentos de Prompt Engineering.md`.
- Business/developer assistant: `Amazon Q.md`.
- ML platform/training/MLOps/Clarify/Model Monitor: `Amazon SageMaker.md`.
- Responsible AI, compliance, governance, security: `Responsabilidad, Cumplimiento, Gobernanza y Seguridad en IA.md`.

## Answer shape

Use this compact structure unless the user asks for more detail:

```markdown
Respuesta: <direct answer>

Por qué:
- <evidence from notes>
- <comparison or elimination if needed>

Trampa de examen: <common confusion, if relevant>

Fuentes:
- `IA_practitioner/<file>.md`
```

## Exam heuristics

- Prefer managed AI services when the question asks for least operational effort.
- Distinguish similar services by input/output: text, speech, image/video, document, enterprise content, code/business assistant, or full ML platform.
- For GenAI safety questions, check Bedrock Guardrails and responsible AI governance notes before answering.
- For bias/explainability/model monitoring, check SageMaker and responsible AI notes together.
