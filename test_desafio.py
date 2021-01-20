import pytest
import desafio_stone

d = desafio_stone

#Teste automatizado pelo pytest
def test_calculate():
    #Test 1 - Empty Itens List
    assert d.calculate([],['a@bol.com.br']) == -1

    #Test 2 - Empty E-mails List
    assert d.calculate([['a', 1, 2.00]],[]) == -1

    #Test 3 - List of 1 item and 1 e-mail
    assert d.calculate([['a', 8, 284]],['a@hotmail.com']) == {'a@hotmail.com': 2272}

    #Test 4 - List of 5 itens and 1 e-mail
    assert d.calculate([['a', 1, 200], ['b', 2, 100], ['c', 3, 500], ['d', 4, 450],
                      ['e', 3, 15]],['b@hotmail.com']) == {'b@hotmail.com': 3745}

    #Test 5 - List of 2 itens and 2 e-mails
    assert d.calculate([['a', 5, 299], ['b', 9, 112]],['a@gmail.com','b@hotmail.com']) == {'a@gmail.com': 1251,'b@hotmail.com': 1252}


    #Test 6 - List of 10 itens and 3 e-mails
    assert d.calculate([['a', 1, 201], ['b', 2, 100], ['c', 3, 500], ['d', 4, 450],['e', 3, 15],
                      ['f', 8, 5], ['g', 7, 200], ['h', 3, 517], ['i', 5, 499], ['j', 6, 297]], 
                      ['a@gmail.com', 'b@hotmail.com', 'c@bol.com']) == {'a@gmail.com': 3671, 'b@hotmail.com': 3671, 'c@bol.com': 3672}

    #Test 7 - List of 20 itens and 7 e-mails
    assert d.calculate([['a', 1, 201], ['b', 2, 100], ['c', 3, 500], ['d', 4, 450],['e', 3, 15], 
                      ['f', 8, 5], ['g', 7, 200], ['h', 3, 515], ['i', 5, 499], ['j', 6, 298], 
                      ['k', 15, 199], ['l', 7, 80], ['m', 3, 620], ['n', 12, 499], ['o', 20, 2], 
                      ['p', 1, 5], ['q', 2, 600], ['r', 4, 915], ['s', 2, 396], ['t', 8, 156]], 
                      ['a@gmail.com', 'b@hotmail.com', 'c@bol.com', 'd@gmail.com', 'e@hotmail.com', 'f@bol.com', 'g@gmail.com']) == {
                          'a@gmail.com': 4193, 'b@hotmail.com': 4193, 'c@bol.com': 4193, 'd@gmail.com': 4193, 'e@hotmail.com': 4193, 'f@bol.com': 4193, 'g@gmail.com': 4194}

