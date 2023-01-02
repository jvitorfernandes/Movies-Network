from similar_users import jaccard_similarity, get_similar_users
from user_profile import UserProfile


def test_jaccard_similarity():
    set_a = {0, 1, 2, 3}
    set_aa = {0, 1, 2, 3}
    set_b = {5, 6, 7, 8}
    set_c = {0, 2, 5, 7}

    assert jaccard_similarity(set_a, set_aa) == 1, "sets are the same and should have similarity 1, but don't."
    assert jaccard_similarity(
        set_a, set_b) == 0, "sets are completely different and should have similarity 0, but don't."
    test_3 = jaccard_similarity(set_a, set_c)
    assert test_3 == 1/3, f"sets should have similarity 1/3 but have {test_3} instead"


def test_get_similar_users():
    similar_users = get_similar_users("jvfernandes")
    assert len(similar_users) == 5
    assert similar_users[0]["username"] == 'leslieshields43', 'Highest Jaccard score should be user leslieshields43'
