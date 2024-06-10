# We will need to load all libraries here
import numpy as np

#test code to see if this is actually executable
#print("Hello World")

# We start with section 5.1, we need define functions that will help us generate the synthetic data.

#We first need figure out what parameters we are gonna need and output.
#We need to specify the input and output
'''
Input:
    Arrival locations are generated uniformly within the range [-0.8*loc_bound, 0.8*loc_bound].
    rand_seed: random seed
    num_position: total number of arrival locations
    bike_num: total number of bikes
    grid_size: grid size of the candidate location
    beta0, beta1: MNL model parameter
    loc_bound: bound of the bike locations and arrival locations
    split_data: whether split the data into train/test set

Output:
    true_pos_ind
    bike_num: total number of bikes
    num_records: number of all arrived riders. 
    book_bike: squence of booking bikes.
    book_index
    dist: 
        this is a matrix of dimension num_position * num_records * bike_num, it returns the distance between each
        arrival location and bike location.
    bike_loc: 
    all_period
    num_booked
    cand_loc
    true_l
    position_weight
'''

def gen_sync_in_grid(rand_seed,num_position,bike_num,lambd,grid_size,beta0=1,beta1_true=-1,T=50,loc_bound=5):

    print("This function is used to generate our syntheyic data.")