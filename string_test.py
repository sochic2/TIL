#pyformat
'{} {}'.format('one', 'two')

name = '남기'
e_name = 'key'
print('안녕하세요. {1}입니다. My name is {0}'.format(name, e_name))


# f-string python 3.6 최신버전
print(f'안녕하세요. {name}입니다. My name is {e_name}')

#lotto
import random
numbers = range(1,46)


lotto = random.sample(numbers,6)
print(f"이번주 로또번호는 {sorted(lotto)}입니다")
'\n'
#string 또다른방법
name = "남기철"
print("안녕하세요. " + name + "입니다.")


'\n'
#파일명 바꾸기
