"""Demonstração local de autorização de chamadas de ferramenta."""

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Principal:
    user_id: str
    can_close_tickets: bool


@dataclass
class Ticket:
    owner_id: str
    status: str = "aberto"


def dispatch(principal, tool_name, arguments, tickets):
    """Valida a proposta antes de modificar qualquer chamado em memória."""
    if tool_name != "close_ticket":
        return "Negado: ferramenta desconhecida."

    if not isinstance(arguments, dict) or arguments.keys() != {"ticket_id"}:
        return "Negado: argumentos inválidos."

    ticket_id = arguments["ticket_id"]
    if not isinstance(ticket_id, str) or not ticket_id:
        return "Negado: argumentos inválidos."

    ticket = tickets.get(ticket_id)
    if not principal.can_close_tickets or ticket is None or ticket.owner_id != principal.user_id:
        return "Negado: solicitante sem permissão para esse chamado."

    ticket.status = "fechado"
    return "Permitido: chamado fechado."


SCENARIOS = {
    "autorizado": Principal("ana", True),
    "outro-titular": Principal("bruno", True),
    "sem-permissao": Principal("ana", False),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cenario", choices=SCENARIOS, required=True)
    args = parser.parse_args()

    tickets = {"CH-01": Ticket(owner_id="ana")}
    print("Antes:", tickets["CH-01"].status)
    decision = dispatch(SCENARIOS[args.cenario], "close_ticket", {"ticket_id": "CH-01"}, tickets)
    print(decision)
    print("Depois:", tickets["CH-01"].status)


if __name__ == "__main__":
    main()
