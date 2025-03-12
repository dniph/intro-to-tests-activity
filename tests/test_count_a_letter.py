from main import count_a_letter
import pytest

# Probar si la letra se repite varias veces en mi nombre 
def test_count_multiple_ocurrences():
    sentence = "Dennif"
    letter = "n"
    
    # Act
    result = count_a_letter(sentence, letter)
    print("result must be 2")
    # Assert
    assert result == 2
    
#Test if it has 0 ocurrences
def test_count_xero_ocurrences():
    sentence = "Dennif"
    letter = "z"
    
    result = count_a_letter(sentence, letter)
    print("Result must fail because is not z i de sentence Dennif")
    
    assert result == 0