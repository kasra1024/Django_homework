# def func (ch) : 
#     if "0" <= ch <= "9" : 
#         print ("your char is number")
#     elif "A" <= ch <= "Z" : 
#         print ("your char is uppercase lether")
#     elif "a" <= ch <= "z" : 
#         print ("your char is lowercase lether")
#     else : 
#         print ("other")
# x = input ("ch:")
# func (x) 
# --------------------------------------------------------------------
# def discount (rate , price) :
#     dicount_rate = int (price * rate / 100)
#     new_price = price - dicount_rate
#     print ("dicount_rate :" , dicount_rate)
#     print ("new_price :" , new_price )
# rate = int (input ("rate:")) 
# price = int (input("price:"))  
# discount (rate , price)
# ---------------------------------------------------------------------p
# def square (n) : 
#     for i in range (1,n) : 
#         if i ** 2 == n : 
#             print (f"yes! , {i} * {i} == {n}") 
#             break 
#     else : 
#         print ("noooooo!") 
# x = int (input ("x:"))
# square(x) 
# ------------------------------------------------------------------------
# def sum2 (it) : 
#     s = 0 
#     for i in it : 
#         s += i
#     return s 
# print (sum2 ((1,2,3)))
# --------------------------------------------------------------------------
# def max2 (*args) : 
#     m = args[0]
#     for i in args : 
#         if i > m : 
#             m = i 
#     return m 
# def min2 (*args) : 
#     n = float("+inf") 
#     for i in args : 
#         if i < n : 
#             n = i 
#     return n 
# print (max2 (1,12,122,143))
# print (min2 (1,12,122,143))
# -----------------------------------------------------------------------------
# def len2 (it) : 
#     counter = 0 
#     for i in it : 
#         counter += 1 
#     return counter 
# s = "kasra is best firend ro"
# print (len2(s))
# -------------------------------
# def max2 (*args) : 
#     s =float ('-inf')
#     for i in args  : 
#         if i > s :
#             s = i 
#     return s 
# def min2 (*args) : 
#     m = float ('+inf') 
#     for i in args : 
#         if i < m : 
#             m = i 
#     return m 
# print (max2(123,23424,2341,34143,1243,134,234144))
# print (min2(123,23424,2341,34143,1243,134,234144))
# # -----------------------------------------------------------
# def sum2 (it) : 
#     s = 0 
#     for i in it : 
#         s += i 
#     return s 
# print (sum2 ((1,2,3,4))) 
# ---------------------------------------------------------------
# def square (n) : 
#     for i in range(1,n) : 
#         if i **2 ==n : 
#             print (f"yes! . {i} * {i} == {n}")
#             break 
#     else : 
#         print ("no") 
# x = int (input ("x:"))
# square (x)             
# ---------------------------------------------------------------
# def discount (rate , price) : 
#     discount_rate = int (price * rate /100)  
#     new_price = price - discount_rate 
#     print ("discount_rate:" , discount_rate)
#     print ("new_price :" , new_price)
# rate = int (input ("rate : "))
# price = int (input ("price"))
# discount (rate , price)
# -----------------------------------------------------------------
# def char (ch) : 
#     if "a" <= ch <= "z" : 
#         print ("lower lether")
#     elif "A" <= ch <= "z" : 
#         print ("unperr lether ")
#     elif "0" <= ch <= "9" : 
#         print ("numbers")
#     else : 
#         print ("other!!!")
# ch = (input ("ch:")) 
# char(ch)
# ---------------------------------------------------------
# lst = [1,23,342,22,33,44,241,124,456,574,56,455,33,55553,345,1]
# print ("list :" ,len (lst))
# ood =len (list(filter (lambda x : x % 2 != 0 , lst )))
# print ("ood :" , (ood)) 
# even = len(list (filter (lambda x : x%2 == 0 , lst)))
# print ("even :" ,( even)) 
# ---------------------------------------------------------------
# s = "fateme" 
# starts_with = lambda s : True if s.startswith("a") else False
# print (starts_with(s))
# -------------------------------------------------------------------
# is_num = lambda s : s.replace ("." , "",1).isdigit()
# print (is_num ("4.12"))
# print (is_num ("12"))
# print (is_num ("afds3421"))
# -------------------------------------------------------------------
# s = "kasra" 
# starts_with = lambda s : True if s.startswith("k") else False
# print (starts_with(s))
# -------------------------------------------------------------------
# s = "deth" 
# starts_with = lambda s : True if s.startswith("d") else False 
# print (starts_with(s))
# ---------------------------------------------------------------------
# users = {"kasra" : "123413" , "darya" : "13412341234" , "dorsa11" : "af1234134"}
# from functools import wraps 
# def star (func) : 
#     @wraps(func) 
#     def inner (*x , **y) : 
#         print ("*" * 20) 
#         func (*x , **y)
#         print ("*" * 20)
#     return inner 

# def print_password (username) : 
#     print (username ,":" , users[username]) 
# print_password("kasra") 

# def change_password (username , new_password) : 
#     users[username] = new_password
#     print (username , ":" ,users[username])  
# change_password ("kasra" , "13121") 

# -----------------------------------------------------
# users = {"kasra" : "123413" , "darya" : "13412341234" , "dorsa11" : "af1234134"}
# black_list = {"kasra" ,"darya"} 
# from functools import wraps
# def ban (func) : 
#     @wraps(func)
#     def inner (*args , **kwargs) : 
#         if args[0] in black_list : 
#             print ("this user is betch!!!!!!")
#         else : 
#             func(*args , **kwargs)
#     return inner 
# @ban
# def change_password (username , new_password) : 
#     users[username] = new_password 
#     print (username , ":" , users[username])
# change_password("kasra" , "1431") 
# print (users)
# -----------------------------------------------------------
# from time import perf_counter 
# from functools import wraps 

# def time_calcultion (func) : 
#     @wraps(func) 
#     def wrapper_decorator (*args , **kwargs) : 
#         star_time = perf_counter()
#         value = func(*args , **kwargs) 
#         end_time = perf_counter()
#         run_time = end_time - star_time
#         print ("the run time of " , func.__name__ , "is"  , run_time)
#         return value
#     return wrapper_decorator

# @time_calcultion
# def A(Y) : 
#     s = 0
#     for i in range (Y) : 
#         s += i**2 

# @time_calcultion
# def B(x) : 
#     fuck = 1 
#     for i in range (1,x+1 ) : 
#         fuck *=1 

# A(100)
# B(10)
# -------------------------------------------------------------------------------
# from functools import wraps 
# def star (func) : 
#      @wraps (func) 
#      def inner (*x , **y ) : 
#         print ("*" * 20) 
#         func (*x , **y)
#         print ("*" * 20 ) 
#      return inner 
# @star
# def msg (name) : 
#     """ print a massage bitch !!!! """ 
#     print ("i am" , name )
# msg("kasra")
# print (msg.__name__)
# print (msg.__doc__) 
# # ----------------------------------------------
# from functools import wraps 
# def decorator (func) : 
#     @wraps (func) 
#     def warpper_decorator (*args , **kwargs ) : 
#         # do someting befor 
#         value = func(*args , **kwargs) 
#         # do someting after 
#         return value
#     return warpper_decorator  
# ------------------------------------------------
# user = {"kasra" : "1234" , "sara" : "4321" , "ali" : "4312"} 
# from functools import wraps 
# def star (func) : 
#     @wraps (func) 
#     def inner (*x , **y) : 
#         print ("*" * 20) 
#         func(*x,**y) 
#         print (*x , **y) 
#     return inner 


# def print_password (username) : 
#     print (username , ":" , user[username])
# print_password ("kasra")

# def change_password (username , new_password) : 
#     user[username] = new_password
#     print (username , ":" , user[username])

# change_password ("kasra" ,"12223") 
# print (user)
# ------------------------------------------------------------------------------- 
# def dec (func) : 
#     def inner () : 
#         print ("*" * 20) 
#         func ()
#         print ("*" * 20) 
#     return inner 
# @dec
# def f () : 
#     print ("kasra") 
# # new_func = dec(f)  
# # new_func()
# f()
# -----------------------------------------------
# def dec (func) : 
#     def inner (x,y) : 
#         if y == 0 : 
#             return("warning") 
#         func(x,y) 
#     return inner 

# @dec 
# def f (x,y) : 
#     return(x/y )
# print (f(4,12))
# -------------------------------------------------
# def star (func) : 
#     def inner (*x , ** y) : 
#         print ("*" * 20 )
#         func(*x , ** y)
#         print ("*" * 20)
#     return inner 

# @ star 
# def msg (name) : 
#     print ("i am " + name )
# msg("mohamad kasra") 
# -------------------------------------------------
import functools 
def decorator (func) : 
    @functools.wraps(func) 
    def warpper_decorator (*args , **kwargs) : 
        # do something befor 
        value = func (*args , **kwargs)
        # do something after 
        return value 
    return warpper_decorator
# ---------------------------------------------
# users = {"kasra" : "1234" , "sara" : "4321" , "bitch" : "8585"}

# from functools import wraps 
# def star (func) : 
#     @wraps(func) 
#     def inner (*x , **y) : 
#         print ("*" * 20 )
#         func(*x , **y) 
#         print ("*" * 20)
#     return inner 

# def  print_password (username) : 
#     print (username , ":" , users[username] )
# print_password("kasra")

# @star
# def change_password ( username, new_password) : 
#     users[username] = new_password 
#     print (username , ":" , users[username])
# change_password ("kasra" , "514313") 
# ----------------------------------------------------
# users = {"kasra" : "1234" , "sara" : "4321" , "bitch" : "8585" , }
# block_list = {"kasra" , "1234"  , "sara" , "4321"}

# from functools import wraps 
# def ban (func) : 
#     @wraps(func) 
#     def inner (*args , **kwargs) : 
#         if args[0] in block_list : 
#             print ("this user is blocked!!!!!!!!!")
#         else :
#             func(*args , **kwargs)
#     return inner 

# def print_password(username) : 
#     print (username , ":" , users[username])
# @ban
# def change_password (username , new_password) : 
#     username = new_password 
#     print (username , ":" , users[username])
# change_password("kasra" , "1234") 
# ----------------------------------------------------
# users = {"kasra" : "1234" , "sara" : "4321" , "bitch" : "8585" , "maryam" : "6989014k" , "fateme" : "rqe12344r" }
# block_list = {"kasra" , "sara" , "maryam" }

# from functools import wraps 
# def ban (func) : 
#     @wraps(func) 
#     def inner (*args , **kwargs) : 
#         if args[0] in block_list : 
#             print ("your username is bitch!!!") 
#         else : 
#             func(*args , **kwargs)
#     return inner 
# @ban
# def print_password (username) : 
#     print (username , ":" , users[username]) 
# print_password("kasra") 
# @ban
# def change_password (username ,new_password ) : 
#     users[username] = new_password
#     print (username , ":" , users[username])
# change_password ("bitch" , "134143afuhhdfkj[pe]")
# print (users)
# --------------------------------------------------------
# from time import perf_counter 
# from functools import wraps 

# def time_calculation (func) : 
#     @wraps(func) 
#     def wrapper_decorator (*args , **kwargs) :
#         start_time = perf_counter()
#         value = func(*args , **kwargs) 
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         print ("the runtime of " , func(__name__ , "is" , run_time))
#         return value
#     return wrapper_decorator

# @time_calculation
# def A(y) : 
#     s = 0 
#     for i in range(y) : 
#         s += i**2

# @time_calculation
# def b(x) : 
#     fact = 1 
#     for i in range (1, x+1) :
#      fact *= i 

# A(100)
# b(1000)
# ------------------------------------------------------- 
# i = iter ([1,2,34,4]) 
# print (next(i))
# print (next(i))
# print (next(i))
# print (next(i))
# print (next(i))
# ----------------------------------
# def func(x) : 
#     print ("bitch") 
#     yield x**3
#     print ("fahime") 
#     yield 3 
#     print ("i would like a pussy") 
#     yield 2-5
#     print ("kosssssss")

# x = func(12) 
# print (next(x))
# print (next(x))
# print (next(x))
# print (next(x))
# --------------------------------
# def my_generator () : 
#     print ("my bitch")
#     for i in range (5) : 
#         yield i**2 
# g = my_generator()
# for i in g : 
#     print (i)
# -------------------------------
# from time import perf_counter 

# def list_range (start , end , step = 1) :
#     new_range  = []
#     while start < end :
#         new_range.append( start )
#         start += step
#     return new_range 
# # ---------------------------------
# from time import perf_counter 

# def gen_range (start , end , step = 1) : 
#     while start < end : 
#         yield start 
#         start += step 
# gr = gen_range (10 , 20 , 2)
# print (list (gr))
# # --------------------------------
# start = perf_counter()
# lr = list_range (1 , 100000)
# s = 0 
# for i in lr : 
#     if i == 3 : 
#         break 
#     s += i **2 
# end = perf_counter()
# print ("lr : " , end-start)
# # ---------------------------------
# start2 = perf_counter()
# gr = list_range (1, 100000000)
# s = 0 
# for j in gr :
#     if j == 3 : 
#         break 
#     s += j **2 
# end2 = perf_counter()
# print ("gr:" , end2 - start2)
#--------------------------------------
# def my_enu (secuence , start = 0) : 
#     c = start 
#     for i in (secuence) : 
#         yield c, i
#         c += 1 

# l = ["kasra" , "sara"]
# for i,j in my_enu(l,6) : 
#     print (i,j) 
#--------------------------------------
# def fibonacci () : 
#     f1 = 0 
#     yield f1 
#     f2 = 1 
#     yield f2 
#     while True : 
#         f3 = f1 + f2 
#         yield f3 
#         f1 = f2 
#         f2 = f3 
# fib = fibonacci() 
# for i in range (10) : 
#     print (next(fib))
# -------------------------------------
# def my_kos (secuence , start) : 
#     c = start 
#     for i in secuence : 
#         yield c , i 
#         c += 1 
# l = ["kassra" , "sara"] 
# for i,j in enumerate(l) : 
#     print (i,j) 
# # ----------------------------------------
# def kos (seuence , start) : 
#     c = start 
#     for i in seuence : 
#         yield c , i 
#         c += 1
# 0 , 1 , 1 ,2 ,3 ,5 ,8 
# l = ["kasssra ", "asars;"]
# for i,j in enumerate (l) : 
#     print (i,j) 
# ------------------------------------------------
# def fibonacci () : 
#     f1 = 0 
#     yield f1 
#     f2 = 1
#     yield f2 
#     while True : 
#         f3 = f1 + f2 
#         yield f3 
#         f1 = f2 
#         f2 = f3 

# fib = fibonacci() 
# for i in range (11) : 
#     print (next(fib))

# -------------------------------------------------
# def sum_gn (lst) : 
#     c = 0 
#     for i in lst : 
#         c += i 
#         yield c 
# sg = sum_gn([1,2,34,5])
# for i in sg : 
#     print (i)
# ---------------------------
# def sum_gen (lst) : 
#     s = 0 
#     for i in lst : 
#         s += i 
#         yield s
# sg = sum_gen  ([1,2,3,4,5])
# for i in sg : 
#     print (i)
# # -------------------------------
# def serv_gen (s) : 
#     l = len(s)
#     for i in range (l-1 , -1 ,-1 ) : 
#         yield s[i]


# sg = serv_gen ("kasra dana") 
# for i in sg : 
#     print (i)
# ------------------------------
# def sum_gen (lst) :
#     s = 0 
#     for i in lst : 
#         s += i 
#         yield s 

# sg = sum_gen ([1,2,3,4])
# for i in sg : 
#     print (i)
# ---------------------------
# def serv_gen (s) : 
#     l = len(s) 
#     for i in range(l-1 , -1 , -1 ) :  
#         yield s[i]

# sg = serv_gen ("kasra") 
# for ch in sg : 
#     print (ch) 
# ------------------------------
# def my_gen (even_or_odd = "e") : 
#     c = 0 
#     if even_or_odd == "o" : 
#         c = 1 
#     while True : 
#         yield c 
#         c += 2 

# eo = my_gen ("e") 
# for _ in range (10 ) : 
#     print (next (eo)) 
# ----------------------------------------
# def kos (even_or_odd = "e") : 
#     c = 0 
#     if even_or_odd == "o" : 
#         c = 1 
#     while True : 
#         yield c 
#         c +=2 
# k = kos ("o") 
# for i in range ( 10 ) : 
#     print (next (k))
# -----------------------------------------
# def bitch (even_or_odd = "e" ) : 
#     c = 0 
#     if even_or_odd == "o" : 
#         c = 1 
#     while True : 
#         yield c 
#         c+= 2 
# k = bitch ("o")
# for i in range (10) : 
#     print (next (k)) 
# 
# ---------------------------------------------- 602 -----------------------
# # 1 ,1 2, 3 ,5 ,8 ,...

# def fibonacci ()  :
#     f1 = 0 
#     yield f1 
#     f2 = 1 
#     yield f2 
#     while True : 
#         f3 = f1 + f2 
#         yield f3 
#         f1 = f2 
#         f2 = f3 
    
# fib = fibonacci() 
# for i in range (9) : 
#     print (next (fib))
# -----------------------------
# def sum_gen (lst) : 
#     s = 0 
#     for i in lst : 
#         s += i 
#         yield s 
# sg = sum_gen ([1,2,3,4,5])
# for i in sg : 
#     print (i)
# -------------------------------
# def sun_gen (lst) : 
#     s = 0
#     for i in lst : 
#         s += i 
#         yield s 
# sg = sun_gen ([1,2,3,4,5]) 
# for i in sg : 
#     print (i)
# # --------------------------------
# def rev_str (s) : 
#     l = len (s) 
#     for i in range (l -1 , -1 , -1) :
#         yield s [i] 
# sg = rev_str ("kasra") 
# for ch in sg :
#     print (ch)
# ------------------------------------
# def kos (s) : 
#     l = len(s) 
#     for i in range (l -1 , -1 , -1) : 
#         yield s[i]
# sg = kos ("kasra") 
# for i in sg : 
#     print (i)
# ---------------------------------------------
# def my_gen (even_or_odd = "e") : 
#     c = 0 
#     if even_or_odd == "o" : 
#         c +=1 
#     while True :  
#         yield c 
#         c += 2 
# mg = my_gen ("e")
# for i in range (10) :
#     print (next (mg))
#________________________________________________________________________________________________________________________________________________________________
# def spl_gen (delimiter) : 
#     print ("start!!!")
#     s = 0 
#     while True : 
#         line = yield s 
#         s = line.split(delimiter) 

# g = spl_gen (" ") 
# next(g) 
# print (g.send("sara kasra"))
# --------------------------------
# def sen_gen (words)  :
#     print ("start")
#     w = 0
#     while True : 
#      word = yield w 
#      if word not in words : 
#          w = word 
#      else : 
#         w = "*" * 10

# g = sen_gen (("bitch" , "pussy" , "aas") )
# next (g) 
# print (g.send("bitch"))
# print (g.send ("kasra")) 
# print (g.send ("pussy"))
# -----------------------------------------------
# from time import sleep 
# def revers (n) : 
#     if n <= 0 : 
#         return 
#     sleep (0.5)
#     print (n) 
#     n -= 1 
#     return revers(n) 
# revers(10) 
# # ----------------------------------------------
# def fact (n) : 
#     if n == 0 : 
#         return 1 
#     elif n % 10 < 5 : 
#         return fact (n//10) 
#     else : 
#         return n %10 * fact (n//10)
    
# print (fact(12345))
# -----------------------------------------------------
# def fib (n) : 
#     if n == 0 or n == 1 : 
#         return n 
#     return fib(n-1) + fib (n-2) 
# print (fib(5)) 
# -----------------------------------
board = list (range(1,10))
winners = ( (0,1,2) , (3,4,5) , (6,7,8) , (0,3,6) , (1,4,7)  , (2,5,8) , (0,4,8) , (2,4,6) )  #(11)
moves = (  (1,7,3,9)  , (5,)    , (2,4,6,8)  )                                #(18)                               # بدون ایتدکس می نو سیم                

def print_board () :                                                          #(4)
    j = 1 
    for i in board : 
        end = " "
        if j % 3 == 0 : 
            end = "\n\n"
        print (f"[{i}]" , end =end)
        j += 1 


def make_move (brd , plyr , mve , undo = False) :                            #(6)
    if can_move (brd , mve ) :                                               #(7)
        brd [mve-1] = plyr 
        win = is_winner (brd,plyr)                                           #(9)
        if undo: 
            brd[mve-1] = mve                                                 #(13)
        return True , win 
    return False , False 
 


def can_move (brd , mve) :                                                   #(8) 
    if mve in range (1,10) and isinstance (brd[mve -1] , int) : 
        return True
    return False


def is_winner (brd,plyr) :                                                   #(10)
    win = True                                                               #(12)
    for tup in winners :                                                      
        win = True
        for j in tup : 
            if brd [j] != plyr : 
                win = False
                break 
        if win :
            break
    return win



def has_empy_space ():                                                        #(2)
    return board.count ("X") + board.count ("O") != 9
    


def computer_move () :                                                        #(16) 
    mv = -1 
    # ایا خود کامپوتر میتونه برنده بشه ؟
    for i in range (1,10 ) : 
        if make_move(board , computer , i , True)[1] : 
            mv = i 
            break
    # اگه کاربر میتونه برنده بشه جلو ی او رو بگییر                          
    if mv == -1 :                                                             #(17)
        for j in range (1,10) : 
            if make_move(board , player , i , True)[1] : 
                mv = j 
                break 
    # حرکت کن جندهههههههههههههه                                                
    if mv == -1 :                                                              #(20)
        for tup in moves : 
            for m in tup : 
                if mv == -1 and can_move(board , m) : 
                    mv = m 
                    break
    return make_move(board , computer , mv)


player , computer = "X" , "O"                                                 #(1)
print ("player : X\ncomputer : O\n")      
while has_empy_space () :                                                     #(3)
    print_board()                                                             #(4)
    move = int (input ("choose your move(1,9) : "))                           #(5)
    moved , won = make_move(board , player , move)                            #(6)
    if not moved :                                                            #(14)
        print ("invalid number! try again")
        continue
    if won :                                                                  #(15) 
        print ("you won!")
        break  
    elif computer_move()[1] :                                                 #(21)                                             
        print ("you lose!")
        break 

print_board()