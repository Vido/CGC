import unittest
from validador import valida_cep

class TestValidaCep(unittest.TestCase):

    def test_cep(self):
        input_list = [
            '121426',
            '523563',
            '552523', # Exemplos do enunciado
            '',
            '12345',
            '1234567',
            '12345A', # Testa Regex
            '112233',
            '012345', # < 100.000
        ]
        output_list = [
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            True,
            False,
        ]

        for ipt, opt in zip(input_list, output_list):
            self.assertEqual(valida_cep(ipt), opt)

if __name__ == '__main__':
    unittest.main()
