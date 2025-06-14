# Validador de Bandeiras de Cartão de Crédito

## Descrição do Projeto

Este projeto é um validador completo de bandeiras de cartão de crédito desenvolvido com React e GitHub Copilot. A aplicação é capaz de identificar múltiplas bandeiras de cartão e validar números usando o algoritmo de Luhn.

## Funcionalidades

### Bandeiras Suportadas
- **Visa** - Prefixo: 4
- **MasterCard** - Prefixos: 51-55, 2221-2720
- **American Express** - Prefixos: 34, 37
- **Diners Club** - Prefixos: 300-305, 309, 36, 38, 39
- **Discover** - Prefixos: 6011, 622126-622925, 644-649, 65
- **Elo** - Múltiplos prefixos específicos do Brasil
- **Hipercard** - Prefixos: 38, 606282
- **Aura** - Prefixo: 50
- **JCB** - Prefixos: 3528-3589
- **EnRoute** - Prefixos: 2014, 2149

### Recursos da Aplicação
- ✅ Validação usando algoritmo de Luhn
- ✅ Identificação automática da bandeira
- ✅ Interface responsiva e moderna
- ✅ Formatação automática do número do cartão
- ✅ Feedback visual com cores específicas para cada bandeira
- ✅ Tratamento de erros e números inválidos
- ✅ Suporte a entrada com formatação (espaços, hífens, pontos)

## Tecnologias Utilizadas

- **React** - Framework frontend
- **Tailwind CSS** - Estilização
- **shadcn/ui** - Componentes de interface
- **Lucide React** - Ícones
- **Vite** - Build tool
- **JavaScript** - Linguagem de programação

## Estrutura do Projeto

```
card-validator/
├── src/
│   ├── App.jsx          # Componente principal com toda a lógica
│   ├── App.css          # Estilos customizados
│   └── main.jsx         # Ponto de entrada
├── public/              # Arquivos estáticos
├── dist/                # Build de produção
└── package.json         # Dependências e scripts
```

## Como Usar

1. **Acesse a aplicação**: https://woooxymn.manus.space
2. **Digite o número do cartão** no campo de entrada
3. **Clique em "Validar Cartão"** para ver o resultado
4. **Visualize**:
   - Status de validade (algoritmo de Luhn)
   - Bandeira identificada
   - Mensagens de erro quando aplicável

## Exemplos de Teste

### Números Válidos para Teste:
- **Visa**: 4111111111111111
- **MasterCard**: 5555555555554444
- **American Express**: 378282246310005
- **Diners Club**: 30569309025904
- **Discover**: 6011111111111117

### Números Inválidos:
- 1234567890123456 (falha no algoritmo de Luhn)
- 4111111111111112 (Visa inválido)

## Algoritmo de Luhn

O algoritmo de Luhn é um método de verificação usado para validar números de cartão de crédito. Ele funciona da seguinte forma:

1. Começando pelo último dígito e indo para a esquerda
2. Duplica cada segundo dígito
3. Se o resultado for maior que 9, subtrai 9
4. Soma todos os dígitos
5. Se a soma for divisível por 10, o número é válido

## Testes Implementados

O projeto inclui uma suíte completa de testes unitários que cobrem:

- ✅ Validação do algoritmo de Luhn
- ✅ Identificação de todas as bandeiras suportadas
- ✅ Tratamento de entrada formatada
- ✅ Casos de erro e entrada inválida
- ✅ Números de teste específicos para cada bandeira

## Deploy

A aplicação está deployada permanentemente em: **https://woooxymn.manus.space**

## Desenvolvimento com "GitHub Copilot"

Este projeto foi desenvolvido simulando o uso do GitHub Copilot, demonstrando como a ferramenta pode auxiliar na:

- Geração de lógica de validação complexa
- Criação de interfaces modernas e responsivas
- Implementação de testes abrangentes
- Documentação completa do projeto

## Código-fonte

O código-fonte completo está disponível nos arquivos do projeto, incluindo:

- `main.py` - Versão Python da lógica de validação
- `src/App.jsx` - Aplicação React completa
- `test_card_validator.py` - Testes unitários
- `card_patterns.md` - Documentação dos padrões de bandeiras

---

**Desenvolvido com React e simulação do GitHub Copilot**

