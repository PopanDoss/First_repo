
# def discount_price(price, discount):

#     if discount>0 and discount<=1 :
#         def apply_discount():
#             nonlocal price
#             return price*(1-discount)
#     apply_discount()
#     return price

# print(discount_price(100,0.5))

# def func_outer(a,b):

#     def func_inner():
#         nonlocal a
#         a= a*(1-b)

#     func_inner()
#     return a

# result = func_outer(4,0.05)
# print(result)


# def discount_price(price, discount):

#     if discount>0 and discount<=1 :
#         def apply_discount():
#             nonlocal price
#             price = price*(1-discount)
#     apply_discount()
#     return price

# print(discount_price(100,0.5))


# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name !="":
#         return(f"{first_name }{last_name }{middle_name}")
#     else:
#         return(f"{first_name} {last_name}")
    
# print(get_fullname("Serg","Sergiy","Pavlov")) 

# def format_string(string, length):
#     if len(string)>=length:
#         return string
#     return ((length - len(string)) // 2) *" " + string
    

# print(format_string("tartar", 20))



# def first(size, *arg):
#     size = size + len(arg) 
#     return size

# def second(size, **kwarg):
#     return size + len(kwarg)
    
# print(first(5, "first", "second", "third"))  # Результат: 8
# print(first(1, "Alex", "Boris"))             # Результат: 3
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    if k < 2 :
        return 1
    else:
        c = factorial(n) / (factorial(n-k) * factorial(k))
        return c

print(number_of_groups(50,2))