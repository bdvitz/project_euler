import requests

# projecteuler.net solutions
def solution0022(names: list) -> int:
    """ Return sum(position in alphabet) * position in names list """
    letter_value = {char:ord(char)-ord('A')+1 for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    names.sort()
    total = 0
    
    # define function for summing character values
    def char_sum(word: str) -> int:
        """ sum of characters positions in the alphabet """
        return sum(letter_value[char] for char in word)
    
    # loop through the names, summing calculated score for each name
    for i, name in enumerate(names):
        total += (i+1) * char_sum(name)
    
    return total

def retrieve_text(url = "https://projecteuler.net/resources/documents/0022_names.txt") -> list:
    """ Retrieves text from the given URL for problem input text """
    response = requests.get(url)
    if response.status_code == 200:
        s = response.text
        return s[1:len(s)-1].split('","')
    return []

if __name__ == "__main__":
    print(solution0022(retrieve_text()))
    