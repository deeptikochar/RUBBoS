import csv

def port_data():
    user_dict = port_users()
    port_stories('stories.data', user_dict)
    port_stories('old_stories.data', user_dict)
    port_submissions()
    port_moderator_log()
    port_comments()
    port_old_comments()

# Function Name: port_users
# 1. Ports users.data to users.csv
# 2. Creates a new file user_logins.csv containing nicknames, passwords, user id and access
# 3. Returns a dictionary of user ids and nicknames (used in port_stories)

def port_users():
    filename = 'users.data'
    output_filename = 'users.csv'
    output_filename1 = 'user_logins.csv'
    input_f = open(filename,'r')
    output_f = open(output_filename, 'w')
    output_f1 = open(output_filename1, 'w')
    user_dict = dict()
    for line in input_f:
        element = line.split("\t")
        output_line = element[0]
        for i in range(1, len(element)):
            output_line = output_line + "," + element[i]
        output_f.write(output_line)
        output_line = element[3] +"," + element[4] + "," + element[0] + "," + element[7]+"\n"
        output_f1.write(output_line)
        user_dict[element[0]] = element[3]

    input_f.close()
    output_f.close()
    output_f1.close()
    return user_dict

# Function name: port_stories
# Called separately to port stories.data and old_stories.data to stories.csv and old_stories.csv respectively
# Uses the dictionary of user ids and nicknames
# To create a file containing nicknames, date, story id and title - user_stories.csv and user_old_stories.csv

def port_stories(filename, user_dict):

    input_f = open(filename,'r')
    temp = filename.find('.')
    output_filename = filename[0:temp] + '.csv'
    output_f = open(output_filename, 'w')
    output_filename1 = "user_" + filename[0:temp] + ".csv"
    output_f1 = open(output_filename1, 'w')
    for line in input_f:
        element = line.split("\t")
        story_id = element[0]
        title = element[1]
        date = element[3]
        writer_id = element[4]
        output_line = story_id + ",\"" + element[1] + "\",\"" + element[2] + "\"," + date + "," + writer_id +","+element[5]
        output_f.write(output_line)

        if(writer_id in user_dict):
            nickname = user_dict[writer_id]
            output_line = nickname + "," + date + "," + story_id + ",\"" + title +"\"\n"
            output_f1.write(output_line)

    input_f.close()
    output_f.close()
    output_f1.close()

# Function name: port_submissions
# Ports submissions.data to submissions.csv

def port_submissions():
    input_f = open('submissions.data', 'r')
    output_f = open('submissions.csv', 'w')

    for line in input_f:
        element = line.split("\t")
        output_line = element[0] + ",\"" + element[1] + "\",\"" + element[2] + "\"," + element[3] + "," + element[4] +","+element[5]
        output_f.write(output_line)

    input_f.close()
    output_f.close()

# Function name: port_moderator_log
# Ports moderator_log.data to moderator_log.csv

def port_moderator_log():
    filename = 'moderator_log.data'
    output_filename = 'moderator_log.csv'
    input_f = open(filename,'r')
    output_f = open(output_filename, 'w')
    for line in input_f:
        element = line.split("\t")
        output_line = element[0]
        for i in range(1, len(element)):
            output_line = output_line + "," + element[i]
        output_f.write(output_line)
    input_f.close()
    output_f.close()

# Function name: port_comments
# 1. Ports comments.data to comments.csv
# 2. Creates a new file comment_count.csv containing story ids, ratings and comment counts

def port_comments():
    filename = 'comments.data'
    output_filename = 'comments.csv'
    input_f = open(filename, 'r')
    output_f = open(output_filename, 'w')
    count_comments = dict()
    for line in input_f:
        line = line.replace('\n', '')
        element = line.split("\t")
        output_line =  element[0]+","+element[1]+","+element[2]+","+element[3]+","+element[4]+","+element[5]+","+str(element[6]) + ",\"" + element[7] + "\",\"" + element[8] + "\"\n"
        output_f.write(output_line)
        tuple1 = (element[2], element[5])
        if tuple1 in count_comments:
            count_comments[tuple1] = count_comments[tuple1] + 1
        else:
            count_comments[tuple1] = 1
    input_f.close()
    output_f.close()

    output_filename = 'comment_count.csv'
    output_f = open(output_filename, 'w')
    for item in count_comments:
        count = count_comments[item]
        output_line = str(item[0]) +","+str(item[1])+","+str(count)+"\n"
        output_f.write(output_line)
    output_f.close()

# Function name: port_old_comments
# Ports old_comments.data to old_comments.csv

def port_old_comments():
    filename = 'old_comments.data'
    output_filename = 'old_comments.csv'
    input_f = open(filename, 'r')
    output_f = open(output_filename, 'w')
    for line in input_f:
        line = line.replace('\n', '')
        element = line.split("\t")
        output_line =  element[0]+","+element[1]+","+element[2]+","+element[3]+","+element[4]+","+element[5]+","+str(element[6]) + ",\"" + element[7] + "\",\"" + element[8] + "\"\n"
        output_f.write(output_line)
    input_f.close()
    output_f.close()

port_data()