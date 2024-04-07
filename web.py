import streamlit as st
from modules import functions as func

todos = func.load_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    func.write_todos(todos)


st.title("Todo App")
st.subheader("Organize your priorities for the future!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a to-do: ", placeholder="Add a new to-do...",
              on_change=add_todo, key="new_todo")
