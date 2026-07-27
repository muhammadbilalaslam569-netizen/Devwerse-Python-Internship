import pandas as pd
import numpy as np

df = pd.read_csv("student_marks.csv")

print("Original Data:\n")
print(df)

#Hadle Missing Values
df.fillna(df.mean(numeric_only=True), inplace=True)

#Remove Duplicate Rows
df.drop_duplicates(inplace=True)

#Fix Invalid Marks
subjects = ["Math","Science","English"]
for subject in subjects:
    df[subject] = np.where(df[subject] > 100, 100, df[subject])
    df[subject] = np.where(df[subject] < 0, 0, df[subject])

#Student Average Marks

df["Average"] = df[subjects].mean(axis=1)

#Pass/fail
df["Result"] = np.where(df["Average"] >= 40, "Pass","Fail")

#Topper
topper= df.loc[df["Average"].idxmax()]

# Lowest Average
lowest = df.loc[df["Average"].idxmin()]

#Numpy Statistics

print("\nSubject Statistics")

for subject in subjects:
    print(f"\{subject}")
    print("Mean:", np.mean(df[subject]))
    print("Median:", np.median(df[subject]))
    print("Standard Deviation:", np.std(df[subject]))


print("\nSummary")
print("Total Students:", len(df))
print("Passed:",(df["Result"] == "Pass").sum())
print("Failed:",(df["Result"] == "Fail").sum())

print("\nSubject-wise Class Average")
print(df[subjects].mean())

print("\nTopper")
print(topper[["Name", "Average"]])

print("\nNeeds Most Help")
print(lowest[["Name", "Average"]])


df = df.sort_values(by="Average", ascending=False)

print("\nFinal Sorted Data")
print(df)

df.to_csv("cleaned_student_marks.csv", index=False)

print("\nCleaned data saved as cleaned_student_marks.csv")
