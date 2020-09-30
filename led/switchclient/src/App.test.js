import React from 'react';
import { render } from '@testing-library/react';
import App from './App';
import configureStore from 'redux-mock-store';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk'

const initialState = {
  switchManagement: {
    switchStatus: { s0: false, s1: false, s2: false, s3: false }
  }
}

const mockStore = configureStore([thunk]);
const store = mockStore(initialState);

test('Renders at least one switch', () => {
  const { getByText } = render(
    <Provider store={store}>
      <App />
    </Provider>
  );
  const linkElement = getByText(/s0/i);
  expect(linkElement).toBeInTheDocument();
});
