from dataclasses import dataclass, field
from typing import Any
import time
import uuid


@dataclass
class EventoSistema:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    tipo: str = ""

    origem: str = ""

    destino: str = ""

    dados: dict = field(default_factory=dict)

    prioridade: int = 0

    timestamp: float = field(default_factory=time.time)

    cancelado: bool = False

    resposta: Any = None
