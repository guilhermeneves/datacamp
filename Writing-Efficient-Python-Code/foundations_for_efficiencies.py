import this ## The Zen of Python, by Tim Peters

#Iterators
class oddNumbersIter:

  def __iter__(self):
    self.num = 1
    return self

  def __next__(self):
    num = self.num
    self.num += 2
    return num

impar = iter(oddNumbersIter())
print(next(impar))
print(next(impar))
print(next(impar))
print(next(impar))

#Enumerate

states = ['SP', 'RJ', 'PR', 'MA']
indexed_states = enumerate(states)
indexed_states_starting_from = enumerate(states,5)
list_indexed_states = list(indexed_states)
list_indexed_states_starting_from = list(indexed_states_starting_from)
print(list_indexed_states)
print(list_indexed_states_starting_from)

#Map

#With a Built-in Function
states_lower_case = list(map(str.lower, states))
print(states_lower_case)

#With a Custom Anonymous Function
states_with_preffix = list(map(lambda state: 'Brazil ' + state, states))
print(states_with_preffix)