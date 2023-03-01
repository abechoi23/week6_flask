# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
movie_lengths1 = [20, 30, 110, 40, 50] #true
movie_lengths2 = [20, 80, 110, 40]  #false
flight_length = 160

def flight_plan_complete (flight_length, movie_lengths):
    dict = {}
    for length in movie_lengths:
        test = flight_length - length
        if test in dict:
            return True
        dict[length] = True
    return False


    
print(flight_plan_complete(flight_length, movie_lengths1))
print(flight_plan_complete(flight_length, movie_lengths2))


def flight_plan_complete (flight_length, movie_lengths):
    for i in range(len(movie_lengths)):
#print(i)
        for j in range(len(movie_lengths)):
            total_movie = (i, j)
            print(total_movie)
            if movie_lengths[i] + movie_lengths[j] == flight_length and i != j:
                return True
            
    return False
flight_length = 160

#movie_lengths1 = [20, 30, 110, 40, 50]
#print(flight_plan_complete(flight_length, movie_lengths1))
movie_lengths2 = [20, 80, 110, 40]
print(flight_plan_complete(flight_length, movie_lengths2))

