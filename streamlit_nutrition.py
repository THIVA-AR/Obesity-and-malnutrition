import streamlit as st
import base64
 
 # Set page config first
st.set_page_config(layout="wide")
 
 # Function to convert image to base64
def get_base64_image(image_path):
     with open(image_path, "rb") as f:
         data = f.read()
     return base64.b64encode(data).decode()
 
 # ✅ Your image path (raw string to avoid backslash issues)
image_path = r"C:\Users\user\OneDrive\Documents\guvi\guvi project 1\dark-grunge-texture-background-with-scratches-stains_1048-18915.avif"
encoded = get_base64_image(image_path)
 
 # Inject CSS to add the background
st.markdown(
     f"""
     <style>
     .stApp {{
         background-image: url("data:image/webp;base64,{encoded}");
         background-size: cover;
         background-repeat: no-repeat;
         background-attachment: fixed;
         background-position: center;
     }}
     </style>
     """,
     unsafe_allow_html=True
)

st.markdown("""
     <h1 style="
         color: red;
         -webkit-text-stroke: 2px pink;
         font-weight: bold;
         text-align: center;
     ">OBESITY AND MALNUTRITION</h1>
 
     <h4 style="
         color: white;
         -webkit-text-stroke: 1px pink;
         text-align: center;
         margin-top: -10px;
     ">^PROJECT RELATED ON WORLD HEALTH ORGANIZATION^</h4>
""", unsafe_allow_html=True)


option = st.selectbox("select an queries below", ["None selected","1. Top 5 regions with the highest average obesity levels in 2022",
                                                   "2. Top 5 countries with highest obesity estimates",
                                                   "3. Obesity trend in India over the years (Mean estimate)",
                                                   "4. Average obesity by gender",
                                                   "5. Country count by obesity level category and age group",
                                                   "6. Top 5 least reliable countries (highest CI Width)",
                                                   "7. Top 5 most consistent countries(smallest average CI Width)",
                                                   "8. Average obesity by age group",
                                                   "9. Top 10 countries with consistent low obesity (low average + low CI) over the years",
                                                   "10. Countries where female obesity exceeds male by a large margin (same year)",
                                                   "11. Global average obesity percentage per year",
                                                   "12. Avg. malnutrition by age group",
                                                   "13. Top 5 countries with highest malnutrition(mean_estimate)",
                                                   "14. Malnutrition trend in African region over the years",
                                                   "15. Gender-based average malnutrition",
                                                   "16. Malnutrition level-wise (average CI_Width by age group)",
                                                   "17. Yearly malnutrition change in specific countries(India, Nigeria, Brazil)",
                                                   "18. Regions with lowest malnutrition averages",
                                                   "19. Countries with increasing malnutrition",
                                                   "20. Min/Max malnutrition levels year-wise comparison",
                                                   "21. High CI_Width flags for monitoring(CI_width > 5)",
                                                   "22. Obesity vs malnutrition comparison by country(any 5 countries)",
                                                   "23. Gender-based disparity in both obesity and malnutrition",
                                                   "24. Region-wise avg estimates side-by-side(Africa and America)",
                                                   "25. Age-wise trend analysis"])
 
 
import mysql.connector
import pandas as pd
 
try:
     conn = mysql.connector.connect(
         host="localhost",
         user="thivagar",
         password="thivagar@123",
         database="nutrition"
     )
     cursor = conn.cursor()
 
except mysql.connector.Error as err:
     st.error(f"Database connection failed: {err}")
     st.stop()  # Stops execution if connection fails)                                              
                                         
if option == "None selected":
     st.markdown(
         """
         <h3 style='color:white;'> HELLO</h3>
         <h3 style='color:green;'> WELCOME TO MY PROJECT</h3>
         """, unsafe_allow_html=True
     )

if option == "1. Top 5 regions with the highest average obesity levels in 2022":
     st.subheader(" Average obesity in 2022")
     query = """
         SELECT Region, AVG(Mean_Estimate) AS avg_obesity
FROM obesity
WHERE Year = 2022
GROUP BY Region
ORDER BY avg_obesity DESC
LIMIT 5;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "2. Top 5 countries with highest obesity estimates":
     st.subheader("Top 5 countries with hishest obesity")
     query = """
       SELECT Country, MAX(Mean_Estimate) AS max_obesity
FROM obesity
GROUP BY Country
ORDER BY max_obesity DESC
LIMIT 5;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "3. Obesity trend in India over the years (Mean estimate)":
     st.subheader("Mean estimate for obesity trend")
     query = """
       SELECT Year, AVG(Mean_Estimate) AS avg_obesity
FROM obesity
WHERE Country = 'India'
GROUP BY Year
ORDER BY Year;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "4. Average obesity by gender":
     st.subheader("Average obesity by gender")
     query = """
               SELECT Gender, AVG(Mean_Estimate) AS avg_obesity
FROM obesity
GROUP BY Gender;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "5. Country count by obesity level category and age group":
     st.subheader("country count by obesity level and age group")
     query = """
         SELECT obesity_level, age_group, COUNT(DISTINCT Country) AS country_count
FROM obesity
GROUP BY obesity_level, age_group;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "6. Top 5 least reliable countries (highest CI Width)":
     st.subheader("highest CI Width for least reliable countries")
     query = """
        SELECT Country, AVG(CI_Width) AS avg_ci_width
FROM obesity
GROUP BY Country
ORDER BY avg_ci_width DESC
LIMIT 5;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "7. Top 5 most consistent countries(smallest average CI Width)":
     st.subheader("smallest Ci Width for consistent countries")
     query = """
        SELECT Country, AVG(CI_Width) AS avg_ci_width
FROM obesity
GROUP BY Country
ORDER BY avg_ci_width ASC
LIMIT 5;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "8. Average obesity by age group":
     st.subheader("average obesity by age group")
     query = """
        SELECT age_group, AVG(Mean_Estimate) AS avg_obesity
FROM obesity
GROUP BY age_group;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)


elif option == "9. Top 10 countries with consistent low obesity (low average + low CI) over the years":
     st.subheader("low obesity in top 10 countries")
     query = """
        SELECT Country, AVG(Mean_Estimate) AS avg_obesity, AVG(CI_Width) AS avg_ci_width
FROM obesity
GROUP BY Country
HAVING AVG(Mean_Estimate) < 20 AND AVG(CI_Width) < 5
ORDER BY avg_obesity ASC
LIMIT 10;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "10. Countries where female obesity exceeds male by a large margin (same year)":
     st.subheader("In a same year female obesity exceeds male")
     query = """
        SELECT f.Country, f.Year, f.age_group, (f.Mean_Estimate - m.Mean_Estimate) AS gender_gap
FROM obesity f
JOIN obesity m 
  ON f.Country = m.Country AND f.Year = m.Year AND f.age_group = m.age_group
WHERE f.Gender = 'Female' AND m.Gender = 'Male'
HAVING gender_gap > 10
ORDER BY gender_gap DESC;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "11. Global average obesity percentage per year":
     st.subheader("Global average obesity per year")
     query = """
        SELECT Year, AVG(Mean_Estimate) AS global_avg_obesity
FROM obesity
GROUP BY Year
ORDER BY Year;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "12. Avg. malnutrition by age group":
     st.subheader("Avg. Malnutrition by age group")
     query = """
        SELECT age_group, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition
GROUP BY age_group;

     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "13. Top 5 countries with highest malnutrition(mean_estimate)":
     st.subheader("Highest malnutrition (mean_estimate)")
     query = """
        SELECT Country, MAX(Mean_Estimate) AS max_malnutrition
FROM malnutrition
GROUP BY Country
ORDER BY max_malnutrition DESC
LIMIT 5;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "14. Malnutrition trend in African region over the years":
     st.subheader("Malnutrition trend in African region over the years")
     query = """
        SELECT Year, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition
WHERE Region = 'Africa'
GROUP BY Year
ORDER BY Year;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "15. Gender-based average malnutrition":
     st.subheader("Gender-based average malnutrition")
     query = """
        SELECT Gender, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition
GROUP BY Gender;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "16. Malnutrition level-wise (average CI_Width by age group)":
     st.subheader("(average CI_Width by age group)")
     query = """
        SELECT malnutrition_level, age_group, AVG(CI_Width) AS avg_ci_width
FROM malnutrition
GROUP BY malnutrition_level, age_group;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "17. Yearly malnutrition change in specific countries(India, Nigeria, Brazil)":
     st.subheader("(India, Nigeria, Brazil)")
     query = """
        SELECT Country, Year, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition
WHERE Country IN ('India', 'Nigeria', 'Brazil')
GROUP BY Country, Year
ORDER BY Country, Year;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "18. Regions with lowest malnutrition averages":
     st.subheader("Regions with lowest malnutrition averages")
     query = """
        SELECT Region, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition
GROUP BY Region
ORDER BY avg_malnutrition ASC;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "19. Countries with increasing malnutrition":
     st.subheader("Countries with increasing malnutrition")
     query = """
        SELECT Country, 
       MIN(Mean_Estimate) AS min_estimate, 
       MAX(Mean_Estimate) AS max_estimate,
       (MAX(Mean_Estimate) - MIN(Mean_Estimate)) AS increase
FROM malnutrition
GROUP BY Country
HAVING increase > 0
ORDER BY increase DESC;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "20. Min/Max malnutrition levels year-wise comparison":
     st.subheader("Min/Max malnutrition levels year-wise comparison")
     query = """
        SELECT Year, 
       MIN(Mean_Estimate) AS min_malnutrition, 
       MAX(Mean_Estimate) AS max_malnutrition
FROM malnutrition
GROUP BY Year
ORDER BY Year;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "21. High CI_Width flags for monitoring(CI_width > 5)":
     st.subheader("Monitoring(CI_width > 5)")
     query = """
        SELECT Country, Region, Year, Gender, age_group, Mean_Estimate, CI_Width
FROM malnutrition
WHERE CI_Width > 5
ORDER BY CI_Width DESC;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "22. Obesity vs malnutrition comparison by country(any 5 countries)":
     st.subheader("Monitoring(CI_width > 5)")
     query = """
        SELECT 
  o.Country,
  AVG(o.Mean_Estimate) AS avg_obesity,
  AVG(m.Mean_Estimate) AS avg_malnutrition
FROM obesity o
JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year
WHERE o.Country IN ('India', 'USA', 'Nigeria', 'Brazil', 'Mexico')
GROUP BY o.Country;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "23. Gender-based disparity in both obesity and malnutrition":
     st.subheader("Gender-based disparity in both obesity and malnutrition")
     query = """
        SELECT 
  o.Gender,
  AVG(o.Mean_Estimate) AS avg_obesity,
  AVG(m.Mean_Estimate) AS avg_malnutrition
FROM obesity o
JOIN malnutrition m 
  ON o.Country = m.Country 
  AND o.Year = m.Year 
  AND o.Gender = m.Gender
GROUP BY o.Gender;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "24. Region-wise avg estimates side-by-side(Africa and America)":
     st.subheader("Region-wise avg estimates side-by-side(Africa and America)")
     query = """
        SELECT 
  o.Region,
  AVG(o.Mean_Estimate) AS avg_obesity,
  AVG(m.Mean_Estimate) AS avg_malnutrition
FROM obesity o
JOIN malnutrition m 
  ON o.Country = m.Country 
  AND o.Year = m.Year 
  AND o.Region = m.Region
WHERE o.Region IN ('Africa', 'America')
GROUP BY o.Region;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)

elif option == "25. Age-wise trend analysis":
     st.subheader(" Age-wise trend analysis")
     query = """
        SELECT 
  o.age_group,
  AVG(o.Mean_Estimate) AS avg_obesity,
  AVG(m.Mean_Estimate) AS avg_malnutrition
FROM obesity o
JOIN malnutrition m 
  ON o.Country = m.Country 
  AND o.Year = m.Year 
  AND o.age_group = m.age_group
GROUP BY o.age_group
ORDER BY o.age_group;
     """
     cursor.execute(query)
     rows = cursor.fetchall()
     columns = cursor.column_names
     df = pd.DataFrame(rows, columns=columns)
     st.dataframe(df)


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the app
st.markdown(
         """
         <h2 style='color:white;'>📊 Exploratory Data Analysis: Histogram Visualization</h2>
         """, unsafe_allow_html=True
     )

# File uploader allows user to upload a CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Display the first few rows of the dataframe
        st.subheader("Preview of Dataset")
        st.write(df.head())

        # Select numerical columns for analysis
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if numerical_columns:
            # User selects a numerical column to visualize
            selected_column = st.selectbox("Select a numerical column to visualize", numerical_columns)

            # User selects the number of bins for the histogram
            bins = st.slider("Number of bins", min_value=5, max_value=100, value=30, step=5)

            # User decides whether to include KDE
            include_kde = st.checkbox("Include Kernel Density Estimate (KDE)", value=True)

            # Create the histogram plot
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(df[selected_column], bins=bins, kde=include_kde, color='skyblue', ax=ax)
            ax.set_title(f'Distribution of {selected_column}')
            ax.set_xlabel(selected_column)
            ax.set_ylabel('Frequency')

            # Display the plot in the Streamlit app
            st.pyplot(fig)
        else:
            st.warning("The uploaded file does not contain any numerical columns for visualization.")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("Please upload a CSV file to begin.")



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("📦 Exploratory Data Analysis: Boxplot Visualization")

# File uploader allows user to upload a CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="unique_file_uploader")

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Display the first few rows of the dataframe
        st.subheader("Preview of Dataset")
        st.write(df.head())

        # Identify categorical and numerical columns
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if categorical_columns and numerical_columns:
            # User selects a categorical column for the x-axis
            x_column = st.selectbox("Select a categorical column for the x-axis", categorical_columns, key="x_column_selectbox")

            # User selects a numerical column for the y-axis
            y_column = st.selectbox("Select a numerical column for the y-axis", numerical_columns, key="y_column_selectbox")

            # Create the boxplot
            fig, ax = plt.subplots(figsize=(14, 7))
            sns.boxplot(data=df, x=x_column, y=y_column, ax=ax)
            ax.set_title(f'Distribution of {y_column} by {x_column}')
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            plt.xticks(rotation=45)

            # Display the plot in the Streamlit app
            st.pyplot(fig)
        else:
            st.warning("The uploaded file must contain at least one categorical and one numerical column for visualization.")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("Please upload a CSV file to begin.")


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the app
st.title("📈 Obesity and Malnutrition Trends Over Years")

# File uploader for Obesity data
obesity_file = st.file_uploader("Upload Obesity CSV file", type=["csv"], key="obesity_file")
# File uploader for Malnutrition data
malnutrition_file = st.file_uploader("Upload Malnutrition CSV file", type=["csv"], key="malnutrition_file")

if obesity_file is not None and malnutrition_file is not None:
    try:
        # Read the uploaded CSV files
        obesity_table = pd.read_csv(obesity_file)
        malnutrition_table = pd.read_csv(malnutrition_file)

        # Display the first few rows of each dataset
        st.subheader("Obesity Dataset Preview")
        st.write(obesity_table.head())

        st.subheader("Malnutrition Dataset Preview")
        st.write(malnutrition_table.head())

        # Ensure 'Year' and 'Mean_Estimate' columns exist in both datasets
        if 'Year' in obesity_table.columns and 'Mean_Estimate' in obesity_table.columns and \
           'Year' in malnutrition_table.columns and 'Mean_Estimate' in malnutrition_table.columns:

            # Group by 'Year' and calculate mean of 'Mean_Estimate'
            obesity_trend = obesity_table.groupby('Year')['Mean_Estimate'].mean().reset_index()
            malnutrition_trend = malnutrition_table.groupby('Year')['Mean_Estimate'].mean().reset_index()

            # Create the line plot
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(data=obesity_trend, x='Year', y='Mean_Estimate', label='Obesity', ax=ax)
            sns.lineplot(data=malnutrition_trend, x='Year', y='Mean_Estimate', label='Malnutrition', ax=ax)
            ax.set_title('Average Mean_Estimate Over Years')
            ax.set_xlabel('Year')
            ax.set_ylabel('Mean_Estimate')
            ax.legend()

            # Display the plot in the Streamlit app
            st.pyplot(fig)
        else:
            st.warning("Both datasets must contain 'Year' and 'Mean_Estimate' columns.")
    except Exception as e:
        st.error(f"An error occurred while processing the files: {e}")
else:
    st.info("Please upload both Obesity and Malnutrition CSV files to begin.")


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Exploratory Data Analysis: Histogram Visualization for ")

# Assuming obesity_table is your DataFrame
plt.figure(figsize=(10, 5))
sns.histplot(obesity_table['CI_Width'], bins=30, kde=True, color='blue')
plt.title('Distribution of CI_Width - Obesity')
plt.xlabel('CI_Width')
plt.ylabel('Frequency')

# Display the plot in Streamlit
st.pyplot(plt)
