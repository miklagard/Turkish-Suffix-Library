from turkish_suffix_library.turkish import Turkish

print(Turkish('it').present_continuous().adverb_verb_during_action())  # itiyorken
print(Turkish('gül').adverb_verb_after_action(negative=True))  # ölmeyince
print(Turkish('git').adverb_verb_after_action_alternative(negative=True))  # gitmeyip
print(Turkish('et').adverb_verb_without_action())  # etmeden
print(Turkish('yürü').adverb_verb_without_action_alternative())  # yürümeksizin
print(Turkish("ata").adverb_verb_by_action())  # atayarak
print(Turkish('anlat').adverb_verb_continuity())  # anlata anlata
print(Turkish('vur').adverb_verb_repeatedly())  # vurdukça
print(Turkish('ara').adverb_verb_since_action(negative=True))  # aramayalı
