# or parsing helpers like star ratings

def get_star_rating(class_string):
    stars = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    for k, v in stars.items():
        if k in class_string:
            return v
    return 0
