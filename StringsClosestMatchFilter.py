import difflib
import re


def covert_to_portions_with_delimiters(stock):
    # don't add (.) in delimeters
    delimeters = ' |,|:|\\|/|;'
    except_delimiter = '.'
    edited_stock = []
    edited_stock.append(re.split(delimeters, stock))
    if except_delimiter in stock:
        edited_stock.append(stock.split(except_delimiter))
    return edited_stock, stock


def covert_to_portions_with_re(stock):
    edited_stock = []
    for i in re.findall(r'[\w+]+', stock):
        edited_stock.append(i)

    return edited_stock, stock


def get_closest_match_from_sequence(query, options, accuracy=0.7):
    all_closest = []
    for index in options:
        n_options, native = covert_to_portions_with_delimiters(index)
        for options in n_options:
            closest_match = difflib.get_close_matches(query, options, n=1, cutoff=accuracy)
            if closest_match:
                all_closest.append(native)
        n_options, native = covert_to_portions_with_re(index)
        closest_match = difflib.get_close_matches(query, n_options, n=1, cutoff=accuracy)
        if closest_match:
            all_closest.append(native)
    result = difflib.get_close_matches(query, all_closest, n=1)
    if result:
        return result[0]
