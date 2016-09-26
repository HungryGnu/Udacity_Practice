import pandas, csv


def filter_by_regular(filename):
    '''
    This function should read the csv file located at filename into a pandas dataframe,
    and filter the dataframe to only rows where the 'DESCn' column has the value 'REGULAR'.

    For example, if the pandas dataframe is as follows:
    ,C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn
    0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
    1,A002,R051,02-00-00,05-01-11,04:00:00,DOOR,3144335,1088159
    2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
    3,A002,R051,02-00-00,05-01-11,12:00:00,DOOR,3144424,1088231

    The dataframe will look like below after filtering to only rows where DESCn column
    has the value 'REGULAR':
    0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
    2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
    '''
#TODO: Make code better

    #turnstile_data = pandas.DataFrame(columns=['C/A', 'UNIT', 'SCP', 'DATEn', 'TIMEn', 'DESCn', 'ENTRIESn', 'EXITSn'])
    file = open(filename, 'r')
    lines = csv.reader(file, delimiter=',')
    Reg_lines=[]
    for line in lines:
        if line[6] == 'REGULAR':
            #works to here, Need to figure out how to append to a dataframe
            del line[0]
            Reg_lines.append(line)
            #print Reg_lines
    turnstile_data = pandas.DataFrame(Reg_lines, columns=['C/A', 'UNIT', 'SCP', 'DATEn', 'TIMEn', 'DESCn', 'ENTRIESn', 'EXITSn'])
    raw_data = pandas.read_csv(filename)
    turnstile_data = raw_data[raw_data.DESCn == 'REGULAR' ]
    # print turnstile_data
    print 'The DataFrame includes ' + str(len(turnstile_data)) + ' items'
    return turnstile_data

filter_by_regular('test_df.txt')