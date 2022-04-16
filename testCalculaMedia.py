import unittest
import calculaMedia

class testCalculaMedia (unittest.TestCase):
    def test_ct01(self):
        ap1 = -0.01
        ap2 = 5
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Entrada inválida, a AP1 tem valor negativo.")

    def test_ct02(self):
        ap1 = 10.01
        ap2 = 5
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Entrada inválida, a AP1 tem valor maior que 10.")

    def test_ct03(self):
        ap1 = 5
        ap2 = -0.01
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Entrada inválida, a AP2 tem valor negativo.")

    def test_ct04(self):
        ap1 = 5
        ap2 = 10.01
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Entrada inválida, a AP2 tem valor maior que 10.")
    
    def test_ct05(self):
        ap1 = 5
        ap2 = "a"
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Entrada inválida, a entrada não é um número.")
    
    def test_ct06(self):
        ap1 = "a"
        ap2 = 5
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Entrada inválida, a entrada não é um número.")

    def test_ct07(self):
        ap1 = 3.9
        ap2 = 3.9
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno reprovado.")

    def test_ct08(self):
        ap1 = 0.01
        ap2 = 0.01
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno reprovado.")

    def test_ct09(self):
        ap1 = 7.9
        ap2 = 7.9
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno precisa fazer PF.")

    def test_ct10(self):
        ap1 = 0
        ap2 = 0
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno reprovado.")

    def test_ct11(self):
        ap1 = 10
        ap2 = 10
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno aprovado.")
    
    def test_ct12(self):
        ap1 = 4
        ap2 = 4
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno precisa fazer PF.")

    def test_ct13(self):
        ap1 = 8
        ap2 = 8
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno aprovado.")

    def test_ct14(self):
        ap1 = 8.01
        ap2 = 8.01
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno aprovado.")

    def test_ct15(self):
        ap1 = 4.01
        ap2 = 4.01
        self.assertEqual(calculaMedia.calculaMedia(ap1, ap2), "Aluno precisa fazer PF.")

if __name__ == '__main__':
    unittest.main()