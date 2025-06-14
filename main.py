import re

def is_valid_luhn(card_number):
    """
    Verifica se o número do cartão de crédito é válido usando o algoritmo de Luhn.
    """
    digits = [int(d) for d in card_number if d.isdigit()]
    if not digits:
        return False

    total = 0
    num_digits = len(digits)
    is_second = False

    for i in range(num_digits - 1, -1, -1):
        digit = digits[i]

        if is_second:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        is_second = not is_second

    return total % 10 == 0

def identify_card_brand(card_number):
    """
    Identifica a bandeira do cartão de crédito com base no número.
    """
    # Remove quaisquer caracteres não numéricos
    card_number = re.sub(r'\D', '', card_number)

    # Verifica o comprimento do cartão
    length = len(card_number)

    # Padrões de bandeiras (prefixos e comprimentos)
    # Ordem é importante: padrões mais específicos devem vir antes dos mais gerais
    patterns = {
        'Visa': {'prefixes': ['4'], 'lengths': [13, 16]},
        'MasterCard': {'prefixes': ['51', '52', '53', '54', '55', '2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '223', '224', '225', '226', '227', '228', '229', '23', '24', '25', '26', '270', '271', '2720'], 'lengths': [16]},
        'American Express': {'prefixes': ['34', '37'], 'lengths': [15]},
        'Diners Club': {'prefixes': ['300', '301', '302', '303', '304', '305', '309', '36', '38', '39'], 'lengths': [14, 16]},
        'Discover': {'prefixes': ['6011', '622126', '622127', '622128', '622129', '62213', '62214', '62215', '62216', '62217', '62218', '62219', '6222', '6223', '6224', '6225', '6226', '6227', '6228', '62290', '62291', '622920', '622921', '622922', '622923', '622924', '622925', '644', '645', '646', '647', '648', '649', '65'], 'lengths': [16]},
        'Elo': {'prefixes': ['401178', '401179', '431274', '438935', '451416', '457631', '457632', '504175', '506699', '50670', '50671', '50672', '50673', '50674', '50675', '50676', '506770', '506771', '506772', '506773', '506774', '506775', '506776', '506777', '506778', '509', '627780', '636297', '636368', '6500', '6504', '6505', '6507', '6509', '6516', '6550'], 'lengths': [16]},
        'Hipercard': {'prefixes': ['38', '606282'], 'lengths': [13, 16]},
        'Aura': {'prefixes': ['50'], 'lengths': [16]},
        'JCB': {'prefixes': ['3528', '3529', '353', '354', '355', '356', '357', '358'], 'lengths': [16]},
        'EnRoute': {'prefixes': ['2014', '2149'], 'lengths': [15]},
        # 'Voyage': {'prefixes': [], 'lengths': []}, # Informações limitadas, não incluído na lógica direta
    }

    for brand, data in patterns.items():
        for prefix in data['prefixes']:
            if card_number.startswith(prefix) and length in data['lengths']:
                return brand

    return 'Desconhecida'

if __name__ == '__main__':
    print("Validador de Bandeiras de Cartão de Crédito")
    while True:
        card_input = input("Digite o número do cartão (ou 'sair' para encerrar): ")
        if card_input.lower() == 'sair':
            break

        # Limpa o input para conter apenas dígitos
        cleaned_card_number = re.sub(r'\D', '', card_input)

        if not cleaned_card_number:
            print("Por favor, digite um número de cartão válido.")
            continue

        if is_valid_luhn(cleaned_card_number):
            brand = identify_card_brand(cleaned_card_number)
            print(f"O número do cartão {card_input} é válido (Luhn) e a bandeira é: {brand}")
        else:
            print(f"O número do cartão {card_input} é inválido (Luhn).")


