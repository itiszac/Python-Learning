print('Enter a noun (thing):')
noun_thing = input().lower()
print('Enter a noun (place):')
noun_place = input().lower()
print('Enter an adverb:')
adverb = input().lower()
print('Enter another noun (person)')
noun_person = input().lower()
print('Enter a adjective (state of emotion):')
adjective = input().lower()

mad_lib = f'The {noun_thing} went to the {noun_place} really {adverb}. {noun_person} was very {adjective} that his ' \
    f'{noun_thing} was so {adverb}.'

print(mad_lib)