from StringsClosestMatchFilter import get_closest_match_from_sequence

if __name__ == "__main__":
    string_tuple = ("youssef alkhodary", "abdallah.marzouq", "hisham gamal", "moaz mobarak", "yahya, alkhodary", "moataz gamal", "mousa ahmed", "حسن عماد")
    print(get_closest_match_from_sequence("mousa", string_tuple))