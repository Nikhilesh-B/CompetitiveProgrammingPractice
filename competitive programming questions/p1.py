
def create_list_of_rankings():
    n_k_c_list = input().split(" ")
    n,k,c = int(n_k_c_list[0]),int(n_k_c_list[1]),int(n_k_c_list[2])

    list_of_rankings = []

    for _ in range(n):
        s_t_list = input().split(" ")
        list_of_rankings.append((int(s_t_list[0]),int(s_t_list[1])))

    return n, k, c, list_of_rankings

def output_rank(n,k,c,list_of_rankings):
    output_lst = []
    counts = {}
    left_over = []
    for t, s in list_of_rankings:
        if len(output_lst)<k:
            if s not in counts:
                counts[s] = 1
                output_lst.append(t)
            else:
                if counts[s] + 1 > c: 
                    left_over.append(t)
                else:
                    counts[s] += 1
                    output_lst.append(t)
            
        else:
            return output_lst
    
    if len(output_lst)<k:
        output_lst = output_lst + left_over[:k-len(output_lst)+1]

    return output_lst
         
def print_output_lst(output_lst):
    for team in output_lst:
        print(team)


if __name__ == "__main__":
    n, k, c, list_of_rankings = create_list_of_rankings()
    output_lst = output_rank(n, k, c, list_of_rankings)
    print_output_lst(output_lst)
