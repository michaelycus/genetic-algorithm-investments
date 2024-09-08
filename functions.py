def validate_currency_entry(text):
    # Verifica se o valor é vazio (permite deletar todo o conteúdo)
    if text == "":
        return True

    # Permite apenas números e uma única vírgula
    try:
        # Substitui a vírgula por um ponto para validação de float
        float(text.replace(",", "."))
        # Verifica se o valor tem no máximo uma vírgula
        if text.count(",") <= 1:
            # Verifica se há no máximo duas casas decimais
            if len(text.split(",")[1]) <= 2 if "," in text else True:
                return True
        return False
    except ValueError:
        return False
