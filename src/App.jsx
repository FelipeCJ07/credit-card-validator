import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { CreditCard, CheckCircle, XCircle, AlertCircle } from 'lucide-react'
import './App.css'

// Função para validar usando algoritmo de Luhn
function isValidLuhn(cardNumber) {
  const digits = cardNumber.replace(/\D/g, '').split('').map(Number)
  if (digits.length === 0) return false

  let total = 0
  let isSecond = false

  for (let i = digits.length - 1; i >= 0; i--) {
    let digit = digits[i]

    if (isSecond) {
      digit *= 2
      if (digit > 9) {
        digit -= 9
      }
    }
    total += digit
    isSecond = !isSecond
  }

  return total % 10 === 0
}

// Função para identificar a bandeira do cartão
function identifyCardBrand(cardNumber) {
  const cleanNumber = cardNumber.replace(/\D/g, '')
  const length = cleanNumber.length

  // Padrões de bandeiras (ordem é importante: mais específicos primeiro)
  const patterns = {
    'Visa': { prefixes: ['4'], lengths: [13, 16] },
    'MasterCard': { 
      prefixes: ['51', '52', '53', '54', '55', '2221', '2222', '2223', '2224', '2225', '2226', '2227', '2228', '2229', '223', '224', '225', '226', '227', '228', '229', '23', '24', '25', '26', '270', '271', '2720'], 
      lengths: [16] 
    },
    'American Express': { prefixes: ['34', '37'], lengths: [15] },
    'Diners Club': { prefixes: ['300', '301', '302', '303', '304', '305', '309', '36', '38', '39'], lengths: [14, 16] },
    'Discover': { 
      prefixes: ['6011', '622126', '622127', '622128', '622129', '62213', '62214', '62215', '62216', '62217', '62218', '62219', '6222', '6223', '6224', '6225', '6226', '6227', '6228', '62290', '62291', '622920', '622921', '622922', '622923', '622924', '622925', '644', '645', '646', '647', '648', '649', '65'], 
      lengths: [16] 
    },
    'Elo': { 
      prefixes: ['401178', '401179', '431274', '438935', '451416', '457631', '457632', '504175', '506699', '50670', '50671', '50672', '50673', '50674', '50675', '50676', '506770', '506771', '506772', '506773', '506774', '506775', '506776', '506777', '506778', '509', '627780', '636297', '636368', '6500', '6504', '6505', '6507', '6509', '6516', '6550'], 
      lengths: [16] 
    },
    'Hipercard': { prefixes: ['38', '606282'], lengths: [13, 16] },
    'Aura': { prefixes: ['50'], lengths: [16] },
    'JCB': { prefixes: ['3528', '3529', '353', '354', '355', '356', '357', '358'], lengths: [16] },
    'EnRoute': { prefixes: ['2014', '2149'], lengths: [15] }
  }

  for (const [brand, data] of Object.entries(patterns)) {
    for (const prefix of data.prefixes) {
      if (cleanNumber.startsWith(prefix) && data.lengths.includes(length)) {
        return brand
      }
    }
  }

  return 'Desconhecida'
}

// Função para formatar o número do cartão
function formatCardNumber(value) {
  const cleanValue = value.replace(/\D/g, '')
  const groups = cleanValue.match(/.{1,4}/g) || []
  return groups.join(' ').substr(0, 19) // Máximo de 16 dígitos + 3 espaços
}

function App() {
  const [cardNumber, setCardNumber] = useState('')
  const [result, setResult] = useState(null)

  const handleInputChange = (e) => {
    const formatted = formatCardNumber(e.target.value)
    setCardNumber(formatted)
    
    // Limpa o resultado quando o usuário está digitando
    if (result) {
      setResult(null)
    }
  }

  const validateCard = () => {
    const cleanNumber = cardNumber.replace(/\D/g, '')
    
    if (cleanNumber.length < 13) {
      setResult({
        isValid: false,
        brand: 'Desconhecida',
        message: 'Número do cartão muito curto'
      })
      return
    }

    const isValid = isValidLuhn(cleanNumber)
    const brand = identifyCardBrand(cleanNumber)

    setResult({
      isValid,
      brand,
      message: isValid ? 'Número válido' : 'Número inválido (falha no algoritmo de Luhn)'
    })
  }

  const getBrandColor = (brand) => {
    const colors = {
      'Visa': 'bg-blue-100 text-blue-800 border-blue-200',
      'MasterCard': 'bg-red-100 text-red-800 border-red-200',
      'American Express': 'bg-green-100 text-green-800 border-green-200',
      'Diners Club': 'bg-purple-100 text-purple-800 border-purple-200',
      'Discover': 'bg-orange-100 text-orange-800 border-orange-200',
      'Elo': 'bg-yellow-100 text-yellow-800 border-yellow-200',
      'Hipercard': 'bg-pink-100 text-pink-800 border-pink-200',
      'Aura': 'bg-indigo-100 text-indigo-800 border-indigo-200',
      'JCB': 'bg-cyan-100 text-cyan-800 border-cyan-200',
      'EnRoute': 'bg-gray-100 text-gray-800 border-gray-200',
      'Desconhecida': 'bg-gray-100 text-gray-800 border-gray-200'
    }
    return colors[brand] || colors['Desconhecida']
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-2xl mx-auto pt-8">
        <div className="text-center mb-8">
          <div className="flex justify-center items-center gap-3 mb-4">
            <CreditCard className="h-8 w-8 text-blue-600" />
            <h1 className="text-3xl font-bold text-gray-900">Validador de Cartão de Crédito</h1>
          </div>
          <p className="text-gray-600">
            Identifique a bandeira e valide números de cartão de crédito usando o algoritmo de Luhn
          </p>
        </div>

        <Card className="shadow-lg">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <CreditCard className="h-5 w-5" />
              Validação de Cartão
            </CardTitle>
            <CardDescription>
              Digite o número do cartão de crédito para identificar a bandeira e validar
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="space-y-2">
              <label htmlFor="card-input" className="text-sm font-medium text-gray-700">
                Número do Cartão
              </label>
              <Input
                id="card-input"
                type="text"
                placeholder="1234 5678 9012 3456"
                value={cardNumber}
                onChange={handleInputChange}
                className="text-lg font-mono"
                maxLength={19}
              />
            </div>

            <Button 
              onClick={validateCard} 
              className="w-full"
              disabled={cardNumber.replace(/\D/g, '').length < 13}
            >
              Validar Cartão
            </Button>

            {result && (
              <div className="space-y-4 p-4 bg-gray-50 rounded-lg border">
                <div className="flex items-center justify-between">
                  <span className="font-medium text-gray-700">Status:</span>
                  <div className="flex items-center gap-2">
                    {result.isValid ? (
                      <CheckCircle className="h-5 w-5 text-green-600" />
                    ) : (
                      <XCircle className="h-5 w-5 text-red-600" />
                    )}
                    <span className={`font-medium ${result.isValid ? 'text-green-600' : 'text-red-600'}`}>
                      {result.message}
                    </span>
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <span className="font-medium text-gray-700">Bandeira:</span>
                  <Badge className={getBrandColor(result.brand)}>
                    {result.brand}
                  </Badge>
                </div>

                {result.brand === 'Desconhecida' && (
                  <div className="flex items-start gap-2 p-3 bg-yellow-50 border border-yellow-200 rounded-md">
                    <AlertCircle className="h-5 w-5 text-yellow-600 mt-0.5" />
                    <div className="text-sm text-yellow-800">
                      <p className="font-medium">Bandeira não reconhecida</p>
                      <p>O número pode ser de uma bandeira não suportada ou estar incorreto.</p>
                    </div>
                  </div>
                )}
              </div>
            )}
          </CardContent>
        </Card>

        <div className="mt-8 text-center text-sm text-gray-500">
          <p>
            Este validador suporta: Visa, MasterCard, American Express, Diners Club, 
            Discover, Elo, Hipercard, Aura, JCB e EnRoute
          </p>
          <p className="mt-2">
            Desenvolvido com React e simulação do GitHub Copilot
          </p>
        </div>
      </div>
    </div>
  )
}

export default App

