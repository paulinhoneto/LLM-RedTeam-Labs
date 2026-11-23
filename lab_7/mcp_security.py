"""Simulador local de validação e autorização de tools/call no MCP."""

import argparse
import json
import re


TOOL_NAME = "read_card"
CARD_ID_PATTERN = r"CARD-[0-9]{3}"
CARDS = {"CARD-001": "Vila Aurora: reunião fictícia às 14h."}


def protocol_error(request_id, code, message):
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": message},
    }


def tool_result(request_id, text, is_error):
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "content": [{"type": "text", "text": text}],
            "isError": is_error,
        },
    }


def handle_request(request, allowed_card_ids):
    """Recebe a mensagem do cliente e o escopo concedido pela sessão."""
    if not isinstance(request, dict) or request.get("jsonrpc") != "2.0":
        return protocol_error(None, -32600, "Requisição inválida.")
    request_id = request.get("id")
    if type(request_id) not in (str, int) or not isinstance(request.get("method"), str):
        return protocol_error(None, -32600, "Requisição inválida.")
    if request["method"] != "tools/call":
        return protocol_error(request_id, -32601, "Método desconhecido.")

    params = request.get("params")
    if not isinstance(params, dict) or params.keys() != {"name", "arguments"}:
        return protocol_error(request_id, -32602, "Parâmetros inválidos.")
    if params["name"] != TOOL_NAME:
        return protocol_error(request_id, -32602, "Ferramenta desconhecida.")

    arguments = params["arguments"]
    if not isinstance(arguments, dict) or arguments.keys() != {"card_id"}:
        return tool_result(request_id, "Entrada inválida: informe apenas card_id.", True)
    card_id = arguments["card_id"]
    if not isinstance(card_id, str) or not re.fullmatch(CARD_ID_PATTERN, card_id):
        return tool_result(request_id, "Entrada inválida: use o formato CARD-000.", True)

    if card_id not in allowed_card_ids or card_id not in CARDS:
        return tool_result(request_id, "Acesso negado ao cartão.", True)
    return tool_result(request_id, CARDS[card_id], False)


def build_call(card_id):
    return {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": TOOL_NAME, "arguments": {"card_id": card_id}},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cenario",
        choices=("autorizado", "entrada-invalida", "sem-permissao"),
        required=True,
    )
    args = parser.parse_args()
    card_id = "" if args.cenario == "entrada-invalida" else "CARD-001"
    allowed = frozenset() if args.cenario == "sem-permissao" else frozenset({"CARD-001"})
    response = handle_request(build_call(card_id), allowed)
    print(json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
