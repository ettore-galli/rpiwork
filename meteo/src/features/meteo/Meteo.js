import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  getMeteoInfoAsync,
  selectInfo,
  selectItems
} from './meteoSlice';
import styles from './Meteo.module.css';

export function Meteo() {
  const info = useSelector(selectInfo);
  const items = useSelector(selectItems);

  const dispatch = useDispatch();
  const [query, setQuery] = useState("");

  // const incrementValue = Number(incrementAmount) || 0;

  return (
    <div>
      <div>
        {info}
      </div>
      <div>
        {items}
      </div>
      <div className={styles.row}>
        <input
          className={styles.query_input}
          aria-label="Query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          className={styles.button}
          onClick={() => dispatch(getMeteoInfoAsync())}
        >
          Get
        </button>
      </div>
    </div>
  );
}
