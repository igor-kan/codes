"""Gale-Shapley stable matching (CLRS 2.3-8 / classic)."""
def stable_marriage(men_prefs: dict[str, list[str]],
                    women_prefs: dict[str, list[str]]) -> dict[str, str]:
    rank = {woman: {man: i for i, man in enumerate(prefs)}
            for woman, prefs in women_prefs.items()}
    free = list(men_prefs)
    next_choice = {man: 0 for man in men_prefs}
    engaged: dict[str, str] = {}   # woman -> man
    while free:
        man = free.pop(0)
        woman = men_prefs[man][next_choice[man]]
        next_choice[man] += 1
        if woman not in engaged:
            engaged[woman] = man
        elif rank[woman][man] < rank[woman][engaged[woman]]:
            free.append(engaged[woman])
            engaged[woman] = man
        else:
            free.append(man)
    return {man: woman for woman, man in engaged.items()}


if __name__ == "__main__":
    men = {"a": ["x", "y", "z"], "b": ["y", "x", "z"], "c": ["x", "y", "z"]}
    women = {"x": ["c", "b", "a"], "y": ["a", "b", "c"], "z": ["a", "b", "c"]}
    matching = stable_marriage(men, women)
    assert matching == {"a": "y", "b": "z", "c": "x"}
    print("stable marriage ok")
