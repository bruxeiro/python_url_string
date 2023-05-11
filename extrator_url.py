class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitizar_url(url)
        self.validar_url()

    @staticmethod
    def sanitizar_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validar_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interogacao = self.url.find("?")
        url_base = self.url[:indice_interogacao]
        return url_base

    def get_url_parametros(self):
        indice_interogacao = self.url.find("?")
        url_parametros = self.url[indice_interogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametros().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
