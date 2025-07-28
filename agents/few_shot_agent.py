import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.chains import LLMChain
from phoenix.trace.langchain import LangChainInstrumentor
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI and Phoenix tracing
LangChainInstrumentor().instrument()
llm = ChatOpenAI(temperature=0, model_name="gpt-4")

examples = [
    {"input": "What is the capital of France?", "output": "The capital of France is Paris."},
    {"input": "What is the capital of Germany?", "output": "The capital of Germany is Berlin."}
]

example_prompt = PromptTemplate(
    input_variables=["input"],
    template="Q: {input}\nA:"
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Answer the following questions about country capitals:",
    suffix="Q: {input}\nA:",
    input_variables=["input"]
)

chain = LLMChain(llm=llm, prompt=few_shot_prompt)

def run_few_shot_agent(question):
    return chain.run({"input": question})

if __name__ == "__main__":
    question = "What is the capital of Italy?"
    print(run_few_shot_agent(question))