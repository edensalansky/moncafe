from persistence import *
import printdb
import sys

file =open(sys.argv[1],"r")

for line in file:
    line = line.replace('\n', "")
    input = line.split(', ')
    print(input)
    activity = Activities(int(input[0]), int(input[1]), int(input[2]), input[3])
    id = activity.product_id
    p = repo.Products.find(int(id))
    if activity.quantity < 0:
        if activity.quantity + p.quantity >= 0:
            repo.Products.update_table(activity.quantity + p.quantity, activity.product_id)
            repo.Activities.insert(activity)
    elif activity.quantity >0:
        repo.Products.update_table(str(activity.quantity + p.quantity), str(activity.product_id))
        repo.Activities.insert(activity)

printdb.printAll()
