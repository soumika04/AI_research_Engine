def structured_paper_prompt(text):
    return f"""
You are an academic research analyst.

Analyze the following research paper content and extract:

1. Main Research Objective
2. Methodology Used
3. Dataset Information
4. Key Findings
5. Limitations

Provide structured bullet-point output.

TEXT:
{text}
"""


def cross_paper_prompt(analyses):
    return f"""
You are a senior academic evaluator.

Based on these paper analyses:

{analyses}

Identify:

1. Common Research Themes
2. Methodology Trends
3. Contradictions
4. Research Gaps
5. Future Research Directions

Provide structured academic output.
"""