import re

texts = ["YEAh, posted with_my_brother, yeah, he_got a MOP", "a special.text b lkdfjgkld,b", 
          "Power_to THE p0sitIVe pe-ple pleAse... push!!! your panic butt0n! :)", 
          "VO_VA aboba and biba aroma_aob Fein"]
# Task 1 

print("\nTask 1: \n")
for text in texts:
    a = re.search("a[b].*", text)
    print(a)

# Task 2

print("\nTask 2: \n")
for text in texts:
    a = re.search("a[b]{2,3}", text)
    print(a)

# Task 3

print("\nTask 3: \n")
for text in texts:
    a = re.findall("[a-z]+_[a-z]+", text)
    print(a)

# Task 4

print("\n Task 4: \n")
for text in texts:
    a = re.findall("[A-Z][a-z]+", text)
    print(a)

# Task 5

print("\nTask 5: \n")
for text in texts:
    print(re.search(r"[a].*[b]", text))

# Task 6

print("\nTask 6: \n")
for text in texts:
    print(re.sub(r"[,.]", ":", text))

# Task 7

print("\nTask 7: \n")
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if components: 
        camel_case_str = components[0] + ''.join(x.title() for x in components[1:])
    else:
        camel_case_str = ''
    return camel_case_str

text = "I_said_I_loved_but_I_lied_In_my_life_all_I_wanted_Was_the_keeping_of_someone_like_you"
print(snake_to_camel(text))

# Task 8

print("\nTask 8: \n")
def split_at_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)
print(split_at_uppercase("DoReMiFaSolLaSiDo"))

# Task 9

print("\nTask 9: \n")
def splif(s):
    return re.sub(r'(?<=[a-zA-Z])(?=[A-Z])', ' ', s)
print(splif("(NeverEndingPain)"))
print(splif("(QuicklyEndingLife)"))


# Task 10

print("\nTask 10: \n")
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(camel_to_snake("lookAtMe"))