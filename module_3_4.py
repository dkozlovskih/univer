def single_root_words (root_word, *other_words):
    same_words = []
    for i in other_words:
#        if root_word.lower().count(i.lower()) or i.lower().count(root_word.lower()):
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return (same_words)


 # single_root_words()
result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)