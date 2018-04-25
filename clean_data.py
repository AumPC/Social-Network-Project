import glob

mahidolU_follower = []
count = 0
error_list = []

with  open("data/MahidolU.txt") as f:
    for line in f:
        mahidolU_follower.append(line.rstrip('\n'))

print(mahidolU_follower[:10])
print("The number of MahidolU's follower : ", len(mahidolU_follower))

f = open('data/error-follower.txt', 'r')
for line in f.readlines():
    error_list.append(line.strip('\n').split(' ')[0])

for file_name in glob.glob('data/follower/*'):
    f = open(file_name, 'r')
    follower = f.read().split('\n')
    f.close()
    clean_follower = list(set(follower) & set(mahidolU_follower))
    if clean_follower != []:
        f = open('data/clean_follower/' + file_name.split('\\')[1], 'a')
    for id in clean_follower:
        f.write(id + '\n')
    f.close()
    print("Normal - finished " + str(count))
    count+=1

count = 0
for file_name in glob.glob('data/following/*'):
    f = open(file_name, 'r')
    following = f.read().split('\n')
    f.close()
    followed_error = list(set(following) & set(error_list))
    for error_node in followed_error:
        f = open('data/clean_follower/' + error_node + '.txt', 'a')
        f.write(file_name.split('\\')[1] + '\n')
        f.close()
    print("Error node - finished " + str(count))
    count+=1
