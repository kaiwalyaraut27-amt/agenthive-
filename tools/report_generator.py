def generate_report(data):

    report = f"""

# AgentHive Startup Report

## Research

{data['research']}

---

## Competitors

{data['competitors']}

---

## Personas

{data['personas']}

---

## Product Plan

{data['product_v2']}

---

## Architecture

{data['architecture']}

"""

    return report