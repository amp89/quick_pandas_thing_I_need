import pandas as pd

single_list = [
        {"key":"a","value":"A"},
        {"key":"b","value":None},
        {"key":"c","value":None},
        {"key":"d","value":"D"},
        {"key":"e","value":"E"},        
]

double_list = [
    {"key":"a","value":"AA"},
    {"key":"b","value":"BB"},
    {"key":"c","value":"CC"},
    {"key":"d","value":"DD"},
    {"key":"e","value":None},        
    {"key":"f","value":"FF"},        
    
]

single_df = pd.DataFrame(single_list)
double_df = pd.DataFrame(double_list)

print(single_df)
print(double_df)

single_df.value.fillna(double_df.value, inplace=True)

print(single_df)


