import re 
movie_id = 0
movies = []
cast_id = 0
cast = []

links = []

def add_movie(text):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    text = text.split()
    title = text[1]
    if len(title) > 20:
        return (False,'invalid title')
    date = text[2]

    try:
        date = int(date)
    except ValueError:
        return (False,'invalid date')
    
    if not (date>= 1888 and date <= 2024 ):
        return (False,'invalid date')
    
    qua = text[3]
    if qua not in ["720p","1080p","4K"]:
        return (False,'invalid quality')
    movies.append([movie_id,title,date,qua])
    movie_id += 1

    return (True,f'added successfully {movie_id-1}')


def rem_movie(id):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    for row_index in range(len(movies)):
        if id == movies[row_index][0]:
            movies = movies[:row_index] + movies[row_index+1:]
            return (True,'removed successfully {id}')
    
    return (False,'invalid movie id')


def add_cast(text):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    text = text.split()
    cast_name = text[1]
    if len(cast_name) > 20 or bool(re.match("^[a-zA-Z]+", cast_name)):
        return (False,'invalid name')

    cast.append([cast_id,cast_name])
    cast_id += 1

    return (True,f'added successfully {cast_id-1}')


def rem_cast(id):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    for row_index in range(len(cast)):
        if id == cast[row_index][0]:
            cast = cast[:row_index] + cast[row_index+1:]
            return (True,'removed successfully {id}')
    
    return (False,'invalid cast id')


def exist_cast(id):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    for ca in cast:
        if ca[0] == id:
            return True
    return False



def return_cast(id):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    if exist_cast(id):
        for ca in cast:
            if ca[0] == id:
                return True,ca
    else:
        (False,"invalid movie id")

def exist_link(movie_id,cast_id):

    global movies
    global cast
    global links

    for link in links:
        if link[0] == movie_id and link[1] == cast_id:
            return True
    return False

def exist_movie(id):
    for movie in movies:
        if movie[0] == id:
            return True
    return False


def return_movie(id):
    global movie_id
    global movies
    global cast_id
    global cast
    global links

    if exist_movie(id):
        for movie in movies:
            if movie[0] == id:
                return (True,movie)
    else:
        (False,"invalid movie id")


def link_cast_movie(cast_id,movie_id):
    global movies
    global cast
    global links


    if not exist_cast(cast_id):
        return (False,"invalid cast id")
    
    if not exist_movie(movie_id):
        return (False,"invalid movie id")
    
    if  exist_link(movie_id,cast_id):
        return (False,"already linked")
    
    links.append([movie_id,cast_id])

    return (True,f"successfully linked {cast_id} to {movie_id}")

def retun_movie_base_cast(cast_id):
    global movie_id
    global movies
    global cast
    global links

    mov = []
    for link in links:
        if link[1] == cast_id:
            mov.append(link[0])
    return sorted(mov)

def retun_cast_base_movie(movie_id):
    global movies
    global cast_id
    global cast
    global links

    cas = []
    for link in links:
        if link[0] == movie_id:
            cas.append(link[1])
    return sorted(cas)


def show_movie(movie_id):
    global movies
    global cast_id
    global cast
    global links
    if not exist_movie(movie_id):
        return (False,'invalid movie id')
    
    _,mov = return_movie(movie_id)
    cas = retun_cast_base_movie(mov[0])

    return (True,{"title":mov[1], "date":mov[2], "quality":mov[3], "casts":cas})

def show_cast(cast_id):
    global movie_id
    global movies
    global cast
    global links    
    if not exist_cast(cast_id):
        return (False,'invalid cast id')
    
    _,ca = return_cast(cast_id)
    movs = retun_movie_base_cast(ca[0])
    return (True,{"name":ca[1], "movies":movs})


def filter_mov_tilte(pat):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    movs = []
    for movie in movies:
        if movie[1].startswith(pat):
            movs.append(str(movie[0]))

    return "["+", ".join(movs)+"]"

def filter_mov_date(ineq,n):
    global movie_id
    global movies
    global cast_id
    global cast
    global links  
    movs = []

    if ineq == "=":
        for movie in movies:
            if movie[2] == n:
                movs.append(movie[0])
    elif ineq == ">":
        for movie in movies:
            if movie[2] > n:
                movs.append(movie[0])
    elif ineq == ">=":
        for movie in movies:
            if movie[2] >= n:
                movs.append(movie[0])
    elif ineq == "<=":
        for movie in movies:
            if movie[2] <= n:
                movs.append(movie[0])
    else:
        for movie in movies:
            if movie[2] < n:
                movs.append(movie[0])



    movs = [str(mov) for mov in movs]
    return "["+", ".join(movs)+"]"


def filter_mov_qu(pat):
    global movie_id
    global movies
    global cast_id
    global cast
    global links
    movs = []
    for movie in movies:
        if movie[3] == pat:
            movs.append(movie[0])
    
    movs = [str(mov) for mov in movs]


    return "["+", ".join(movs)+"]"

def print_show_cast(di):
    title = di["title"]
    date =  di["date"]
    casts = di["casts"]
    return f"{{title:\"{title}\", date:\"{date}\", casts:{casts}}}"

def print_show_mov(di):
    name = di["name"]
    movies =  di["movies"]
    return f"{{name:\"{name}\", movies:{movies}}}"

n = int(input(""))
meessage = []
for _ in range(n):
    text = input("")
    task = text.split()[0]

    if task == "ADD-MOVIE":
        _,mes = add_movie(text)
        meessage.append(mes)
    elif task == "REM-MOVIE":
        mov_id = int(text.split()[1])
        _,mes = rem_movie(mov_id)
        meessage.append(mes)

    elif task == "ADD-CAST":
        _,mes = add_cast(text)
        meessage.append(mes)
    elif task == "REM-CAST":
        cast_id = int(text.split()[1])
        _,mes = rem_cast(cast_id)
        meessage.append(mes)

    elif task == "SHOW-MOVIE":
        mov_id = int(text.split()[1])
        state,mes = show_movie(mov_id)
        if state:
            meessage.append(print_show_cast(mes))
        else:
            meessage.append(mes)
        
    elif task == "SHOW-CAST":
        cast_id = int(text.split()[1])
        state,mes = show_cast(cast_id)
        if state:
            meessage.append(print_show_mov(mes))
        else:
            meessage.append(mes)
    elif task == "LINK-CAST-TO-MOVIE":
         mov_id,cast_id = int(text.split()[1]),int(text.split()[2])
         _,mes = link_cast_movie(mov_id,cast_id)
         meessage.append(mes)
    elif task == "FILTER-MOVIES-BY-TITLE":
        pat = text.split()[1]
        mes = filter_mov_tilte(pat)
        meessage.append(mes)

    elif task == "FILTER-MOVIES-BY-DATE":
        eq,n = text.split()[1],int(text.split()[2])
        mes = filter_mov_date(eq,n)
        meessage.append(mes)
    elif task == "FILTER-MOVIES-BY-QUALITY":
        pat = text.split()[1]
        mes = filter_mov_qu(pat)
        meessage.append(mes)



for i in meessage:
    print(i)
