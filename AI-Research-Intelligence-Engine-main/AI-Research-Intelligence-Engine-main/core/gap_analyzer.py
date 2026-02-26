from prompts.research_prompts import structured_paper_prompt, cross_paper_prompt
from core.llm_engine import query_llm
from core.text_chunker import chunk_text
from config.settings import CHUNK_SIZE

def analyze_single_paper(text, chunk_limit):
    chunks = chunk_text(text, CHUNK_SIZE)
    combined_analysis = ""

    for chunk in chunks[:chunk_limit]:
        prompt = structured_paper_prompt(chunk)
        result = query_llm(prompt)
        combined_analysis += result + "\n"

    return combined_analysis


def analyze_cross_papers(analyses):
    prompt = cross_paper_prompt(analyses)
    return query_llm(prompt, temperature=0.2)