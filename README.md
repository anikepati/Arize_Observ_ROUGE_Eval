# GenAI Agent with Few-Shot Learning, ROUGE-L Evaluation, and Arize Phoenix Observability

This project demonstrates how to build a GenAI agent using OpenAI, LangChain, few-shot prompting, local Arize Phoenix tracing, and automated evaluation using ROUGE-L.

## 📁 Structure

- `agent/few_shot_agent.py`: Few-shot prompting using LangChain
- `tests/test_rouge_eval.py`: Pytest-based evaluation with ROUGE-L
- `.env`: Stores OpenAI and Arize API keys

## ⚙️ Setup Instructions

### Step 1: Create and activate virtual environment using `uv` or `venv`

Using `uv`:
```bash
uv venv .venv
source .venv/bin/activate
```

Alternatively using `venv`:
```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Environment Variables
Create a `.env` file:
```env
OPENAI_API_KEY=your-openai-api-key
ARIZE_API_KEY=your-arize-api-key
```

### Step 4: Run the Agent
```bash
python agent/few_shot_agent.py
```

### Step 5: Run Tests
```bash
pytest tests/
```

## 📊 Observability with Arize Phoenix
- Local: Install and run Phoenix locally using Docker (https://docs.arize.com/phoenix)
- SaaS: Connect using your `ARIZE_API_KEY` to monitor hosted agents

---

Made with ❤️ using OpenAI, LangChain, and Arize Phoenix.