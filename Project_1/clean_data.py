import pandas as pd

# ----------------------------
# 1. Load raw sales CSV
# ----------------------------
df = pd.read_csv("raw_sales.csv")

# ----------------------------
# 2. Remove duplicates
# ----------------------------
df = df.drop_duplicates()

# ----------------------------
# 3. Standardize column names
# ----------------------------
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ----------------------------
# 4. Fix inconsistent date formats
# ----------------------------
date_formats = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", "%m-%d-%Y"]

def parse_dates(date_str):
    for fmt in date_formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    return pd.NaT  # if no format matches

df['date'] = df['date'].apply(parse_dates)

# Drop rows with missing dates
df = df.dropna(subset=['date'])

# ----------------------------
# 5. Fill missing numeric values
# ----------------------------
# Fill missing quantity with 1
df['quantity'] = df['quantity'].fillna(1)

# Fill missing amount with quantity * 10 (dummy price if unknown)
df['amount'] = df['amount'].fillna(df['quantity'] * 10)

# ----------------------------
# 6. Optional: Sort data by date
# ----------------------------
df = df.sort_values('date')

# ----------------------------
# 7. Save cleaned CSV
# ----------------------------
df.to_csv("cleaned_sales.csv", index=False)

print("Data cleaned successfully!")
