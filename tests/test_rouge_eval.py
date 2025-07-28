import pytest
from agent.few_shot_agent import run_few_shot_agent
from rouge_score import rouge_scorer

@pytest.mark.parametrize("question,expected", [
    ("What is the capital of Italy?", "The capital of Italy is Rome."),
    ("What is the capital of Spain?", "The capital of Spain is Madrid.")
])
def test_rouge_l(question, expected):
    prediction = run_few_shot_agent(question)
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(expected, prediction)
    assert scores['rougeL'].fmeasure > 0.5