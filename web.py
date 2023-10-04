import streamlit as st

import functions

todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state.get("new_todo")
    if new_todo:  # Check if the input is not empty
        todo = new_todo + "\n"
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state.new_todo = ""  # Clear the input field
        # st.experimental_rerun()  # Trigger a rerun to update the UI


st.title("My Todo-App")

st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}_{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"checkbox_{index}_{todo}"]
        st.experimental_rerun()

st.text_input(label="Todo-List", placeholder="Enter a todo.........", on_change=add_todo, key="new_todo")




