import tweepy
import time
import math
import datetime

file_start_node = "data/MahidolU"

keys_count = 9
api = []
select = 0

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def get_token(folder):
    global consumer_key
    global consumer_secret
    global access_token
    global access_secret
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

def set_api():
    global api
    for num in range(keys_count):
        get_token(num)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api_set = tweepy.API(auth)
        api.append(api_set)

def get_follower(file_line):
    global select
    count_complete = 0
    count_error = 0
    wait = 0
    count_total = len(file_line)
    for line in file_line:
        pointer = -1
        ids = line.strip('\n\r')
        round = 0
        while (pointer != 0):
            current_time = str(datetime.datetime.now())
            print("--------------------------")
            print("current time: " + current_time)
            print("--------------------------")
            try:
                results = api[select].friends_ids(user_id=ids , cursor = pointer)
                file_complete = "following/" + str(ids)
                file_follow = open('%s.txt' % file_complete, 'a')
                for follower in results[0]:
                    file_follow.write(str(follower) + str("\n"))
                file_follow.close()
                pointer = results[1][1]
                wait = 0
                round += 1
                print("ID " + str(ids) + " " + str(round))
            except tweepy.RateLimitError:
                select += 1
                print("CHANGE TO API KEY ", select)
                if(select == keys_count):
                    select = 0
                    print(wait , " WAIT 60 SECONDs  " + str(ids) + " " + str(count_complete))
                    print("     COMPLETE    :     " + str(count_complete-count_error))
                    print("     ERROR       :     " + str(count_error))
                    print("     TOTAL       :     " + str(count_complete) + " OF " + str(count_total))
                    wait += 1
                    time.sleep(60)
            except tweepy.TweepError as e:
                file_error = open('data/error-following.txt', 'a')
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
    file_summary = open('data/summary-following.txt', 'a')
    file_summary.write("SUCCESS:     " + str(count_complete-count_error)+'\n')
    file_summary.write("ERROR:     " + str(count_error)+'\n')
    file_summary.write("TOTAL:     " + str(count_total)+'\n')
    file_summary.write("--------------------------------------------------" + '\n')
    file_summary.close()

def main():
    file_start = open('%s.txt' % file_start_node, 'r')
    file_line = file_start.readlines()
    set_api()
    get_follower(file_line)

if __name__ == "__main__":
    main()
