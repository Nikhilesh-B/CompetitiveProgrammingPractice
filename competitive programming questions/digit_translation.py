def find_potential_neighbors(string):
    intervals = []
    for i, char in enumerate(string):
        if i+3<len(string):
            if string[-3:] == "one" or string[-3:] == "two" or string[-3:] == "three":
                    intervals.append(i,i+3)
        if i+4<len(string):
            if string[-4:] == "zero" or string[-4:] == "four" or string[-4:] == "five" or string[-4:] == "nine":
                    intervals.append(i,i+4)
        if i+5<len(string):
            if string[-5
                      :] == "zero" or string[-4:] == "four" or string[-4:] == "five" or string[-4:] == "nine":
                    intervals.append(i,i+4)

            
        


    

def compute():
    string = input()
    potential_strings = set()
    from_right = ""
    for i, char in enumerate(string):
        for from_right in potential_strings:
            from_right += char
            if len(from_right)>=3:
                if from_right[-3:] == "one":
                    print(from_right)
                    from_right = from_right[0:-3]+"1"
                    continue
                elif from_right[-3:] == "two":
                    from_right = from_right[0:-3]+"2"
                    continue
                elif from_right[-3:] == "six":
                    from_right = from_right[0:-3]+"6"
                    continue
                
                
            if len(from_right)>=4:
                if from_right[-4:] == "zero":
                    from_right = from_right[0:-4]+"0"
                    continue
                elif from_right[-4:] == "four":
                    from_right = from_right[0:-4]+"4"
                    continue
                elif from_right[-4:] == "five":
                    from_right = from_right[0:-4]+"5"
                    continue
                elif from_right[-4:] == "nine":
                    from_right = from_right[0:-4]+"9"
                    continue
                
            if len(from_right)>=5:
                if from_right[-5:] == "three":
                    from_right = from_right[0:-5]+"3"
                    continue
                elif from_right[-5:] == "seven":
                    from_right = from_right[0:-5]+"7"
                    continue
                elif from_right[-5:] == "eight":
                    from_right = from_right[0:-5]+"8"
                    continue


    
if __name__ == "__main__":
    compute()