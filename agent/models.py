"""OpenRouter model configuration — per-node LLM selection using free open-source models."""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file from project root so OPENROUTER_API_KEY is picked up
load_dotenv()

_client = None

# Free open-source models via OpenRouter
MODEL_CONFIG = {
    "research":  "qwen/qwq-32b:free",
    "synthesis": "nousresearch/hermes-3-llama-3.1-405b:free",
    "calculate": "google/gemini-2.0-flash-exp:free",
    "design":    "qwen/qwq-32b:free",
    "default":   "qwen/qwq-32b:free",
}


def get_client() -> OpenAI:
    """Get or create the OpenRouter client."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENROUTER_API_KEY environment variable not set. "
                "Set it or pass via .env file."
            )
        _client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
    return _client


def get_model_for_node(node_name: str) -> str:
    """Get the recommended model for a pipeline node."""
    return MODEL_CONFIG.get(node_name, MODEL_CONFIG["default"])


def call_llm(
    system_prompt: str,
    user_prompt: str,
    node: str = "default",
    temperature: float = 0.0,
) -> str:
    """Simple LLM call via OpenRouter. Returns response text."""
    model = get_model_for_node(node)
    client = get_client()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


def call_llm_structured(
    system_prompt: str,
    user_prompt: str,
    response_model: type,
    node: str = "default",
) -> object:
    """LLM call returning a Pydantic-structured object.

    Uses the OpenAI structured-outputs / response_format feature.
    """
    model = get_model_for_node(node)
    client = get_client()
    response = client.beta.chat.completions.parse(
        model=model,
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format=response_model,
    )
    return response.choices[0].message.parsed
