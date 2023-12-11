# String Closest Match Filter
## Filter to get a closest match string from a sequence (touple, list) with high accuracy
### #Features
- works with any type of delimiters
- customizeable accuracy
- very fast and smooth

#### Simple Example
```sh
from StringClosestMatchFilter import get_closest_match_from_sequence

query = "ahmd mos"
list_of_names = ["ahmed gamal", "ahmed mostafa", "ebrahim", "ashraf", "youssef alkhodary", "yahya alkhodary", "mousa ahmed", "moataz gamal"]
result = get_closest_match_from_sequence(query, list_of_names, accuracy=0.8) #Default accuracy is 0.7
print(result)
```

#### output: 'ahmed mostafa'


#### Example With Delimiters
```sh
from StringClosestMatchFilter import get_closest_match_from_sequence

query = "mostfa"
list_of_names = ["ahmed, gamal", "ahmed.mostafa", "ebrahim", "ashraf", "youssef alkhodary", "yahya alkhodary", "mousa ahmed", "moataz gamal"]
result = get_closest_match_from_sequence(query, list_of_names, accuracy=0.8) #Default accuracy is 0.7
print(result)
```

#### output: 'ahmed.mostafa'
