class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' is not remetente:
            raise EmailInvalido(f'Email de remetente inválido {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass