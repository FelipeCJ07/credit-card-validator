import unittest
import sys
import os

# Adiciona o diretório pai ao path para importar o módulo main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa as funções do arquivo main.py
from main import is_valid_luhn, identify_card_brand

class TestCardValidator(unittest.TestCase):
    
    def test_luhn_algorithm_valid_cards(self):
        """Testa o algoritmo de Luhn com números válidos"""
        valid_cards = [
            "4111111111111111",  # Visa
            "5555555555554444",  # MasterCard
            "378282246310005",   # American Express
            "30569309025904",    # Diners Club
            "6011111111111117",  # Discover
        ]
        
        for card in valid_cards:
            with self.subTest(card=card):
                self.assertTrue(is_valid_luhn(card), f"Cartão {card} deveria ser válido")
    
    def test_luhn_algorithm_invalid_cards(self):
        """Testa o algoritmo de Luhn com números inválidos"""
        invalid_cards = [
            "4111111111111112",  # Visa inválido
            "5555555555554445",  # MasterCard inválido
            "378282246310006",   # American Express inválido
            "1234567890123456",  # Número aleatório
        ]
        
        for card in invalid_cards:
            with self.subTest(card=card):
                self.assertFalse(is_valid_luhn(card), f"Cartão {card} deveria ser inválido")
    
    def test_visa_identification(self):
        """Testa identificação de cartões Visa"""
        visa_cards = [
            "4111111111111111",  # 16 dígitos
            "4000000000000",     # 13 dígitos
        ]
        
        for card in visa_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Visa")
    
    def test_mastercard_identification(self):
        """Testa identificação de cartões MasterCard"""
        mastercard_cards = [
            "5555555555554444",  # Prefixo 55
            "5105105105105100",  # Prefixo 51
            "2223000048400011",  # Novo prefixo 2223
        ]
        
        for card in mastercard_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "MasterCard")
    
    def test_amex_identification(self):
        """Testa identificação de cartões American Express"""
        amex_cards = [
            "378282246310005",   # Prefixo 37
            "341111111111111",   # Prefixo 34
        ]
        
        for card in amex_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "American Express")
    
    def test_diners_identification(self):
        """Testa identificação de cartões Diners Club"""
        diners_cards = [
            "30569309025904",    # Prefixo 305
            "38520000023237",    # Prefixo 38
        ]
        
        for card in diners_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Diners Club")
    
    def test_discover_identification(self):
        """Testa identificação de cartões Discover"""
        discover_cards = [
            "6011111111111117",  # Prefixo 6011
            "6500000000000002",  # Prefixo 65
        ]
        
        for card in discover_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Discover")
    
    def test_elo_identification(self):
        """Testa identificação de cartões Elo"""
        elo_cards = [
            "5067310000000010",  # Prefixo Elo
            "6362970000457013",  # Outro prefixo Elo
        ]
        
        for card in elo_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Elo")
    
    def test_hipercard_identification(self):
        """Testa identificação de cartões Hipercard"""
        hipercard_cards = [
            "6062820524845321",  # Prefixo 606282
        ]
        
        for card in hipercard_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Hipercard")
    
    def test_jcb_identification(self):
        """Testa identificação de cartões JCB"""
        jcb_cards = [
            "3530111333300000",  # Prefixo 353
            "3566002020360505",  # Prefixo 356
        ]
        
        for card in jcb_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "JCB")
    
    def test_unknown_brand(self):
        """Testa identificação de bandeiras desconhecidas"""
        unknown_cards = [
            "1234567890123456",  # Número que não corresponde a nenhuma bandeira
            "9999999999999999",  # Outro número desconhecido
        ]
        
        for card in unknown_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Desconhecida")
    
    def test_formatted_input(self):
        """Testa entrada com formatação (espaços, hífens)"""
        formatted_cards = [
            "4111 1111 1111 1111",   # Com espaços
            "4111-1111-1111-1111",   # Com hífens
            "4111.1111.1111.1111",   # Com pontos
        ]
        
        for card in formatted_cards:
            with self.subTest(card=card):
                self.assertEqual(identify_card_brand(card), "Visa")
    
    def test_empty_and_invalid_input(self):
        """Testa entradas vazias e inválidas"""
        invalid_inputs = [
            "",           # String vazia
            "abc",        # Apenas letras
            "12",         # Muito curto
        ]
        
        for card in invalid_inputs:
            with self.subTest(card=card):
                # Para entradas muito curtas ou inválidas, deve retornar Desconhecida
                result = identify_card_brand(card)
                self.assertEqual(result, "Desconhecida")

if __name__ == '__main__':
    # Executa os testes
    unittest.main(verbosity=2)

