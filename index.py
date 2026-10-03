def mostrar_cardapio():
    print("\n" + "="*40)
    print("           CARDÁPIO")
    print("="*40)
    print("Código  |  Produto               | Preço")
    print("--------|------------------------|-------")
    print("   1    |  X-Burguer             | R$ 18.00")
    print("   2    |  X-Salada              | R$ 15.50")
    print("   3    |  Batata Frita          | R$  8.00")
    print("   4    |  Refrigerante          | R$  5.00")
    print("   5    |  Milkshake             | R$ 12.00")
    print("--------|------------------------|-------")
    print("   0    |  FINALIZAR PEDIDO")
    print("="*40)

def obter_preco(codigo):
    if codigo == 1:
        return 18.00
    elif codigo == 2:
        return 15.50
    elif codigo == 3:
        return 8.00
    elif codigo == 4:
        return 5.00
    elif codigo == 5:
        return 12.00
    else:
        return None

def calcular_desconto(valor_total):
    if valor_total < 50.00:
        desconto = 0.0
        percentual = 0
    elif valor_total < 100.00:
        desconto = valor_total * 0.05
        percentual = 5
    else:
        desconto = valor_total * 0.10
        percentual = 10
    valor_final = valor_total - desconto
    return percentual, desconto, valor_final

def escolher_pagamento():
    print("\n--- FORMA DE PAGAMENTO ---")
    print("1 - Dinheiro")
    print("2 - PIX")
    print("3 - Cartão")
    opcao = input("Escolha a forma de pagamento: ")
    
    while opcao not in ["1", "2", "3"]:
        print("Opção inválida! Tente novamente.")
        opcao = input("Escolha a forma de pagamento: ")
    
    if opcao == "1":
        return "Dinheiro"
    elif opcao == "2":
        return "PIX"
    else:
        return "Cartão"

def main():
    print("="*40)
    print("   SISTEMA DE ATENDIMENTO — LANCHONETE")
    print("="*40)
    nome = input("Olá! Qual é o seu nome? ")
    
    total_compra = 0.0
    continuar = True
    
    while continuar:
        mostrar_cardapio()
        
        codigo_str = input("\nDigite o código do produto: ")
        
        if not codigo_str.isdigit():
            print("Digite apenas números!")
            continue
        
        codigo = int(codigo_str)
        
        if codigo == 0:
            continuar = False
            break
        
        preco = obter_preco(codigo)
        if preco is None:
            print("Código inválido! Tente novamente.")
            continue
        
        qtd_str = input(f"Quantas unidades? Preço: R$ {preco:.2f} — ")
        if not qtd_str.isdigit():
            print("Quantidade inválida!")
            continue
        
        quantidade = int(qtd_str)
        subtotal = preco * quantidade
        total_compra = total_compra + subtotal
        
        print(f"Adicionado! Total atual: R$ {total_compra:.2f}")
    
    if total_compra == 0:
        print(f"\nObrigado, {nome}! Volte sempre!")
        return
    
    percentual, valor_desconto, valor_final = calcular_desconto(total_compra)
    pagamento = escolher_pagamento()
    
    print("\n" + "="*40)
    print("         RESUMO DO PEDIDO")
    print("="*40)
    print(f"Cliente:          {nome}")
    print(f"Valor original:   R$ {total_compra:.2f}")
    print(f"Desconto ({percentual}%):      R$ {valor_desconto:.2f}")
    print(f"Valor final:      R$ {valor_final:.2f}")
    print(f"Pagamento:        {pagamento}")
    print("="*40)
    print("   Obrigado pela preferência!")
    print("="*40)

if __name__ == "__main__":
    main() 