cmt_list = []
while True:
    comment = input("Enter your comment: ")
    cmt_list.append(comment)
    print("Previously entered comments: ")
    j = 0
    while len(cmt_list) >= j+1:
        print(str(j+1) + ". " + cmt_list[j])
        j = j+1
