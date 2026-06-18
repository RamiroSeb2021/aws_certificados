# AWS Course Notes Style

Use this style when converting raw AWS course material into study notes.

## Language

- Preserve the source language mix. These notes commonly mix Spanish explanations with English AWS/course terms.
- Keep AWS service names in official casing when clear: `Amazon EC2`, `Amazon S3`, `IAM`, `CloudFront`, `Route 53`, `CloudWatch`, `CloudTrail`, `DynamoDB`, `ElastiCache`, `AWS Organizations`.
- Preserve exam-oriented labels such as `EXAMEN`, `TIP PARA EXAMEN`, and strong warnings.

## Structure

- One H1 for the course note title.
- H2 for major sections, AWS domains, or source sections.
- H3 for individual services, comparisons, pricing blocks, responsibility model blocks, and short conceptual groups.
- Prefer bullets for facts, capabilities, caveats, responsibilities, and use cases.
- Use tables only for explicit comparisons or compact category matrices already present in the source.

## Editing Boundaries

- Correct obvious typos and casing when technical meaning is unchanged.
- Do not add missing AWS facts, current pricing, updated limits, or official clarifications unless the source says them.
- Do not remove rough notes, incomplete phrases, or source artifacts that may reflect the learner's intent.
- If a phrase looks factually suspicious, preserve it and mention caveat in final response instead of rewriting the concept.

## Preservation Checklist

- All source AWS services still appear in the Markdown.
- Identity/security concepts remain: root user, IAM users/groups/roles/policies, MFA, STS, Cognito, Directory Services, IAM Identity Center, SCPs.
- Infrastructure concepts remain: Regions, AZs, Edge Locations, VPC, subnets, NAT, gateways, Direct Connect, VPN, Transit Gateway.
- Cost/support concepts remain: Free Tier/credits, pricing models, Budgets, Cost Explorer, CUR, Trusted Advisor, support plans.
