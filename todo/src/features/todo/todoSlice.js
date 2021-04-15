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
      state.entries = state.entries.filter(e => e.id !== action.payload.id);
    },
    loadEntries: (state, action) => {
      state.entries =  action.payload;
    }
  },

});

export const { addEntry, deleteEntry, loadEntries } = todoSlice.actions;

export const selectEntries = (state) => state.todo.entries;
export const selectStatus = (state) => state.todo.status;

export default todoSlice.reducer;
