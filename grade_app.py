import streamlit as st


st.set_page_config(page_title="Student Grade App", page_icon="📘", layout="centered")


def get_grade(mark: int) -> str:
    if 90 <= mark <= 100:
        return "A"
    if 80 <= mark <= 89:
        return "B"
    if 70 <= mark <= 79:
        return "C"
    if 60 <= mark <= 69:
        return "D"
    return "E"


if "students" not in st.session_state:
    st.session_state.students = []


st.title("Student Grade Manager")
st.write("Add a student, view grades, and track class metrics.")

with st.form("add_student_form", clear_on_submit=True):
    name = st.text_input("Student name")
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1)
    submitted = st.form_submit_button("Add student")

    if submitted:
        clean_name = name.strip()
        if not clean_name:
            st.error("Name cannot be empty.")
        else:
            student = {
                "name": clean_name,
                "mark": int(mark),
                "grade": get_grade(int(mark)),
            }
            st.session_state.students.append(student)
            st.success(f"Added {clean_name} successfully.")

students = st.session_state.students

if students:
    st.subheader("Student Results")
    st.table(students)

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    col1, col2, col3 = st.columns(3)
    col1.metric("Class Average", f"{average:.1f}")
    col2.metric("Highest", str(highest))
    col3.metric("Lowest", str(lowest))
else:
    st.info("No student records available yet.")
