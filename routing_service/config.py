# config.py
WEAK_ENDPOINT = "http://model_weak:8080/infer"
STRONG_ENDPOINT = "http://model_strong:8080/infer"

model_map = {
    "llama_3_7b": WEAK_ENDPOINT,
    "mistral_7b_instruct": STRONG_ENDPOINT
}
