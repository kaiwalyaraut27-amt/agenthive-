RESEARCH_PROMPT = """
Act as a startup market researcher.

Analyze this startup idea:

{idea}

Provide:

1. Market Opportunity
2. Industry Trends
3. Risks
4. Opportunities
"""


COMPETITOR_PROMPT = """
Act as a startup competitor analyst.

Analyze this startup idea:

{idea}

Provide:

1. Top Competitors
2. Strengths
3. Weaknesses
"""


PERSONA_PROMPT = """
Act as a UX researcher.

For this startup idea:

{idea}

Create 3 customer personas.

Include:
- Age
- Occupation
- Pain Points
- Goals
"""


PRODUCT_PROMPT = """
Based on:

Research:
{research}

Competitors:
{competitors}

Personas:
{personas}

Create:

1. Product Vision
2. MVP Features
3. User Stories
4. Pricing Strategy
"""

IMPROVEMENT_PROMPT = """
You are a senior product strategist.

Original Product Plan:

{product_plan}

Critic Feedback:

{feedback}

Create an improved version of the product plan.
"""

ARCHITECTURE_PROMPT = """
You are a senior startup CTO.

Startup Idea:

{idea}

Product Plan:

{product}

Design a complete technical architecture.

Include:

1. Frontend
2. Backend
3. Database
4. Authentication
5. AI Layer
6. Deployment
7. Estimated Monthly Cost
8. Scaling Considerations
"""

IMPROVEMENT_PROMPT = """
You are a senior startup strategist.

Original Product Plan:

{product_plan}

Critic Feedback:

{feedback}

Create an improved version of the product plan.

Include:

1. Better features
2. Better pricing
3. Better monetization
4. Better competitive advantages

Return the improved product plan.
"""