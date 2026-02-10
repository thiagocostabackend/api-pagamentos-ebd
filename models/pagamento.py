from datetime import date

class Pagamento: #Representa um pagamento realizado por uma matrícula da EBD
    formas_pagamento_validas = ["PIX", "ESPECIE"]
    def __init__(
            self,
            id_matricula: int,
            valor_pago : float,
            data_pagamento : date,
            forma_pagamento : str
    ):
        self.id_pagamento = None
        self.id_matricula = id_matricula
        self.valor_pago = valor_pago
        self.data_pagamento = data_pagamento
        self.forma_pagamento = forma_pagamento

        self._validar()

    def _validar(self):
        if not isinstance(self.id_matricula, int) or self.id_matricula <= 0:
            raise ValueError("Id matrícula de ser um número inteiro válido")
        if self.valor_pago <= 0:
            raise ValueError("Valor pago deve ser maior doque zero")
        if not isinstance(self.data_pagamento, date):
            raise ValueError("data_pagamento deve ser tipo date")
        if self.forma_pagamento not in self.formas_pagamento_validas:
            raise ValueError(
                f"forma_pagamento inválida. Use {self.formas_pagamento_validas} "
                )