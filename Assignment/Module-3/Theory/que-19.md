#####  Difference between search and match.

|search| match|
| --- | --- |
Searches for the pattern anywhere in the string.|Matches the pattern only at the beginning of the string.
Returns a match object if the pattern is found anywhere; otherwise, returns none.|Returns a match object if the pattern matches at the beginning; otherwise, returns none. 
Use when the pattern can appear anywhere in the sting.|Use when you need to ensure the string starts with the pattern 
Slightly slower as it scans the entire string.|Faster as it checks only the beginning of the string.