
#calculate three passive income such as writing_article, Tutoring, and walking dog 

#cost of services 
one_written_article = 80
one_hour_tutoring = 20
one_hour_walking_dog = 10

writing_article = []
tutoring = []
walking_dog = []
totals = []
counter = 1

def subscription_summary(writing_article, tutoring, walking_dog):
    counter = 1
    all_friends = 0

    #section for writing_article 
    for i in range(len(writing_article)):
        total = 0
        article = int(writing_article[i] * one_written_article)
        total = total + article


    #section for tutoring
        tutor = int(tutoring[i]) * one_hour_tutoring
        total = total + tutor
    
    #section for walking dog 
        dog = int(walking_dog[i]) * one_hour_walking_dog
        total = total + dog
        totals.append(total)
        all_friends = all_friends + total
        
#prints summary of each accounts 
        print("\nFriend " + str(counter) + " made $" + format(total, '.2f') + " total.")
        print(">>> $" + format(article, '.2f')  + " from writing articles.")
        print(">>> $" + format(tutor, '.2f') + " from tutoring.")
        print(">>> $" + format(dog, '.2f') + " from walking dog.\n")
        counter = counter + 1

#prints account summary 
    print("Combined all friends made $" + format(sum(totals), '.2f') + " total")
    print("$" + format(max(totals),'.2f') + " was the most earned among friends.")

    max_value = max(totals) 
    #1, #3
    max_indexes = [f'{idx + 1}' for idx in range(len(totals)) if totals[idx] == max_value]
    print("The friend that earned the most were: friend ", end='')
    print(', '.join(max_indexes))


    print('\nThank you for using this program.')


print(' --------------------------------------')
print('| Calculate passive among three friends |')
print(' --------------------------------------')

##Taking input for three Friends income
#Written article
print("\nEnter number of articles written by friends this month:")
writing_article.append(int(input("Friend 1:  ")))
writing_article.append(int(input("Friend 2:  ")))
writing_article.append(int(input("Friend 3:  ")))

#Tutoring
print("\nEnter number of hours worked as tutor this month:")
tutoring.append(int(input("Friend 1:  ")))
tutoring.append(int(input("Friend 2:  ")))
tutoring.append(int(input("Friend 3:  ")))

#dog walking 
print("\nEnter number of hours worked as dog walker this month:")
walking_dog.append(int(input("Friend 1:  ")))
walking_dog.append(int(input("Friend 2:  ")))
walking_dog.append(int(input("Friend 3:  ")))

subscription_summary(writing_article, tutoring, walking_dog)
