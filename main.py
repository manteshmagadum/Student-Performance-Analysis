import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ವಿದ್ಯಾರ್ಥಿಗಳ ಮಾದರಿ ದತ್ತಾಂಶ
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Rahul', 'Ankita', 'Priya', 'Kiran', 'Suresh', 'Kavya', 'Amit', 'Meena'],
    'Kannada': [85, 92, 78, 65, 45, 88, 95, 52],
    'English': [78, 88, 82, 70, 50, 85, 90, 60],
    'Maths': [90, 95, 70, 55, 40, 92, 88, 48]
}

# DataFrame ರಚನೆ
df = pd.DataFrame(data)

# ಒಟ್ಟು ಅಂಕ ಮತ್ತು ಶೇಕಡಾವಾರು ಲೆಕ್ಕಾಚಾರ
df['Total'] = df['Kannada'] + df['English'] + df['Maths']
df['Percentage'] = round(df['Total'] / 3, 2)

# ಪಾಸ್ ಅಥವಾ ಫೇಲ್ (Result) ನಿರ್ಧಾರ (ಕನಿಷ್ಠ 50% ಇರಬೇಕು)
df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

print("--- ವಿದ್ಯಾರ್ಥಿಗಳ ಪೂರ್ಣ ವಿವರ ---")
print(df)

# ರಿಸಲ್ಟ್ ಪ್ರಕಾರ ಬಣ್ಣ ಬದಲಾಯಿಸಿ ಗ್ರಾಫ್ ಪ್ರದರ್ಶಿಸುವುದು
plt.figure(figsize=(8, 5))
sns.barplot(x='Name', y='Percentage', hue='Result', data=df, palette={'Pass': 'green', 'Fail': 'red'})

plt.title('Student Performance Analysis (Pass / Fail)')
plt.xlabel('Student Name')
plt.ylabel('Percentage (%)')
plt.ylim(0, 100)

plt.show()

# ಫಲಿತಾಂಶವನ್ನು CSV ಫೈಲ್ ಆಗಿ ಸೇವ್ಯೂ ಮಾಡುವುದು
df.to_csv('Student_Performance_Report.csv', index=False)
print("\n--- 'Student_Performance_Report.csv' ಫೈಲ್ ಯಶಸ್ವಿಯಾಗಿ ಸೇವ್ ಆಗಿದೆ! ---")