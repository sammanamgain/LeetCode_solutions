import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    header=["student_id","age"]
    return (pd.DataFrame(student_data,columns=header))
    