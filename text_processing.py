#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""

import re

def normalize(input_string):

    normalized_string = input_string.lower().strip() #소문자화 + 왼/오른쪽 공백 제거
    normalized_string = re.sub(' +',' ',normalized_string) # 정규식을 활용해 1개 이상 공백은 1개 공백으로 처리
    
    return normalized_string


def no_vowels(input_string):
    no_voewl_string = re.sub('[aeiouAEIOU]','',input_string)
    
    return no_voewl_string

no_vowels("This is an example.")