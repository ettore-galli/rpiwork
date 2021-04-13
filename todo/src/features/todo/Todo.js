import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  createEntry,
  addEntry,
  deleteEntry,
  selectEntries,
  // selectStatus,
} from './todoSlice';
import styles from './Todo.module.css';

export function Todo() {
  const entries = useSelector(selectEntries);
  const dispatch = useDispatch();
  const [entryText, setEntryText] = useState('');

  const todoEntries = entries.map((e) =>
    <div key={e.id} className={styles.row}
    >
      <div>* {e.text}</div>
      <div>
        <button
          className={styles.button}
          onClick={() => dispatch(deleteEntry(e))}
        >
          Delete
        </button>

      </div>
    </div>
  )

  console.log("entries/render", entries)

  return (
    <div>
      {todoEntries}

      <div className={styles.row}>
        <input
          className={styles.textbox}
          aria-label="Todo"
          value={entryText}
          onChange={(e) => setEntryText(e.target.value)}
        />
        <button
          className={styles.button}
          onClick={() => {
            const entry = createEntry(entries, entryText);
            dispatch(addEntry(entry))
          }}
        >
          Add Entry
        </button>
      </div>

    </div>
  );
}
