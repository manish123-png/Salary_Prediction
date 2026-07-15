import pandas as pd
import joblib
import streamlit as st

def main():

    st.title("Employee Salary Prediction")
    st.write("Enter employee details below")

    # Load trained model
    model = joblib.load("gb_model.pkl")

    age = st.number_input("Age", 18, 65, 28)

    experience = st.number_input("Experience (Years)", 0, 40, 6)

    certifications = st.number_input("Certifications", 0, 20, 4)

    

    company_tenure = st.number_input("Company Tenure", 0, 40, 6)

    projects = st.number_input("Projects Completed", 0, 50, 5)

    skill_score = st.slider("Skill Score", 0, 100, 97)

    performance = st.slider("Performance Rating", 1, 5, 3)


    gender = st.selectbox(
        "Gender",
        ("Male", "Female")
    )

    gender = 1 if gender == "Male" else 0

    

    education = st.selectbox(
        "Education",
        (
            "Diploma",
            "Bachelor",
            "Master",
            "PhD"
        )
    )

    education_map = {'Diploma':0, 'Bachelor':1, 'Master':2,'PhD':3}

    education = education_map[education]

    

    department = st.selectbox(
        "Department",
        (
            "Operations","IT","Finance","Sales","HR","Marketing"
        )
    )

    department_map = {'Operations':0, 'IT':1, 'Finance':2,'Sales':3,'HR':4,'Marketing':5}

    department = department_map[department]

   

    job_level = st.selectbox(
        "Job Level",
        (
            'Junior','Mid','Senior','Lead','Manager'
        )
    )

    level_map = {'Junior':1,'Mid':2,'Senior':3,'Lead':4,'Manager':5}
    job_level = level_map[job_level]

    

    remote = st.selectbox(
        "Remote Work",
        ("No","Yes")
    )

    remote = 1 if remote == "Yes" else 0

    

    city = st.selectbox(
        "City",
        ('Hyderabad', 'Mumbai', 'Pune','Chennai','Bangalore', 'Delhi'
        )
    )

    city_map = {'Hyderabad':0, 'Mumbai':1, 'Pune':2,'Chennai':3,'Bangalore':4, 'Delhi':5}

    city = city_map[city]

   

    new_employee = pd.DataFrame({

        'Age':[age],
        'Gender':[gender],
        'Education':[education],
        'Experience_Years':[experience],
        'Department':[department],
        'Job_Level':[job_level],
        'Performance_Rating':[performance],
        'Certifications':[certifications],
        'Remote_Work':[remote],
        'City':[city],
        'Company_Tenure':[company_tenure],
        'Projects_Completed':[projects],
        'Skill_Score':[skill_score]
        },index=[0])

    if st.button("Predict Salary"):

        prediction = model.predict(new_employee)

        st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")


if __name__ == "__main__":
    main()