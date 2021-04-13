import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  entries: [],
  status: 'idle',
};


export const createEntry = (entries, text) => {
  console.log("entries/createentry", entries)
  let id = Math.max(...entries.map(e => e.id), 0) + 1;
  
  return { id, text }
}

export const todoSlice = createSlice({
  name: 'todo',
  initialState,
  reducers: {
    addEntry: (state, action) => {
      state.entries.push(action.payload);
    },
    deleteEntry: (state, action) => {
      console.log(action)
      state.entries = state.entries.filter(e => e.id !== action.payload.id);
    }
  },

});

export const { addEntry, deleteEntry } = todoSlice.actions;

// The function below is called a selector and allows us to select a value from
// the state. Selectors can also be defined inline where they're used instead of
// in the slice file. For example: `useSelector((state: RootState) => state.counter.value)`
export const selectEntries = (state) => state.todo.entries;
export const selectStatus = (state) => state.todo.status;


export default todoSlice.reducer;
