"""Demonstração de limites antes da inferência em um serviço fictício."""

from collections import Counter


MAX_PROMPT_CHARS = 40
MAX_CALLS_PER_ACCOUNT = 2


class InferenceGateway:
    def __init__(self, model):
        self.model = model
        self.calls_by_account = Counter()

    def submit(self, account_id, prompt):
        if not isinstance(prompt, str) or not prompt.strip():
            return "Entrada inválida."
        if len(prompt) > MAX_PROMPT_CHARS:
            return "Entrada acima do limite."
        if self.calls_by_account[account_id] >= MAX_CALLS_PER_ACCOUNT:
            return "Cota da conta esgotada."

        self.calls_by_account[account_id] += 1
        return self.model(prompt)


def main():
    model_calls = []

    def fake_model(prompt):
        model_calls.append(prompt)
        return "Inferência simulada concluída."

    gateway = InferenceGateway(fake_model)
    cases = (
        ("Solicitação normal de Ana", "ana", "Resuma a nota pública."),
        ("Entrada acima do limite", "ana", "x" * (MAX_PROMPT_CHARS + 1)),
        ("Segunda solicitação de Ana", "ana", "Liste os horários públicos."),
        ("Solicitação sem cota", "ana", "Confira a agenda pública."),
        ("Solicitação de Bruno", "bruno", "Resuma a nota pública."),
    )
    for label, account, prompt in cases:
        print(f"{label}: {gateway.submit(account, prompt)}")
    print(f"Chamadas ao modelo simulado: {len(model_calls)}")


if __name__ == "__main__":
    main()
