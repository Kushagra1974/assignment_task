import pandas as pd

df = pd.read_csv("input_1.csv")
df.replace('-',0,inplace=True)
df = df.rename(columns = {'id':'Username'})
df1 = df.melt(
    id_vars=['Name', 'Username', 'Chapter Tag'],
    var_name='Test_Name',
    value_vars= ["Concept Test 1 - answered", "Concept Test 2 - answered", "Concept Test 3 - answered", "Concept Test 4 - answered", "Concept Test 5 - answered", "Full Chapter Test 1 - answered", "Full Chapter Test 2 - answered", "Topic Test 1 - answered", "Topic Test 2 - answered"],    
    value_name='answered'
    )
df2 = df.melt(
    value_vars= ["Concept Test 1- correct", "Concept Test 2- correct", "Concept Test 3- correct", "Concept Test 4- correct", "Concept Test 5- correct", "Full Chapter Test 1- correct", "Full Chapter Test 2- correct","Topic Test 1- correct", "Topic Test 2- correct"],
    value_name='correct'
)
df2.drop(['variable'], axis=1,inplace=True)

df3 = df.melt(
    value_vars= ["Concept Test 1 - score", "Concept Test 2 - score", "Concept Test 3 - score", "Concept Test 4 - score", "Concept Test 5 - score", "Full Chapter Test 1 - score", "Full Chapter Test 2 - score","Topic Test 1 - score", "Topic Test 2 - score"],
    value_name='score'
)
df3.drop(['variable'], axis=1,inplace=True)

df4 = df.melt(
    value_vars= ["Concept Test 1- skipped", "Concept Test 2- skipped", "Concept Test 3- skipped", "Concept Test 4- skipped", "Concept Test 5- skipped", "Full Chapter Test 1- skipped", "Full Chapter Test 2- skipped","Topic Test 1- skipped", "Topic Test 2- skipped"],
    value_name='skipped'
)
df4.drop(['variable'], axis=1,inplace=True)

df5 = df.melt(
    value_vars= ["Concept Test 1 - time-taken (seconds)", "Concept Test 2 - time-taken (seconds)", "Concept Test 3 - time-taken (seconds)", "Concept Test 4 - time-taken (seconds)", "Concept Test 5 - time-taken (seconds)", "Full Chapter Test 1 - time-taken (seconds)", "Full Chapter Test 2 - time-taken (seconds)","Topic Test 1 - time-taken (seconds)", "Topic Test 2 - time-taken (seconds)"],
    value_name='time-taken (seconds)'
)
df5.drop(['variable'], axis=1,inplace=True)

df6 = df.melt(
    value_vars= ["Concept Test 1- wrong", "Concept Test 2- wrong", "Concept Test 3- wrong", "Concept Test 4- wrong", "Concept Test 5- wrong", "Full Chapter Test 1- wrong", "Full Chapter Test 2- wrong","Topic Test 1- wrong", "Topic Test 2- wrong"],
    value_name='wrong'
)
df6.drop(['variable'], axis=1,inplace=True)

frames = [df1,df2,df3,df4,df5,df6]

df_final = pd.concat(frames,axis=1)
df_final['Test_Name'].replace(["Concept Test 1 - answered", "Concept Test 2 - answered", "Concept Test 3 - answered", "Concept Test 4 - answered", "Concept Test 5 - answered", "Full Chapter Test 1 - answered", "Full Chapter Test 2 - answered","Topic Test 1 - answered", "Topic Test 2 - answered"],    
["Concept Test 1", "Concept Test 2", "Concept Test 3", "Concept Test 4", "Concept Test 5", "Full Chapter Test 1", "Full Chapter Test 2","Topic Test 1", "Topic Test 2"],    
inplace=True)

grp_df = df_final.groupby('Name')

arr = []

for n,df in grp_df:
    arr.append(df)

new_df = pd.concat(arr)

new_df.drop(new_df.index[new_df['answered'] == 0], inplace=True) 
new_df.to_csv('output.csv',index= False)