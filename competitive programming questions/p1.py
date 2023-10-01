
def create_list_of_rankings():
    n_k_c_list = input().split(" ")
    n,k,c = int(n_k_c_list[0]),int(n_k_c_list[1]),int(n_k_c_list[2])

    list_of_rankings = []

    for i in range(n):
        s_t_list = input().split(" ")
        list_of_rankings.append((int(s_t_list[0]),int(s_t_list[1]), i))

    return n, k, c, list_of_rankings

def output_rank(n,k,c,list_of_rankings):
    output_lst = []
    counts = {}
    left_over = []
    for t, s, i in list_of_rankings:
        if len(output_lst)<k:
            if s not in counts:
                counts[s] = 1
                output_lst.append((t,i))
            else:
                if counts[s] == c: 
                    left_over.append((t,i))
                else:
                    counts[s] += 1
                    output_lst.append((t,i))
            
        else:
            return output_lst
    
    if len(output_lst)<k:
        output_lst = output_lst + left_over
        output_lst = output_lst[:k]

    return output_lst
         
def print_output_lst(output_lst):
    output_lst.sort(key = lambda x:x[1])
    for team in output_lst:
        print(team[0])


if __name__ == "__main__":
    n, k, c, list_of_rankings = create_list_of_rankings()
    output_lst = output_rank(n, k, c, list_of_rankings)
    print_output_lst(output_lst)
