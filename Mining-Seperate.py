import tweepy
import time
import math

file_start_node = "1403874758"
file_start = open('%s.txt' % file_start_node, 'r')

consumer_key = '343'
consumer_secret = ''
access_token = ''
access_secret = ''

keys_count = 8
user_count = []


def get_token(folder):
    global consumer_key
    global consumer_secret
    global access_token
    global access_secret
    print(folder)
    # if folder == 0:
    #     consumer_key = ''
    #     consumer_secret = ''
    #     access_token = ''
    #     access_secret = ''
    # elif folder == 1:
    #     consumer_key = ''
    #     consumer_secret = ''
    #     access_token = ''
    #     access_secret = ''

def create_list(folder):
    file_line = file_start.readlines()
    user_reminder = len(file_line) % keys_count
    user_sub = math.floor(len(file_line) / keys_count)
    user_count.append(0)
    for i in range(keys_count):
        user_count.append(user_count[i] + user_sub)
        if(user_reminder):
            user_count[i+1] += 1
            user_reminder -= 1
    return file_line[user_count[folder-1]:user_count[folder]]

def get_follower(api,folder,file_line):
    count_complete = 0
    count_error = 0
    wait = 0
    count_total = user_count[folder]-user_count[folder-1]
    for line in file_line:
        pointer = -1
        ids = line.strip('\n\r')
        round = 0
        while (pointer != 0):
            try:
                results = api.followers_ids(user_id=ids , cursor = pointer)
                file_complete = "LIST" + str(folder) + "/" + str(ids)
                file_follow = open('%s.txt' % file_complete, 'a')
                for follower in results[0]:
                    file_follow.write(str(follower) + str("\n"))
                file_follow.close()
                pointer = results[1][1]
                wait = 0
                round += 1
                print("ID ", ids , str(round))
            except tweepy.RateLimitError:
                print(wait , " WAIT 60 SECONDs  ", ids)
                print("     COMPLETE    :     ", count_complete-count_error)
                print("     ERROR       :     ", count_error)
                print("     TOTAL       :     ", count_complete , " OF " , count_total)
                wait += 1
                time.sleep(60)
            except tweepy.TweepError as e:
                err_name = "error" + str(folder)
                file_error = open('%s.txt' % err_name, 'a')
                file_error.write(str(ids) + " " + str(e) + '\n')
                file_error.close()
                pointer = 0
                count_error += 1
                wait = 0
                print(type(e))
                print(e)
        count_complete += 1
        print("COMPLETE " + str(count_complete))
    print("TASK COMPLETE")
    file_summary = open('summary.txt', 'a')
    file_summary.write("KEY " + str(folder)+'\n')
    file_summary.write("SUCCESS:     " + str(count_error)+'\n')
    file_summary.write("SUCCESS:     " + str(count_complete)+'\n')
    file_summary.write("TOTAL:     " + str(count_total)+'\n')
    file_summary.write("--------------------------------------------------" + '\n')
    file_summary.close()

def main():
    folder = int(input("ENTER KEY NUMBER:"))

    get_token(folder)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    file_line = create_list(folder)
    print(file_line)
    file_summary = open('summary.txt', 'a')
    file_summary.write("KEY " + str(folder) +'\n')
    file_summary.write("Search For " + str(file_line) + '\n')
    file_summary.write("Size" + str(user_count) + '\n')
    file_summary.write("--------------------------------------------------" + '\n')
    file_summary.close()

    get_follower(api,folder,file_line)

if __name__ == "__main__":
    main()
